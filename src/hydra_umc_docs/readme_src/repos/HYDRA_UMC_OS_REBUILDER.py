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

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'security': {'en': '`--public-image` (on `build-image` and `profile-build`, and the **Public image** box of the build window; off by default) refuses any first-boot configuration and also scans the boot partition (`firstrun.sh`, `wpa_supplicant.conf`, `userconf*`, `custom.toml`, `user-data`, `network-config`) and `/opt/hydra-umc` (`.env` files and data folders with files) for credentials; any finding stops the image from being promoted. It has not been tried on a real image, because that needs Linux.', 'es': '`--public-image` (en `build-image` y `profile-build`, y la casilla **Imagen pública** de la ventana de construcción; apagada por defecto) rechaza cualquier configuración de primer arranque y además busca credenciales en la partición de arranque (`firstrun.sh`, `wpa_supplicant.conf`, `userconf*`, `custom.toml`, `user-data`, `network-config`) y en `/opt/hydra-umc` (ficheros `.env` y carpetas de datos con ficheros); cualquier hallazgo impide promover la imagen. No se ha probado con una imagen real, porque requiere Linux.', 'de': '`--public-image` (bei `build-image` und `profile-build` sowie das Kästchen **Öffentliches Image** im Build-Fenster; standardmäßig aus) lehnt jede Erststart-Konfiguration ab und durchsucht außerdem die Boot-Partition (`firstrun.sh`, `wpa_supplicant.conf`, `userconf*`, `custom.toml`, `user-data`, `network-config`) und `/opt/hydra-umc` (`.env`-Dateien und Datenordner mit Dateien) nach Zugangsdaten; jeder Fund verhindert die Freigabe des Images. Mit einem echten Image wurde es nicht erprobt, da dafür Linux nötig ist.', 'fr': "`--public-image` (sur `build-image` et `profile-build`, et la case **Image publique** de la fenêtre de construction ; décochée par défaut) refuse toute configuration du premier démarrage et recherche aussi des identifiants dans la partition de démarrage (`firstrun.sh`, `wpa_supplicant.conf`, `userconf*`, `custom.toml`, `user-data`, `network-config`) et dans `/opt/hydra-umc` (fichiers `.env` et dossiers de données contenant des fichiers) ; tout résultat empêche de promouvoir l'image. Il n'a pas été essayé sur une image réelle, car cela demande Linux.", 'it': "`--public-image` (su `build-image` e `profile-build`, e la casella **Immagine pubblica** della finestra di costruzione; spenta per impostazione predefinita) rifiuta qualsiasi configurazione del primo avvio e cerca anche credenziali nella partizione di avvio (`firstrun.sh`, `wpa_supplicant.conf`, `userconf*`, `custom.toml`, `user-data`, `network-config`) e in `/opt/hydra-umc` (file `.env` e cartelle di dati con file); qualsiasi rilevamento impedisce di promuovere l'immagine. Non è stato provato su un'immagine reale, perché serve Linux.", 'ja': '`--public-image`（`build-image` と `profile-build`、およびビルドウィンドウの **公開イメージ** チェックボックス。既定ではオフ）は、初回起動の設定をすべて拒否し、さらにブートパーティション（`firstrun.sh`、`wpa_supplicant.conf`、`userconf*`、`custom.toml`、`user-data`、`network-config`）と `/opt/hydra-umc`（`.env` ファイルとファイルを含むデータフォルダー）に認証情報がないか調べます。何か見つかるとイメージは昇格されません。Linux が必要なため、実際のイメージではまだ試していません。', 'zh': '`--public-image`（用于 `build-image` 和 `profile-build`，以及构建窗口中的 **公开镜像** 复选框；默认关闭）会拒绝任何首次启动配置，并扫描引导分区（`firstrun.sh`、`wpa_supplicant.conf`、`userconf*`、`custom.toml`、`user-data`、`network-config`）和 `/opt/hydra-umc`（`.env` 文件及含文件的数据文件夹）中的凭据；只要有发现，镜像就不会被提升。由于需要 Linux，尚未在真实镜像上试过。', 'pt': '`--public-image` (em `build-image` e `profile-build`, e a caixa **Imagem pública** da janela de construção; desligada por predefinição) recusa qualquer configuração de primeiro arranque e procura também credenciais na partição de arranque (`firstrun.sh`, `wpa_supplicant.conf`, `userconf*`, `custom.toml`, `user-data`, `network-config`) e em `/opt/hydra-umc` (ficheiros `.env` e pastas de dados com ficheiros); qualquer deteção impede a promoção da imagem. Não foi experimentada com uma imagem real, porque isso requer Linux.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
