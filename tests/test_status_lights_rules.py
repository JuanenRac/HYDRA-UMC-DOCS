# =============================================================================
# HYDRA-UMC-DOCS - tests/test_status_lights_rules.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
#
# The rules that keep the traffic lights of the "Project status" table honest: what kind of row a label is, the highest light each kind of row may
# hold for every maturity and evidence, how the table is read and rewritten, and what `evaluate` and `problems_of` say about a throw-away repository.
# Nothing is ever allowed above its ceiling, and nothing here touches a real repository or asks GitHub.
# =============================================================================
from __future__ import annotations

import importlib.util
import itertools
import json
import random
from pathlib import Path

import pytest

TOOL = Path(__file__).resolve().parents[1] / "tools" / "status_lights.py"
spec = importlib.util.spec_from_file_location("status_lights_under_test", TOOL)
assert spec is not None and spec.loader is not None
sl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sl)

RED, ORANGE, YELLOW, GREEN = sl.RED, sl.ORANGE, sl.YELLOW, sl.GREEN


def rank(light: str) -> int:
    return sl.ORDER.index(light)


# --- the kind of a row ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "label, kind",
    [
        ("Hardware", "hardware"), ("Board bring-up", "hardware"), ("Firmware on the board", "hardware"), ("System integration", "integration"),
        ("Integration with the Server", "integration"), ("Hardware integration", "integration"), ("Tests", "tests"), ("Test coverage", "tests"),
        ("Documentation", "docs"), ("docs", "docs"), ("Software", "software"), ("  SOFTWARE  ", "software"), ("Roadmap", "other"), ("", "other"),
    ],
)
def test_the_kind_of_a_row_comes_from_its_english_label(label, kind) -> None:
    assert sl.kind_of(label) == kind


# --- the ceiling -----------------------------------------------------------------------------------------------------------------------------
def test_hardware_rows_are_limited_by_the_evidence() -> None:
    expected = {"none": ORANGE, "host-test": ORANGE, "simulator": ORANGE, "bench": YELLOW, "field": GREEN}
    for kind in ("hardware", "integration"):
        for evidence, top in expected.items():
            assert sl.ceiling(kind, {"evidence": evidence}, True, True, "green")[0] == top, (kind, evidence)


def test_a_simulator_never_lifts_a_hardware_row_above_orange() -> None:
    top, why = sl.ceiling("hardware", {"evidence": "simulator", "maturity": "established"}, True, True, "green")
    assert top == ORANGE
    assert "simulator" in why


def test_an_unknown_evidence_is_treated_as_the_lowest() -> None:
    assert sl.ceiling("hardware", {"evidence": "wishful"}, True, True, "green")[0] == ORANGE
    assert sl.ceiling("hardware", {}, True, True, "green")[0] == ORANGE


def test_a_manifest_without_hardware_does_not_limit_those_rows() -> None:
    assert sl.ceiling("hardware", {"evidence": "none", "hardware_bound": False}, True, True, "green")[0] == GREEN
    assert sl.ceiling("hardware", {"evidence": "none", "hardware_bound": True}, True, True, "green")[0] == ORANGE
    assert sl.ceiling("hardware", {"evidence": "none", "hardware_bound": None}, True, True, "green")[0] == ORANGE


def test_software_tests_and_docs_need_tests_and_a_workflow_and_a_green_run() -> None:
    for kind in ("software", "tests", "docs"):
        assert sl.ceiling(kind, {}, True, True, "green")[0] == GREEN
        assert sl.ceiling(kind, {}, True, True, "unknown")[0] == GREEN
        top, why = sl.ceiling(kind, {}, False, True, "green")
        assert (top, why) == (YELLOW, "no tests in the repository")
        assert sl.ceiling(kind, {}, True, False, "green") == (YELLOW, "no CI workflow")
        assert sl.ceiling(kind, {}, True, True, "red") == (YELLOW, "the CI of the default branch is red")


def test_other_rows_are_not_limited_by_tests_or_evidence() -> None:
    assert sl.ceiling("other", {"evidence": "none"}, False, False, "red")[0] == GREEN


