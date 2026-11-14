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
        "en": "**HYDRA-UMC-PATH-PLANNER-3D** plans a collision-free path for one robot through a scene of sphere and box obstacles (an RRT search; the danger zones of a zones file of the safety zones can be read as boxes), plans several robots one after the other in the order of their priority (each keeps clear of the paths of the earlier ones, or, when the timing is set, leaves later and shares a corridor with them in time), plans for an arm in the space of its joint angles, and checks a path against obstacles and workspace bounds. It is a Rust library and command-line tool. The optional `serve` command starts a small HTTP listener (off unless asked for, loopback only by default, token optional) that answers `GET /health` and `GET /metrics` (the latter only when the `metrics` section of the configuration file opens it) with numbers about the service; `POST /plan`, which plans a scenario sent in the body, exists only when the `plan` section of that file opens it, needs the token off the loopback and has limits of size and time.",
        "es": "**HYDRA-UMC-PATH-PLANNER-3D** planifica una trayectoria sin colisiones para un robot a través de una escena de obstáculos esféricos y de caja (búsqueda RRT; las zonas de peligro de un fichero de zonas de seguridad pueden leerse como cajas), planifica varios robots uno tras otro por orden de prioridad (cada uno se mantiene lejos de las trayectorias de los anteriores o, si se configura el tiempo, sale más tarde y comparte un pasillo con ellos en el tiempo), planifica para un brazo en el espacio de sus ángulos de articulación y comprueba una trayectoria contra obstáculos y límites del espacio de trabajo. Es una biblioteca y una herramienta de línea de órdenes en Rust. El comando opcional `serve` arranca un pequeño servidor HTTP (apagado salvo que se pida, solo en loopback por defecto, token opcional) que responde a `GET /health` y a `GET /metrics` (este último solo cuando lo abre la sección `metrics` del fichero de configuración) con números del propio servicio; `POST /plan`, que planifica un escenario enviado en el cuerpo, existe solo cuando lo abre la sección `plan` de ese fichero, exige el token fuera del loopback y tiene límites de tamaño y de tiempo.",
        "de": "**HYDRA-UMC-PATH-PLANNER-3D** plant einen kollisionsfreien Weg für einen Roboter durch eine Szene mit Kugel- und Quaderhindernissen (RRT-Suche; die Gefahrenzonen einer Zonendatei der Sicherheitszonen können als Quader gelesen werden), plant mehrere Roboter nacheinander in der Reihenfolge ihrer Priorität (jeder hält Abstand zu den Wegen der früheren oder fährt, wenn die Zeitplanung eingestellt ist, später los und teilt sich mit ihnen einen Gang in der Zeit), plant für einen Arm im Raum seiner Gelenkwinkel und prüft einen Weg gegen Hindernisse und Arbeitsraumgrenzen. Es ist eine Rust-Bibliothek und ein Kommandozeilenwerkzeug. Der optionale Befehl `serve` startet einen kleinen HTTP-Listener (aus, solange er nicht verlangt wird, standardmäßig nur Loopback, Token optional), der `GET /health` und `GET /metrics` (letzteres nur, wenn der Abschnitt `metrics` der Konfigurationsdatei es öffnet) mit Zahlen über den Dienst beantwortet; `POST /plan`, das ein im Körper gesendetes Szenario plant, gibt es nur, wenn der Abschnitt `plan` dieser Datei es öffnet; es braucht außerhalb des Loopbacks das Token und hat Grenzen für Größe und Zeit.",
        "fr": "**HYDRA-UMC-PATH-PLANNER-3D** planifie une trajectoire sans collision pour un robot à travers une scène d'obstacles sphériques et en boîte (recherche RRT ; les zones de danger d'un fichier de zones de sécurité peuvent être lues comme des boîtes), planifie plusieurs robots l'un après l'autre dans l'ordre de leur priorité (chacun reste à l'écart des trajectoires des précédents ou, si le temps est configuré, part plus tard et partage un couloir avec eux dans le temps), planifie pour un bras dans l'espace de ses angles d'articulation, et vérifie une trajectoire par rapport aux obstacles et aux limites de l'espace de travail. C'est une bibliothèque et un outil en ligne de commande en Rust. La commande facultative `serve` démarre un petit serveur HTTP (désactivé sauf demande, en loopback seulement par défaut, jeton facultatif) qui répond à `GET /health` et à `GET /metrics` (ce dernier seulement quand la section `metrics` du fichier de configuration l'ouvre) avec des chiffres sur le service ; `POST /plan`, qui planifie un scénario envoyé dans le corps, n'existe que lorsque la section `plan` de ce fichier l'ouvre, exige le jeton hors du loopback et a des limites de taille et de durée.",
        "it": "**HYDRA-UMC-PATH-PLANNER-3D** pianifica un percorso senza collisioni per un robot in una scena di ostacoli sferici e a scatola (ricerca RRT; le zone di pericolo di un file di zone di sicurezza possono essere lette come scatole), pianifica più robot uno dopo l'altro nell'ordine della loro priorità (ognuno resta lontano dai percorsi dei precedenti o, se il tempo è configurato, parte più tardi e condivide un corridoio con loro nel tempo), pianifica per un braccio nello spazio dei suoi angoli di giunto e verifica un percorso rispetto a ostacoli e limiti dello spazio di lavoro. È una libreria e uno strumento da riga di comando in Rust. Il comando facoltativo `serve` avvia un piccolo server HTTP (spento salvo richiesta, solo loopback per impostazione predefinita, token facoltativo) che risponde a `GET /health` e a `GET /metrics` (quest'ultimo solo quando lo apre la sezione `metrics` del file di configurazione) con numeri sul servizio; `POST /plan`, che pianifica uno scenario inviato nel corpo, esiste solo quando lo apre la sezione `plan` di quel file, richiede il token fuori dal loopback e ha limiti di dimensione e di tempo.",
        "ja": "**HYDRA-UMC-PATH-PLANNER-3D** は、球形と箱形の障害物がある場面で 1 台のロボットの衝突しない経路を計画し（RRT 探索。安全ゾーンのゾーンファイルの危険ゾーンは箱として読み込めます）、複数のロボットを優先順位の順に 1 台ずつ計画し（各ロボットは先に計画されたロボットの経路から離れるか、時間設定がある場合は出発を遅らせて時間をずらし、同じ通路を共有します）、アームを関節角の空間で計画し、経路を障害物と作業空間の境界に照らして検証します。Rust のライブラリ兼コマンドラインツールです。任意の `serve` コマンドは小さな HTTP リスナーを起動します（指定しない限り無効、既定ではループバックのみ、トークンは任意）。`GET /health` と、サービス自体の数値を返す `GET /metrics`（後者は設定ファイルの `metrics` セクションで有効にした場合のみ）に応答します。本文で送られたシナリオを計画する `POST /plan` は、そのファイルの `plan` セクションで有効にした場合にだけ存在し、ループバック以外ではトークンが必要で、サイズと時間の上限があります。",
        "zh": "**HYDRA-UMC-PATH-PLANNER-3D** 在由球形和箱形障碍物构成的场景中为一台机器人规划无碰撞路径（RRT 搜索；安全区域的区域文件中的危险区域可作为箱体读取），按优先级顺序逐台规划多台机器人（每台与先前机器人的路径保持距离，或在设置了时间时推迟出发，在时间上与它们共用同一通道），在关节角空间中为机械臂规划，并对照障碍物和工作空间边界检查路径。它是 Rust 库兼命令行工具。可选的 `serve` 命令会启动一个小型 HTTP 监听器（不指定则不启动，默认仅回环地址，令牌可选），响应 `GET /health` 和返回服务自身数字的 `GET /metrics`（后者仅在配置文件的 `metrics` 部分启用时可用）；规划请求正文中所发送场景的 `POST /plan` 仅在该文件的 `plan` 部分启用时才存在，在回环地址之外需要令牌，并有大小和时间限制。",
        "pt": "O **HYDRA-UMC-PATH-PLANNER-3D** planeia um caminho sem colisões para um robô numa cena de obstáculos esféricos e em caixa (pesquisa RRT; as zonas de perigo de um ficheiro de zonas de segurança podem ser lidas como caixas), planeia vários robôs um a seguir ao outro pela ordem da sua prioridade (cada um mantém-se afastado dos caminhos dos anteriores ou, se o tempo estiver configurado, parte mais tarde e partilha um corredor com eles no tempo), planeia para um braço no espaço dos seus ângulos de articulação e verifica um caminho contra obstáculos e limites do espaço de trabalho. É uma biblioteca e uma ferramenta de linha de comandos em Rust. O comando opcional `serve` arranca um pequeno servidor HTTP (desligado salvo pedido, só em loopback por predefinição, token opcional) que responde a `GET /health` e a `GET /metrics` (este último só quando a secção `metrics` do ficheiro de configuração o abre) com números do próprio serviço; o `POST /plan`, que planeia um cenário enviado no corpo, só existe quando a secção `plan` desse ficheiro o abre, exige o token fora do loopback e tem limites de tamanho e de tempo."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
