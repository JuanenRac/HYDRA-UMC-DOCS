# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_PHYSICS_REPLICA.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-PHYSICS-REPLICA."""
from __future__ import annotations

from .. import service_kit as S

ICON = '📐'
COMMENT = 'Digital twin module'
BADGES = [('Solver', 'URDF%20FK', 'blue'), ('Language', 'Rust', 'orange'), ('Stage', 'Functional%20v0', 'yellow')]
NO_UI = True

SPEC = {
    "stack": "rust",
    "req": "2021",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh fk --urdf arm.urdf --joints \"shoulder=0,elbow=0\"",
        "./run.sh validate-limits --urdf arm.urdf --joints \"shoulder=3.0,elbow=0.2\"",
        "cargo test"
    ],
    "test_cmd": "cargo test",
    "alt": "HYDRA-UMC-PHYSICS-REPLICA architecture",
    "role": {
        "en": "**HYDRA-UMC-PHYSICS-REPLICA** is the kinematics module of the digital twin: it reads a URDF tree, computes the pose of every joint (forward kinematics), checks joint positions against their limits and estimates joint torques from the inertial data (inverse dynamics). It does not simulate contact, friction or a rigid-body world. The optional `serve` command starts a small HTTP listener (off unless asked for, loopback only by default, token optional) that answers `GET /health` and `GET /metrics` and, when given a URDF with `--urdf`, `POST /fk`, `/ik`, `/check-trajectory` and `/inverse-dynamics` for that robot.",
        "es": "**HYDRA-UMC-PHYSICS-REPLICA** es el módulo de cinemática del gemelo digital: lee un árbol URDF, calcula la pose de cada articulación (cinemática directa), comprueba las posiciones de las articulaciones contra sus límites y estima los pares de las articulaciones a partir de los datos de inercia (dinámica inversa). No simula contacto, fricción ni un mundo de cuerpos rígidos. El comando opcional `serve` arranca un pequeño servidor HTTP (apagado salvo que se pida, solo en loopback por defecto, token opcional) que responde a `GET /health` y `GET /metrics` y, si se le da un URDF con `--urdf`, a `POST /fk`, `/ik`, `/check-trajectory` y `/inverse-dynamics` para ese robot.",
        "de": "**HYDRA-UMC-PHYSICS-REPLICA** ist das Kinematikmodul des digitalen Zwillings: Es liest einen URDF-Baum, berechnet die Pose jedes Gelenks (Vorwärtskinematik), prüft Gelenkstellungen gegen ihre Grenzen und schätzt die Gelenkmomente aus den Trägheitsdaten (inverse Dynamik). Es simuliert weder Kontakt noch Reibung noch eine Starrkörperwelt. Der optionale Befehl `serve` startet einen kleinen HTTP-Listener (aus, solange er nicht verlangt wird, standardmäßig nur Loopback, Token optional), der `GET /health` und `GET /metrics` beantwortet und, wenn ihm mit `--urdf` ein URDF gegeben wird, `POST /fk`, `/ik`, `/check-trajectory` und `/inverse-dynamics` für diesen Roboter.",
        "fr": "**HYDRA-UMC-PHYSICS-REPLICA** est le module de cinématique du jumeau numérique : il lit un arbre URDF, calcule la pose de chaque articulation (cinématique directe), vérifie les positions des articulations par rapport à leurs limites et estime les couples articulaires à partir des données d'inertie (dynamique inverse). Il ne simule ni contact, ni frottement, ni monde de corps rigides. La commande facultative `serve` démarre un petit serveur HTTP (désactivé sauf demande, en loopback seulement par défaut, jeton facultatif) qui répond à `GET /health` et `GET /metrics` et, si on lui donne un URDF avec `--urdf`, à `POST /fk`, `/ik`, `/check-trajectory` et `/inverse-dynamics` pour ce robot.",
        "it": "**HYDRA-UMC-PHYSICS-REPLICA** è il modulo di cinematica del gemello digitale: legge un albero URDF, calcola la posa di ogni giunto (cinematica diretta), verifica le posizioni dei giunti rispetto ai loro limiti e stima le coppie dei giunti dai dati di inerzia (dinamica inversa). Non simula contatto, attrito né un mondo di corpi rigidi. Il comando facoltativo `serve` avvia un piccolo server HTTP (spento salvo richiesta, solo loopback per impostazione predefinita, token facoltativo) che risponde a `GET /health` e `GET /metrics` e, se gli si dà un URDF con `--urdf`, a `POST /fk`, `/ik`, `/check-trajectory` e `/inverse-dynamics` per quel robot.",
        "ja": "**HYDRA-UMC-PHYSICS-REPLICA** はデジタルツインの運動学モジュールです。URDF のツリーを読み、各関節の姿勢を計算し（順運動学）、関節の位置を制限に照らして検証し、慣性データから関節トルクを推定します（逆動力学）。接触、摩擦、剛体の世界はシミュレートしません。 任意の `serve` コマンドは小さな HTTP リスナーを起動します（指定しない限り無効、既定ではループバックのみ、トークンは任意）。`GET /health` と `GET /metrics` に応答し、`--urdf` で URDF を渡した場合は、そのロボットについて `POST /fk`、`/ik`、`/check-trajectory`、`/inverse-dynamics` にも応答します。",
        "zh": "**HYDRA-UMC-PHYSICS-REPLICA** 是数字孪生的运动学模块：读取 URDF 树，计算每个关节的位姿（正向运动学），对照限位检查关节位置，并根据惯性数据估算关节力矩（逆动力学）。它不模拟接触、摩擦或刚体世界。 可选的 `serve` 命令会启动一个小型 HTTP 监听器（不指定则不启动，默认仅回环地址，令牌可选），响应 `GET /health` 和 `GET /metrics`；若用 `--urdf` 给定 URDF，还会针对该机器人响应 `POST /fk`、`/ik`、`/check-trajectory` 和 `/inverse-dynamics`。",
        "pt": "O **HYDRA-UMC-PHYSICS-REPLICA** é o módulo de cinemática do gémeo digital: lê uma árvore URDF, calcula a pose de cada articulação (cinemática direta), verifica as posições das articulações contra os seus limites e estima os binários das articulações a partir dos dados de inércia (dinâmica inversa). Não simula contacto, atrito nem um mundo de corpos rígidos. O comando opcional `serve` arranca um pequeno servidor HTTP (desligado salvo pedido, só em loopback por predefinição, token opcional) que responde a `GET /health` e `GET /metrics` e, se lhe for dado um URDF com `--urdf`, a `POST /fk`, `/ik`, `/check-trajectory` e `/inverse-dynamics` para esse robô."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
