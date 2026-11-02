# =============================================================================
# HYDRA-UMC-DOCS - tests/test_i18n_align.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("i18n_align", REPO / "tools" / "i18n_align.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)
check = tool.check

STUDIO = {
    "delete": {"en": "Delete", "es": "Borrar", "de": "Löschen", "fr": "Supprimer", "it": "Elimina", "ja": "削除", "zh": "删除", "pt": "Apagar"},
    "connected": {"en": "Connected", "es": "Conectados", "de": "Verbunden", "fr": "Connectés", "it": "Connessi", "ja": "接続中", "zh": "已连接", "pt": "Ligadas"},
    "greeting": {"en": "Hello {{name}}", "es": "Hola {{name}}", "de": "Hallo {{name}}", "fr": "Bonjour {{name}}", "it": "Ciao {{name}}", "ja": "{{name}}", "zh": "{{name}}", "pt": "Olá {{name}}"},
    "info": {"en": "The server's answer", "es": "La respuesta del servidor", "de": "Die Antwort", "fr": "La réponse du serveur", "it": "La risposta", "ja": "応答", "zh": "回应", "pt": "A resposta"},
}
SUITE = {
    "BTN_DELETE": {"en": "Delete", "es": "Eliminar", "de": "Löschen", "fr": "Supprimer", "it": "Elimina", "ja": "削除", "zh": "删除", "pt": "Eliminar"},
    "STATUS_CONNECTED": {"en": "Connected", "es": "Conectado", "de": "Verbunden", "fr": "Connecté", "it": "Connesso", "ja": "接続済み", "zh": "已连接", "pt": "Ligado"},
    "GREETING": {"en": "Hello {name}", "es": "Hola {name}", "de": "Hallo {name}", "fr": "Salut {name}", "it": "Ciao {name}", "ja": "{name}", "zh": "{name}", "pt": "Olá {name}"},
    "INFO": {"en": "The server's answer", "es": "La respuesta del servidor", "de": "Die Antwort", "fr": "La réponse du serveur", "it": "La risposta", "ja": "応答", "zh": "回应", "pt": "A resposta"},
}


def make(root: Path) -> None:
    locales = root / "HYDRA-UMC-STUDIO" / "src" / "locales"
    locales.mkdir(parents=True)
    for lang in tool.LANGS:
        (locales / f"{lang}.json").write_text(json.dumps({"k": {key: value[lang] for key, value in STUDIO.items()}}, ensure_ascii=False), encoding="utf-8")
    language = root / "HYDRA-UMC-SUITE" / "language"
    language.mkdir(parents=True)
    for lang, name in check.SUITE_NAMES.items():
        body = "# comment\n" + "".join(f"{key}={value[lang]}\n" for key, value in SUITE.items())
        (language / f"{name}.lng").write_text(body, encoding="utf-8")


def test_only_plain_texts_that_studio_reads_one_way_are_candidates(tmp_path):
    make(tmp_path)
    found = tool.candidates(check.readers(tmp_path), "suite")
    assert set(found) == {"Delete", "Connected"}
    assert "Hello {name}" not in found
    assert "The server's answer" not in found  # identical wording needs no change


def test_apply_writes_only_the_named_texts_and_keeps_the_rest(tmp_path):
    make(tmp_path)
    before = (tmp_path / "HYDRA-UMC-SUITE" / "language" / "spanish.lng").read_text(encoding="utf-8")
    assert tool.main(["--target", "suite", "--root", str(tmp_path), "--apply", "--only", "Delete"]) == 0
    spanish = (tmp_path / "HYDRA-UMC-SUITE" / "language" / "spanish.lng").read_text(encoding="utf-8")
    assert "BTN_DELETE=Borrar" in spanish
    assert "STATUS_CONNECTED=Conectado\n" in spanish
    assert spanish.replace("BTN_DELETE=Borrar", "BTN_DELETE=Eliminar") == before
    assert tool.candidates(check.readers(tmp_path), "suite").get("Delete") is None


def test_nothing_is_written_without_apply(tmp_path):
    make(tmp_path)
    before = (tmp_path / "HYDRA-UMC-SUITE" / "language" / "portuguese.lng").read_bytes()
    assert tool.main(["--target", "suite", "--root", str(tmp_path), "--list"]) == 0
    assert (tmp_path / "HYDRA-UMC-SUITE" / "language" / "portuguese.lng").read_bytes() == before


def test_the_apostrophe_of_the_client_is_kept():
    assert tool._in_style_of("l’adresse", "l'adresse") == "l’adresse"
    assert tool._in_style_of("l'adresse", "l'adresse") == "l'adresse"
    assert tool._same("l’adresse", "l'adresse")
    assert tool._same(chr(92) + "'x", "'x")
    assert tool._xml_escape("l'a & b") == "l" + chr(92) + "'a &amp; b"
