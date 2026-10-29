# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_DEV_SERVER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-DEV-SERVER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🖥️'
COMMENT = 'Reproducible development host'
BADGES = [('Language', 'Python%203.11%2B', 'blue'), ('Core', 'stdlib%20only', 'brightgreen')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.11",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        [
            "./run.sh",
            "demo: inventory scan, then config validate"
        ],
        "./run.sh config validate configs/task-policy.example.json --kind task-policy"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-DEV-SERVER architecture",
    "role": {
        "en": "**HYDRA-UMC-DEV-SERVER** is the development host of the ecosystem: it runs bounded, allow-listed build and test tasks in isolated workspaces and coordinates repair candidates with `HYDRA-UMC-OPS-AGENT`. It never approves its own tasks and deploys nothing; delivery to a node always goes through `HYDRA-UMC-UPDATER`.",
        "es": "**HYDRA-UMC-DEV-SERVER** es el equipo de desarrollo del ecosistema: ejecuta tareas de compilación y pruebas acotadas y permitidas en espacios de trabajo aislados y coordina candidatos de reparación con `HYDRA-UMC-OPS-AGENT`. Nunca aprueba sus propias tareas y no despliega nada; la entrega a un nodo pasa siempre por `HYDRA-UMC-UPDATER`.",
        "de": "**HYDRA-UMC-DEV-SERVER** ist der Entwicklungsrechner des Ökosystems: Er führt begrenzte, freigegebene Build- und Testaufgaben in isolierten Arbeitsbereichen aus und stimmt Reparaturkandidaten mit `HYDRA-UMC-OPS-AGENT` ab. Er genehmigt nie seine eigenen Aufgaben und liefert nichts aus; die Auslieferung an einen Knoten läuft immer über `HYDRA-UMC-UPDATER`.",
        "fr": "**HYDRA-UMC-DEV-SERVER** est l'hôte de développement de l'écosystème : il exécute des tâches de compilation et de test bornées et autorisées dans des espaces de travail isolés et coordonne les candidats de réparation avec `HYDRA-UMC-OPS-AGENT`. Il n'approuve jamais ses propres tâches et ne déploie rien ; la livraison vers un nœud passe toujours par `HYDRA-UMC-UPDATER`.",
        "it": "**HYDRA-UMC-DEV-SERVER** è l'host di sviluppo dell'ecosistema: esegue attività di compilazione e test limitate e ammesse in aree di lavoro isolate e coordina i candidati di riparazione con `HYDRA-UMC-OPS-AGENT`. Non approva mai le proprie attività e non distribuisce nulla; la consegna a un nodo passa sempre da `HYDRA-UMC-UPDATER`.",
        "ja": "**HYDRA-UMC-DEV-SERVER** はエコシステムの開発ホストです。許可リストにある範囲限定のビルドとテストのタスクを隔離されたワークスペースで実行し、修復候補を `HYDRA-UMC-OPS-AGENT` と調整します。自分のタスクを自分で承認することはなく、何もデプロイしません。ノードへの配信は常に `HYDRA-UMC-UPDATER` を通ります。",
        "zh": "**HYDRA-UMC-DEV-SERVER** 是生态系统的开发主机：它在隔离的工作区中运行受限的、在允许列表内的构建和测试任务，并与 `HYDRA-UMC-OPS-AGENT` 协调修复候选。它从不批准自己的任务，也不部署任何东西；向节点交付始终经过 `HYDRA-UMC-UPDATER`。",
        "pt": "O **HYDRA-UMC-DEV-SERVER** é o anfitrião de desenvolvimento do ecossistema: executa tarefas de compilação e de testes limitadas e permitidas em áreas de trabalho isoladas e coordena candidatos de reparação com o `HYDRA-UMC-OPS-AGENT`. Nunca aprova as suas próprias tarefas e não implanta nada; a entrega a um nó passa sempre pelo `HYDRA-UMC-UPDATER`."
    },
    "test_note": {
        "en": " The sandbox tests skip, saying why, on a host without a usable sandbox; none of them needs hardware.",
        "es": " Las pruebas del sandbox se saltan, diciendo por qué, en un equipo sin sandbox utilizable; ninguna necesita hardware.",
        "de": " Die Sandbox-Tests werden auf einem Rechner ohne nutzbare Sandbox übersprungen und sagen warum; keiner braucht Hardware.",
        "fr": " Les tests du bac à sable sont ignorés, en disant pourquoi, sur une machine sans bac à sable utilisable ; aucun n'exige de matériel.",
        "it": " I test della sandbox vengono saltati, dicendo perché, su una macchina senza sandbox utilizzabile; nessuno richiede hardware.",
        "ja": " サンドボックスのテストは、使えるサンドボックスがないホストでは理由を示してスキップされます。ハードウェアが必要なテストはありません。",
        "zh": " 在没有可用沙箱的主机上，沙箱测试会说明原因并跳过；没有任何测试需要硬件。",
        "pt": " Os testes da sandbox são saltados, a dizer porquê, num equipamento sem sandbox utilizável; nenhum precisa de hardware."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
