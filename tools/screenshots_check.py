#!/usr/bin/env python3
# =============================================================================
# HYDRA-UMC-DOCS - tools/screenshots_check.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Checks the screenshots of a repository: docs/screenshots.json, the PNG files, their weight, and that the file tree (docs/structure.json) mentions them.

    python tools/screenshots_check.py --repo PATH      # one repository
    python tools/screenshots_check.py --all [ROOT]     # every HYDRA-UMC-* folder next to this repository (or in ROOT)

Prints one line per problem and ``SCREENSHOTS=PASS`` or ``SCREENSHOTS=FAIL <n>``; exits 1 on a problem.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hydra_umc_docs.readme_src import shots  # noqa: E402


def check_repository(repo: Path) -> list[str]:
    """The problems of the screenshots of one repository, including the file tree of docs/structure.json."""
    found = shots.problems(repo)
    screens = shots.read(repo)
    if screens is None:
        return found
    structure = repo / "docs" / "structure.json"
    text = structure.read_text(encoding="utf-8") if structure.is_file() else ""
    if text:
        try:
            json.loads(text)
        except ValueError:
            found.append("docs/structure.json is not valid JSON")
        if "screenshot" not in text.lower():
            found.append("the file tree (docs/structure.json) does not mention the screenshots: describe images/ as the banner and the screenshots")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--all", nargs="?", const="", metavar="ROOT")
    args = parser.parse_args(argv)
    if args.all is not None:
        root = Path(args.all) if args.all else Path(__file__).resolve().parents[2]
        repos = sorted(path for path in root.glob("HYDRA-UMC-*") if shots.has(path))
    else:
        repos = [args.repo or Path.cwd()]
    problems = [f"{repo.name}: {problem}" for repo in repos for problem in check_repository(repo)]
    for problem in problems:
        print(problem)
    print("SCREENSHOTS=PASS" if not problems else f"SCREENSHOTS=FAIL {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
