# =============================================================================
# HYDRA-UMC-DOCS - tests/test_urtc_tools_and_ledger.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
from __future__ import annotations

import json
from pathlib import Path

import pytest
from conftest import make_manifest, write_repo

from hydra_umc_docs import cli, ledger, urtc_tools

HEADER = """
typedef enum { OTHER_A = 0, OTHER_B = 1 } SomethingElse_t;
typedef enum {
    TOOL_SOLDERING_IRON = 0,  // note
    TOOL_DRILL          = 1,
    // TOOL_GHOST = 9,
    TOOL_3D_PRINTER     = 2,
    TOOL_INVALID        = 25
} ToolMode_t;
"""
TEXT = """
1. Soldering Station (T12) - ID 0x00
Expansion board: none needed.

2. Drill (BL4260) - ID 0x01
Expansion board: required - either variant.

3. 3D Printing Hotend - ID 0x02
Expansion board: recommended if the head sits far.
"""


def _urtc(tmp_path: Path, header: str = HEADER, text: str = TEXT) -> Path:
    root = tmp_path / "URTC"
    (root / "src" / "F303-master").mkdir(parents=True)
    (root / "docs").mkdir()
    (root / urtc_tools.HEADER).write_text(header, encoding="utf-8")
    (root / urtc_tools.TOOLS_TEXT).write_text(text, encoding="utf-8")
    return root


def test_the_catalogue_is_built_from_the_enum_and_the_headings(tmp_path: Path) -> None:
    catalog = urtc_tools.build(_urtc(tmp_path))
    assert catalog["invalid_tool_id"] == 25
    assert [(t["tool_id"], t["name"], t["title"], t["expansion"]) for t in catalog["tools"]] == [
        (0, "TOOL_SOLDERING_IRON", "Soldering Station (T12)", "none"),
        (1, "TOOL_DRILL", "Drill (BL4260)", "required"),
        (2, "TOOL_3D_PRINTER", "3D Printing Hotend", "recommended"),
    ]


def test_an_enum_and_a_text_that_disagree_are_an_error(tmp_path: Path) -> None:
    with pytest.raises(urtc_tools.ToolCatalogError, match="disagree"):
        urtc_tools.build(_urtc(tmp_path, text=TEXT.split("3. 3D")[0]))
    with pytest.raises(urtc_tools.ToolCatalogError, match="twice"):
        urtc_tools.parse_enum("typedef enum { TOOL_A = 1, TOOL_B = 1 } ToolMode_t;")
    with pytest.raises(urtc_tools.ToolCatalogError, match="not found"):
        urtc_tools.parse_enum("typedef enum { TOOL_A = 1 } Other_t;")
    with pytest.raises(urtc_tools.ToolCatalogError, match="cannot be read"):
        urtc_tools.build(tmp_path / "missing")


def test_resolve_accepts_what_a_client_may_send_and_nothing_else(tmp_path: Path) -> None:
    catalog = urtc_tools.build(_urtc(tmp_path))
    for value in (1, "1", "0x01", "TOOL_DRILL", "drill", "Drill (BL4260)", " DRILL "):
        found = urtc_tools.resolve(catalog, value)
        assert found is not None and found["tool_id"] == 1, value
    assert urtc_tools.resolve(catalog, "3d printer")["tool_id"] == 2  # type: ignore[index]
    for value in (True, 25, 3, -1, "", "laser", None, 1.0, "0x1FF", "TOOL_INVALID"):
        assert urtc_tools.resolve(catalog, value) is None, value


def test_descriptors_need_the_kinds_and_are_never_guessed(tmp_path: Path) -> None:
    catalog = urtc_tools.build(_urtc(tmp_path))
    with pytest.raises(urtc_tools.ToolCatalogError, match="no kind"):
        urtc_tools.to_descriptors(catalog, {0: "actuator"})
    with pytest.raises(urtc_tools.ToolCatalogError):
        urtc_tools.to_descriptors(catalog, {0: "actuator", 1: "weird", 2: "motion"})
    descriptors = urtc_tools.to_descriptors(catalog, {0: "actuator", 1: "motion", 2: "actuator"})
    assert descriptors[1] == {"schema_version": "1.0", "tool_id": 1, "name": "TOOL_DRILL", "title": "Drill (BL4260)", "kind": "motion"}


def test_the_check_notices_a_stale_data_file(tmp_path: Path) -> None:
    root = _urtc(tmp_path)
    data = tmp_path / "tools.json"
    data.write_text(urtc_tools.render(urtc_tools.build(root)), encoding="utf-8")
    assert urtc_tools.check(data, root)[0] is True
    (root / urtc_tools.TOOLS_TEXT).write_text(TEXT.replace("Drill (BL4260)", "Drill"), encoding="utf-8")
    ok, message = urtc_tools.check(data, root)
    assert ok is False and "no longer matches" in message


def test_the_shipped_catalogue_is_complete_and_valid() -> None:
    catalog = urtc_tools.load(cli.TOOLS_FILE)
    assert [t["tool_id"] for t in catalog["tools"]] == list(range(25)) and catalog["invalid_tool_id"] == 25
    assert len({t["name"] for t in catalog["tools"]}) == 25
    for tool in catalog["tools"]:
        assert urtc_tools._NAME.fullmatch(tool["name"]) and tool["expansion"] in urtc_tools.EXPANSIONS
    assert urtc_tools.resolve(catalog, "TOOL_DRILL")["tool_id"] == 5  # type: ignore[index]


