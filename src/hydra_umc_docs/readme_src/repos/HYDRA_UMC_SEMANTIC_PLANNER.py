# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_SEMANTIC_PLANNER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-SEMANTIC-PLANNER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🧭'
COMMENT = 'Rule-based mission planner and semantic error recovery'
BADGES = []
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh decompose \"assemble the pcb\"",
        "./run.sh recover --component gripper --error-code TIMEOUT",
        "./run.sh serve --port 8110"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-SEMANTIC-PLANNER architecture",
    "role": {
        "en": "**HYDRA-UMC-SEMANTIC-PLANNER** turns a high-level goal into a plan made of a closed vocabulary of robot primitives and proposes a recovery when a step fails. Today it is rule-based, not a language model; a plan is only a proposal until a named person approves that exact plan.",
        "es": "**HYDRA-UMC-SEMANTIC-PLANNER** convierte un objetivo de alto nivel en un plan hecho con un vocabulario cerrado de primitivas del robot y propone una recuperación cuando falla un paso. Hoy se basa en reglas, no en un modelo de lenguaje; un plan es solo una propuesta hasta que una persona con nombre aprueba ese plan exacto.",
        "de": "**HYDRA-UMC-SEMANTIC-PLANNER** macht aus einem übergeordneten Ziel einen Plan aus einem geschlossenen Vokabular von Roboter-Primitiven und schlägt eine Wiederherstellung vor, wenn ein Schritt scheitert. Heute arbeitet er regelbasiert, nicht mit einem Sprachmodell; ein Plan ist nur ein Vorschlag, bis eine benannte Person genau diesen Plan freigibt.",
        "fr": "**HYDRA-UMC-SEMANTIC-PLANNER** transforme un objectif de haut niveau en un plan fait d'un vocabulaire fermé de primitives du robot et propose une reprise quand une étape échoue. Aujourd'hui il est fondé sur des règles, pas sur un modèle de langage ; un plan n'est qu'une proposition tant qu'une personne nommée n'a pas approuvé ce plan exact.",
        "it": "**HYDRA-UMC-SEMANTIC-PLANNER** trasforma un obiettivo di alto livello in un piano fatto di un vocabolario chiuso di primitive del robot e propone un ripristino quando un passo fallisce. Oggi è basato su regole, non su un modello linguistico; un piano è solo una proposta finché una persona con nome non approva quel piano esatto.",
        "ja": "**HYDRA-UMC-SEMANTIC-PLANNER** は高レベルの目標を、閉じたロボットプリミティブの語彙で作られた計画に変換し、ステップが失敗したときの回復案を提案します。現在はルールベースで言語モデルではなく、計画は名前のある担当者がその計画そのものを承認するまで提案にすぎません。",
        "zh": "**HYDRA-UMC-SEMANTIC-PLANNER** 把高层目标转换为由封闭的机器人原语词汇组成的计划，并在某一步失败时提出恢复方案。目前它基于规则而不是语言模型；在具名人员批准这份确切的计划之前，计划只是建议。",
        "pt": "O **HYDRA-UMC-SEMANTIC-PLANNER** transforma um objetivo de alto nível num plano feito de um vocabulário fechado de primitivas do robô e propõe uma recuperação quando um passo falha. Hoje baseia-se em regras, não num modelo de linguagem; um plano é apenas uma proposta até uma pessoa identificada aprovar esse plano exato."
    }
}


from ... import readme_kit as K

EXTRAS = {}


def EXTRA(lg):
    out = {}
    sec = EXTRAS.get("security")
    if sec:
        out["security"] = K.table(lg, "threat", sec["rows"]) + ("\n\n" + K.pick(sec["never"], lg) if sec.get("never") else "")
    cfg = EXTRAS.get("configuration")
    if cfg:
        out["configuration"] = (K.pick(cfg["intro"], lg) + "\n\n" if cfg.get("intro") else "") + K.table(lg, "config", cfg["rows"])
    trb = EXTRAS.get("troubleshooting")
    if trb:
        out["troubleshooting"] = K.table(lg, "trouble", trb)
    itf = EXTRAS.get("interfaces")
    if itf:
        out["interfaces"] = K.table(lg, itf["head"], itf["rows"]) if isinstance(itf["head"], str) else K.table(lg, [K.pick(h, lg) for h in itf["head"]], itf["rows"])
    return out


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    body = S.make_body(lg, ctx, SPEC)
    body.update(EXTRA(lg))
    return body