@pytest.mark.parametrize("maturity", ["scaffolding", "experimental", "alpha", "prototype", "Alpha", "PROTOTYPE"])
def test_a_young_repository_is_yellow_at_most_on_every_row(maturity) -> None:
    for kind in ("hardware", "integration", "software", "tests", "docs", "other"):
        assert rank(sl.ceiling(kind, {"maturity": maturity, "evidence": "field"}, True, True, "green")[0]) <= rank(YELLOW), kind


@pytest.mark.parametrize("maturity", ["functional", "established", "stable", "", None])
def test_an_older_repository_is_not_limited_by_its_maturity(maturity) -> None:
    assert sl.ceiling("other", {"maturity": maturity}, True, True, "green")[0] == GREEN


def test_no_combination_can_exceed_what_the_evidence_allows() -> None:
    kinds = ["hardware", "integration", "software", "tests", "docs", "other"]
    evidences = [*sl.EVIDENCE_LEVELS, "bogus", None]
    maturities = ["scaffolding", "functional", None]
    for kind, evidence, maturity, tests, ci, ci_now, bound in itertools.product(kinds, evidences, maturities, (True, False), (True, False), ("green", "red", "unknown"), (True, False)):
        manifest = {"evidence": evidence, "maturity": maturity, "hardware_bound": bound}
        top, _ = sl.ceiling(kind, manifest, tests, ci, ci_now)
        assert top in sl.ORDER
        if kind in ("hardware", "integration") and bound:
            assert rank(top) <= rank(sl.EVIDENCE_CEILING.get(evidence, ORANGE))
        if kind in ("software", "tests", "docs") and not (tests and ci):
            assert rank(top) <= rank(YELLOW)
        if maturity == "scaffolding":
            assert rank(top) <= rank(YELLOW)


# --- the repository facts ------------------------------------------------------------------------------------------------------------------------------
def test_tests_are_found_by_folder_or_by_file_name_and_vendored_folders_are_skipped(tmp_path: Path) -> None:
    assert sl.has_tests(tmp_path) is False
    (tmp_path / "node_modules" / "pkg" / "tests").mkdir(parents=True)
    (tmp_path / "node_modules" / "pkg" / "tests" / "t.js").write_text("x", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    assert sl.has_tests(tmp_path) is False  # an empty tests folder is not tests
    (tmp_path / "tests" / "case.py").write_text("x", encoding="utf-8")
    assert sl.has_tests(tmp_path) is True


def test_a_test_file_name_alone_counts(tmp_path: Path) -> None:
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "widget.test.ts").write_text("x", encoding="utf-8")
    assert sl.has_tests(tmp_path) is True


def test_a_workflow_file_is_the_ci(tmp_path: Path) -> None:
    assert sl.has_ci(tmp_path) is False
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    assert sl.has_ci(tmp_path) is False
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text("on: push", encoding="utf-8")
    assert sl.has_ci(tmp_path) is True


def test_the_ci_state_is_unknown_without_gh_or_without_a_completed_run_on_the_default_branch(tmp_path: Path, monkeypatch) -> None:
    import subprocess

    def missing(*_a, **_k):
        raise FileNotFoundError("gh")

    monkeypatch.setattr(sl.subprocess, "run", missing)
    assert sl.ci_state(tmp_path) == "unknown"

    def answer(runs):
        return lambda *_a, **_k: subprocess.CompletedProcess([], 0, stdout=json.dumps(runs), stderr="")

    monkeypatch.setattr(sl.subprocess, "run", answer([]))
    assert sl.ci_state(tmp_path) == "unknown"
    monkeypatch.setattr(sl.subprocess, "run", answer([{"status": "in_progress", "headBranch": "main", "conclusion": None}, {"status": "completed", "headBranch": "feature", "conclusion": "failure"}]))
    assert sl.ci_state(tmp_path) == "unknown"
    monkeypatch.setattr(sl.subprocess, "run", answer([{"status": "completed", "headBranch": "main", "conclusion": "success"}]))
    assert sl.ci_state(tmp_path) == "green"
    monkeypatch.setattr(sl.subprocess, "run", answer([{"status": "completed", "headBranch": "master", "conclusion": "failure"}, {"status": "completed", "headBranch": "main", "conclusion": "success"}]))
    assert sl.ci_state(tmp_path) == "red"  # the newest completed run of the default branch decides
    monkeypatch.setattr(sl.subprocess, "run", lambda *_a, **_k: subprocess.CompletedProcess([], 1, stdout="not json", stderr=""))
    assert sl.ci_state(tmp_path) == "unknown"