def test_the_shipped_catalogue_matches_urtc_when_it_is_next_to_this_repository() -> None:
    urtc = cli.REPO.parent / "URTC"
    if not (urtc / urtc_tools.HEADER).is_file():
        pytest.skip("URTC is not next to this repository")
    assert urtc_tools.check(cli.TOOLS_FILE, urtc)[0] is True


def test_the_command_writes_checks_and_skips(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    _urtc(tmp_path)
    target = tmp_path / "out.json"
    assert cli.make_urtc_tools(["--workspace", str(tmp_path), "--data", str(target)]) == 0
    assert "WRITTEN" in capsys.readouterr().out and target.is_file()
    assert cli.make_urtc_tools(["--workspace", str(tmp_path), "--data", str(target), "--check"]) == 0
    assert cli.make_urtc_tools(["--workspace", str(tmp_path), "--data", str(target)]) == 0
    assert "already current" in capsys.readouterr().out
    target.write_text("{}", encoding="utf-8")
    assert cli.make_urtc_tools(["--workspace", str(tmp_path), "--data", str(target), "--check"]) == 1
    empty = tmp_path / "empty"
    empty.mkdir()
    assert cli.make_urtc_tools(["--workspace", str(empty)]) == 0
    assert cli.make_urtc_tools(["--workspace", str(empty), "--require-siblings"]) == 1


# --- the ledger ---------------------------------------------------------------------------------------------------


def _manifest(name: str, **fields: object) -> dict:
    return make_manifest(name, **fields)


def test_the_ledger_pairs_each_maturity_with_its_evidence() -> None:
    manifests = [
        _manifest("HYDRA-UMC-B", maturity="established", evidence="host-test", hardware_bound=False),
        _manifest("HYDRA-UMC-A", maturity="functional", evidence="simulator", hardware_bound=True),
        _manifest("HYDRA-UMC-C", maturity="scaffolding"),
        _manifest("HYDRA-UMC-D", maturity="functional", evidence="soak test"),
    ]
    built = ledger.build(manifests, {"repos": {"HYDRA-UMC-A": {"hardware": "simulated"}}})
    rows = {row["name"]: row for row in built["repos"]}
    assert list(rows) == ["HYDRA-UMC-A", "HYDRA-UMC-B", "HYDRA-UMC-C", "HYDRA-UMC-D"]
    assert rows["HYDRA-UMC-A"]["colour"] == "warn" and rows["HYDRA-UMC-A"]["gaps"] == ["hardware-bound-not-on-hardware"]
    assert rows["HYDRA-UMC-A"]["hardware_statement"] == "simulated"
    assert rows["HYDRA-UMC-B"]["colour"] == "info" and rows["HYDRA-UMC-B"]["gaps"] == []
    assert rows["HYDRA-UMC-C"]["evidence"] == "none" and rows["HYDRA-UMC-C"]["gaps"] == []  # scaffolding needs no evidence
    assert rows["HYDRA-UMC-D"]["evidence"] == "other"
    assert built["summary"]["repositories"] == 4 and built["summary"]["by_evidence"] == {"host-test": 1, "none": 1, "other": 1, "simulator": 1}


def test_a_functional_project_without_evidence_is_a_gap_and_hardware_closes_the_hardware_gap() -> None:
    rows = {r["name"]: r for r in ledger.build([_manifest("X-A", maturity="functional"), _manifest("X-B", maturity="functional", evidence="bench", hardware_bound=True)], {})["repos"]}
    assert rows["X-A"]["gaps"] == ["no-evidence-recorded"]
    assert rows["X-B"]["gaps"] == [] and rows["X-B"]["colour"] == "ok_soft"


def test_the_labels_exist_in_the_eight_languages() -> None:
    built = ledger.build([_manifest("X-A")], {})
    for kind in built["evidence_kinds"]:
        assert set(kind["label"]) == set(ledger.LANGUAGES) and all(kind["label"].values())
    for gap in built["gaps"]:
        assert set(gap["label"]) == set(ledger.LANGUAGES) and all(gap["label"].values())
    assert {k["colour"] for k in built["evidence_kinds"]} <= {"neutral", "info", "warn", "ok_soft", "ok"}


def test_the_ledger_holds_no_date_and_no_version() -> None:
    text = ledger.render(ledger.build([_manifest("X-A", version="9.9.9")], {}))
    assert "9.9.9" not in text and "version" not in text.replace("schema_version", "")


def test_the_check_and_the_command(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    write_repo(tmp_path, "HYDRA-UMC-A", evidence="host-test")
    write_repo(tmp_path, "HYDRA-UMC-B")
    target = tmp_path / "ledger.json"
    assert cli.make_ledger(["--workspace", str(tmp_path), "--data", str(target)]) == 0
    assert "WRITTEN 2 repositories" in capsys.readouterr().out
    assert cli.make_ledger(["--workspace", str(tmp_path), "--data", str(target), "--check"]) == 0
    data = json.loads(target.read_text(encoding="utf-8"))
    data["repos"][0]["evidence"] = "hardware"
    target.write_text(json.dumps(data), encoding="utf-8")
    assert cli.make_ledger(["--workspace", str(tmp_path), "--data", str(target), "--check"]) == 1
    lone = tmp_path / "lone"
    lone.mkdir()
    assert cli.make_ledger(["--workspace", str(lone)]) == 0
    assert cli.make_ledger(["--workspace", str(lone), "--require-siblings"]) == 1
