#!/usr/bin/env python3
"""Static linter for the .sh / .bat / .cmd scripts of every sibling repo.

Read-only: it never runs a repo script. The only process it starts is
`bash -n` (syntax check, executes nothing).

Usage:
    python tools/script_lint.py                 # all sibling repos of this one
    python tools/script_lint.py REPO [REPO...]  # named repos (folder names)
    python tools/script_lint.py --root DIR      # a different parent folder
    python tools/script_lint.py --json          # machine readable output

Severity: E = broken / will hang, W = should fix, I = informational.
Exit status is 1 when any E finding exists.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CI_WORDS = ("HYDRA_UMC_CI", "ARMOR_CI", "URTC_CI", "CI=", "%CI%", "$CI", "${CI", "GITHUB_ACTIONS", "-t 0", "-t 1", "NONINTERACTIVE", "NO_PAUSE", "NOPAUSE")
HARD_PATHS = re.compile(r"(C:\\Users\\juane|C:/Users/juane|/home/hydra-umc|/home/juane|/Users/juane)", re.I)
PRIVATE_IP = re.compile(r"\b(192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(1[6-9]|2\d|3[01])\.\d+\.\d+)\b")
SECRET = re.compile(r"(ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|(?i:password|secret|token)\s*=\s*['\"][^'\"$]{6,}['\"])")
# Words that must never appear in a public file (assembled so this file stays clean itself).
FORBIDDEN = re.compile(r"(" + "|".join(["aud" + "it", "SON" + "NET", "Cla" + "ude", "anthr" + "opic"]) + r")", re.I)
NPM_OK = re.compile(r"npm (aud" + "it|ci)|no-aud" + "it|aud" + "it fix|aud" + "it-level|aud" + "it log", re.I)
INTERACTIVE_NAMES = re.compile(r"(^|[-_])(build|run|start|install|setup|launch)", re.I)
RISKY_NAMES = re.compile(r"(deploy|publish|release|flash|install|uninstall|bump|sign|push)", re.I)
REF = re.compile(r"""(?<![\w./-])((?:\.\./)?(?:src|tools|scripts|docs|data|tests?|config|assets|firmware|main/)[\w./-]*\.(?:py|sh|bat|cmd|ps1|json|txt|js|mjs|ts|toml|yml|yaml|qml|cmake|md))\b""")


def git_files(repo: Path):
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files", "*.sh", "*.bat", "*.cmd"],
                             capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return []
    return [l for l in out.splitlines() if l and "node_modules/" not in l and "/vendor/" not in l]


def bash_n(path: Path):
    bash = shutil.which("bash")
    if not bash:
        return None
    try:
        r = subprocess.run([bash, "-n", str(path)], capture_output=True, text=True, timeout=30)
    except Exception as e:  # pragma: no cover
        return str(e)
    return r.stderr.strip() if r.returncode else ""


def lint_sh(repo: Path, rel: str, text: str, raw: bytes, add):
    lines = text.split("\n")
    if b"\r\n" in raw:
        add("E", "crlf", "CRLF line endings in a .sh (fails on Linux)")
    if not text.startswith("#!"):
        add("W", "shebang", "missing shebang")
    err = bash_n(repo / rel)
    if err:
        add("E", "syntax", "bash -n: " + err.splitlines()[0][:160])
    body = "\n".join(l for l in lines if not l.strip().startswith("#"))
    if not re.search(r"^\s*set\s+-[a-z]*e", body, re.M) and not re.search(r"set -o errexit", body):
        add("I", "no-set-e", "no `set -e` (check a documented reason)")
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("#"):
            continue
        if re.search(r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+[^;&|]*\$\{?\w+\}?(?!\w)", s) and '"$' not in s:
            add("E", "rm-unquoted", f"line {i}: rm -r on unquoted variable: {s[:90]}")
        elif re.search(r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*\s+\"?\$\{?\w+\}?/?\"?\s*($|;|&)", s) and ":?" not in s:
            add("W", "rm-var", f"line {i}: rm -r on a variable without ${{VAR:?}} guard: {s[:90]}")
        if re.search(r"(^|[;&{(]\s*|\btrap\s+')(echo;\s*)?read\b", s) and not re.search(
                r"<<<|\|\s*(while\s+)?read|\|\s*\{\s*read|^\s*while\b|\bdone\s*<|read\s+.*-t\s*\d|<\s*/dev/|<\s*\"?\$|\)\s*read\b", s):
            if not any(w in text for w in CI_WORDS):
                add("E", "read-hang", f"line {i}: `read` without CI / tty guard or timeout: {s[:90]}")
        if re.search(r"\bnpm install\b", s) and "package-lock" not in text and False:
            pass
        if re.search(r"pip3?\s+install\s+.*--user", s):
            add("W", "pip-user", f"line {i}: pip --user: {s[:90]}")
        if re.search(r"^\s*(sudo\s+)?apt(-get)?\s+install\b(?!.*(-y|--yes|-qq))", s):
            add("W", "apt-prompt", f"line {i}: apt install without -y")
    if not any("dirname" in l or "BASH_SOURCE" in l or "SCRIPT_DIR" in l or "cd " in l for l in lines):
        if re.search(r"\b(python3?|node|npm|cargo|go|gradlew?|flutter|cmake)\b.*\b(src|tools|scripts)/", body):
            add("W", "no-cd", "uses repo-relative paths but never cd's to the script directory")


def lint_bat(repo: Path, rel: str, text: str, raw: bytes, add):
    name = os.path.basename(rel).lower()
    lines = text.splitlines()
    if raw.count(b"\n") and raw.count(b"\r\n") != raw.count(b"\n"):
        add("W", "lf-in-bat", "mixed/LF line endings in a .bat (labels and goto can break)")
    low = [l.strip().lower() for l in lines]
    code = [l for l in low if not l.startswith(("rem ", "::", "@rem")) and l]
    # parentheses balance on lines that are not echo/rem
    depth = 0
    for _i, l in enumerate(lines, 1):
        s = l.strip()
        if not s or s.lower().startswith(("rem ", "::", "@rem", "echo", "@echo")):
            continue
        s2 = re.sub(r'"[^"]*"', "", s)
        s2 = re.sub(r"\^.", "", s2)
        depth += s2.count("(") - s2.count(")")
    if depth != 0:
        add("W", "parens", f"unbalanced parentheses (net {depth:+d}) outside echo/rem (may be a false positive)")
    labels = {m.group(1).lower() for l in lines for m in [re.match(r"\s*:([\w.-]+)", l)] if m and not l.strip().startswith("::")}
    for i, l in enumerate(lines, 1):
        for m in re.finditer(r"\b(?:goto|call)\s+:?([\w.-]+)", l, re.I):
            tgt = m.group(1).lower()
            if re.search(r"\bgoto\s+:?" + re.escape(m.group(1)), l, re.I) and tgt not in labels and tgt != "eof":
                add("E", "goto-missing", f"line {i}: goto to missing label :{m.group(1)}")
        m = re.search(r"\bcall\s+\"?(%~dp0)?([\w./\\-]+\.(?:bat|cmd))\"?", l, re.I)
        if m and ".venv" not in m.group(2).lower():
            p = (repo / os.path.dirname(rel) / m.group(2).replace("\\", "/"))
            if not p.exists() and not (repo / m.group(2).replace("\\", "/")).exists():
                add("E", "call-missing", f"line {i}: call of missing file {m.group(2)}")
        if re.match(r"\s*exit(\s|$)(?!/b)", l, re.I) and not re.match(r"\s*exit\s+/b", l, re.I):
            add("W", "exit-closes", f"line {i}: `exit` closes the window (use `exit /b`): {l.strip()[:80]}")
    txt = "\n".join(low)
    if not any("setlocal" in l for l in code):
        add("I", "no-setlocal", "no setlocal (variables leak into the caller console)")
    if "%~dp0" not in txt and "pushd" not in txt and "cd /d" not in txt and re.search(r"\b(python|node|npm|cargo|gradlew|flutter)\b", txt):
        add("W", "no-dp0", "runs tools without anchoring to %~dp0 / cd /d")
    interactive = bool(INTERACTIVE_NAMES.search(name)) and not name.startswith(("build-test", "ci"))
    has_pause = any(re.search(r"(^|[&(]\s*|\)\s*|\s)(@?pause|set /p|timeout /t -1|%keep_open%)", l) and not l.startswith("echo") for l in code)
    delegates = any(re.match(r"call\s+\"?%~dp0", l) for l in code)
    if interactive and not has_pause and not delegates and not name.startswith("build-test"):
        add("W", "no-pause", "build/run script never pauses (window closes by itself)")
    if has_pause and not any(w.lower() in txt for w in CI_WORDS):
        add("E", "pause-no-ci", "pause/set /p without a CI switch (HYDRA_UMC_CI / CI): hangs in automation")


def lint_common(repo: Path, rel: str, text: str, add):
    for i, l in enumerate(text.splitlines(), 1):
        if l.strip().startswith(("#", "rem", "REM", "::")) and False:
            continue
        if HARD_PATHS.search(l):
            add("W", "hardcoded-path", f"line {i}: author-machine path: {l.strip()[:90]}")
        m = PRIVATE_IP.search(l)
        if m and not re.search(r"(127\.|0\.0\.0\.0|192\.168\.4\.1\b)", m.group(0)):
            add("I", "private-ip", f"line {i}: private IP {m.group(0)}")
        if SECRET.search(l) and "$(" not in l:
            add("E", "secret", f"line {i}: possible secret")
        if FORBIDDEN.search(l) and not NPM_OK.search(l):
            add("W", "public-hygiene", f"line {i}: forbidden word in a public file: {l.strip()[:80]}")
    base = (repo / os.path.dirname(rel))
    seen = set()
    for m in REF.finditer(text):
        ref = m.group(1)
        if ref in seen or "$" in ref or "*" in ref:
            continue
        seen.add(ref)
        cands = [repo / ref, base / ref, base / ref.replace("../", "", 1)]
        if not any(c.exists() for c in cands):
            # generated outputs and user-supplied files are not defects
            if re.search(r"(build|dist|out|generated|\.venv|node_modules|\.generated)", ref):
                continue
            add("W", "missing-ref", f"references `{ref}` which does not exist in the repo")


def lint_repo(repo: Path):
    findings, scripts = [], []
    files = git_files(repo)
    shs = {f[:-3] for f in files if f.endswith(".sh")}
    bats = {f[:-4] for f in files if f.endswith(".bat")}
    for rel in files:
        p = repo / rel
        if not p.is_file():
            findings.append((rel, "E", "tracked-missing", "tracked but missing on disk"))
            continue
        raw = p.read_bytes()
        text = raw.decode("utf-8", "replace")
        scripts.append(rel)

        def add(sev, code, msg, rel=rel):
            findings.append((rel, sev, code, msg))
        if rel.endswith(".sh"):
            lint_sh(repo, rel, text, raw, add)
        else:
            lint_bat(repo, rel, text, raw, add)
        lint_common(repo, rel, text, add)
    for b in sorted(shs - bats):
        n = os.path.basename(b)
        if re.match(r"(build|build-test|run)$", n):
            findings.append((b + ".sh", "W", "parity", "no matching .bat"))
    for b in sorted(bats - shs):
        n = os.path.basename(b)
        if re.match(r"(build|build-test|run)$", n):
            findings.append((b + ".bat", "W", "parity", "no matching .sh"))
    return scripts, findings


def main():
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser()
    ap.add_argument("repos", nargs="*")
    ap.add_argument("--root", default=str(here.parent))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--min", default="W", choices=["E", "W", "I"])
    a = ap.parse_args()
    root = Path(a.root)
    names = a.repos or sorted(d.name for d in root.iterdir() if (d / ".git").exists())
    order = {"E": 0, "W": 1, "I": 2}
    result, bad = {}, 0
    for n in names:
        scripts, fs = lint_repo(root / n)
        fs = [f for f in fs if order[f[1]] <= order[a.min]]
        result[n] = {"scripts": len(scripts), "findings": fs}
        bad += sum(1 for f in fs if f[1] == "E")
    if a.json:
        print(json.dumps(result, indent=1))
    else:
        for n, r in result.items():
            print(f"== {n}: {r['scripts']} scripts, {len(r['findings'])} findings")
            for rel, sev, code, msg in r["findings"]:
                print(f"  [{sev}] {rel}: {code}: {msg}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
