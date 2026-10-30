# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/status.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The "Project status" traffic-light table of the README of every repository, in the eight languages.

Like the "At a glance" table it is made only from what the repository can show: the maturity of its
manifest, the test count and the hardware statement of data/glance.json. Nothing is typed by hand, so
the table can never say more than those data say. The section sits right after "At a glance" and is
rewritten in place; :func:`check_text` says what is missing, misplaced or stale. The State column
holds only the light.
"""
from __future__ import annotations

import re

from . import glance

LIGHTS = {"green": "🟢", "yellow": "🟡", "orange": "🟠", "red": "🔴"}

MATURITY_LIGHT = {"scaffolding": "orange", "functional": "yellow", "established": "green", "production": "green"}
LOW_MATURITY = {"scaffolding"}
HARDWARE_LIGHT = {"not_applicable": "green", "not_run": "red", "simulated": "orange", "bench": "yellow", "in_use": "green"}

UI: dict[str, dict[str, str]] = {
    "en": {"heading": "Project status", "intro": "Each line is one part of this repository and the light says how far it is today. It is written from what the repository can show (tests, builds, runs), not from what is planned.",
           "area": "Area", "state": "State", "note": "What it means here", "software": "Software", "tests": "Tests", "hardware": "Real hardware", "docs": "Documentation",
           "green": "Done and verified", "yellow": "Works, with known limits", "orange": "Partly done or not verified yet", "red": "Not done or not working"},
    "es": {"heading": "Estado del proyecto", "intro": "Cada línea es una parte de este repositorio y la luz dice hasta dónde llega hoy. Se escribe con lo que el repositorio puede demostrar (pruebas, compilaciones, ejecuciones), no con lo previsto.",
           "area": "Área", "state": "Estado", "note": "Qué significa aquí", "software": "Software", "tests": "Pruebas", "hardware": "Hardware real", "docs": "Documentación",
           "green": "Hecho y verificado", "yellow": "Funciona, con límites conocidos", "orange": "Hecho a medias o sin verificar", "red": "Sin hacer o sin funcionar"},
    "de": {"heading": "Projektstatus", "intro": "Jede Zeile ist ein Teil dieses Repositorys, und die Ampel sagt, wie weit er heute ist. Sie beruht auf dem, was das Repository zeigen kann (Tests, Builds, Läufe), nicht auf dem, was geplant ist.",
           "area": "Bereich", "state": "Stand", "note": "Was das hier bedeutet", "software": "Software", "tests": "Tests", "hardware": "Echte Hardware", "docs": "Dokumentation",
           "green": "Fertig und überprüft", "yellow": "Funktioniert, mit bekannten Grenzen", "orange": "Teilweise fertig oder noch nicht überprüft", "red": "Nicht gemacht oder funktioniert nicht"},
    "fr": {"heading": "État du projet", "intro": "Chaque ligne est une partie de ce dépôt et le feu dit où elle en est aujourd'hui. Elle est écrite d'après ce que le dépôt peut montrer (tests, compilations, exécutions), pas d'après ce qui est prévu.",
           "area": "Domaine", "state": "État", "note": "Ce que cela veut dire ici", "software": "Logiciel", "tests": "Tests", "hardware": "Matériel réel", "docs": "Documentation",
           "green": "Fait et vérifié", "yellow": "Fonctionne, avec des limites connues", "orange": "À moitié fait ou pas encore vérifié", "red": "Pas fait ou ne fonctionne pas"},
    "it": {"heading": "Stato del progetto", "intro": "Ogni riga è una parte di questo repository e il semaforo dice a che punto è oggi. È scritta in base a ciò che il repository può mostrare (test, compilazioni, esecuzioni), non a ciò che è previsto.",
           "area": "Area", "state": "Stato", "note": "Cosa significa qui", "software": "Software", "tests": "Test", "hardware": "Hardware reale", "docs": "Documentazione",
           "green": "Fatto e verificato", "yellow": "Funziona, con limiti noti", "orange": "Fatto a metà o non ancora verificato", "red": "Non fatto o non funzionante"},
    "ja": {"heading": "プロジェクトの状況", "intro": "各行はこのリポジトリの一部分で、信号は今日どこまで進んでいるかを示します。計画ではなく、リポジトリが示せるもの（テスト、ビルド、実行）に基づいて書かれています。",
           "area": "領域", "state": "状態", "note": "ここでの意味", "software": "ソフトウェア", "tests": "テスト", "hardware": "実機", "docs": "ドキュメント",
           "green": "完了・検証済み", "yellow": "動作する（既知の制限あり）", "orange": "一部のみ、または未検証", "red": "未実装または動作しない"},
    "zh": {"heading": "项目状态", "intro": "每一行是本仓库的一个部分，灯号表示它今天做到了哪一步。内容依据仓库能够展示的证据（测试、构建、运行），而不是计划。",
           "area": "领域", "state": "状态", "note": "在这里的含义", "software": "软件", "tests": "测试", "hardware": "真实硬件", "docs": "文档",
           "green": "已完成并验证", "yellow": "可用，有已知限制", "orange": "部分完成或尚未验证", "red": "未完成或不可用"},
    "pt": {"heading": "Estado do projeto", "intro": "Cada linha é uma parte deste repositório e a luz diz até onde chega hoje. É escrita com o que o repositório consegue demonstrar (testes, compilações, execuções), não com o que está previsto.",
           "area": "Área", "state": "Estado", "note": "O que significa aqui", "software": "Software", "tests": "Testes", "hardware": "Hardware real", "docs": "Documentação",
           "green": "Feito e verificado", "yellow": "Funciona, com limites conhecidos", "orange": "Feito a meio ou ainda por verificar", "red": "Por fazer ou a não funcionar"},
}

# the notes: software by maturity, tests with {n} or without a recorded count, documentation
NOTES: dict[str, dict[str, str]] = {
    "en": {"scaffolding": "Structure and first pieces only; most of the work is still to do",
           "functional": "Works for its main purpose; the honesty check above lists what is still missing",
           "established": "Complete for its purpose and stable; the honesty check above lists the known limits",
           "production": "In production use; the honesty check above lists the known limits",
           "tests": "{n} automated tests, run on every change", "tests_none": "No test count is recorded for this repository yet",
           "docs": "README in eight languages, checked against the manifest on every change"},
    "es": {"scaffolding": "Solo estructura y primeras piezas; falta la mayor parte del trabajo",
           "functional": "Funciona para su propósito principal; la comprobación de honestidad de arriba lista lo que aún falta",
           "established": "Completo para su propósito y estable; la comprobación de honestidad de arriba lista los límites conocidos",
           "production": "En uso en producción; la comprobación de honestidad de arriba lista los límites conocidos",
           "tests": "{n} pruebas automáticas, ejecutadas en cada cambio", "tests_none": "Todavía no consta el número de pruebas de este repositorio",
           "docs": "README en ocho idiomas, comprobado contra el manifiesto en cada cambio"},
    "de": {"scaffolding": "Nur Struktur und erste Teile; der größte Teil der Arbeit steht noch aus",
           "functional": "Funktioniert für seinen Hauptzweck; die Ehrlichkeitsprüfung oben nennt, was noch fehlt",
           "established": "Für seinen Zweck vollständig und stabil; die Ehrlichkeitsprüfung oben nennt die bekannten Grenzen",
           "production": "Im produktiven Einsatz; die Ehrlichkeitsprüfung oben nennt die bekannten Grenzen",
           "tests": "{n} automatische Tests, bei jeder Änderung ausgeführt", "tests_none": "Für dieses Repository ist noch keine Testanzahl vermerkt",
           "docs": "README in acht Sprachen, bei jeder Änderung gegen das Manifest geprüft"},
    "fr": {"scaffolding": "Seulement la structure et les premières pièces ; l'essentiel du travail reste à faire",
           "functional": "Fonctionne pour son usage principal ; la vérification d'honnêteté ci-dessus liste ce qui manque encore",
           "established": "Complet pour son usage et stable ; la vérification d'honnêteté ci-dessus liste les limites connues",
           "production": "En usage en production ; la vérification d'honnêteté ci-dessus liste les limites connues",
           "tests": "{n} tests automatiques, exécutés à chaque modification", "tests_none": "Aucun nombre de tests n'est encore consigné pour ce dépôt",
           "docs": "README en huit langues, vérifié par rapport au manifeste à chaque modification"},
    "it": {"scaffolding": "Solo struttura e primi pezzi; gran parte del lavoro è ancora da fare",
           "functional": "Funziona per il suo scopo principale; la verifica di onestà qui sopra elenca ciò che manca ancora",
           "established": "Completo per il suo scopo e stabile; la verifica di onestà qui sopra elenca i limiti noti",
           "production": "In uso in produzione; la verifica di onestà qui sopra elenca i limiti noti",
           "tests": "{n} test automatici, eseguiti a ogni modifica", "tests_none": "Per questo repository non è ancora registrato il numero di test",
           "docs": "README in otto lingue, verificato rispetto al manifesto a ogni modifica"},
    "ja": {"scaffolding": "構造と最初の部品のみで、作業の大部分はこれからです",
           "functional": "主な目的では動作します。足りない点は上の正直さの確認に書かれています",
           "established": "目的に対して完成していて安定しています。既知の制限は上の正直さの確認に書かれています",
           "production": "本番で使用中です。既知の制限は上の正直さの確認に書かれています",
           "tests": "自動テスト {n} 件。変更のたびに実行されます", "tests_none": "このリポジトリのテスト件数はまだ記録されていません",
           "docs": "8 言語の README。変更のたびにマニフェストと照合されます"},
    "zh": {"scaffolding": "目前只有结构和最初的部分，大部分工作尚未完成",
           "functional": "主要用途可用；上面的诚实性检查列出了仍然缺少的内容",
           "established": "就其用途而言已完整且稳定；上面的诚实性检查列出了已知限制",
           "production": "已投入生产使用；上面的诚实性检查列出了已知限制",
           "tests": "{n} 项自动测试，每次变更都会运行", "tests_none": "此仓库尚未记录测试数量",
           "docs": "八种语言的 README，每次变更都会与清单核对"},
    "pt": {"scaffolding": "Só estrutura e as primeiras peças; falta a maior parte do trabalho",
           "functional": "Funciona para o seu propósito principal; a verificação de honestidade acima lista o que ainda falta",
           "established": "Completo para o seu propósito e estável; a verificação de honestidade acima lista os limites conhecidos",
           "production": "Em uso em produção; a verificação de honestidade acima lista os limites conhecidos",
           "tests": "{n} testes automáticos, executados a cada alteração", "tests_none": "Ainda não há registo do número de testes deste repositório",
           "docs": "README em oito idiomas, verificado contra o manifesto a cada alteração"},
}

HEADING = re.compile(r"^## 🚦 ")
ANY_H2 = re.compile(r"^## ")
FENCE = re.compile(r"^\s*(```|~~~)")


def rows(code: str, manifest: dict, entry: dict) -> list[tuple[str, str, str]]:
    """(area, light, note) for the common areas of one repository in one language."""
    ui, notes = UI[code], NOTES[code]
    maturity = str(manifest["maturity"])
    tests = entry.get("tests")
    made = [
        (ui["software"], MATURITY_LIGHT.get(maturity, "orange"), notes.get(maturity, notes["functional"])),
        (ui["tests"], "green" if tests else "orange", notes["tests"].format(n=tests["count"]) if tests else notes["tests_none"]),
        (ui["hardware"], HARDWARE_LIGHT[entry["hardware"]], glance.HARDWARE[code][entry["hardware"]]),
        (ui["docs"], "green", notes["docs"]),
    ]
    if maturity in LOW_MATURITY:
        # the same ceiling tools/status_lights.py checks: a repository that is still scaffolding has no green row
        made = [(area, "yellow" if level == "green" else level, note) for area, level, note in made]
    return made


def render_section(code: str, manifest: dict, entry: dict) -> str:
    """The section for one language, with LF line endings and a closing blank line."""
    ui = UI[code]
    legend = " · ".join(f"{LIGHTS[level]} {ui[level]}" for level in LIGHTS)
    lines = [f"## 🚦 {ui['heading']}", "", ui["intro"], "", legend, "", f"| {ui['area']} | {ui['state']} | {ui['note']} |", "|---|---|---|"]
    for area, level, note in rows(code, manifest, entry):
        lines.append(f"| {glance._cell(area)} | {LIGHTS[level]} | {glance._cell(note)} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def _locate(lines: list[str]) -> tuple[int | None, int | None, int | None]:
    """(start of an existing status section, its end, the end of the glance section where a new one belongs)."""
    fenced, headings = False, []
    for index, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and ANY_H2.match(line):
            headings.append(index)
    start = end = None
    for position, index in enumerate(headings):
        if HEADING.match(lines[index]):
            start = index
            end = headings[position + 1] if position + 1 < len(headings) else len(lines)
            break
    _, glance_end, _ = glance.locate(lines)
    return start, end, glance_end


def apply_to_text(text: str, section: str) -> str:
    """Insert the section right after the glance section, or rewrite it where it is. Idempotent."""
    lines, newline = glance._split(text)
    start, end, after_glance = _locate(lines)
    block = section.split("\n")[:-1]
    if start is not None:
        lines[start:end] = block
    elif after_glance is not None:
        lines[after_glance:after_glance] = block
    else:
        raise glance.GlanceError("no 'At a glance' section to put the status after")
    return newline.join(lines)


def check_text(text: str, section: str) -> list[str]:
    lines, _ = glance._split(text)
    start, end, after_glance = _locate(lines)
    if start is None:
        return ["the status table is missing"]
    problems = []
    g_start, g_end, _ = glance.locate(lines)
    if g_start is None or g_end != start:
        problems.append("the status table does not follow the 'At a glance' section")
    if "\n".join(lines[start:end]) + "\n" != section:
        problems.append("the status table is stale (maturity, tests or hardware differ from the data)")
    return problems


def apply_repo(repo, entry: dict) -> list[str]:
    """Write the eight sections; a repository whose entry says "status": "own" keeps the table its own README carries."""
    if entry.get("status") == "own":
        return []
    changed = []
    manifest = glance.load_manifest(repo)
    for code in glance.LANGUAGE_FILES:
        path = glance.readme_path(repo, code)
        original = path.read_bytes().decode("utf-8")
        updated = apply_to_text(original, render_section(code, manifest, entry))
        if updated != original:
            path.write_bytes(updated.encode("utf-8"))
            changed.append(path.name)
    return changed


def check_repo(repo, entry: dict) -> list[str]:
    if entry.get("status") == "own":
        return []
    problems = []
    manifest = glance.load_manifest(repo)
    for code in glance.LANGUAGE_FILES:
        path = glance.readme_path(repo, code)
        if not path.is_file():
            continue
        for problem in check_text(path.read_bytes().decode("utf-8"), render_section(code, manifest, entry)):
            problems.append(f"{repo.name}/{path.name}: {problem}")
    return problems
