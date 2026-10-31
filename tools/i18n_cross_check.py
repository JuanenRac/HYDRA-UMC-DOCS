#!/usr/bin/env python3
# =============================================================================
# HYDRA-UMC-DOCS - tools/i18n_cross_check.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Compare the language files of the HYDRA-UMC clients that sit next to this repository.

Every client keeps its own format (STUDIO: JSON, SUITE: .lng, ANDROID-CONTROL and WATCH: strings.xml), so this tool reads
them all into the same shape and reports two things:

* keys that are missing or extra in any of the eight languages of one client (a failure, exit code 1);
* texts that are the same in English in two clients but read differently in another language (information only: it
  lists the differences so that the wording can be aligned when a client is touched; exit code 0).

Usage: py -3 tools/i18n_cross_check.py [--root PARENT_DIR] [--lang pt] [--list] [--json]
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

LANGS = ("en", "es", "de", "fr", "it", "ja", "zh", "pt")
SUITE_NAMES = {"en": "english", "es": "spanish", "de": "german", "fr": "french", "it": "italian", "ja": "japanese", "zh": "chinese", "pt": "portuguese"}
PLACEHOLDER = re.compile(r"\{\{\w+\}\}|%\d*\$?[sdf]|\{\w+\}")


def flatten(tree: dict, prefix: str = "") -> dict[str, str]:
    """Nested JSON to dotted keys; only text values are kept."""
    out: dict[str, str] = {}
    for key, value in tree.items():
        name = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            out.update(flatten(value, name))
        elif isinstance(value, str):
            out[name] = value
    return out


def read_studio(root: Path) -> dict[str, dict[str, str]]:
    folder = root / "HYDRA-UMC-STUDIO" / "src" / "locales"
    return {lang: flatten(json.loads((folder / f"{lang}.json").read_text(encoding="utf-8"))) for lang in LANGS}


def read_suite(root: Path) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for lang in LANGS:
        entries: dict[str, str] = {}
        path = root / "HYDRA-UMC-SUITE" / "language" / f"{SUITE_NAMES[lang]}.lng"
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                entries[key] = value
        out[lang] = entries
    return out


def read_android(root: Path, repo: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for lang in LANGS:
        folder = "values" if lang == "en" else f"values-{lang}"
        path = root / repo / "app" / "src" / "main" / "res" / folder / "strings.xml"
        entries: dict[str, str] = {}
        if path.exists():
            for m in re.finditer(r'<string name="([^"]+)"([^>]*)>(.*?)</string>', path.read_text(encoding="utf-8"), re.DOTALL):
                if 'translatable="false"' not in m.group(2):
                    entries[m.group(1)] = m.group(3)
        out[lang] = entries
    return out


def readers(root: Path) -> dict[str, dict[str, dict[str, str]]]:
    """The language data of every client repository found under `root`."""
    found: dict[str, dict[str, dict[str, str]]] = {}
    if (root / "HYDRA-UMC-STUDIO").is_dir():
        found["studio"] = read_studio(root)
    if (root / "HYDRA-UMC-SUITE").is_dir():
        found["suite"] = read_suite(root)
    if (root / "HYDRA-UMC-ANDROID-CONTROL").is_dir():
        found["android"] = read_android(root, "HYDRA-UMC-ANDROID-CONTROL")
    if (root / "HYDRA-UMC-WATCH").is_dir():
        found["watch"] = read_android(root, "HYDRA-UMC-WATCH")
    return found


def key_gaps(data: dict[str, dict[str, str]]) -> dict[str, tuple[list[str], list[str]]]:
    """For each language: (keys missing against English, keys that English does not have)."""
    base = data["en"]
    return {lang: ([k for k in base if k not in data[lang]], [k for k in data[lang] if k not in base]) for lang in LANGS[1:]}


def normalise_english(text: str) -> str:
    text = PLACEHOLDER.sub("#", text).replace("&", "").replace("\\n", " ")
    return re.sub(r"\s+", " ", text).strip().lower()


def same_text_differences(clients: dict[str, dict[str, dict[str, str]]], lang: str) -> list[tuple[str, dict[str, list[str]]]]:
    """English texts shared by two or more clients whose translation into `lang` is not the same everywhere."""
    index: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    for client, data in clients.items():
        for key, value in data["en"].items():
            norm = normalise_english(value)
            if len(norm) >= 4:
                index[norm].append((client, key))
    result = []
    for norm, items in sorted(index.items()):
        if len({client for client, _ in items}) < 2:
            continue
        variants: dict[str, list[str]] = collections.defaultdict(list)
        for client, key in items:
            value = clients[client][lang].get(key)
            if value is not None:
                variants[PLACEHOLDER.sub("#", value).replace("&", "").strip().lower()].append(f"{client}:{key}")
        if len(variants) > 1:
            result.append((norm, dict(variants)))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="folder that holds the client repositories")
    parser.add_argument("--lang", choices=LANGS[1:], help="only this language for the wording differences")
    parser.add_argument("--list", action="store_true", help="print every difference, not only the counts")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    clients = readers(args.root)
    if not clients:
        print(f"no client repository found under {args.root}", file=sys.stderr)
        return 2
    failed = False
    report: dict = {"gaps": {}, "differences": {}}
    for name, data in clients.items():
        for lang, (missing, extra) in key_gaps(data).items():
            if missing or extra:
                failed = True
                report["gaps"][f"{name}/{lang}"] = {"missing": missing, "extra": extra}
    for lang in [args.lang] if args.lang else LANGS[1:]:
        report["differences"][lang] = same_text_differences(clients, lang)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for name, data in clients.items():
            print(f"{name}: {len(data['en'])} keys in English")
        for place, gap in report["gaps"].items():
            print(f"KEYS {place}: missing {len(gap['missing'])}, extra {len(gap['extra'])}")
        for lang, diffs in report["differences"].items():
            print(f"{lang}: {len(diffs)} shared English texts read differently between clients")
            if args.list:
                for norm, variants in diffs:
                    print(f"  {norm}")
                    for text, where in variants.items():
                        print(f"      {text!r}  {', '.join(where[:3])}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
