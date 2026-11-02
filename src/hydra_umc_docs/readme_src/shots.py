# The screenshots of the READMEs: each repository that has a window or a web page lists its pictures in docs/screenshots.json (the pictures live in its
# images/screenshots/), with a short name and a caption in the eight languages. The pictures are taken on a test bench with made-up sample data.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""``load(repo)`` reads and checks ``docs/screenshots.json``; ``section(lg, repo)`` is the body of the Screenshots section (the note, then a picture and its caption).

The file is ``{"screens": [{"file": "overview.png", "alt": {<8 languages>}, "caption": {<8 languages>}}]}``. ``problems(repo)`` lists what is wrong: a language
missing, a file that does not exist or is not a PNG, a picture heavier than ``MAX_BYTES`` or more than ``MAX_SHOTS`` pictures.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

MAX_BYTES = 400 * 1024
MAX_SHOTS = 8
LANGS = ("en", "es", "fr", "it", "de", "zh", "ja", "pt")
RELATIVE = Path("docs") / "screenshots.json"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

NOTE = {
    "en": "Captured on a test bench with made-up sample data and no real installation behind them.",
    "es": "Capturadas en un banco de pruebas con datos de ejemplo inventados y sin ninguna instalación real detrás.",
    "fr": "Capturées sur un banc d'essai avec des données d'exemple fictives et sans installation réelle derrière.",
    "it": "Catturate su un banco di prova con dati di esempio inventati e senza alcuna installazione reale dietro.",
    "de": "Aufgenommen auf einem Prüfstand mit erfundenen Beispieldaten und ohne eine echte Anlage dahinter.",
    "zh": "在测试台上使用虚构的示例数据截取，背后没有真实的安装。",
    "ja": "テストベンチで架空のサンプルデータを使って撮影したもので、実際の設備は接続されていません。",
    "pt": "Capturadas numa bancada de testes com dados de exemplo inventados e sem qualquer instalação real por trás.",
}


def read(repo: Path) -> list[dict[str, Any]] | None:
    """The screens listed by the repository, or None when it has no docs/screenshots.json."""
    path = repo / RELATIVE
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    screens = data.get("screens") if isinstance(data, dict) else None
    return screens if isinstance(screens, list) else []


def problems(repo: Path) -> list[str]:
    """Everything that is wrong with the screenshots of a repository (an empty list when there are none or all is well)."""
    screens = read(repo)
    if screens is None:
        return []
    found: list[str] = []
    if not screens:
        found.append(f"{RELATIVE.as_posix()} lists no screens")
    if len(screens) > MAX_SHOTS:
        found.append(f"{len(screens)} screenshots; at most {MAX_SHOTS}")
    seen: set[str] = set()
    for index, screen in enumerate(screens):
        name = screen.get("file") if isinstance(screen, dict) else None
        if not isinstance(name, str) or not name.endswith(".png") or "/" in name or "\\" in name:
            found.append(f"screen {index}: 'file' must be the name of a .png")
            continue
        if name in seen:
            found.append(f"{name}: listed twice")
        seen.add(name)
        for key in ("alt", "caption"):
            texts = screen.get(key)
            missing = [lg for lg in LANGS if not isinstance(texts, dict) or not str(texts.get(lg, "")).strip()]
            if missing:
                found.append(f"{name}: '{key}' lacks {', '.join(missing)}")
        picture = repo / "images" / "screenshots" / name
        if not picture.is_file():
            found.append(f"{name}: images/screenshots/{name} does not exist")
        elif picture.stat().st_size > MAX_BYTES:
            found.append(f"{name}: {picture.stat().st_size} bytes; at most {MAX_BYTES}")
        elif not picture.read_bytes().startswith(PNG_MAGIC):
            found.append(f"{name}: not a PNG")
    return found


def has(repo: Path) -> bool:
    return (repo / RELATIVE).is_file()


def section(lg: str, repo: Path) -> str:
    """The body of the Screenshots section: the note and, for each picture, the picture and its caption (the pattern of the other families)."""
    bad = problems(repo)
    if bad:
        raise ValueError(f"{repo.name}: screenshots: " + "; ".join(bad))
    blocks = [NOTE[lg]]
    for screen in read(repo) or []:
        blocks.append(f'<p align="center">\n  <img src="images/screenshots/{screen["file"]}" alt="{screen["alt"][lg]}" width="100%">\n</p>')
        blocks.append(f'<p align="center"><em>{screen["caption"][lg]}</em></p>')
    return "\n\n".join(blocks)
