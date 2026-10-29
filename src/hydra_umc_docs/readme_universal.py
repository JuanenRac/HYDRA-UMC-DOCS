# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/readme_universal.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Write the README of a repository of the family, in the eight languages, in the universal layout of 22 sections.

One source per repository (``readme_src/repos/<NAME>.py``) says what is specific to it; this module adds what is the same everywhere: the header, the
At a glance and Project status sections (written by :mod:`glance` and :mod:`status` from the manifest and ``data/glance.json``, so ``make_glance.py``
and this module always agree), the names, the icons and the order of the sections, Repository Structure (from ``docs/structure.json`` of the
repository), Languages, Documentation, Contributing, AUTHOR and LICENSE.

A source is a module with

* ``ICON`` and ``COMMENT`` (the emoji of the title and the one-line description in the licence comment at the top of the file);
* ``BADGES`` (``[(label, value, colour)]``) and ``BODY(lg, ctx)``, a mapping from the name of a section to its Markdown (without the heading). The
  sections that a source gives are the ones that appear; ``related`` and the rest of the fixed ones are added here.
"""
from __future__ import annotations

import importlib
import importlib.util
import json
import re
import sys
from pathlib import Path

from . import glance, readme_kit as K, status

REPO = Path(__file__).resolve().parents[2]
GITHUB = "https://github.com/JuanenRac/{name}"
LANGUAGES = [
    ("en", "README.md", "🇺🇸", "English"), ("es", "README_spa.md", "🇪🇸", "Español"), ("fr", "README_fra.md", "🇫🇷", "Français"), ("it", "README_ita.md", "🇮🇹", "Italiano"),
    ("de", "README_deu.md", "🇩🇪", "Deutsch"), ("zh", "README_zho.md", "🇨🇳", "简体中文"), ("ja", "README_jpn.md", "🇯🇵", "日本語"), ("pt", "README_por.md", "🇵🇹", "Português"),
]
FILE_OF = {code: file for code, file, _, _ in LANGUAGES}
MATURITY_COLOUR = {"scaffolding": "FFB020", "functional": "0F6CBD", "established": "2EA44F", "production": "2EA44F"}
# the order of the 22 sections, with their icons
SECTIONS = [
    ("glance", "📋"), ("status", "🚦"), ("overview", "🎯"), ("role", "🧩"), ("architecture", "🏛️"), ("screenshots", "🖼️"), ("features", "✨"), ("security", "🔒"),
    ("interfaces", "🔌"), ("configuration", "⚙️"), ("quickstart", "🚀"), ("testing", "🧪"), ("build", "🏗️"), ("troubleshooting", "🩺"), ("structure", "📂"),
    ("roadmap", "🗺️"), ("languages", "🌍"), ("related", "🔗"), ("documentation", "📚"), ("contributing", "🤝"), ("author", "👤"), ("license", "📜"),
]
ICON = dict(SECTIONS)
JUMP_SECTIONS = ["overview", "architecture", "features", "security", "interfaces", "configuration", "quickstart", "testing", "troubleshooting", "structure", "related"]
ALWAYS = {"glance", "status", "structure", "languages", "related", "documentation", "contributing", "author", "license"}


def _check_module():
    """tools/universal_readme_check.py of this repository: it owns the names of the sections in the eight languages."""
    name = "_hydra_universal_readme_check"
    if name in sys.modules:
        return sys.modules[name]
    path = REPO / "tools" / "universal_readme_check.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def section_name(lg: str, section: str) -> str:
    if section == "role":
        return K.ROLE_NAME[lg]
    return _check_module().NAMES[lg][section]


def heading(lg: str, section: str) -> str:
    return f"## {ICON[section]} {section_name(lg, section)}"


def jump_line(lg: str, present: list[str]) -> str:
    """The "Jump to" line of At a glance, from the sections the README has."""
    links = " · ".join(f"[{section_name(lg, s)}](#{K.github_anchor(heading(lg, s)[3:])})" for s in JUMP_SECTIONS if s in present)
    return f"{K.JUMP[lg]} {links}"


def present_sections(text: str) -> list[str]:
    """The sections (by name) that the level-two headings of a README text stand for."""
    by_icon = {icon.replace("️", ""): section for section, icon in SECTIONS}
    found, fenced = [], False
    for line in text.replace("\r\n", "\n").split("\n"):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        elif not fenced and line.startswith("## "):
            icon = line[3:].split(" ", 1)[0].replace("️", "")
            if icon in by_icon:
                found.append(by_icon[icon])
    return found


def load_source(name: str):
    module = "readme_src.repos." + name.replace("-", "_")
    return importlib.import_module("hydra_umc_docs." + module)


def structure_tool(repo: Path):
    path = repo / "tools" / "make_structure.py"
    spec = importlib.util.spec_from_file_location("_hydra_make_structure_" + repo.name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(path.parent))
    return module


class Context:
    """What a source may read: the name, the manifest, the number of tests and the text tree of docs/structure.json."""

    def __init__(self, repo: Path, entry: dict, manifest: dict):
        self.repo, self.name, self.manifest, self.entry = repo, repo.name, manifest, entry
        self.tests = entry["tests"]["count"]
        self.version, self.maturity = manifest["version"], manifest["maturity"]

    def tree(self, lg: str) -> str:
        tool = structure_tool(self.repo)
        return tool.render_tree(tool.load_spec(self.repo / "docs" / "structure.json"), lg)

    def v(self, lg: str, key: str) -> str:
        return K.verbatim(self.name, lg, key, tests=self.tests, version=self.version)

    def has(self, lg: str, key: str) -> bool:
        return K.has_verbatim(self.name, lg, key)


def render(repo: Path, lg: str, entry: dict) -> str:
    source = load_source(repo.name)
    manifest = glance.load_manifest(repo)
    ctx = Context(repo, entry, manifest)
    body = source.BODY(lg, ctx)
    structure_extra = body.pop("structure", "")
    bodies = {key: text.strip() for key, text in body.items() if text and text.strip()}
    present = [s for s, _ in SECTIONS if s in ALWAYS or s in bodies]
    name = repo.name
    badges = [b for b in source.BADGES if b[0] not in ("Tests", "Version", "Maturity")]
    badges.append(("Tests", f"{ctx.tests}%20passing", "2ea44f"))
    badges.append(("Version", ctx.version, "0f6cbd"))
    badges.append(("Maturity", ctx.maturity, MATURITY_COLOUR.get(ctx.maturity, "0f6cbd")))
    alt = {"License": "GPL 3.0 or later"}
    badge_html = '  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">\n' + "\n".join(
        f'  <img src="https://img.shields.io/badge/{label}-{value}-{colour}.svg" alt="{alt.get(label, label)}">' for label, value, colour in badges)
    bar = " | ".join(f"{flag} <b>{title}</b>" if code == lg else f'<a href="{file}">{flag} {title}</a>' for code, file, flag, title in LANGUAGES)
    parts = [f"""<!-- =============================================================================
{name} - {source.COMMENT}
Copyright (C) JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
GPL-3.0-or-later - see LICENSE
============================================================================= -->

