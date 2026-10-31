# =============================================================================
# HYDRA-UMC-DOCS - tests/test_i18n_cross_check.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("i18n_cross_check", REPO / "tools" / "i18n_cross_check.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


def make_clients(root: Path, suite_pt: str = "Parar tudo", drop_key: bool = False) -> None:
    locales = root / "HYDRA-UMC-STUDIO" / "src" / "locales"
    locales.mkdir(parents=True)
    for lang in tool.LANGS:
        text = "Stop all" if lang == "en" else ("Parar tudo" if lang == "pt" else f"studio-{lang}")
        body = {"stop": {} if drop_key and lang == "de" else {"all": text}}
        (locales / f"{lang}.json").write_text(json.dumps(body), encoding="utf-8")
    language = root / "HYDRA-UMC-SUITE" / "language"
    language.mkdir(parents=True)
    for lang, name in tool.SUITE_NAMES.items():
        text = "Stop all" if lang == "en" else (suite_pt if lang == "pt" else f"studio-{lang}")
        (language / f"{name}.lng").write_text(f"# comment\nSTOP_ALL={text}\n", encoding="utf-8")


def test_flatten_keeps_only_text():
    assert tool.flatten({"a": {"b": "x", "c": ["y"]}, "d": "z"}) == {"a.b": "x", "d": "z"}


def test_same_wording_is_not_reported(tmp_path):
    make_clients(tmp_path)
    assert tool.main(["--root", str(tmp_path)]) == 0
    assert tool.same_text_differences(tool.readers(tmp_path), "pt") == []


def test_different_wording_is_reported_but_not_a_failure(tmp_path):
    make_clients(tmp_path, suite_pt="Parar todos")
    assert tool.main(["--root", str(tmp_path)]) == 0
    found = tool.same_text_differences(tool.readers(tmp_path), "pt")
    assert [norm for norm, _ in found] == ["stop all"]


def test_a_missing_key_is_a_failure(tmp_path):
    make_clients(tmp_path, drop_key=True)
    assert tool.main(["--root", str(tmp_path)]) == 1


def test_no_clients_found(tmp_path):
    assert tool.main(["--root", str(tmp_path)]) == 2
