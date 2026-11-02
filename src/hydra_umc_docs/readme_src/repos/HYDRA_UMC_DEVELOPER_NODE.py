# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_DEVELOPER_NODE.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-DEVELOPER-NODE."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🧑‍💻'
COMMENT = 'Developer node: evidence, repro cases and checkouts, approved by a person'
BADGES = [('Language', 'Python%203.11%2B', 'blue'), ('Core', 'stdlib%20only', 'brightgreen'), ('Parts', 'closed%20by%20default', '367BF5')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.11",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh",
        "./run.sh --config configs/developer-node.json evidence verify bundle.json"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-DEVELOPER-NODE architecture",
    "role": {
        "en": "**HYDRA-UMC-DEVELOPER-NODE** is the developer node of the ecosystem: it reads the evidence bundles of `HYDRA-UMC-LOCAL-TECHNICIAN`, keeps a cache of checkouts by revision, runs repro recipes and the shared CI, and each of these stays closed until the configuration opens it and a person approves the exact run.",
        "es": "**HYDRA-UMC-DEVELOPER-NODE** es el nodo de desarrollo del ecosistema: lee los paquetes de pruebas de `HYDRA-UMC-LOCAL-TECHNICIAN`, mantiene una caché de checkouts por revisión, ejecuta recetas de reproducción y el CI compartido, y cada una de estas partes sigue cerrada hasta que la configuración la abre y una persona aprueba la ejecución exacta.",
        "de": "**HYDRA-UMC-DEVELOPER-NODE** ist der Entwicklungsknoten des Ökosystems: Er liest die Belegpakete von `HYDRA-UMC-LOCAL-TECHNICIAN`, führt einen Cache von Checkouts pro Revision, startet Reproduktionsrezepte und die gemeinsame CI, und jeder dieser Teile bleibt geschlossen, bis die Konfiguration ihn öffnet und ein Mensch den genauen Lauf freigibt.",
        "fr": "**HYDRA-UMC-DEVELOPER-NODE** est le nœud de développement de l'écosystème : il lit les paquets de preuves de `HYDRA-UMC-LOCAL-TECHNICIAN`, tient un cache de checkouts par révision, exécute des recettes de reproduction et la CI partagée, et chacune de ces parties reste fermée tant que la configuration ne l'ouvre pas et qu'une personne n'approuve pas l'exécution exacte.",
        "it": "**HYDRA-UMC-DEVELOPER-NODE** è il nodo di sviluppo dell'ecosistema: legge i pacchetti di prove di `HYDRA-UMC-LOCAL-TECHNICIAN`, mantiene una cache di checkout per revisione, esegue ricette di riproduzione e la CI condivisa, e ognuna di queste parti resta chiusa finché la configurazione non la apre e una persona non approva l'esecuzione esatta.",
        "ja": "**HYDRA-UMC-DEVELOPER-NODE** はエコシステムの開発ノードです。`HYDRA-UMC-LOCAL-TECHNICIAN` の証拠バンドルを読み、リビジョン別のチェックアウトのキャッシュを持ち、再現レシピと共有 CI を実行します。これらはいずれも、設定が開き、担当者がその実行を正確に承認するまで閉じたままです。",
        "zh": "**HYDRA-UMC-DEVELOPER-NODE** 是生态系统的开发节点：它读取 `HYDRA-UMC-LOCAL-TECHNICIAN` 的证据包，维护按修订版本的检出缓存，运行复现配方和共享 CI；这些部分在配置将其打开、且有人批准确切的运行之前都保持关闭。",
        "pt": "O **HYDRA-UMC-DEVELOPER-NODE** é o nó de desenvolvimento do ecossistema: lê os pacotes de provas do `HYDRA-UMC-LOCAL-TECHNICIAN`, mantém uma cache de checkouts por revisão, executa receitas de reprodução e a CI partilhada, e cada uma destas partes fica fechada até a configuração a abrir e uma pessoa aprovar a execução exata."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
