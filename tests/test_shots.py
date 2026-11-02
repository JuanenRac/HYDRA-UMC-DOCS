# =============================================================================
# HYDRA-UMC-DOCS - tests/test_shots.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The Screenshots section: read from docs/screenshots.json, checked (eight languages, files, weight) and rendered picture plus caption."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from hydra_umc_docs.readme_src import shots

TOOL = Path(__file__).resolve().parents[1] / "tools" / "screenshots_check.py"
PNG = shots.PNG_MAGIC + b"\x00" * 32


def texts(prefix: str) -> dict[str, str]:
    return {lg: f"{prefix} {lg}" for lg in shots.LANGS}


def make_repo(tmp_path: Path, screens: list[dict], files: dict[str, bytes] | None = None) -> Path:
    repo = tmp_path / "HYDRA-UMC-DEMO"
    (repo / "docs").mkdir(parents=True)
    (repo / "images" / "screenshots").mkdir(parents=True)
    (repo / "docs" / "screenshots.json").write_text(json.dumps({"screens": screens}), encoding="utf-8")
    for name, data in (files or {}).items():
        (repo / "images" / "screenshots" / name).write_bytes(data)
    return repo


def screen(name: str = "overview.png") -> dict:
    return {"file": name, "alt": texts("alt"), "caption": texts("caption")}


def load_tool():
    spec = importlib.util.spec_from_file_location("shots_check_tool", TOOL)
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def test_a_repository_without_the_file_has_no_section(tmp_path):
    assert not shots.has(tmp_path) and shots.problems(tmp_path) == []


def test_a_good_manifest_renders_picture_and_caption_in_every_language(tmp_path):
    repo = make_repo(tmp_path, [screen()], {"overview.png": PNG})
    assert shots.problems(repo) == []
    for lg in shots.LANGS:
        body = shots.section(lg, repo)
        assert body.startswith(shots.NOTE[lg])
        assert f'<img src="images/screenshots/overview.png" alt="alt {lg}" width="100%">' in body
        assert f'<p align="center"><em>caption {lg}</em></p>' in body


def test_the_note_exists_in_eight_languages():
    assert set(shots.NOTE) == set(shots.LANGS)


def test_problems_name_a_missing_file_a_heavy_one_and_a_missing_language(tmp_path):
    broken = screen("gone.png")
    del broken["caption"]["ja"]
    heavy = screen("heavy.png")
    repo = make_repo(tmp_path, [broken, heavy, screen("fake.png")],
                     {"heavy.png": PNG + b"\x00" * shots.MAX_BYTES, "fake.png": b"GIF89a"})
    found = " | ".join(shots.problems(repo))
    assert "'caption' lacks ja" in found and "gone.png" in found and "does not exist" in found
    assert "heavy.png" in found and "at most" in found and "fake.png: not a PNG" in found
    with pytest.raises(ValueError):
        shots.section("en", repo)


def test_more_than_eight_screens_or_a_repeated_one_are_refused(tmp_path):
    many = [screen(f"s{i}.png") for i in range(shots.MAX_SHOTS + 1)]
    repo = make_repo(tmp_path, many, {f"s{i}.png": PNG for i in range(shots.MAX_SHOTS + 1)})
    assert any("at most 8" in problem for problem in shots.problems(repo))
    twice = make_repo(tmp_path / "b", [screen(), screen()], {"overview.png": PNG})
    assert any("listed twice" in problem for problem in shots.problems(twice))


def test_the_check_tool_wants_the_pictures_in_the_file_tree(tmp_path, capsys):
    tool = load_tool()
    repo = make_repo(tmp_path, [screen()], {"overview.png": PNG})
    assert tool.check_repository(repo) == []
    (repo / "docs" / "structure.json").write_text('{"items": ["overview.png"]}', encoding="utf-8")
    assert len(tool.check_repository(repo)) == 1 and "does not mention the screenshots" in tool.check_repository(repo)[0]
    (repo / "docs" / "structure.json").write_text('{"desc": "README banner and screenshots"}', encoding="utf-8")
    assert tool.main(["--repo", str(repo)]) == 0
    assert "SCREENSHOTS=PASS" in capsys.readouterr().out
