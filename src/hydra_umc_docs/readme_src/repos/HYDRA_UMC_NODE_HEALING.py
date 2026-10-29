# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_NODE_HEALING.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-NODE-HEALING."""
from __future__ import annotations

from .. import service_kit as S

ICON = '💊'
COMMENT = 'Fleet health watchdog'
BADGES = [('Feature', 'Self--Healing', 'green'), ('Platform', 'Distributed%20Edge', 'blue')]
NO_UI = True

SPEC = {
    "stack": "go",
    "req": "1.25",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh -nodes nodes.example.json",
        "go test ./..."
    ],
    "test_cmd": "go test ./...",
    "alt": "HYDRA-UMC-NODE-HEALING architecture",
    "role": {
        "en": "**HYDRA-UMC-NODE-HEALING** is the health watchdog of the fleet: it polls every node over HTTP or gRPC, classifies it and asks `HYDRA-UMC-ORCHESTRATOR` to recover its missions when a node is gone. It watches and reports; it does not restart hardware.",
        "es": "**HYDRA-UMC-NODE-HEALING** es el vigilante de salud de la flota: sondea cada nodo por HTTP o gRPC, lo clasifica y pide a `HYDRA-UMC-ORCHESTRATOR` que recupere sus misiones cuando un nodo desaparece. Vigila e informa; no reinicia hardware.",
        "de": "**HYDRA-UMC-NODE-HEALING** ist der Gesundheitswächter der Flotte: Er fragt jeden Knoten per HTTP oder gRPC ab, stuft ihn ein und bittet `HYDRA-UMC-ORCHESTRATOR`, seine Missionen zu übernehmen, wenn ein Knoten ausfällt. Er überwacht und meldet; er startet keine Hardware neu.",
        "fr": "**HYDRA-UMC-NODE-HEALING** est le chien de garde de santé de la flotte : il interroge chaque nœud en HTTP ou gRPC, le classe et demande à `HYDRA-UMC-ORCHESTRATOR` de récupérer ses missions quand un nœud disparaît. Il surveille et signale ; il ne redémarre pas de matériel.",
        "it": "**HYDRA-UMC-NODE-HEALING** è il guardiano della salute della flotta: interroga ogni nodo via HTTP o gRPC, lo classifica e chiede a `HYDRA-UMC-ORCHESTRATOR` di recuperare le sue missioni quando un nodo scompare. Sorveglia e segnala; non riavvia hardware.",
        "ja": "**HYDRA-UMC-NODE-HEALING** はフリートの健全性ウォッチドッグです。各ノードを HTTP または gRPC で定期的に確認して状態を分類し、ノードが消えたときはそのミッションの回復を `HYDRA-UMC-ORCHESTRATOR` に依頼します。監視と報告だけを行い、ハードウェアを再起動することはありません。",
        "zh": "**HYDRA-UMC-NODE-HEALING** 是机群的健康看门狗：它通过 HTTP 或 gRPC 轮询每个节点并进行分类，节点消失时请求 `HYDRA-UMC-ORCHESTRATOR` 接管其任务。它只监视和报告，不会重启硬件。",
        "pt": "O **HYDRA-UMC-NODE-HEALING** é o vigilante de saúde da frota: consulta cada nó por HTTP ou gRPC, classifica-o e pede ao `HYDRA-UMC-ORCHESTRATOR` que recupere as suas missões quando um nó desaparece. Vigia e comunica; não reinicia hardware."
    },
    "test_note": {
        "en": " Each count is a top-level Go test; the sub-tests are not added. They need no hardware.",
        "es": " Cada cifra es una prueba de Go de primer nivel; las subpruebas no se suman. No necesitan hardware.",
        "de": " Jede Zahl ist ein Go-Test der obersten Ebene; Untertests werden nicht addiert. Sie brauchen keine Hardware.",
        "fr": " Chaque nombre est un test Go de premier niveau ; les sous-tests ne sont pas ajoutés. Ils n'exigent aucun matériel.",
        "it": " Ogni numero è un test Go di primo livello; i sotto-test non sono sommati. Non richiedono hardware.",
        "ja": " 件数は最上位の Go テストの数で、サブテストは加えていません。ハードウェアは不要です。",
        "zh": " 数字为顶层 Go 测试的数量，不含子测试。不需要硬件。",
        "pt": " Cada número é um teste Go de nível superior; os subtestes não são somados. Não precisam de hardware."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
