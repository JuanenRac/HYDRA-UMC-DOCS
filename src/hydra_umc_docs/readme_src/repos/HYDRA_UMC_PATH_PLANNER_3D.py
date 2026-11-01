# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_PATH_PLANNER_3D.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-PATH-PLANNER-3D."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🗺️'
COMMENT = 'RRT path planner with collision validation'
BADGES = [('Algorithm', 'RRT', 'orange'), ('Engine', 'Rust', 'blue')]
NO_UI = True

SPEC = {
    "stack": "rust",
    "req": "2021",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh scenarios/example.json",
        "cargo test"
    ],
    "test_cmd": "cargo test",
    "alt": "HYDRA-UMC-PATH-PLANNER-3D architecture",
    "role": {
        "en": "**HYDRA-UMC-PATH-PLANNER-3D** plans a collision-free path for one robot through a scene of sphere obstacles (an RRT search) and checks a path against obstacles and workspace bounds. It is a Rust library and command-line tool; it does not yet plan for several robots at once. The optional `serve` command starts a small HTTP listener (off unless asked for, loopback only by default, token optional) that answers only `GET /health` and `GET /metrics` with numbers about the service; it plans nothing.",
        "es": "**HYDRA-UMC-PATH-PLANNER-3D** planifica una trayectoria sin colisiones para un robot a través de una escena de obstáculos esféricos (búsqueda RRT) y comprueba una trayectoria contra obstáculos y límites del espacio de trabajo. Es una biblioteca y una herramienta de línea de órdenes en Rust; todavía no planifica para varios robots a la vez. El comando opcional `serve` arranca un pequeño servidor HTTP (apagado salvo que se pida, solo en loopback por defecto, token opcional) que responde únicamente a `GET /health` y `GET /metrics` con números del propio servicio; no planifica nada.",
        "de": "**HYDRA-UMC-PATH-PLANNER-3D** plant einen kollisionsfreien Weg für einen Roboter durch eine Szene mit Kugelhindernissen (RRT-Suche) und prüft einen Weg gegen Hindernisse und Arbeitsraumgrenzen. Es ist eine Rust-Bibliothek und ein Kommandozeilenwerkzeug; für mehrere Roboter gleichzeitig plant es noch nicht. Der optionale Befehl `serve` startet einen kleinen HTTP-Listener (aus, solange er nicht verlangt wird, standardmäßig nur Loopback, Token optional), der nur `GET /health` und `GET /metrics` mit Zahlen über den Dienst beantwortet; er plant nichts.",
        "fr": "**HYDRA-UMC-PATH-PLANNER-3D** planifie une trajectoire sans collision pour un robot à travers une scène d'obstacles sphériques (recherche RRT) et vérifie une trajectoire par rapport aux obstacles et aux limites de l'espace de travail. C'est une bibliothèque et un outil en ligne de commande en Rust ; il ne planifie pas encore pour plusieurs robots à la fois. La commande facultative `serve` démarre un petit serveur HTTP (désactivé sauf demande, en loopback seulement par défaut, jeton facultatif) qui ne répond qu'à `GET /health` et `GET /metrics` avec des chiffres sur le service ; il ne planifie rien.",
        "it": "**HYDRA-UMC-PATH-PLANNER-3D** pianifica un percorso senza collisioni per un robot in una scena di ostacoli sferici (ricerca RRT) e verifica un percorso rispetto a ostacoli e limiti dello spazio di lavoro. È una libreria e uno strumento da riga di comando in Rust; non pianifica ancora per più robot insieme. Il comando facoltativo `serve` avvia un piccolo server HTTP (spento salvo richiesta, solo loopback per impostazione predefinita, token facoltativo) che risponde soltanto a `GET /health` e `GET /metrics` con numeri sul servizio; non pianifica nulla.",
        "ja": "**HYDRA-UMC-PATH-PLANNER-3D** は、球形の障害物がある場面で 1 台のロボットの衝突しない経路を計画し（RRT 探索）、経路を障害物と作業空間の境界に照らして検証します。Rust のライブラリ兼コマンドラインツールで、複数台のロボットを同時に計画することはまだできません。 任意の `serve` コマンドは小さな HTTP リスナーを起動します（指定しない限り無効、既定ではループバックのみ、トークンは任意）。応答するのは `GET /health` と、サービス自体の数値を返す `GET /metrics` だけで、経路計画は行いません。",
        "zh": "**HYDRA-UMC-PATH-PLANNER-3D** 在由球形障碍物构成的场景中为一台机器人规划无碰撞路径（RRT 搜索），并对照障碍物和工作空间边界检查路径。它是 Rust 库兼命令行工具；目前还不能同时为多台机器人规划。 可选的 `serve` 命令会启动一个小型 HTTP 监听器（不指定则不启动，默认仅回环地址，令牌可选），只响应 `GET /health` 和返回服务自身数字的 `GET /metrics`，不做任何规划。",
        "pt": "O **HYDRA-UMC-PATH-PLANNER-3D** planeia um caminho sem colisões para um robô numa cena de obstáculos esféricos (pesquisa RRT) e verifica um caminho contra obstáculos e limites do espaço de trabalho. É uma biblioteca e uma ferramenta de linha de comandos em Rust; ainda não planeia para vários robôs ao mesmo tempo. O comando opcional `serve` arranca um pequeno servidor HTTP (desligado salvo pedido, só em loopback por predefinição, token opcional) que responde apenas a `GET /health` e `GET /metrics` com números do próprio serviço; não planeia nada."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
