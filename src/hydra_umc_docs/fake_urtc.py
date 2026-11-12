# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/fake_urtc.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""A tool head of URTC that exists only as software: it answers on a CAN bus the way the firmware does.

It lets a flasher, a tester or a bridge be tried without the board. It answers exactly two requests, with the frames the
cross-implementation vectors of URTC fix byte for byte:

* `0x110` (query the active tool) -> `0x111`, four to six bytes: tool, system error, CAN error, booting and, when the
  configuration says the firmware is that new, the thermal fault and the reset cause;
* `0x7F8` (query the version) -> `0x7F9` and, when the head knows its patch, `0x7E9`; a head set to answer as the bootloader
  also sends `0x7FA`.

Every other frame is ignored: this is a responder for the read-only queries, not a simulation of the motion, heating or
flashing commands. Nothing here ever writes to a real head.

The bus is a small interface so that the same responder runs on a real SocketCAN interface (`vcan0` on Linux) and on the
in-memory pair the tests use. `SocketCanBus` only works on Linux: it is tested against a simulated socket and runs on a real
`vcan0` interface in the URTC bench of HYDRA-UMC-DEV-SERVER. The parameters of the head live in `data/fake_urtc.json`, not in this code."""
from __future__ import annotations

import json
import queue
import socket
import struct
import threading
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Protocol

ID_QUERY_ACTIVE_TOOL = 0x110
ID_ACTIVE_TOOL_RESP = 0x111
ID_QUERY_VERSION = 0x7F8
ID_VERSION_RESPONSE = 0x7F9
ID_BOOTLOADER_VERSION = 0x7FA
ID_VERSION_PATCH = 0x7E9
MAX_STANDARD_ID = 0x7FF
UNKNOWN_PATCH = 0xFF
#: the layout of `struct can_frame` of Linux: identifier, length, three bytes of padding, eight bytes of data
_CAN_FRAME = struct.Struct("=IB3x8s")
#: flags in the top bits of the identifier: extended frame, remote request, error frame
_NOT_STANDARD = 0xE0000000


class BusUnavailable(RuntimeError):
    """The bus cannot be opened here (SocketCAN needs Linux and an interface that exists)."""


@dataclass(frozen=True)
class CanFrame:
    can_id: int
    data: bytes = b""

    def __post_init__(self) -> None:
        if not 0 <= self.can_id <= MAX_STANDARD_ID:
            raise ValueError(f"{self.can_id:#x} is not an 11-bit CAN identifier")
        if len(self.data) > 8:
            raise ValueError("a classic CAN frame carries at most 8 bytes")


class Bus(Protocol):
    def send(self, frame: CanFrame) -> None: ...

    def recv(self, timeout: float) -> CanFrame | None: ...

    def close(self) -> None: ...


class SimulatedBus:
    """One end of an in-memory bus; `make_pair` gives the two ends (what one sends the other receives)."""

    def __init__(self, inbox: queue.Queue[CanFrame], outbox: queue.Queue[CanFrame]) -> None:
        self._inbox, self._outbox = inbox, outbox

    @classmethod
    def make_pair(cls) -> tuple[SimulatedBus, SimulatedBus]:
        a: queue.Queue[CanFrame] = queue.Queue()
        b: queue.Queue[CanFrame] = queue.Queue()
        return cls(a, b), cls(b, a)

    def send(self, frame: CanFrame) -> None:
        self._outbox.put(frame)

    def recv(self, timeout: float) -> CanFrame | None:
        try:
            return self._inbox.get(timeout=timeout)
        except queue.Empty:
            return None

    def close(self) -> None:
        pass


def pack_frame(frame: CanFrame) -> bytes:
    """The 16 bytes Linux expects on a raw CAN socket."""
    return _CAN_FRAME.pack(frame.can_id, len(frame.data), frame.data.ljust(8, b"\0"))


def unpack_frame(raw: bytes) -> CanFrame | None:
    """The standard data frame in `raw`, or None for anything else (too short, extended, remote, error frame, a length over 8)."""
    if len(raw) < _CAN_FRAME.size:
        return None
    can_id, length, data = _CAN_FRAME.unpack(raw[: _CAN_FRAME.size])
    if can_id & _NOT_STANDARD or length > 8:
        return None
    return CanFrame(can_id, data[:length])


class SocketCanBus:
    """A raw SocketCAN socket bound to `interface` (for example `vcan0`). Linux only; `socket_module` is for tests."""

    def __init__(self, interface: str, *, socket_module: Any = socket) -> None:
        if not hasattr(socket_module, "AF_CAN"):
            raise BusUnavailable("SocketCAN is only available on Linux")
        try:
            self._socket = socket_module.socket(socket_module.AF_CAN, socket_module.SOCK_RAW, socket_module.CAN_RAW)
            self._socket.bind((interface,))
        except OSError as exc:
            raise BusUnavailable(f"the CAN interface {interface!r} cannot be opened ({exc})") from exc
        self._timeout_error: type[BaseException] = getattr(socket_module, "timeout", TimeoutError)

    def send(self, frame: CanFrame) -> None:
        self._socket.send(pack_frame(frame))

    def recv(self, timeout: float) -> CanFrame | None:
        self._socket.settimeout(timeout)
        try:
            raw = self._socket.recv(_CAN_FRAME.size)
        except (self._timeout_error, TimeoutError, BlockingIOError):
            return None
        return unpack_frame(raw)

    def close(self) -> None:
        self._socket.close()


def setup_commands(interface: str = "vcan0") -> list[str]:
    """The commands that create a virtual CAN interface on Linux. They are shown, never run by this module."""
    return [
        "sudo modprobe vcan",
        f"sudo ip link add dev {interface} type vcan",
        f"sudo ip link set up {interface}",
    ]


@dataclass(frozen=True)
class FakeUrtcConfig:
    """The state of the simulated head."""

    #: the tool the head reports (0 to 24 name a tool, 25 to 31 name none)
    tool_id: int = 0
    system_error: bool = False
    can_error: bool = False
    booting: bool = False
    #: the thermal fault byte of 0x111; None leaves the byte out, as firmware before the thermal guard does
    thermal_fault: int | None = 0
    #: the reset cause byte of 0x111; None leaves it out (it needs `thermal_fault` too, as the frame is positional)
    reset_cause: int | None = 8
    hardware_id: int = 0x0303CC01
    major: int = 0
    minor: int = 3
    #: the patch of the installed application; None: the head predates the patch frame and sends no 0x7E9; 255: not known
    patch: int | None = 0
    #: answer as the bootloader (0x7F9 with the first byte 1, plus 0x7FA)
    bootloader: bool = False
    bootloader_version: tuple[int, int, int] = (0, 3, 9)
    #: bit 0 of 0x7E9: the bootloader reads the patch from the minor field of the end-of-update frame
    accepts_patch_in_end_update: bool = False


def _int(value: Any, name: str, low: int, high: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
        raise ValueError(f"{name} must be a whole number from {low} to {high}")
    return value


def _flag(value: Any, name: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be true or false")
    return value


def config_from_dict(data: dict[str, Any]) -> FakeUrtcConfig:
    """A validated configuration; an unknown key or a value out of range is an error, never ignored."""
    known = set(FakeUrtcConfig.__dataclass_fields__)
    unknown = sorted(set(data) - known)
    if unknown:
        raise ValueError("unknown setting(s): " + ", ".join(unknown))
    values: dict[str, Any] = {}
    for name, value in data.items():
        if name == "tool_id":
            values[name] = _int(value, name, 0, 31)
        elif name in {"system_error", "can_error", "booting", "bootloader", "accepts_patch_in_end_update"}:
            values[name] = _flag(value, name)
        elif name in {"thermal_fault", "reset_cause"}:
            values[name] = None if value is None else _int(value, name, 0, 255)
        elif name == "patch":
            values[name] = None if value is None else _int(value, name, 0, 255)
        elif name == "hardware_id":
            values[name] = _int(value, name, 0, 0xFFFFFFFF)
        elif name in {"major"}:
            values[name] = _int(value, name, 0, 0xFFFF)
        elif name == "minor":
            values[name] = _int(value, name, 0, 255)
        else:  # bootloader_version
            if not isinstance(value, list) or len(value) != 3:
                raise ValueError("bootloader_version must be a list of three numbers")
            values[name] = tuple(_int(part, "bootloader_version", 0, 255) for part in value)
    config = FakeUrtcConfig(**values)
    if config.reset_cause is not None and config.thermal_fault is None:
        raise ValueError("reset_cause needs thermal_fault: the frame is positional")
    return config


def with_tool(config: FakeUrtcConfig, tool_id: int) -> FakeUrtcConfig:
    """The same head reporting another tool."""
    return replace(config, tool_id=_int(tool_id, "tool_id", 0, 31))


def load_config(path: Path) -> FakeUrtcConfig:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"the configuration {path} cannot be read: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path} must hold an object")
    return config_from_dict(data)


class FakeUrtc:
    """The responder. `handle` is pure (a frame in, the answers out); `serve` runs it on a bus."""

    def __init__(self, config: FakeUrtcConfig | None = None) -> None:
        self.config = config or FakeUrtcConfig()

    def handle(self, frame: CanFrame) -> list[CanFrame]:
        if frame.can_id == ID_QUERY_ACTIVE_TOOL:
            return [self._active_tool()]
        if frame.can_id == ID_QUERY_VERSION:
            return self._version()
        return []

    def _active_tool(self) -> CanFrame:
        c = self.config
        data = bytes([c.tool_id, int(c.system_error), int(c.can_error), int(c.booting)])
        if c.thermal_fault is not None:
            data += bytes([c.thermal_fault])
            if c.reset_cause is not None:
                data += bytes([c.reset_cause])
        return CanFrame(ID_ACTIVE_TOOL_RESP, data)

    def _version(self) -> list[CanFrame]:
        c = self.config
        side = 1 if c.bootloader else 0
        frames = [CanFrame(ID_VERSION_RESPONSE, bytes([side]) + c.hardware_id.to_bytes(4, "big") + c.major.to_bytes(2, "big") + bytes([c.minor]))]
        if c.bootloader:
            frames.append(CanFrame(ID_BOOTLOADER_VERSION, bytes(c.bootloader_version)))
        if c.patch is not None:
            flags = 1 if c.bootloader and c.accepts_patch_in_end_update else 0
            frames.append(CanFrame(ID_VERSION_PATCH, bytes([side, c.patch, flags])))
        return frames

    def serve(self, bus: Bus, stop: threading.Event, *, poll: float = 0.05) -> int:
        """Answer queries until `stop` is set; returns how many frames were sent."""
        sent = 0
        while not stop.is_set():
            frame = bus.recv(poll)
            if frame is None:
                continue
            for answer in self.handle(frame):
                bus.send(answer)
                sent += 1
        return sent
