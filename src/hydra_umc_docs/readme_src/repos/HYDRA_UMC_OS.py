# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_OS.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-OS."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🖥️'
COMMENT = 'Platform layer for a CM5 node on Raspberry Pi OS'
BADGES = [('Platform', 'Raspberry%20Pi%20OS%20%7C%20CM5', 'red'), ('Services', 'systemd%20%7C%20udev', 'orange'), ('Stack', 'Debian%20%7C%20Python%20%7C%20Shell', 'blueviolet')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.11",
    "quick": [
        "PYTHONPATH=agent/src python3 -m unittest discover -s agent/tests",
        [
            "./build-test.sh",
            "non-mutating build check (build-test.bat on Windows)"
        ]
    ],
    "test_cmd": "python -m unittest discover -s agent/tests",
    "alt": "HYDRA-UMC-OS architecture",
    "role": {
        "en": "**HYDRA-UMC-OS** is the platform layer of a CM5 node: configuration, service lifecycle, local identity, diagnostics, branding and coordinated updates on top of Raspberry Pi OS, with a read-only device agent. It replaces neither Linux, nor systemd, nor the vendor SDKs; the image is built by `HYDRA-UMC-OS-REBUILDER`.",
        "es": "**HYDRA-UMC-OS** es la capa de plataforma de un nodo CM5: configuración, ciclo de vida de los servicios, identidad local, diagnóstico, imagen visual y actualizaciones coordinadas sobre Raspberry Pi OS, con un agente de dispositivo de solo lectura. No sustituye a Linux, ni a systemd, ni a los SDK de los fabricantes; la imagen la construye `HYDRA-UMC-OS-REBUILDER`.",
        "de": "**HYDRA-UMC-OS** ist die Plattformschicht eines CM5-Knotens: Konfiguration, Dienstlebenszyklus, lokale Identität, Diagnose, Erscheinungsbild und koordinierte Updates auf Raspberry Pi OS, mit einem nur lesenden Geräte-Agenten. Es ersetzt weder Linux noch systemd noch die Hersteller-SDKs; das Image baut `HYDRA-UMC-OS-REBUILDER`.",
        "fr": "**HYDRA-UMC-OS** est la couche plateforme d'un nœud CM5 : configuration, cycle de vie des services, identité locale, diagnostic, habillage visuel et mises à jour coordonnées sur Raspberry Pi OS, avec un agent d'appareil en lecture seule. Il ne remplace ni Linux, ni systemd, ni les SDK des fabricants ; l'image est construite par `HYDRA-UMC-OS-REBUILDER`.",
        "it": "**HYDRA-UMC-OS** è lo strato di piattaforma di un nodo CM5: configurazione, ciclo di vita dei servizi, identità locale, diagnostica, aspetto visivo e aggiornamenti coordinati su Raspberry Pi OS, con un agente di dispositivo in sola lettura. Non sostituisce Linux, systemd né gli SDK dei produttori; l'immagine è costruita da `HYDRA-UMC-OS-REBUILDER`.",
        "ja": "**HYDRA-UMC-OS** は CM5 ノードのプラットフォーム層です。Raspberry Pi OS の上で、設定、サービスのライフサイクル、ローカルな識別、診断、見た目、調整された更新を提供し、読み取り専用のデバイスエージェントを備えます。Linux、systemd、ベンダーの SDK を置き換えるものではなく、イメージは `HYDRA-UMC-OS-REBUILDER` が作ります。",
        "zh": "**HYDRA-UMC-OS** 是 CM5 节点的平台层：在 Raspberry Pi OS 之上提供配置、服务生命周期、本地身份、诊断、视觉外观和协调更新，并带有只读的设备代理。它不替代 Linux、systemd 或厂商 SDK；镜像由 `HYDRA-UMC-OS-REBUILDER` 构建。",
        "pt": "O **HYDRA-UMC-OS** é a camada de plataforma de um nó CM5: configuração, ciclo de vida dos serviços, identidade local, diagnóstico, aspeto visual e atualizações coordenadas sobre o Raspberry Pi OS, com um agente de dispositivo só de leitura. Não substitui o Linux, o systemd nem os SDK dos fabricantes; a imagem é construída pelo `HYDRA-UMC-OS-REBUILDER`."
    },
    "quick_intro": {
        "en": "The agent tests need Python 3.11 or newer and nothing else; the image itself is built by `HYDRA-UMC-OS-REBUILDER`.",
        "es": "Las pruebas del agente solo necesitan Python 3.11 o superior; la imagen en sí la construye `HYDRA-UMC-OS-REBUILDER`.",
        "de": "Die Agent-Tests brauchen nur Python 3.11 oder neuer; das Image selbst baut `HYDRA-UMC-OS-REBUILDER`.",
        "fr": "Les tests de l'agent n'exigent que Python 3.11 ou plus récent ; l'image elle-même est construite par `HYDRA-UMC-OS-REBUILDER`.",
        "it": "I test dell'agente richiedono solo Python 3.11 o successivo; l'immagine in sé è costruita da `HYDRA-UMC-OS-REBUILDER`.",
        "ja": "エージェントのテストに必要なのは Python 3.11 以上だけです。イメージ自体は `HYDRA-UMC-OS-REBUILDER` が作ります。",
        "zh": "代理测试只需要 Python 3.11 或更高版本；镜像本身由 `HYDRA-UMC-OS-REBUILDER` 构建。",
        "pt": "Os testes do agente só precisam de Python 3.11 ou superior; a imagem em si é construída pelo `HYDRA-UMC-OS-REBUILDER`."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
