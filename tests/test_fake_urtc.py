# =============================================================================
# HYDRA-UMC-DOCS - tests/test_fake_urtc.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The simulated tool head, against the vectors of URTC and a simulated bus. Nothing here touches SocketCAN on a real Linux interface."""
from __future__ import annotations

import json
import random
import socket
import threading
import time
from pathlib import Path

import pytest

from hydra_umc_docs import cli, fake_urtc
from hydra_umc_docs.fake_urtc import CanFrame, FakeUrtc, FakeUrtcConfig, SimulatedBus

VECTORS = Path(__file__).resolve().parents[2] / "URTC-DOCS" / "tests" / "fixtures" / "can_conformance_vectors.json"


def _answers(config: FakeUrtcConfig, request_id: int) -> list[tuple[int, str]]:
    return [(f.can_id, f.data.hex().upper()) for f in FakeUrtc(config).handle(CanFrame(request_id))]


# the same vectors as URTC-DOCS, written out so the tests also run where that repository is not next to this one
def test_the_active_tool_answers_have_the_bytes_of_the_vectors() -> None:
    assert _answers(FakeUrtcConfig(tool_id=10, can_error=True, thermal_fault=None, reset_cause=None), 0x110) == [(0x111, "0A000100")]
    assert _answers(FakeUrtcConfig(tool_id=10, system_error=True, thermal_fault=2, reset_cause=None), 0x110) == [(0x111, "0A01000002")]
    assert _answers(FakeUrtcConfig(tool_id=0, thermal_fault=0, reset_cause=1), 0x110) == [(0x111, "000000000001")]
    assert _answers(FakeUrtcConfig(tool_id=25, booting=True, thermal_fault=1, reset_cause=8), 0x110) == [(0x111, "190000010108")]


def test_the_version_answers_have_the_frames_of_the_vectors() -> None:
    application = FakeUrtcConfig(patch=5)
    assert _answers(application, 0x7F8) == [(0x7F9, "000303CC01000003"), (0x7E9, "000500")]
    assert _answers(FakeUrtcConfig(patch=None), 0x7F8) == [(0x7F9, "000303CC01000003")]
    assert _answers(FakeUrtcConfig(patch=255), 0x7F8) == [(0x7F9, "000303CC01000003"), (0x7E9, "00FF00")]
    bootloader = FakeUrtcConfig(bootloader=True, minor=4, patch=7, accepts_patch_in_end_update=True)
    assert _answers(bootloader, 0x7F8) == [(0x7F9, "010303CC01000004"), (0x7FA, "000309"), (0x7E9, "010701")]


@pytest.mark.skipif(not VECTORS.is_file(), reason="URTC-DOCS is not next to this repository")
def test_every_vector_of_urtc_that_the_head_answers_is_reproduced() -> None:
    vectors = json.loads(VECTORS.read_text(encoding="utf-8"))
    for vector in vectors["quick_state"]:
        if vector["expect"] is None:
            continue
        data = bytes.fromhex(vector["data"])
        config = FakeUrtcConfig(
            tool_id=data[0], system_error=bool(data[1]), can_error=bool(data[2]), booting=bool(data[3]),
            thermal_fault=data[4] if len(data) > 4 else None, reset_cause=data[5] if len(data) > 5 else None,
        )
        assert _answers(config, 0x110) == [(0x111, vector["data"].upper())], vector["name"]
    for vector in vectors["version_query"]:
        if vector["expect"] is None or any(len(bytes.fromhex(data)) != 3 for identifier, data in vector["frames"] if identifier == "0x7E9"):
            continue  # an answer that is not a frame to send, or a patch frame only a reader has to tolerate
        frames = {int(identifier, 16): bytes.fromhex(data) for identifier, data in vector["frames"]}
        head = frames[0x7F9]
        config = FakeUrtcConfig(
            bootloader=head[0] == 1, hardware_id=int.from_bytes(head[1:5], "big"), major=int.from_bytes(head[5:7], "big"), minor=head[7],
            bootloader_version=tuple(frames[0x7FA][:3]) if 0x7FA in frames else (0, 0, 0),  # type: ignore[arg-type]
            patch=frames[0x7E9][1] if len(frames.get(0x7E9, b"")) >= 3 else None,
            accepts_patch_in_end_update=bool(frames[0x7E9][2] & 1) if len(frames.get(0x7E9, b"")) >= 3 else False,
        )
        wanted = [(int(identifier, 16), data.upper()) for identifier, data in vector["frames"]]
        assert _answers(config, 0x7F8) == wanted, vector["name"]


