#!/usr/bin/env python3
# =============================================================================
# HYDRA-UMC-DOCS - tools/check_test_counts.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Compare the real number of tests of every repository with data/glance.json and with its README.

For each repository listed in data/glance.json (the siblings of this folder) the script counts the
tests without running them:

* pytest and unittest suites are COLLECTED (exact: the same tests the runner would run);
* Go, Rust, JavaScript, Dart and Kotlin suites are counted from the source (approximate: a
  parameterised test counts once). They are reported as "approx" and only checked with --strict-approx.

It then says, per repository, whether glance.json and the "Tests" row of the README agree with the
count. Exit code 0 when every exactly-counted repository agrees, 1 otherwise, 2 on bad usage.

    python tools/check_test_counts.py                 # compare and report
    python tools/check_test_counts.py --apply         # write the exact counts into data/glance.json
    python tools/check_test_counts.py --repo UPDATER  # one repository (name with or without prefix)
    python tools/check_test_counts.py --json          # machine readable report

After --apply run tools/make_glance.py --apply to rewrite the READMEs.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
GLANCE = ROOT / "data" / "glance.json"
SKIP_DIRS = {".git", "node_modules", "target", "build", "dist", "__pycache__", ".venv", "venv", ".gradle"}

# Exact counting needs the repository's own dependencies; a collection error means "unknown", never "zero".
UNITTEST_SNIPPET = """
import sys, unittest
sys.path.insert(0, '.')
top = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None
suite = unittest.TestLoader().discover(sys.argv[1], pattern=sys.argv[2], top_level_dir=top)

def flat(node):
    for item in node:
        if isinstance(item, unittest.TestSuite):
            yield from flat(item)
        else:
            yield item

found = list(flat(suite))
print('COUNT=%d FAILED=%d' % (len(found), sum(type(t).__name__ == '_FailedTest' for t in found)))
"""


# Some repositories document one number that adds up several suites run by their own scripts.
# repository -> list of (start directory, file pattern, extra import paths) counted on top of the glance command.
EXTRA_UNITTEST_SUITES: dict[str, list[tuple[str, str, tuple[str, ...]]]] = {
    "HYDRA-UMC": [("src/cm5_host/spi_bridge/tests", "test_*.py", ("src/cm5_host/spi_bridge", "src/cm5_host/spi_bridge/tests"))],
}


def walk(base: Path, suffixes: tuple[str, ...]):
    for path in base.rglob("*"):
        if path.is_file() and path.suffix in suffixes and not (set(path.relative_to(base).parts) & SKIP_DIRS):
            yield path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def test_env(repo: Path, extra: tuple[str, ...] = ()) -> dict[str, str]:
    """The environment the repositories' own build_test.py gives their tests: the sources of the repository and the SDK first."""
    import os

    paths = [*(repo / e for e in extra), repo / "src", repo, repo / "agent", WORKSPACE / "HYDRA-UMC-SDK" / "clients" / "python" / "src"]
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONPATH"] = os.pathsep.join(str(p) for p in paths if p.is_dir())
    return environment