# --- the table -----------------------------------------------------------------------------------------------------------------------------------------------
def readme(rows: list[tuple[str, str]], heading: str = "## \U0001F6A6 Project status") -> str:
    lines = ["# Project", "", "intro", "", heading, "", "| Part | Status | Notes |", "| --- | --- | --- |"]
    lines += [f"| {label} | {light} | a note \\| with a pipe |" for label, light in rows]
    lines += ["", "## Next", "", "text"]
    return "\n".join(lines)


ROWS = [("Hardware", ORANGE), ("Software", GREEN), ("Tests", YELLOW)]


def test_the_table_is_read_row_by_row_with_an_escaped_pipe_kept() -> None:
    first, rows = sl.read_table(readme(ROWS))
    assert first == 8
    assert [row[0] for row in rows] == ["Hardware", "Software", "Tests"]
    assert sl.lights_of(rows) == [ORANGE, GREEN, YELLOW]
    assert rows[0][2] == "a note \\| with a pipe"


def test_a_readme_without_the_table_or_with_no_rows_gives_none() -> None:
    assert sl.read_table("# Title\n\ntext\n") is None
    assert sl.read_table("## \U0001F6A6 Project status\n\n| Part | Status |\n| --- | --- |\n\n## Next") is None
    assert sl.read_table("## Project status\n\n| Part | Status |\n| --- | --- |\n| A | x |") is None  # the heading needs its sign


def test_the_table_inside_a_code_fence_is_ignored() -> None:
    fenced = "```\n" + readme(ROWS) + "\n```\n"
    assert sl.read_table(fenced) is None


def test_the_table_ends_at_the_next_heading() -> None:
    text = readme(ROWS) + "\n\n| Not | Part |\n| - | - |\n| X | Y |"
    assert len(sl.read_table(text)[1]) == 3


def test_a_row_with_one_cell_has_an_empty_light() -> None:
    assert sl.lights_of([["only"], ["a", RED]]) == ["", RED]


def test_lights_are_replaced_in_place_and_nothing_else_changes() -> None:
    text = readme(ROWS)
    changed = sl.replace_lights(text, [RED, YELLOW, YELLOW])
    assert sl.lights_of(sl.read_table(changed)[1]) == [RED, YELLOW, YELLOW]
    again = sl.replace_lights(changed, [ORANGE, GREEN, YELLOW])
    assert again == text
    assert changed.count("\n") == text.count("\n")


def test_replacing_with_fewer_lights_changes_only_those_rows() -> None:
    changed = sl.replace_lights(readme(ROWS), [RED])
    assert sl.lights_of(sl.read_table(changed)[1]) == [RED, GREEN, YELLOW]


# --- evaluate and problems_of ------------------------------------------------------------------------------------------------------------------------------
def make_repo(tmp_path: Path, manifest: dict, rows=ROWS, tests: bool = True, ci: bool = True, languages: bool = False) -> Path:
    root = tmp_path / "HYDRA-UMC-DEMO"
    root.mkdir()
    (root / "demo.project.json").write_text(json.dumps(manifest), encoding="utf-8")
    (root / "README.md").write_text(readme(rows), encoding="utf-8")
    if tests:
        (root / "tests").mkdir()
        (root / "tests" / "test_demo.py").write_text("x", encoding="utf-8")
    if ci:
        (root / ".github" / "workflows").mkdir(parents=True)
        (root / ".github" / "workflows" / "ci.yml").write_text("on: push", encoding="utf-8")
    if languages:
        for name in sl.LANGUAGE_FILES[1:]:
            (root / name).write_text(readme(rows), encoding="utf-8")
    return root


def test_evaluate_gives_every_row_its_kind_and_ceiling(tmp_path: Path) -> None:
    root = make_repo(tmp_path, {"evidence": "simulator", "maturity": "established"})
    state = sl.evaluate(root, "off")
    assert [(i["kind"], i["ceiling"]) for i in state["items"]] == [("hardware", ORANGE), ("software", GREEN), ("tests", GREEN)]
    assert state["ci"] == "unknown"


