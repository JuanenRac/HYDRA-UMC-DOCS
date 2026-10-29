# =============================================================================
# HYDRA-UMC-DOCS - tests/test_readme_universal.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The universal README layout: the words in eight languages, the Jump to line, the sources and their prose files."""
from __future__ import annotations

from pathlib import Path

import pytest

from hydra_umc_docs import glance, glance_jump, readme_kit as K, readme_universal as U
from hydra_umc_docs.readme_src import bridge_kit as B

SRC = Path(__file__).resolve().parents[1] / "src" / "hydra_umc_docs" / "readme_src"
SOURCES = sorted(path.stem for path in (SRC / "repos").glob("HYDRA_UMC*.py"))


def test_a_text_in_eight_languages_has_all_eight():
    text = K.P("a", "b", "c", "d", "e", "f", "g", "h")
    assert list(text) == K.LGS
    assert K.pick(text, "pt") == "h" and K.pick("same", "ja") == "same"


def test_the_shared_sentences_exist_in_every_language():
    for name in ("LANGUAGES_TEXT", "NO_UI", "CONTRIB", "JUMP", "ROLE_NAME"):
        assert set(getattr(K, name)) == set(K.LGS), name
    for name in ("MQTT_ENV_ROWS", "BUILD_ROWS"):
        for row in getattr(B, name):
            assert all(set(cell) == set(K.LGS) for cell in row[1:]), name
    assert set(B.BUILD_GENERIC) == set(K.LGS)


def test_h3_split_gives_the_text_before_and_the_parts():
    pre, parts = K.h3_split("intro\n\n### One\n\nbody one\n\n### Two\n\nbody two\n")
    assert pre == "intro"
    assert parts == [("One", "body one"), ("Two", "body two")]


def test_the_jump_line_follows_the_sections_the_readme_has():
    present = ["glance", "status", "overview", "architecture", "security", "structure", "related", "documentation", "author", "license"]
    line = U.jump_line("en", present)
    assert line.startswith("**Jump to:**") and "[Overview](#-overview)" in line and "[Interfaces]" not in line
    text = "## 📋 At a glance\n\n```\n## 🎯 not a heading\n```\n\n## 🚦 Project status\n\n## 🏛️ Architecture\n"
    assert U.present_sections(text) == ["glance", "status", "architecture"]


def test_a_readme_in_the_old_layout_is_left_as_glance_writes_it(tmp_path):
    assert glance_jump.migrated("## 📋 At a glance\n\n## 🎯 Overview\n") is False
    assert glance_jump.migrated("## 📋 At a glance\n\n## 🏛️ Architecture\n") is True


@pytest.mark.parametrize("name", SOURCES)
def test_every_source_has_its_prose_files_in_the_eight_languages(name):
    repo = name.replace("_", "-")
    module = U.load_source(repo)
    # a source may give its own roadmap text (EXTRAS) instead of a prose file
    own = set(getattr(module, "EXTRAS", {})) | set(getattr(module, "OWN_PROSE", ()))
    for lg in K.LGS:
        for key in ("tagline", "honesty", "overview", "roadmap", "related"):
            if key in own:
                continue
            assert (SRC / "verbatim" / repo / lg / f"{key}.txt").is_file(), (repo, lg, key)
    assert module.ICON and module.COMMENT and module.BADGES is not None


def test_the_names_of_the_sections_come_from_the_check():
    assert U.section_name("en", "role") == "Role in HYDRA-UMC"
    assert U.section_name("pt", "roadmap").startswith("Roteiro")
    assert [section for section, _ in U.SECTIONS][0] == "glance" and len(U.SECTIONS) == 22