<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="{name} banner" width="100%">
</p>

# {source.ICON} {name}

<p align="center">{bar}</p>

### {ctx.v(lg, 'tagline')}

<p align="center">
{badge_html}
</p>

---

{ctx.v(lg, 'honesty')}

---
"""]
    for section in present:
        if section == "glance":
            text = glance.render_section(lg, manifest, entry).rstrip("\n")
            parts.append(text + "\n\n" + jump_line(lg, present) + "\n")
        elif section == "status":
            parts.append(status.render_section(lg, manifest, entry).rstrip("\n") + "\n")
        elif section == "structure":
            tree = ctx.tree(lg)
            spec_svg = f'<p align="center">\n  <img src="images/repository-structure.svg" alt="Repository structure of {name}" width="100%">\n</p>'
            details = f"<details>\n<summary>{K.SUMMARY_TREE[lg]}</summary>\n\n```text\n{tree}\n```\n\n</details>"
            extra = ("\n\n" + structure_extra.strip()) if structure_extra.strip() else ""
            parts.append(f"{heading(lg, 'structure')}\n\n{spec_svg}\n\n{details}{extra}\n")
        elif section == "languages":
            ui = K.NO_UI[lg] if getattr(source, "NO_UI", True) else ""
            parts.append(f"{heading(lg, 'languages')}\n\n{K.LANGUAGES_TEXT[lg]} {ui}".rstrip() + "\n")
        elif section == "documentation":
            items = list(source.DOCS(lg, ctx)) if hasattr(source, "DOCS") else []
            sec = "https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/"
            items += [f"[{K.DOC_SECURITY_BASELINE[lg]}]({sec}SECURITY_BASELINE.md)", f"[{K.DOC_THREAT_MODEL[lg]}]({sec}THREAT_MODEL.md)",
                      f"[{K.DOC_CHANGELOG[lg]}](CHANGELOG.md)", f"[{K.DOC_LICENSE[lg]}](LICENSE.md)"]
            parts.append(f"{heading(lg, 'documentation')}\n\n{K.DOCS_INTRO[lg]}\n\n" + "\n".join(f"* {item}" for item in items) + "\n")
        elif section == "contributing":
            parts.append(f"{heading(lg, 'contributing')}\n\n" + "\n".join(f"* {item}" for item in K.CONTRIB[lg]) + "\n")
        elif section == "author":
            parts.append(f"{heading(lg, 'author')}\n\n**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com\n")
        elif section == "license":
            parts.append(f"{heading(lg, 'license')}\n\nGPL-3.0-or-later - [LICENSE](LICENSE).\n")
        else:
            parts.append(f"{heading(lg, section)}\n\n{bodies[section]}\n")
    return "\n".join(parts)


def outputs(repo: Path, entry: dict) -> dict[str, str]:
    return {FILE_OF[lg]: render(repo, lg, entry) for lg in K.LGS}
