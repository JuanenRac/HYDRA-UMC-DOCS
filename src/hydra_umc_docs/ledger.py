# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/ledger.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The maturity ledger: for every repository of the family, what its maturity rests on.

A manifest says how mature a project is (`maturity`) and, separately, what it has been tried on (`evidence`: nothing, a
host test, a simulator, a bench, real hardware). The ledger puts the two side by side for the whole family, with a
colour token per kind of evidence, so a panel (the map of the ecosystem of STUDIO) can show the claim and its proof
together and never let a lighter proof stand in for a heavier one.

It is made only from the manifests and the hardware statement of `data/glance.json`; nothing is typed by hand. It holds
no date and no version, so it changes only when the maturity, the evidence or the hardware statement of a project does.
`gaps` are observations (a project is hardware bound and has not met hardware; a project is past scaffolding and records
no evidence), never verdicts: they do not fail anything. The colours are tokens (`neutral`, `info`, `warn`, `ok_soft`,
`ok`); the panel chooses the actual colours of its theme. The labels come in the eight languages."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
LANGUAGES = ("en", "es", "de", "fr", "it", "ja", "zh", "pt")

#: evidence kind -> colour token, from the lightest proof to the heaviest
EVIDENCE_COLOURS: dict[str, str] = {"none": "neutral", "host-test": "info", "simulator": "warn", "bench": "ok_soft", "hardware": "ok", "other": "neutral"}
HARDWARE_STATEMENTS = ("not_applicable", "not_run", "simulated", "bench", "in_use")

EVIDENCE_LABELS: dict[str, dict[str, str]] = {
    "none": {"en": "No evidence recorded", "es": "Sin evidencia registrada", "de": "Kein Nachweis erfasst", "fr": "Aucune preuve enregistrée", "it": "Nessuna evidenza registrata", "ja": "証跡の記録なし", "zh": "未记录证据", "pt": "Sem evidência registada"},
    "host-test": {"en": "Tested on a computer", "es": "Probado en un ordenador", "de": "Auf einem Rechner getestet", "fr": "Testé sur un ordinateur", "it": "Provato su un computer", "ja": "コンピューター上でテスト済み", "zh": "已在电脑上测试", "pt": "Testado num computador"},
    "simulator": {"en": "Tried on a simulator", "es": "Probado en un simulador", "de": "Auf einem Simulator erprobt", "fr": "Essayé sur un simulateur", "it": "Provato su un simulatore", "ja": "シミュレーターで試行済み", "zh": "已在模拟器上试用", "pt": "Experimentado num simulador"},
    "bench": {"en": "Tried on the bench", "es": "Probado en el banco", "de": "Auf dem Prüfstand erprobt", "fr": "Essayé sur le banc", "it": "Provato al banco", "ja": "ベンチで試行済み", "zh": "已在试验台上试用", "pt": "Experimentado na bancada"},
    "hardware": {"en": "Tried on real hardware", "es": "Probado en hardware real", "de": "Auf echter Hardware erprobt", "fr": "Essayé sur du matériel réel", "it": "Provato su hardware reale", "ja": "実機で試行済み", "zh": "已在真实硬件上试用", "pt": "Experimentado em hardware real"},
    "other": {"en": "Other evidence", "es": "Otra evidencia", "de": "Anderer Nachweis", "fr": "Autre preuve", "it": "Altra evidenza", "ja": "その他の証跡", "zh": "其他证据", "pt": "Outra evidência"},
}
GAP_LABELS: dict[str, dict[str, str]] = {
    "hardware-bound-not-on-hardware": {
        "en": "Needs hardware and has not met it", "es": "Necesita hardware y no lo ha tocado", "de": "Braucht Hardware und hatte keine", "fr": "A besoin de matériel et n'en a pas vu",
        "it": "Richiede hardware e non l'ha incontrato", "ja": "ハードウェアが必要だが未検証", "zh": "需要硬件但尚未接触", "pt": "Precisa de hardware e ainda não o encontrou",
    },
    "no-evidence-recorded": {
        "en": "Past scaffolding and no evidence recorded", "es": "Pasó de andamio y sin evidencia registrada", "de": "Über das Gerüst hinaus, aber ohne Nachweis", "fr": "Au-delà de l'ébauche et sans preuve enregistrée",
        "it": "Oltre l'impalcatura e senza evidenza registrata", "ja": "骨組みを超えているが証跡の記録なし", "zh": "已超出脚手架阶段但未记录证据", "pt": "Passou do andaime e sem evidência registada",
    },
}


def evidence_kind(value: object) -> str:
    """The kind of a manifest `evidence` text; a text this ledger does not know is `other`, an absent one is `none`."""
    if value is None:
        return "none"
    text = str(value).strip().lower()
    return text if text in EVIDENCE_COLOURS and text != "other" else "other"


def _row(manifest: dict[str, Any], glance_repos: dict[str, Any]) -> dict[str, Any]:
    name = str(manifest["name"])
    kind = evidence_kind(manifest.get("evidence"))
    maturity = str(manifest["maturity"])
    statement = (glance_repos.get(name) or {}).get("hardware")
    bound = manifest.get("hardware_bound")
    gaps = []
    if bound is True and kind not in {"bench", "hardware"}:
        gaps.append("hardware-bound-not-on-hardware")
    if kind == "none" and maturity != "scaffolding":
        gaps.append("no-evidence-recorded")
    return {
        "name": name,
        "maturity": maturity,
        "evidence": kind,
        "colour": EVIDENCE_COLOURS[kind],
        "hardware_bound": bound if isinstance(bound, bool) else None,
        "hardware_statement": statement if statement in HARDWARE_STATEMENTS else None,
        "gaps": gaps,
    }


def build(manifests: list[dict[str, Any]], glance_data: dict[str, Any]) -> dict[str, Any]:
    """The ledger of the given manifests (any family order; the rows come out sorted by name)."""
    raw_repos = glance_data.get("repos")
    glance_repos: dict[str, Any] = raw_repos if isinstance(raw_repos, dict) else {}
    rows = sorted((_row(manifest, glance_repos) for manifest in manifests), key=lambda row: row["name"])
    return {
        "schema_version": SCHEMA_VERSION,
        "evidence_kinds": [{"id": kind, "colour": colour, "label": EVIDENCE_LABELS[kind]} for kind, colour in EVIDENCE_COLOURS.items()],
        "gaps": [{"id": gap, "label": label} for gap, label in GAP_LABELS.items()],
        "summary": {
            "repositories": len(rows),
            "by_evidence": dict(sorted(Counter(row["evidence"] for row in rows).items())),
            "by_maturity": dict(sorted(Counter(row["maturity"] for row in rows).items())),
            "with_gaps": sum(1 for row in rows if row["gaps"]),
        },
        "repos": rows,
    }


def render(ledger: dict[str, Any]) -> str:
    return json.dumps(ledger, indent=2, ensure_ascii=False) + "\n"


def check(path: Path, ledger: dict[str, Any]) -> tuple[bool, str]:
    try:
        current = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    except OSError as exc:
        return False, f"{path.name} cannot be read ({exc})"
    if current != render(ledger):
        return False, f"{path.name} is out of date; write it again with make_ledger.py"
    return True, f"{path.name} is current ({ledger['summary']['repositories']} repositories)"
