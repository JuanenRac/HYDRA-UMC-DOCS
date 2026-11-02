#!/usr/bin/env python3
# =============================================================================
# HYDRA-UMC-DOCS - tools/i18n_align.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Align the wording of a HYDRA-UMC client with the wording of STUDIO where the English text is the same.

STUDIO's wording wins. A text of another client is a candidate only when

* its English is exactly the English of one or more STUDIO texts,
* STUDIO reads that English the same way in every one of its keys (otherwise STUDIO itself depends on the context),
* neither side has a placeholder, a menu accelerator (&), a line break or a percent sign (the formats of the clients differ there),
* the translation of the client differs from STUDIO's in at least one language.

Nothing is changed unless `--apply` is given, and then only for the English texts named with `--only` or the first `--max`
candidates in alphabetical order (a small batch per client). The meaning never changes: only the words of the translations.

Usage:
    py -3 tools/i18n_align.py --target suite|android|watch|ios|dsi [--root PARENT_DIR] [--list]
    py -3 tools/i18n_align.py --target suite --apply [--max 15 | --only "Delete" --only "Done"]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections.abc import Callable
from pathlib import Path

_spec = importlib.util.spec_from_file_location("i18n_cross_check", Path(__file__).with_name("i18n_cross_check.py"))
assert _spec is not None and _spec.loader is not None
check = importlib.util.module_from_spec(_spec)
sys.modules["i18n_cross_check"] = check
_spec.loader.exec_module(check)

LANGS = check.LANGS
UNSAFE = re.compile(r"\{|\}|%|&|\\n|\n|<|>|@|\?")


def _same(a: str, b: str) -> bool:
    """Equal apart from the shape of the apostrophe (typographic, or escaped in a strings.xml)."""
    def shape(text: str) -> str:
        return text.replace(chr(92) + "'", "'").replace(chr(92) + '"', '"').replace(chr(0x2019), "'")

    return shape(a) == shape(b)


def _in_style_of(current: str, wanted: str) -> str:
    """STUDIO's words with the apostrophe the client already uses."""
    if "’" in current and "'" not in current:
        return wanted.replace("'", "’")
    return wanted


def _plain(text: str) -> bool:
    return bool(text.strip()) and not UNSAFE.search(text)


def candidates(clients: dict, target: str) -> dict[str, list[dict]]:
    """English text -> [{key, values: {lang: (current, studio)}}] for the keys of `target` that can be aligned."""
    studio = clients["studio"]
    by_english: dict[str, list[str]] = {}
    for key, english in studio["en"].items():
        by_english.setdefault(english.strip(), []).append(key)
    found: dict[str, list[dict]] = {}
    for key, english in clients[target]["en"].items():
        english = english.strip()
        keys = by_english.get(english)
        if not keys or not _plain(english):
            continue
        values: dict[str, tuple[str, str]] = {}
        ok = True
        for lang in LANGS[1:]:
            wanted = {studio[lang].get(k) for k in keys}
            if len(wanted) != 1 or None in wanted:
                ok = False
                break
            wanted_text = next(iter(wanted))
            current = clients[target][lang].get(key)
            if current is None or not _plain(wanted_text):
                ok = False
                break
            values[lang] = (current, _in_style_of(current, wanted_text))
        if ok and any(not _same(current, wanted) for current, wanted in values.values()):
            found.setdefault(english, []).append({"key": key, "values": values})
    return found


# --- writing ------------------------------------------------------------------------------------------------------

def _xml_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace("'", "\\'").replace('"', '\\"')


def _write_suite(path: Path, key: str, value: str) -> bool:
    raw = path.read_bytes().decode("utf-8")
    pattern = re.compile(r"^(" + re.escape(key) + r"=)(.*?)(\r?)$", re.M)
    new, count = pattern.subn(lambda m: m.group(1) + value + m.group(3), raw, count=1)
    if count:
        path.write_bytes(new.encode("utf-8"))
    return bool(count)


def _write_android(path: Path, key: str, value: str) -> bool:
    raw = path.read_bytes().decode("utf-8")
    pattern = re.compile(r'(<string name="' + re.escape(key) + r'"[^>]*>)(.*?)(</string>)', re.S)
    new, count = pattern.subn(lambda m: m.group(1) + _xml_escape(value) + m.group(3), raw, count=1)
    if count:
        path.write_bytes(new.encode("utf-8"))
    return bool(count)


def _write_arb(path: Path, key: str, value: str) -> bool:
    raw = path.read_bytes().decode("utf-8")
    pattern = re.compile(r'^(\s*"' + re.escape(key) + r'":\s*)"(?:[^"\\]|\\.)*"(,?)(\r?)$', re.M)
    new, count = pattern.subn(lambda m: m.group(1) + json.dumps(value, ensure_ascii=False) + m.group(2) + m.group(3), raw, count=1)
    if count:
        json.loads(new)
        path.write_bytes(new.encode("utf-8"))
    return bool(count)


def target_file(root: Path, target: str, lang: str) -> tuple[Path, Callable[[Path, str, str], bool]]:
    if target == "suite":
        return root / "HYDRA-UMC-SUITE" / "language" / f"{check.SUITE_NAMES[lang]}.lng", _write_suite
    if target in ("android", "watch"):
        repo = "HYDRA-UMC-ANDROID-CONTROL" if target == "android" else "HYDRA-UMC-WATCH"
        folder = "values" if lang == "en" else f"values-{lang}"
        return root / repo / "app" / "src" / "main" / "res" / folder / "strings.xml", _write_android
    repo = "HYDRA-UMC-IOS-CONTROL" if target == "ios" else "HYDRA-UMC-DSI"
    return root / repo / "lib" / "l10n" / f"app_{lang}.arb", _write_arb


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--target", required=True, choices=["suite", "android", "watch", "ios", "dsi"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--list", action="store_true", help="print every candidate with the words of each language")
    parser.add_argument("--apply", action="store_true", help="write the studio wording into the client")
    parser.add_argument("--max", type=int, default=15, help="with --apply: the most English texts to change (default 15)")
    parser.add_argument("--only", action="append", default=[], help="with --apply: only these English texts")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    clients = check.readers(args.root)
    if "studio" not in clients or args.target not in clients:
        print(f"STUDIO and the target must sit under {args.root}", file=sys.stderr)
        return 2
    found = candidates(clients, args.target)
    chosen = sorted(found)
    if args.only:
        chosen = [english for english in chosen if english in args.only]
    elif args.apply:
        chosen = chosen[: args.max]
    print(f"{args.target}: {len(found)} English texts can be aligned with STUDIO")
    if args.list or not args.apply:
        for english in sorted(found) if not args.only else chosen:
            print(f"  {english!r}  ({', '.join(item['key'] for item in found[english])})")
            if args.list:
                for lang in LANGS[1:]:
                    for item in found[english]:
                        current, wanted = item["values"][lang]
                        if not _same(current, wanted):
                            print(f"      {lang}: {current!r} -> {wanted!r}")
    if not args.apply:
        return 0
    changed = 0
    for english in chosen:
        for item in found[english]:
            for lang in LANGS[1:]:
                current, wanted = item["values"][lang]
                if _same(current, wanted):
                    continue
                path, writer = target_file(args.root, args.target, lang)
                if not writer(path, item["key"], wanted):
                    print(f"could not write {item['key']} in {path}", file=sys.stderr)
                    return 1
                changed += 1
    print(f"changed {changed} translations of {len(chosen)} English texts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
