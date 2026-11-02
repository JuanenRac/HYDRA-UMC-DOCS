# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/urtc_tools.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The common catalogue of the URTC tool heads (`ToolMode_t`, tools 0 to 24).

Today the server and the clients carry the tool as a free string, with no relation to the enum of the URTC
firmware. This module reads the two places where URTC states the tools (the enum of `firmware_common.h` and the
headings of `docs/TOOLS.TXT`) and writes `data/urtc_tools.json`: for each tool its number, its constant name, its
title and whether it needs an expansion board. The entries are the static part of the `ToolDescriptor` contract of
the SDK (`tool_id`, `name`, `title`); the `kind` that contract requires is a classification nobody has made yet, so
it is not invented here: `to_descriptors` builds descriptors only when it is given the kinds.

The data file is derived, not typed: `check` says when it no longer matches the URTC sources that sit next to this
repository. `resolve` turns what a client sends (a number, a constant name or a title) into the one tool it means,
or None, which is what a server needs to stop accepting any string."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

URTC = "URTC"
HEADER = Path("src") / "F303-master" / "firmware_common.h"
TOOLS_TEXT = Path("docs") / "TOOLS.TXT"
SCHEMA_VERSION = "1.0"

_ENUM = re.compile(r"typedef\s+enum\s*\{(?P<body>[^{}]*)\}\s*ToolMode_t\s*;", re.DOTALL)
_ENTRY = re.compile(r"\b(TOOL_[A-Z0-9_]+)\s*=\s*(\d+)")
_HEADING = re.compile(r"^\d+\.\s+(?P<title>.+?)\s+-\s+ID\s+0x(?P<id>[0-9A-Fa-f]{2})\s*$")
_NAME = re.compile(r"[A-Z][A-Z0-9_]{0,63}")
KINDS = ("motion", "actuator", "telemetry", "external")
EXPANSIONS = ("none", "recommended", "required", "unknown")


class ToolCatalogError(ValueError):
    """The URTC sources cannot be read as a catalogue of tools."""


def parse_enum(header_text: str) -> tuple[dict[int, str], int | None]:
    """The tools of the enum as {number: constant}, and the number of `TOOL_INVALID` (the value that names no tool)."""
    found = _ENUM.search(header_text)
    if not found:
        raise ToolCatalogError("the ToolMode_t enum was not found in the firmware header")
    body = re.sub(r"//[^\n]*", "", found.group("body"))
    tools: dict[int, str] = {}
    invalid: int | None = None
    for name, number in _ENTRY.findall(body):
        value = int(number)
        if name == "TOOL_INVALID":
            invalid = value
        elif value in tools:
            raise ToolCatalogError(f"the tool number {value} is given twice in the enum")
        else:
            tools[value] = name
    return tools, invalid


def parse_tools_text(text: str) -> dict[int, dict[str, str]]:
    """The title and the expansion board of every tool of `TOOLS.TXT` as {number: {title, expansion}}."""
    result: dict[int, dict[str, str]] = {}
    current: int | None = None
    for line in text.replace("\r\n", "\n").split("\n"):
        heading = _HEADING.match(line)
        if heading:
            current = int(heading.group("id"), 16)
            result[current] = {"title": heading.group("title"), "expansion": "unknown"}
        elif current is not None and line.startswith("Expansion board") and result[current]["expansion"] == "unknown":
            lowered = line.lower()
            if "none needed" in lowered:
                result[current]["expansion"] = "none"
            elif "required" in lowered[:90]:
                result[current]["expansion"] = "required"
            elif "recommended" in lowered[:90]:
                result[current]["expansion"] = "recommended"
    return result


def build(urtc_root: Path) -> dict[str, Any]:
    """The catalogue made from a checkout of URTC."""
    try:
        header = (urtc_root / HEADER).read_text(encoding="utf-8", errors="replace")
        text = (urtc_root / TOOLS_TEXT).read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise ToolCatalogError(f"the URTC sources cannot be read: {exc}") from exc
    constants, invalid = parse_enum(header)
    described = parse_tools_text(text)
    if invalid is None:
        raise ToolCatalogError("the enum has no TOOL_INVALID: the first number that names no tool is unknown")
    missing = sorted(set(constants) - set(described))
    extra = sorted(set(described) - set(constants))
    if missing or extra:
        raise ToolCatalogError(f"the enum and TOOLS.TXT disagree (not in the text: {missing}; not in the enum: {extra})")
    tools = []
    for number in sorted(constants):
        if not _NAME.fullmatch(constants[number]):
            raise ToolCatalogError(f"{constants[number]} is not a valid tool name")
        tools.append({"tool_id": number, "name": constants[number], "title": described[number]["title"], "expansion": described[number]["expansion"]})
    return {"schema_version": SCHEMA_VERSION, "source": "URTC firmware_common.h (ToolMode_t) and docs/TOOLS.TXT", "invalid_tool_id": invalid, "tools": tools}


def render(catalog: dict[str, Any]) -> str:
    return json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"


def load(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ToolCatalogError(f"the catalogue {path} cannot be read: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("tools"), list):
        raise ToolCatalogError(f"{path} is not a catalogue of tools")
    return data


def check(path: Path, urtc_root: Path) -> tuple[bool, str]:
    """Whether the data file still matches the URTC sources."""
    try:
        wanted = render(build(urtc_root))
        current = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    except (ToolCatalogError, OSError) as exc:
        return False, str(exc)
    if current != wanted:
        return False, f"{path.name} no longer matches the URTC sources; write it again with make_urtc_tools.py"
    return True, f"{path.name} matches the URTC sources"


def _key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def resolve(catalog: dict[str, Any], value: object) -> dict[str, Any] | None:
    """The tool a client means by `value` (a number, a decimal or 0x text, a constant name with or without `TOOL_`, or a title), or None.
    A boolean is never a tool number; the number that names no tool is not a tool."""
    tools: list[dict[str, Any]] = catalog["tools"]
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return next((tool for tool in tools if tool["tool_id"] == value), None)
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    if re.fullmatch(r"\d{1,3}|0[xX][0-9A-Fa-f]{1,2}", text):
        return resolve(catalog, int(text, 16 if text[:2].lower() == "0x" else 10))
    wanted = _key(text)
    for tool in tools:
        if wanted in {_key(tool["name"]), _key(tool["name"].removeprefix("TOOL_")), _key(tool["title"])}:
            return tool
    return None


def to_descriptors(catalog: dict[str, Any], kinds: dict[int, str]) -> list[dict[str, Any]]:
    """`ToolDescriptor` objects (schema_version, tool_id, name, title, kind) for every tool, given the kind of each. A tool without a kind is an
    error: the kind is a classification that is not made here."""
    descriptors = []
    for tool in catalog["tools"]:
        kind = kinds.get(tool["tool_id"])
        if kind not in KINDS:
            raise ToolCatalogError(f"tool {tool['tool_id']} ({tool['name']}) has no kind among {', '.join(KINDS)}")
        descriptors.append({"schema_version": SCHEMA_VERSION, "tool_id": tool["tool_id"], "name": tool["name"], "title": tool["title"], "kind": kind})
    return descriptors
