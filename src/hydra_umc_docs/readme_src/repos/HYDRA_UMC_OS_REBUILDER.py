# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_OS_REBUILDER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-OS-REBUILDER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '📀'
COMMENT = 'Builds a ready-to-flash CM5 image'
BADGES = [('Language', 'Python%203.10%2B', 'blue'), ('Desktop', 'PySide6%20%7C%20Qt%20Quick', '367BF5'), ('Platform', 'Windows%20%7C%20Linux', 'lightgrey')]
NO_UI = False

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        [
            "./run.sh",
            "windowed GUI"
        ],
        [
            "./run.sh --cli status",
            "latest real version of every project"
        ]
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-OS-REBUILDER architecture",
    "role": {
        "en": "**HYDRA-UMC-OS-REBUILDER** builds a fresh CM5 image with the current version of every ecosystem project already on it, and writes the first-boot settings (Wi-Fi, user, host name, SSH) before the image is flashed. The platform layer that image carries is described by `HYDRA-UMC-OS`.",
        "es": "**HYDRA-UMC-OS-REBUILDER** construye una imagen nueva de la CM5 con la versión actual de cada proyecto del ecosistema ya incluida, y escribe los ajustes del primer arranque (Wi-Fi, usuario, nombre de equipo, SSH) antes de grabar la imagen. La capa de plataforma que lleva esa imagen la describe `HYDRA-UMC-OS`.",
        "de": "**HYDRA-UMC-OS-REBUILDER** baut ein frisches CM5-Image, auf dem die aktuelle Version jedes Ökosystem-Projekts schon liegt, und schreibt die Einstellungen für den ersten Start (WLAN, Benutzer, Hostname, SSH), bevor das Image geflasht wird. Die Plattformschicht, die dieses Image trägt, beschreibt `HYDRA-UMC-OS`.",
        "fr": "**HYDRA-UMC-OS-REBUILDER** construit une image CM5 neuve avec la version actuelle de chaque projet de l'écosystème déjà dessus, et écrit les réglages du premier démarrage (Wi-Fi, utilisateur, nom d'hôte, SSH) avant de flasher l'image. La couche plateforme que porte cette image est décrite par `HYDRA-UMC-OS`.",
        "it": "**HYDRA-UMC-OS-REBUILDER** costruisce una nuova immagine della CM5 con la versione attuale di ogni progetto dell'ecosistema già inclusa, e scrive le impostazioni del primo avvio (Wi-Fi, utente, nome host, SSH) prima di scrivere l'immagine. Lo strato di piattaforma che l'immagine porta è descritto da `HYDRA-UMC-OS`.",
        "ja": "**HYDRA-UMC-OS-REBUILDER** は、エコシステムの各プロジェクトの最新版を最初から収めた新しい CM5 イメージを作り、イメージを書き込む前に初回起動の設定（Wi-Fi、ユーザー、ホスト名、SSH）を書き出します。そのイメージが載せるプラットフォーム層は `HYDRA-UMC-OS` が説明しています。",
        "zh": "**HYDRA-UMC-OS-REBUILDER** 构建一个全新的 CM5 镜像，镜像中已包含生态系统各项目的当前版本，并在写入镜像之前写好首次启动设置（Wi-Fi、用户、主机名、SSH）。该镜像所携带的平台层由 `HYDRA-UMC-OS` 描述。",
        "pt": "O **HYDRA-UMC-OS-REBUILDER** constrói uma imagem nova da CM5 com a versão atual de cada projeto do ecossistema já incluída, e escreve as definições do primeiro arranque (Wi-Fi, utilizador, nome do anfitrião, SSH) antes de a imagem ser gravada. A camada de plataforma que essa imagem leva é descrita pelo `HYDRA-UMC-OS`."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
