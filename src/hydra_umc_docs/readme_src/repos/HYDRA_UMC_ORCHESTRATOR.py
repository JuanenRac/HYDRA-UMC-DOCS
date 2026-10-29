# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_ORCHESTRATOR.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-ORCHESTRATOR."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🕸️'
COMMENT = 'Mission coordinator'
BADGES = [('Language', 'Rust', 'orange'), ('Architecture', 'Distributed%20Edge', 'blue'), ('Sync', 'JSON%2FHTTP', 'yellow')]
NO_UI = True

SPEC = {
    "stack": "rust",
    "req": "2021",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        [
            "./run.sh mission-demo",
            "a real scenario of the mission state machine"
        ],
        "cargo test"
    ],
    "test_cmd": "cargo test",
    "alt": "HYDRA-UMC-ORCHESTRATOR architecture",
    "role": {
        "en": "**HYDRA-UMC-ORCHESTRATOR** is the mission coordinator: a Rust service that tracks missions in a state machine, hands them to `HYDRA-UMC-JOB-DISPATCHER` and takes the missions back when `HYDRA-UMC-NODE-HEALING` reports a node as unreachable. It does not synchronise robots or prevent collisions.",
        "es": "**HYDRA-UMC-ORCHESTRATOR** es el coordinador de misiones: un servicio en Rust que sigue las misiones en una máquina de estados, se las entrega a `HYDRA-UMC-JOB-DISPATCHER` y las recupera cuando `HYDRA-UMC-NODE-HEALING` informa de que un nodo es inalcanzable. No sincroniza robots ni evita colisiones.",
        "de": "**HYDRA-UMC-ORCHESTRATOR** ist der Missionskoordinator: ein Rust-Dienst, der Missionen in einer Zustandsmaschine verfolgt, sie an `HYDRA-UMC-JOB-DISPATCHER` übergibt und sie zurücknimmt, wenn `HYDRA-UMC-NODE-HEALING` einen Knoten als unerreichbar meldet. Er synchronisiert keine Roboter und verhindert keine Kollisionen.",
        "fr": "**HYDRA-UMC-ORCHESTRATOR** est le coordinateur de missions : un service Rust qui suit les missions dans une machine à états, les confie à `HYDRA-UMC-JOB-DISPATCHER` et les reprend quand `HYDRA-UMC-NODE-HEALING` signale un nœud injoignable. Il ne synchronise pas les robots et n'évite pas les collisions.",
        "it": "**HYDRA-UMC-ORCHESTRATOR** è il coordinatore delle missioni: un servizio Rust che segue le missioni in una macchina a stati, le affida a `HYDRA-UMC-JOB-DISPATCHER` e le riprende quando `HYDRA-UMC-NODE-HEALING` segnala un nodo irraggiungibile. Non sincronizza i robot e non evita le collisioni.",
        "ja": "**HYDRA-UMC-ORCHESTRATOR** はミッションのコーディネーターです。Rust のサービスで、ミッションをステートマシンで追跡し、`HYDRA-UMC-JOB-DISPATCHER` に渡し、`HYDRA-UMC-NODE-HEALING` がノードを到達不能と報告したときはそのミッションを取り戻します。ロボットの同期や衝突の回避は行いません。",
        "zh": "**HYDRA-UMC-ORCHESTRATOR** 是任务协调器：一个 Rust 服务，用状态机跟踪任务，把任务交给 `HYDRA-UMC-JOB-DISPATCHER`，并在 `HYDRA-UMC-NODE-HEALING` 报告节点不可达时收回任务。它不同步机器人，也不避免碰撞。",
        "pt": "O **HYDRA-UMC-ORCHESTRATOR** é o coordenador de missões: um serviço em Rust que acompanha as missões numa máquina de estados, entrega-as ao `HYDRA-UMC-JOB-DISPATCHER` e retoma-as quando o `HYDRA-UMC-NODE-HEALING` indica que um nó está inalcançável. Não sincroniza robôs nem evita colisões."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
