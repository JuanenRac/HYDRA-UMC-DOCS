# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/glance_jump.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The "Jump to" line that closes At a glance in the repositories that follow the universal README layout.

glance.py (shared line by line with the other documentation hub) writes the table only. For a README that is already in the universal layout this module
adds the "Jump to" line, built from the sections the README really has, so that ``make_glance.py`` keeps the table and the line in step and neither
one is ever written by hand. A README still in the old layout is left exactly as glance.py writes it.
"""
from __future__ import annotations

from pathlib import Path

from . import glance, readme_universal as universal


def migrated(text: str) -> bool:
    return "architecture" in universal.present_sections(text)


def expected_sections(repo: Path, entry: dict) -> dict[str, str]:
    manifest = glance.load_manifest(repo)
    out = {}
    for code in glance.LANGUAGE_FILES:
        base = glance.render_section(code, manifest, entry)
        path = glance.readme_path(repo, code)
        text = path.read_bytes().decode("utf-8") if path.is_file() else ""
        if migrated(text):
            base = base.rstrip("\n") + "\n\n" + universal.jump_line(code, universal.present_sections(text)) + "\n\n"
        out[code] = base
    return out


def apply_repo(repo: Path, entry: dict) -> list[str]:
    changed = []
    for code, section in expected_sections(repo, entry).items():
        path = glance.readme_path(repo, code)
        original = path.read_bytes().decode("utf-8")
        updated = glance.apply_to_text(original, section)
        if updated != original:
            path.write_bytes(updated.encode("utf-8"))
            changed.append(path.name)
    return changed


def check_repo(repo: Path, entry: dict) -> list[str]:
    problems = []
    for code, section in expected_sections(repo, entry).items():
        path = glance.readme_path(repo, code)
        if not path.is_file():
            problems.append(f"{repo.name}/{path.name}: the file is missing")
            continue
        for problem in glance.check_text(path.read_bytes().decode("utf-8"), section):
            problems.append(f"{repo.name}/{path.name}: {problem}")
    return problems