def test_a_light_above_its_ceiling_is_a_problem_that_names_the_reason(tmp_path: Path) -> None:
    root = make_repo(tmp_path, {"evidence": "none", "maturity": "established"}, rows=[("Hardware", GREEN), ("Software", GREEN), ("Tests", GREEN)])
    problems = sl.problems_of(root, sl.evaluate(root, "off"))
    assert len(problems) == 1
    assert "Hardware" in problems[0] and "green" in problems[0] and "orange" in problems[0] and "evidence none" in problems[0]


def test_lights_at_or_below_the_ceiling_are_fine(tmp_path: Path) -> None:
    root = make_repo(tmp_path, {"evidence": "simulator", "maturity": "established", "hardware_bound": True}, rows=[("Hardware", ORANGE), ("Software", GREEN), ("Tests", RED)])
    assert sl.problems_of(root, sl.evaluate(root, "off")) == []


def test_without_tests_or_a_workflow_software_cannot_be_green(tmp_path: Path) -> None:
    root = make_repo(tmp_path, {"evidence": "none"}, tests=False, ci=False)
    assert any("Software" in p for p in sl.problems_of(root, sl.evaluate(root, "off")))


def test_the_manifest_must_name_an_evidence_that_exists(tmp_path: Path) -> None:
    missing = make_repo(tmp_path, {"maturity": "established"})
    assert any("no 'evidence'" in p for p in sl.problems_of(missing, sl.evaluate(missing, "off")))
    bogus_parent = tmp_path / "other"
    bogus_parent.mkdir()
    bogus = make_repo(bogus_parent, {"evidence": "wishful"})
    assert any("wishful" in p for p in sl.problems_of(bogus, sl.evaluate(bogus, "off")))


def test_a_word_in_place_of_a_light_is_a_problem(tmp_path: Path) -> None:
    root = make_repo(tmp_path, {"evidence": "none"}, rows=[("Hardware", "green"), ("Software", GREEN), ("Tests", GREEN)])
    assert any("not a light" in p for p in sl.problems_of(root, sl.evaluate(root, "off")))


def test_the_translations_must_carry_the_same_lights(tmp_path: Path) -> None:
    root = make_repo(tmp_path, {"evidence": "simulator"}, languages=True)
    assert sl.problems_of(root, sl.evaluate(root, "off")) == []
    (root / "README_deu.md").write_text(readme([("Hardware", RED), ("Software", GREEN), ("Tests", YELLOW)]), encoding="utf-8")
    (root / "README_jpn.md").write_text("# no table here", encoding="utf-8")
    problems = sl.problems_of(root, sl.evaluate(root, "off"))
    assert any("README_deu.md" in p and "differ" in p for p in problems)
    assert any("README_jpn.md" in p and "no Project status table" in p for p in problems)


def test_a_repository_without_a_manifest_or_a_table_stops_with_one_line(tmp_path: Path, capsys) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    with pytest.raises(SystemExit) as caught:
        sl.manifest_of(empty)
    assert caught.value.code == 1
    assert "STATUS_LIGHTS=FAIL" in capsys.readouterr().err
    root = make_repo(tmp_path, {"evidence": "none"})
    (root / "README.md").write_text("# no table", encoding="utf-8")
    with pytest.raises(SystemExit):
        sl.evaluate(root, "off")
    (root / "demo.project.json").write_text("{broken", encoding="utf-8")
    with pytest.raises(SystemExit):
        sl.manifest_of(root)


def test_a_seeded_set_of_random_manifests_never_passes_a_light_above_its_ceiling(tmp_path: Path) -> None:
    rng = random.Random(20261113)
    for index in range(60):
        manifest = {
            "evidence": rng.choice([*sl.EVIDENCE_LEVELS, None]),
            "maturity": rng.choice(["scaffolding", "alpha", "functional", "established"]),
            "hardware_bound": rng.choice([True, False]),
        }
        manifest = {k: v for k, v in manifest.items() if v is not None}
        lights = [rng.choice(sl.ORDER) for _ in ROWS]
        parent = tmp_path / f"r{index}"
        parent.mkdir()
        root = make_repo(parent, manifest, rows=[(label, light) for (label, _), light in zip(ROWS, lights, strict=True)], tests=rng.random() < 0.8, ci=rng.random() < 0.8)
        state = sl.evaluate(root, "off")
        problems = [p for p in sl.problems_of(root, state) if "ceiling" in p]
        above = [i for i in state["items"] if rank(i["light"]) > rank(i["ceiling"])]
        assert len(problems) == len(above)