def count_pytest(repo: Path, target: str) -> int | None:
    result = subprocess.run([sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", target], cwd=repo, env=test_env(repo), capture_output=True, text=True)
    lines = [line for line in result.stdout.splitlines() if "::" in line and not line.startswith((" ", "="))]
    summary = re.search(r"(\d+)(?:/\d+)? tests? collected", result.stdout)
    if result.returncode not in (0, 5):
        return None
    if summary:
        return int(summary.group(1))
    return len(lines) if lines else None


def count_unittest(repo: Path, start: str, pattern: str = "test*.py", extra: tuple[str, ...] = ()) -> int | None:
    top = "agent" if start.startswith("agent") else ""
    result = subprocess.run([sys.executable, "-c", UNITTEST_SNIPPET, start, pattern, top], cwd=repo, env=test_env(repo, extra), capture_output=True, text=True)
    match = re.search(r"COUNT=(\d+) FAILED=(\d+)", result.stdout)
    # a failed import shows up as a _FailedTest inside the suite: do not trust the number then
    if not match or int(match.group(2)):
        return None
    return int(match.group(1))


def count_static(repo: Path, kind: str) -> int | None:
    total = 0
    if kind == "go":
        for path in walk(repo, (".go",)):
            if path.name.endswith("_test.go"):
                total += len(re.findall(r"(?m)^func (?:\([^)]*\) )?Test\w*\(", read(path)))
    elif kind == "cargo":
        for path in walk(repo, (".rs",)):
            total += len(re.findall(r"#\[(?:tokio::)?test(?:\([^)]*\))?\]", read(path)))
    elif kind == "js":
        for path in walk(repo, (".ts", ".tsx", ".js", ".mjs", ".cjs")):
            if re.search(r"\.(test|spec)\.\w+$", path.name) or "tests" in path.relative_to(repo).parts or "test" in path.relative_to(repo).parts:
                total += len(re.findall(r"(?m)^\s*(?:it|test)(?:\.(?:only|each))?\s*\(", read(path)))
    elif kind == "dart":
        for path in walk(repo, (".dart",)):
            if path.name.endswith("_test.dart"):
                total += len(re.findall(r"(?m)^\s*(?:test|testWidgets)\s*\(", read(path)))
    elif kind == "kotlin":
        for path in walk(repo, (".kt", ".java")):
            if "test" in path.relative_to(repo).parts:
                total += len(re.findall(r"@Test\b", read(path)))
    return total or None


def measure(name: str, entry: dict) -> tuple[int | None, str]:
    """Return (count, method) where method is 'exact', 'approx' or 'unmeasured'."""
    real, method = measure_main(name, entry)
    for start, pattern, extra in EXTRA_UNITTEST_SUITES.get(name, []):
        more = count_unittest(WORKSPACE / name, start, pattern, extra)
        real = None if real is None or more is None else real + more
    return real, method


def measure_main(name: str, entry: dict) -> tuple[int | None, str]:
    repo = WORKSPACE / name
    tests = entry.get("tests") or {}
    command = tests.get("command") or ""
    if not repo.is_dir():
        return None, "unmeasured"
    if "pytest" in command:
        match = re.search(r"\b(tests|agent/tests)\b", command)
        return count_pytest(repo, match.group(1) if match else "tests"), "exact"
    if "unittest" in command:
        match = re.search(r"-s (\S+)", command)
        pattern = re.search(r"-p '?([^' ]+)'?", command)
        return count_unittest(repo, match.group(1) if match else "tests", pattern.group(1) if pattern else "test*.py"), "exact"
    if "build_test" in command:
        return count_unittest(repo, "tests"), "exact"
    if not command and (repo / "tests").is_dir():
        return count_pytest(repo, "tests"), "exact"
    for key, kind in (("go test", "go"), ("cargo", "cargo"), ("npm", "js"), ("flutter", "dart"), ("gradlew", "kotlin")):
        if key in command:
            return count_static(repo, kind), "approx"
    return None, "unmeasured"


def readme_count(name: str) -> int | None:
    readme = WORKSPACE / name / "README.md"
    if not readme.is_file():
        return None
    match = re.search(r"(?im)^\|\s*Tests\s*\|\s*(\d+)\b", read(readme))
    return int(match.group(1)) if match else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="check_test_counts.py", description=__doc__.split("\n\n")[0])
    parser.add_argument("--apply", action="store_true", help="write the exactly counted numbers into data/glance.json")
    parser.add_argument("--repo", action="append", default=[], help="only this repository (repeatable)")
    parser.add_argument("--strict-approx", action="store_true", help="also fail when an approximate count disagrees")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args(argv)

    data = json.loads(read(GLANCE))
    wanted = {(r if r.startswith("HYDRA-UMC") else f"HYDRA-UMC-{r}") for r in args.repo}
    rows, failures = [], 0
    for name, entry in data["repos"].items():
        if wanted and name not in wanted:
            continue
        if not entry.get("tests"):
            continue
        recorded = (entry.get("tests") or {}).get("count")
        real, method = measure(name, entry)
        shown = readme_count(name)
        problems = []
        if real is not None:
            if recorded != real:
                problems.append(f"glance says {recorded}")
            if shown is not None and shown != real:
                problems.append(f"README says {shown}")
        elif method != "unmeasured":
            problems.append("could not be counted (a dependency of its tests is not installed here)")
        blocking = real is not None and bool(problems) and (method == "exact" or args.strict_approx)
        failures += blocking
        rows.append({"repo": name, "real": real, "method": method, "glance": recorded, "readme": shown, "problems": problems, "blocking": blocking})
        if args.apply and method == "exact" and real is not None and recorded != real and isinstance(entry.get("tests"), dict):
            entry["tests"]["count"] = real

    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        for row in rows:
            flag = "OK  " if not row["problems"] else ("FAIL" if row["blocking"] else "warn")
            print(f"{flag} {row['repo']:<34} real={row['real']} ({row['method']}) glance={row['glance']} readme={row['readme']} {'; '.join(row['problems'])}")
        print(f"TEST_COUNTS={'FAIL' if failures else 'PASS'} repositories={len(rows)} failing={failures}")
    if args.apply:
        GLANCE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("TEST_COUNTS=APPLIED data/glance.json updated for the exactly counted repositories")
        return 0
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