def test_other_frames_are_ignored() -> None:
    for identifier in (0x095, 0x120, 0x7F0, 0x7FD, 0x111):
        assert FakeUrtc().handle(CanFrame(identifier, b"\x01")) == []


def test_a_frame_must_be_a_standard_classic_frame() -> None:
    with pytest.raises(ValueError):
        CanFrame(0x800)
    with pytest.raises(ValueError):
        CanFrame(0x100, bytes(9))
    assert CanFrame(0x7FF, bytes(8)).can_id == 0x7FF


def test_the_responder_serves_a_simulated_bus() -> None:
    host, device = SimulatedBus.make_pair()
    stop = threading.Event()
    result: list[int] = []
    thread = threading.Thread(target=lambda: result.append(FakeUrtc(FakeUrtcConfig(tool_id=5)).serve(device, stop, poll=0.01)))
    thread.start()
    host.send(CanFrame(0x110))
    host.send(CanFrame(0x7F8))
    host.send(CanFrame(0x120, b"\x01\x00\x00\x03\xe8"))
    received = [host.recv(1.0) for _ in range(3)]
    stop.set()
    thread.join(2)
    assert [f.can_id for f in received if f] == [0x111, 0x7F9, 0x7E9]
    assert received[0] is not None and received[0].data[0] == 5
    assert host.recv(0.05) is None and result == [3]


def test_the_linux_frame_layout_round_trips() -> None:
    frame = CanFrame(0x111, bytes.fromhex("0A000100"))
    raw = fake_urtc.pack_frame(frame)
    assert len(raw) == 16 and raw[:4] == (0x111).to_bytes(4, "little") and raw[4] == 4
    assert fake_urtc.unpack_frame(raw) == frame
    extended = (0x80000123).to_bytes(4, "little") + raw[4:]
    assert fake_urtc.unpack_frame(extended) is None
    error_frame = (0x20000001).to_bytes(4, "little") + raw[4:]
    assert fake_urtc.unpack_frame(error_frame) is None
    assert fake_urtc.unpack_frame(raw[:8]) is None
    assert fake_urtc.unpack_frame(raw[:4] + bytes([9]) + raw[5:]) is None


class _FakeSocketModule:
    """Stands in for the socket module of Linux: records what is bound and sent, and plays back received frames."""

    AF_CAN, SOCK_RAW, CAN_RAW = 29, 3, 1
    timeout = socket.timeout

    def __init__(self, incoming: list[bytes], *, fail_bind: bool = False) -> None:
        self.incoming, self.sent, self.bound, self.closed, self.fail_bind = incoming, [], None, False, fail_bind

    def socket(self, family: int, kind: int, protocol: int) -> _FakeSocketModule:
        assert (family, kind, protocol) == (29, 3, 1)
        return self

    def bind(self, address: tuple[str]) -> None:
        if self.fail_bind:
            raise OSError("no such device")
        self.bound = address

    def settimeout(self, value: float) -> None:
        pass

    def send(self, raw: bytes) -> None:
        self.sent.append(raw)

    def recv(self, size: int) -> bytes:
        if not self.incoming:
            raise socket.timeout()
        return self.incoming.pop(0)

    def close(self) -> None:
        self.closed = True


def test_the_socketcan_bus_speaks_the_linux_layout_to_its_socket() -> None:
    module = _FakeSocketModule([fake_urtc.pack_frame(CanFrame(0x110))])
    bus = fake_urtc.SocketCanBus("vcan0", socket_module=module)
    assert module.bound == ("vcan0",)
    stop = threading.Event()
    threading.Timer(0.3, stop.set).start()
    assert FakeUrtc().serve(bus, stop, poll=0.01) == 1
    assert fake_urtc.unpack_frame(module.sent[0]) == CanFrame(0x111, bytes.fromhex("000000000008"))
    assert bus.recv(0.01) is None
    bus.close()
    assert module.closed


