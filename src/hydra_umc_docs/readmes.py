# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/readmes.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The languages of the README of this repository.

The eight files are written by :mod:`readme_universal` from the source ``readme_src/repos/HYDRA_UMC_DOCS.py``, which takes the words of the
hub from :mod:`readme_text` and the list of related projects from :mod:`readme_family`, so the eight files have the same structure and the
same links by construction (the CI check of the ecosystem compares exactly that).
"""
from __future__ import annotations

from .readme_text import LANGUAGES

__all__ = ["LANGUAGES"]
