# =============================================================================
# HYDRA-UMC-DOCS - tests/conftest.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Shared helpers: a throw-away workspace of family repositories with manifests."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))


def make_manifest(name: str, **overrides) -> dict:
    manifest = {
        "schema_version": "1.0",
        "ecosystem": "HYDRA-UMC",
        "name": name,
        "version": "0.1.0",
        "role": "service",
        "stack": "python",
        "technologies": ["Python"],
        "deployment_target": "cm5",
        "maturity": "established",
        "family": "Test Family",
        "parent": None,
        "build": "python tools/build_test.py",
        "notes": "Notes of the manifest. A second sentence that is not used.",
        "native_version": {"file": "pyproject.toml", "pattern": "x"},
    }
    manifest.update(overrides)
    return manifest


def write_repo(workspace: Path, name: str, **overrides) -> Path:
    repo = workspace / name
    repo.mkdir(parents=True, exist_ok=True)
    (repo / "hydra-umc.project.json").write_text(json.dumps(make_manifest(name, **overrides)), encoding="utf-8")
    return repo


@pytest.fixture()
def workspace(tmp_path: Path) -> Path:
    write_repo(tmp_path, "HYDRA-UMC", family="Core Hardware", role="firmware", stack="firmware-c", maturity="functional", deployment_target="user-pc")
    write_repo(tmp_path, "HYDRA-UMC-SERVER", family="Core Backend & Clients", role="api", stack="node")
    write_repo(tmp_path, "HYDRA-UMC-STUDIO", family="Core Backend & Clients", role="ui", stack="node", parent="HYDRA-UMC-SERVER", version="0.7.9")
    (tmp_path / "NOT-A-FAMILY-REPO").mkdir()
    (tmp_path / "NOT-A-FAMILY-REPO" / "hydra-umc.project.json").write_text("{}", encoding="utf-8")
    (tmp_path / "HYDRA-UMC-NO-MANIFEST").mkdir()
    return tmp_path