def test_the_socketcan_bus_says_why_it_cannot_open() -> None:
    class NoLinux:
        pass

    with pytest.raises(fake_urtc.BusUnavailable, match="Linux"):
        fake_urtc.SocketCanBus("vcan0", socket_module=NoLinux())
    with pytest.raises(fake_urtc.BusUnavailable, match="vcan9"):
        fake_urtc.SocketCanBus("vcan9", socket_module=_FakeSocketModule([], fail_bind=True))


def test_the_setup_commands_are_text_that_is_never_run() -> None:
    assert fake_urtc.setup_commands("vcan1") == ["sudo modprobe vcan", "sudo ip link add dev vcan1 type vcan", "sudo ip link set up vcan1"]


def test_the_configuration_is_validated() -> None:
    assert fake_urtc.config_from_dict({"tool_id": 5, "patch": None}).patch is None
    for bad in ({"tool_id": 32}, {"tool_id": True}, {"system_error": 1}, {"nonsense": 1}, {"bootloader_version": [1, 2]}, {"thermal_fault": None, "reset_cause": 1}, {"minor": 256}):
        with pytest.raises(ValueError):
            fake_urtc.config_from_dict(bad)


def test_the_shipped_configuration_loads_and_matches_the_defaults() -> None:
    shipped = fake_urtc.load_config(cli.FAKE_URTC_FILE)
    assert shipped == FakeUrtcConfig()
    assert fake_urtc.with_tool(shipped, 9).tool_id == 9
    with pytest.raises(ValueError):
        fake_urtc.with_tool(shipped, 99)


