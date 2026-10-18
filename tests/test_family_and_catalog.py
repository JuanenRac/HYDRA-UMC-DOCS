# =============================================================================
# HYDRA-UMC-DOCS - tests/test_family_and_catalog.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
from __future__ import annotations

import json
import re

import pytest
from conftest import make_manifest, write_repo

from hydra_umc_docs import catalog, family
from hydra_umc_docs.descriptions import DESCRIPTIONS


def test_family_names():
    assert family.is_family_name("HYDRA-UMC")
    assert family.is_family_name("HYDRA-UMC-SDK")
    assert not family.is_family_name("HYDRA-UMCX")
    assert not family.is_family_name("URTC")
    assert not family.is_family_name("ARMOR-DOCS")


def test_discover_ignores_other_folders_and_those_without_manifest(workspace):
    names = [repo.name for repo in family.discover(workspace)]
    assert names == ["HYDRA-UMC", "HYDRA-UMC-SERVER", "HYDRA-UMC-STUDIO"]


def test_read_manifest_checks_keys_and_name(tmp_path):
    repo = write_repo(tmp_path, "HYDRA-UMC-X")
    assert family.read_manifest(repo)["name"] == "HYDRA-UMC-X"
    data = make_manifest("HYDRA-UMC-X")
    del data["family"]
    (repo / "hydra-umc.project.json").write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError, match="family"):
        family.read_manifest(repo)
    (repo / "hydra-umc.project.json").write_text(json.dumps(make_manifest("HYDRA-UMC-OTHER")), encoding="utf-8")
    with pytest.raises(ValueError, match="manifest name"):
        family.read_manifest(repo)


def test_describe_prefers_the_curated_sentence_and_falls_back_to_the_notes():
    curated = make_manifest("HYDRA-UMC-SDK")
    assert catalog.describe(curated) == DESCRIPTIONS["HYDRA-UMC-SDK"]
    unknown = make_manifest("HYDRA-UMC-NEW")
    assert catalog.describe(unknown) == "Notes of the manifest."
    long_notes = make_manifest("HYDRA-UMC-NEW", notes="word " * 60)
    assert len(catalog.describe(long_notes)) <= 120
    assert catalog.describe(long_notes).endswith("...")


def test_table_groups_by_family_with_the_parent_first_and_counts(workspace):
    manifests = family.load_manifests(workspace)
    text = catalog.table(manifests)
    assert text.startswith("**3 repositories** in 2 families: 1 functional, 2 established.")
    assert text.index("### Core Backend & Clients") < text.index("### Core Hardware")
    assert text.index("HYDRA-UMC-SERVER](") < text.index("HYDRA-UMC-STUDIO](")
    assert "| 0.7.9 | Established | ui | node | cm5 | HYDRA-UMC-SERVER |" in text


def test_a_pipe_in_a_cell_cannot_break_the_table():
    manifest = make_manifest("HYDRA-UMC-NEW", stack="a|b")
    assert "a\\|b" in catalog.table([manifest])


def test_render_replaces_only_the_block():
    manifests = [make_manifest("HYDRA-UMC-SDK")]
    page = f"intro\n\n{catalog.BEGIN}\nold\n{catalog.END}\n\noutro\n"
    new = catalog.render(page, manifests)
    assert new.startswith("intro\n") and new.endswith("\n\noutro\n")
    assert "old" not in new and "HYDRA-UMC-SDK" in new
    assert catalog.render(new, manifests) == new   # idempotent
    with pytest.raises(ValueError):
        catalog.render("no markers", manifests)


def test_check_file_strict_and_structure_only(workspace, tmp_path):
    manifests = family.load_manifests(workspace)
    page = tmp_path / "PROJECT_CATALOG.md"
    page.write_text(catalog.render(f"{catalog.BEGIN}\n{catalog.END}\n", manifests), encoding="utf-8")
    assert catalog.check_file(page, manifests)[0]
    assert catalog.check_file(page, manifests, structure_only=True)[0]

    bumped = [dict(m, version="9.9.9") if m["name"] == "HYDRA-UMC-SERVER" else m for m in manifests]
    assert not catalog.check_file(page, bumped)[0]                          # a version moved: stale
    assert catalog.check_file(page, bumped, structure_only=True)[0]         # but the structure is the same

    promoted = [dict(m, maturity="production") for m in manifests]
    assert not catalog.check_file(page, promoted)[0]
    assert catalog.check_file(page, promoted, structure_only=True)[0]

    extra = manifests + [make_manifest("HYDRA-UMC-NEW")]
    assert not catalog.check_file(page, extra, structure_only=True)[0]      # a repository appeared
    moved = [dict(m, family="Elsewhere") if m["name"] == "HYDRA-UMC-STUDIO" else m for m in manifests]
    assert not catalog.check_file(page, moved, structure_only=True)[0]      # a repository changed family

    page.write_text("no block", encoding="utf-8")
    assert not catalog.check_file(page, manifests)[0]


def test_structure_round_trip_through_the_written_table(workspace):
    manifests = family.load_manifests(workspace)
    assert catalog.structure_from_block(catalog.table(manifests)) == catalog.structure(manifests)


def test_missing_descriptions_lists_the_repositories_without_one():
    manifests = [make_manifest("HYDRA-UMC-SDK"), make_manifest("HYDRA-UMC-NEW")]
    assert catalog.missing_descriptions(manifests) == ["HYDRA-UMC-NEW"]


def test_every_description_is_one_short_line_without_a_date():
    for name, text in DESCRIPTIONS.items():
        assert "\n" not in text and 20 < len(text) < 200, name
        assert re.search(r"\b20\d\d\b", text) is None, name
