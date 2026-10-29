# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_MQTT_BROKER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-MQTT-BROKER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '📡'
COMMENT = 'MQTT broker for telemetry and integrations'
BADGES = [('Protocol', 'MQTT%203.1.1', 'orange'), ('Feature', 'Pub%20%2F%20Sub%20Telemetry', 'blue')]
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
    "alt": "HYDRA-UMC-MQTT-BROKER architecture",
    "role": {
        "en": "**HYDRA-UMC-MQTT-BROKER** is the message hub of the ecosystem: an MQTT 3.1.1 broker (Aedes) with optional per-client authentication and topic ACLs, between dashboards, home-automation systems and the machine bridges (`HYDRA-UMC-BRIDGE-*`) and `HYDRA-UMC-SERVER`. It routes messages; the safety decision stays with the receiver.",
        "es": "**HYDRA-UMC-MQTT-BROKER** es el centro de mensajes del ecosistema: un broker MQTT 3.1.1 (Aedes) con autenticación opcional por cliente y ACL de topics, entre paneles, sistemas domóticos, los bridges de máquinas (`HYDRA-UMC-BRIDGE-*`) y `HYDRA-UMC-SERVER`. Enruta mensajes; la decisión de seguridad queda en el receptor.",
        "de": "**HYDRA-UMC-MQTT-BROKER** ist die Nachrichtenzentrale des Ökosystems: ein MQTT-3.1.1-Broker (Aedes) mit optionaler Authentifizierung pro Client und Topic-ACLs, zwischen Dashboards, Hausautomation, den Maschinen-Bridges (`HYDRA-UMC-BRIDGE-*`) und `HYDRA-UMC-SERVER`. Er leitet Nachrichten weiter; die Sicherheitsentscheidung bleibt beim Empfänger.",
        "fr": "**HYDRA-UMC-MQTT-BROKER** est le centre de messages de l'écosystème : un broker MQTT 3.1.1 (Aedes) avec authentification facultative par client et ACL de topics, entre tableaux de bord, domotique, ponts machines (`HYDRA-UMC-BRIDGE-*`) et `HYDRA-UMC-SERVER`. Il route les messages ; la décision de sécurité reste au destinataire.",
        "it": "**HYDRA-UMC-MQTT-BROKER** è il centro messaggi dell'ecosistema: un broker MQTT 3.1.1 (Aedes) con autenticazione facoltativa per client e ACL dei topic, tra dashboard, domotica, bridge delle macchine (`HYDRA-UMC-BRIDGE-*`) e `HYDRA-UMC-SERVER`. Instrada i messaggi; la decisione di sicurezza resta al ricevente.",
        "ja": "**HYDRA-UMC-MQTT-BROKER** はエコシステムのメッセージハブです。クライアントごとの認証（任意）とトピック ACL を備えた MQTT 3.1.1 ブローカー（Aedes）で、ダッシュボード、ホームオートメーション、機械ブリッジ（`HYDRA-UMC-BRIDGE-*`）、`HYDRA-UMC-SERVER` の間に立ちます。メッセージを中継するだけで、安全の判断は受信側に残ります。",
        "zh": "**HYDRA-UMC-MQTT-BROKER** 是生态系统的消息中心：一个 MQTT 3.1.1 代理（Aedes），支持可选的按客户端认证和主题 ACL，位于仪表板、家居自动化、机器桥接（`HYDRA-UMC-BRIDGE-*`）与 `HYDRA-UMC-SERVER` 之间。它只转发消息；安全决定仍在接收方。",
        "pt": "O **HYDRA-UMC-MQTT-BROKER** é o centro de mensagens do ecossistema: um broker MQTT 3.1.1 (Aedes) com autenticação opcional por cliente e ACL de tópicos, entre painéis, domótica, as pontes de máquinas (`HYDRA-UMC-BRIDGE-*`) e o `HYDRA-UMC-SERVER`. Encaminha mensagens; a decisão de segurança fica com o recetor."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
