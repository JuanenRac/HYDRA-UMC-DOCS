# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_GATEWAY_INDUSTRIAL.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-GATEWAY-INDUSTRIAL."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🌐'
COMMENT = 'Single status surface in front of the industrial bridges'
BADGES = [('Standard', 'Industry%204.0', 'blue'), ('Security', 'TLS%20and%20mTLS%20optional%2C%20off%20by%20default', 'orange'), ('Protocols', 'OPC--UA%20%2F%20MQTT%20%2F%20MTConnect', 'orange')]
NO_UI = True

SPEC = {
    "stack": "node",
    "req": "20",
    "quick": [
        "npm install",
        "npm test",
        "npm run build",
        "npm start"
    ],
    "test_cmd": "npm test",
    "alt": "HYDRA-UMC-GATEWAY-INDUSTRIAL architecture",
    "role": {
        "en": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** is the single status surface in front of `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` and `HYDRA-UMC-MTCONNECT-ADAPTER`: it checks that each answers and accepts only an allow-listed set of commands whose effect is a reachability check. It never moves a machine.",
        "es": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** es la superficie de estado única delante de `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` y `HYDRA-UMC-MTCONNECT-ADAPTER`: comprueba que cada uno responde y acepta solo un conjunto permitido de órdenes cuyo efecto es una comprobación de alcance. Nunca mueve una máquina.",
        "de": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** ist die einzige Statusfläche vor `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` und `HYDRA-UMC-MTCONNECT-ADAPTER`: Er prüft, ob jeder antwortet, und nimmt nur freigegebene Befehle an, deren Wirkung eine Erreichbarkeitsprüfung ist. Er bewegt nie eine Maschine.",
        "fr": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** est la surface d'état unique devant `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` et `HYDRA-UMC-MTCONNECT-ADAPTER` : il vérifie que chacun répond et n'accepte qu'un ensemble autorisé de commandes dont l'effet est un test de joignabilité. Il ne déplace jamais une machine.",
        "it": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** è l'unica superficie di stato davanti a `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` e `HYDRA-UMC-MTCONNECT-ADAPTER`: verifica che ognuno risponda e accetta solo un insieme ammesso di comandi il cui effetto è un controllo di raggiungibilità. Non muove mai una macchina.",
        "ja": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** は `HYDRA-UMC-OPCUA-SERVER`、`HYDRA-UMC-MQTT-BROKER`、`HYDRA-UMC-MTCONNECT-ADAPTER` の手前にある単一のステータス窓口です。それぞれが応答するかを確認し、効果が到達性の確認だけに限られる許可リストのコマンドしか受け付けません。機械を動かすことはありません。",
        "zh": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** 是 `HYDRA-UMC-OPCUA-SERVER`、`HYDRA-UMC-MQTT-BROKER` 和 `HYDRA-UMC-MTCONNECT-ADAPTER` 前面唯一的状态窗口：它检查各自是否应答，并且只接受效果仅为可达性检查的允许列表命令。它从不移动机器。",
        "pt": "O **HYDRA-UMC-GATEWAY-INDUSTRIAL** é a superfície de estado única à frente do `HYDRA-UMC-OPCUA-SERVER`, do `HYDRA-UMC-MQTT-BROKER` e do `HYDRA-UMC-MTCONNECT-ADAPTER`: verifica se cada um responde e aceita apenas um conjunto permitido de comandos cujo efeito é uma verificação de alcance. Nunca move uma máquina."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
