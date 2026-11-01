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
        "en": "**HYDRA-UMC-PHYSICS-REPLICA** is the kinematics module of the digital twin: it reads a URDF tree, computes the pose of every joint (forward kinematics) and checks joint positions against their limits. It does not simulate dynamics: there is no contact, friction or rigid-body model. The optional `serve` command starts a small HTTP listener (off unless asked for, loopback only by default, token optional) that answers only `GET /health` and `GET /metrics` with numbers about the service; it computes nothing.",
        "es": "**HYDRA-UMC-PHYSICS-REPLICA** es el módulo de cinemática del gemelo digital: lee un árbol URDF, calcula la pose de cada articulación (cinemática directa) y comprueba las posiciones de las articulaciones contra sus límites. No simula dinámica: no hay modelo de contacto, de fricción ni de cuerpo rígido. El comando opcional `serve` arranca un pequeño servidor HTTP (apagado salvo que se pida, solo en loopback por defecto, token opcional) que responde únicamente a `GET /health` y `GET /metrics` con números del propio servicio; no calcula nada.",
        "de": "**HYDRA-UMC-PHYSICS-REPLICA** ist das Kinematikmodul des digitalen Zwillings: Es liest einen URDF-Baum, berechnet die Pose jedes Gelenks (Vorwärtskinematik) und prüft Gelenkstellungen gegen ihre Grenzen. Es simuliert keine Dynamik: Es gibt kein Kontakt-, Reibungs- oder Starrkörpermodell. Der optionale Befehl `serve` startet einen kleinen HTTP-Listener (aus, solange er nicht verlangt wird, standardmäßig nur Loopback, Token optional), der nur `GET /health` und `GET /metrics` mit Zahlen über den Dienst beantwortet; er berechnet nichts.",
        "fr": "**HYDRA-UMC-PHYSICS-REPLICA** est le module de cinématique du jumeau numérique : il lit un arbre URDF, calcule la pose de chaque articulation (cinématique directe) et vérifie les positions des articulations par rapport à leurs limites. Il ne simule pas la dynamique : il n'y a ni modèle de contact, ni de frottement, ni de corps rigide. La commande facultative `serve` démarre un petit serveur HTTP (désactivé sauf demande, en loopback seulement par défaut, jeton facultatif) qui ne répond qu'à `GET /health` et `GET /metrics` avec des chiffres sur le service ; il ne calcule rien.",
        "it": "**HYDRA-UMC-PHYSICS-REPLICA** è il modulo di cinematica del gemello digitale: legge un albero URDF, calcola la posa di ogni giunto (cinematica diretta) e verifica le posizioni dei giunti rispetto ai loro limiti. Non simula la dinamica: non c'è un modello di contatto, di attrito o di corpo rigido. Il comando facoltativo `serve` avvia un piccolo server HTTP (spento salvo richiesta, solo loopback per impostazione predefinita, token facoltativo) che risponde soltanto a `GET /health` e `GET /metrics` con numeri sul servizio; non calcola nulla.",
        "ja": "**HYDRA-UMC-PHYSICS-REPLICA** はデジタルツインの運動学モジュールです。URDF のツリーを読み、各関節の姿勢を計算し（順運動学）、関節の位置を制限に照らして検証します。動力学のシミュレーションは行わず、接触、摩擦、剛体のモデルはありません。 任意の `serve` コマンドは小さな HTTP リスナーを起動します（指定しない限り無効、既定ではループバックのみ、トークンは任意）。応答するのは `GET /health` と、サービス自体の数値を返す `GET /metrics` だけで、計算は行いません。",
        "zh": "**HYDRA-UMC-PHYSICS-REPLICA** 是数字孪生的运动学模块：读取 URDF 树，计算每个关节的位姿（正向运动学），并对照限位检查关节位置。它不模拟动力学：没有接触、摩擦或刚体模型。 可选的 `serve` 命令会启动一个小型 HTTP 监听器（不指定则不启动，默认仅回环地址，令牌可选），只响应 `GET /health` 和返回服务自身数字的 `GET /metrics`，不做任何计算。",
        "pt": "O **HYDRA-UMC-PHYSICS-REPLICA** é o módulo de cinemática do gémeo digital: lê uma árvore URDF, calcula a pose de cada articulação (cinemática direta) e verifica as posições das articulações contra os seus limites. Não simula dinâmica: não há modelo de contacto, de atrito nem de corpo rígido. O comando opcional `serve` arranca um pequeno servidor HTTP (desligado salvo pedido, só em loopback por predefinição, token opcional) que responde apenas a `GET /health` e `GET /metrics` com números do próprio serviço; não calcula nada."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