def test_the_command_prints_the_setup_and_fails_cleanly_without_socketcan(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.run_fake_urtc(["--print-setup", "--interface", "vcan3"]) == 0
    assert "ip link add dev vcan3 type vcan" in capsys.readouterr().out
    if not hasattr(socket, "AF_CAN"):
        assert cli.run_fake_urtc(["--duration", "0.1"]) == 1
        assert "FAKE_URTC=FAIL" in capsys.readouterr().err


# --- failure and recovery: a bus that loses, doubles and breaks frames, and an interface that goes down and comes back (evidence=simulator) -------------------------
SEED = 20260101


def _wait(condition, what: str, timeout: float = 5.0) -> None:  # noqa: ANN001
    deadline = time.monotonic() + timeout
    while not condition():
        assert time.monotonic() < deadline, f"timed out waiting for {what}"
        time.sleep(0.01)


def _settled(condition, what: str) -> None:  # noqa: ANN001
    """The condition holds twice in a row, a moment apart: the responder is not between taking a frame and counting it."""
    _wait(condition, what)
    time.sleep(0.05)
    _wait(condition, what)


def _drain(bus: SimulatedBus) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    while (frame := bus.recv(0.05)) is not None:
        out.append((frame.can_id, frame.data.hex().upper()))
    return out


def _lossy_run(seed: int) -> tuple[list[tuple[int, str]], fake_urtc.FaultyBus, FakeUrtc]:
    host, device = SimulatedBus.make_pair()
    link = fake_urtc.FaultyBus(device, seed=seed, drop=0.2, duplicate=0.1, corrupt=0.15)
    responder = FakeUrtc(FakeUrtcConfig(tool_id=5, patch=2))
    stop = threading.Event()
    thread = threading.Thread(target=responder.serve, args=(link, stop), kwargs={"poll": 0.005})
    thread.start()
    for n in range(60):
        host.send(CanFrame(0x110 if n % 2 else 0x7F8))
    _settled(lambda: device._inbox.empty() and not link.pending, "the responder to take in every frame")  # noqa: SLF001
    stop.set()
    thread.join(5)
    return _drain(host), link, responder


def _bit_distance(a: tuple[int, str], b: tuple[int, str]) -> int | None:
    if len(a[1]) != len(b[1]):
        return None
    return bin(a[0] ^ b[0]).count("1") + bin(int(a[1] or "0", 16) ^ int(b[1] or "0", 16)).count("1")


def test_a_lossy_link_breaks_frames_the_same_way_on_every_run_and_every_answer_is_right_or_one_bit_off() -> None:
    first, link, responder = _lossy_run(SEED)
    second, _, _ = _lossy_run(SEED)
    other, _, _ = _lossy_run(SEED + 1)
    assert first == second and first != other
    assert link.dropped > 0 and link.duplicated > 0 and link.corrupted > 0
    assert responder.bus_errors == 0
    valid = {(f.can_id, f.data.hex().upper()) for request in (0x110, 0x7F8) for f in FakeUrtc(FakeUrtcConfig(tool_id=5, patch=2)).handle(CanFrame(request))}
    assert first, "some answers must get through"
    for answer in first:
        assert answer in valid or any(_bit_distance(answer, good) == 1 for good in valid), answer


def test_a_link_that_breaks_nothing_changes_nothing() -> None:
    host, device = SimulatedBus.make_pair()
    link = fake_urtc.FaultyBus(device, seed=SEED)
    stop = threading.Event()
    thread = threading.Thread(target=FakeUrtc().serve, args=(link, stop), kwargs={"poll": 0.005})
    thread.start()
    host.send(CanFrame(0x110))
    _wait(lambda: host._inbox.qsize() >= 1, "the answer")  # noqa: SLF001
    stop.set()
    thread.join(5)
    assert _drain(host) == [(0x111, "000000000008")]
    assert (link.dropped, link.duplicated, link.corrupted, link.refused) == (0, 0, 0, 0)


def test_a_link_must_be_given_chances_between_zero_and_one() -> None:
    host, _ = SimulatedBus.make_pair()
    for name in ("drop", "duplicate", "corrupt"):
        with pytest.raises(ValueError, match=name):
            fake_urtc.FaultyBus(host, seed=1, **{name: 1.5})


def test_an_interface_that_goes_down_does_not_stop_the_head_and_it_answers_when_the_interface_is_back() -> None:
    host, device = SimulatedBus.make_pair()
    link = fake_urtc.FaultyBus(device, seed=SEED)
    responder = FakeUrtc()
    stop = threading.Event()
    thread = threading.Thread(target=responder.serve, args=(link, stop), kwargs={"poll": 0.005})
    thread.start()
    link.go_down()
    _wait(lambda: responder.bus_errors >= 3, "the failures to be counted")  # the responder is now only failing, so it takes in nothing
    host.send(CanFrame(0x110))
    time.sleep(0.1)
    assert host.recv(0.05) is None  # nothing was answered while the interface was down
    link.come_back()
    _wait(lambda: host._inbox.qsize() >= 1, "the answer after the interface came back")  # noqa: SLF001
    stop.set()
    thread.join(5)
    assert _drain(host) == [(0x111, "000000000008")]
    assert not thread.is_alive()


def test_answers_that_cannot_be_sent_are_lost_and_counted_and_the_next_one_goes_out() -> None:
    host, device = SimulatedBus.make_pair()
    link = fake_urtc.FaultyBus(device, seed=SEED)
    link.fail_sends(2)
    responder = FakeUrtc()
    stop = threading.Event()
    thread = threading.Thread(target=responder.serve, args=(link, stop), kwargs={"poll": 0.005})
    thread.start()
    for _ in range(3):
        host.send(CanFrame(0x110))
    _settled(lambda: device._inbox.empty() and link.refused == 2, "the three queries to be taken in")  # noqa: SLF001
    stop.set()
    thread.join(5)
    assert _drain(host) == [(0x111, "000000000008")]
    assert responder.bus_errors == 2 and link.refused == 2


def test_bytes_of_any_kind_from_a_socket_never_break_the_reader() -> None:
    rng = random.Random(SEED)
    seen_valid = 0
    for _ in range(3000):
        if rng.random() < 0.5:
            raw = bytes(rng.randrange(256) for _ in range(rng.choice([0, 3, 15, 16, 16, 16, 20])))
        else:  # a frame of the right size with an identifier, a length and flags of every kind
            can_id = rng.choice([rng.randrange(0x800), rng.randrange(0x800, 0x1000000), rng.randrange(0x1000000) | 0xE0000000])
            raw = can_id.to_bytes(4, "little") + bytes([rng.randrange(14)]) + bytes(3) + bytes(rng.randrange(256) for _ in range(8))
        frame = fake_urtc.unpack_frame(raw)
        if frame is None:
            continue
        seen_valid += 1
        assert fake_urtc.unpack_frame(fake_urtc.pack_frame(frame)) == frame
        FakeUrtc().handle(frame)  # any frame that unpacks can be handled
    assert seen_valid > 0
