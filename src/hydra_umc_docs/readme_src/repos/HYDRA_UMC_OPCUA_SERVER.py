# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_OPCUA_SERVER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-OPCUA-SERVER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🏭'
COMMENT = 'OPC-UA address space of the robot roster'
BADGES = [('Standard', 'OPC--UA', 'orange'), ('Feature', 'Address%20Space%20Modeling', 'blue')]
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
    "alt": "HYDRA-UMC-OPCUA-SERVER architecture",
    "role": {
        "en": "**HYDRA-UMC-OPCUA-SERVER** publishes the robot roster of `HYDRA-UMC-SERVER` as an OPC-UA address space that SCADA and automation software can browse. Sessions carry OPC UA roles and no role may write: no node controls a joint or an effector.",
        "es": "**HYDRA-UMC-OPCUA-SERVER** publica la lista de robots de `HYDRA-UMC-SERVER` como un espacio de direcciones OPC-UA que el software SCADA y de automatización puede explorar. Las sesiones llevan roles OPC UA y ningún rol puede escribir: ningún nodo controla una articulación ni un efector.",
        "de": "**HYDRA-UMC-OPCUA-SERVER** veröffentlicht die Roboterliste von `HYDRA-UMC-SERVER` als OPC-UA-Adressraum, den SCADA- und Automatisierungssoftware durchsuchen kann. Sitzungen tragen OPC-UA-Rollen, und keine Rolle darf schreiben: Kein Knoten steuert ein Gelenk oder einen Effektor.",
        "fr": "**HYDRA-UMC-OPCUA-SERVER** publie la liste des robots de `HYDRA-UMC-SERVER` comme un espace d'adressage OPC-UA que les logiciels SCADA et d'automatisation peuvent parcourir. Les sessions portent des rôles OPC UA et aucun rôle ne peut écrire : aucun nœud ne commande une articulation ni un effecteur.",
        "it": "**HYDRA-UMC-OPCUA-SERVER** pubblica l'elenco dei robot di `HYDRA-UMC-SERVER` come spazio di indirizzi OPC-UA che il software SCADA e di automazione può esplorare. Le sessioni portano ruoli OPC UA e nessun ruolo può scrivere: nessun nodo controlla un giunto o un effettore.",
        "ja": "**HYDRA-UMC-OPCUA-SERVER** は `HYDRA-UMC-SERVER` のロボット一覧を、SCADA やオートメーションのソフトウェアが閲覧できる OPC-UA アドレス空間として公開します。セッションは OPC UA のロールを持ち、書き込みできるロールはありません。関節やエンドエフェクターを制御するノードはありません。",
        "zh": "**HYDRA-UMC-OPCUA-SERVER** 把 `HYDRA-UMC-SERVER` 的机器人列表发布为 OPC-UA 地址空间，供 SCADA 和自动化软件浏览。会话带有 OPC UA 角色，任何角色都不能写入：没有任何节点控制关节或末端执行器。",
        "pt": "O **HYDRA-UMC-OPCUA-SERVER** publica a lista de robôs do `HYDRA-UMC-SERVER` como um espaço de endereços OPC-UA que o software SCADA e de automação pode explorar. As sessões trazem funções OPC UA e nenhuma função pode escrever: nenhum nó controla uma articulação nem um efetor."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
