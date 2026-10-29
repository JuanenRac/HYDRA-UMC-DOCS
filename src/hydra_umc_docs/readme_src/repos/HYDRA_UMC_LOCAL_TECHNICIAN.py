# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_LOCAL_TECHNICIAN.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-LOCAL-TECHNICIAN."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🤖'
COMMENT = 'Local, policy-gated maintenance assistant'
BADGES = [('Language', 'Python%203.11%2B', 'blue'), ('Core', 'stdlib%20only', 'brightgreen'), ('Phase', '1%2C%203%20%26%204%20of%206%20complete', '367BF5')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.11",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh contracts validate tests/fixtures/tool_request.valid.json --contract ToolRequest",
        "./run.sh --version"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-LOCAL-TECHNICIAN architecture",
    "role": {
        "en": "**HYDRA-UMC-LOCAL-TECHNICIAN** is the local maintenance assistant of the ecosystem: it observes, explains and proposes, and a model's text is never authority to act. Its tools are allow-listed and read-only, and what it finds is handed to people or to `HYDRA-UMC-OPS-AGENT` as evidence and proposals.",
        "es": "**HYDRA-UMC-LOCAL-TECHNICIAN** es el asistente de mantenimiento local del ecosistema: observa, explica y propone, y el texto de un modelo nunca es autoridad para actuar. Sus herramientas están permitidas y son de solo lectura, y lo que encuentra se entrega a personas o a `HYDRA-UMC-OPS-AGENT` como pruebas y propuestas.",
        "de": "**HYDRA-UMC-LOCAL-TECHNICIAN** ist der lokale Wartungsassistent des Ökosystems: Er beobachtet, erklärt und schlägt vor, und der Text eines Modells ist nie eine Berechtigung zum Handeln. Seine Werkzeuge sind freigegeben und nur lesend, und was er findet, geht als Belege und Vorschläge an Menschen oder an `HYDRA-UMC-OPS-AGENT`.",
        "fr": "**HYDRA-UMC-LOCAL-TECHNICIAN** est l'assistant de maintenance local de l'écosystème : il observe, explique et propose, et le texte d'un modèle n'est jamais une autorité pour agir. Ses outils sont autorisés et en lecture seule, et ce qu'il trouve est remis à des personnes ou à `HYDRA-UMC-OPS-AGENT` sous forme de preuves et de propositions.",
        "it": "**HYDRA-UMC-LOCAL-TECHNICIAN** è l'assistente di manutenzione locale dell'ecosistema: osserva, spiega e propone, e il testo di un modello non è mai un'autorità per agire. I suoi strumenti sono ammessi e in sola lettura, e ciò che trova viene consegnato a persone o a `HYDRA-UMC-OPS-AGENT` come prove e proposte.",
        "ja": "**HYDRA-UMC-LOCAL-TECHNICIAN** はエコシステムのローカルな保守アシスタントです。観察し、説明し、提案しますが、モデルの出力した文章が動作の権限になることはありません。ツールは許可リストにある読み取り専用のもので、見つけたことは証拠と提案として人または `HYDRA-UMC-OPS-AGENT` に渡されます。",
        "zh": "**HYDRA-UMC-LOCAL-TECHNICIAN** 是生态系统的本地维护助手：它观察、解释并提出建议，模型生成的文本永远不是行动的授权。它的工具在允许列表内且只读，发现的内容会作为证据和建议交给人或 `HYDRA-UMC-OPS-AGENT`。",
        "pt": "O **HYDRA-UMC-LOCAL-TECHNICIAN** é o assistente de manutenção local do ecossistema: observa, explica e propõe, e o texto de um modelo nunca é autoridade para agir. As suas ferramentas são permitidas e só de leitura, e o que encontra é entregue a pessoas ou ao `HYDRA-UMC-OPS-AGENT` como provas e propostas."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
