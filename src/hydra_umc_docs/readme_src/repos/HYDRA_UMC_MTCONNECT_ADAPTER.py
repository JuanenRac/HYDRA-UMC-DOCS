# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_MTCONNECT_ADAPTER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-MTCONNECT-ADAPTER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🏭'
COMMENT = 'MTConnect probe/current/sample endpoints'
BADGES = [('Standard', 'MTConnect', 'blue'), ('Format', 'XML%20%2F%20HTTP', 'orange')]
NO_UI = True

SPEC = {
    "stack": "node",
    "req": "20",
    "quick": [
        "npm install",
        "npm test",
        "npm run build",
        "npm start",
        "curl http://127.0.0.1:5000/probe"
    ],
    "test_cmd": "npm test",
    "alt": "HYDRA-UMC-MTCONNECT-ADAPTER architecture",
    "role": {
        "en": "**HYDRA-UMC-MTCONNECT-ADAPTER** shows the robots to factory monitoring software as MTConnect devices: read-only XML over HTTP (`/probe`, `/current`, `/sample`), fed from `HYDRA-UMC-SERVER`. It sends no command to any machine.",
        "es": "**HYDRA-UMC-MTCONNECT-ADAPTER** muestra los robots al software de supervisión de fábrica como dispositivos MTConnect: XML de solo lectura sobre HTTP (`/probe`, `/current`, `/sample`), alimentado desde `HYDRA-UMC-SERVER`. No envía ninguna orden a ninguna máquina.",
        "de": "**HYDRA-UMC-MTCONNECT-ADAPTER** zeigt die Roboter der Fabrik-Überwachungssoftware als MTConnect-Geräte: XML nur lesend über HTTP (`/probe`, `/current`, `/sample`), gespeist aus `HYDRA-UMC-SERVER`. Er sendet keinen Befehl an eine Maschine.",
        "fr": "**HYDRA-UMC-MTCONNECT-ADAPTER** présente les robots aux logiciels de supervision d'usine comme des appareils MTConnect : du XML en lecture seule sur HTTP (`/probe`, `/current`, `/sample`), alimenté depuis `HYDRA-UMC-SERVER`. Il n'envoie aucune commande à aucune machine.",
        "it": "**HYDRA-UMC-MTCONNECT-ADAPTER** mostra i robot al software di monitoraggio di fabbrica come dispositivi MTConnect: XML in sola lettura su HTTP (`/probe`, `/current`, `/sample`), alimentato da `HYDRA-UMC-SERVER`. Non invia alcun comando ad alcuna macchina.",
        "ja": "**HYDRA-UMC-MTCONNECT-ADAPTER** は、工場の監視ソフトウェアに対してロボットを MTConnect デバイスとして見せます。`HYDRA-UMC-SERVER` から取得した状態を、読み取り専用の XML over HTTP（`/probe`、`/current`、`/sample`）で提供します。どの機械にもコマンドを送りません。",
        "zh": "**HYDRA-UMC-MTCONNECT-ADAPTER** 把机器人以 MTConnect 设备的形式呈现给工厂监控软件：通过 HTTP 提供只读 XML（`/probe`、`/current`、`/sample`），数据来自 `HYDRA-UMC-SERVER`。它不会向任何机器发送命令。",
        "pt": "O **HYDRA-UMC-MTCONNECT-ADAPTER** mostra os robôs ao software de monitorização de fábrica como dispositivos MTConnect: XML só de leitura sobre HTTP (`/probe`, `/current`, `/sample`), alimentado a partir do `HYDRA-UMC-SERVER`. Não envia nenhum comando a nenhuma máquina."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
