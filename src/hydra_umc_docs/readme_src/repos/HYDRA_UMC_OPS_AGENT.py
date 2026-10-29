# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_OPS_AGENT.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-OPS-AGENT."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🩺'
COMMENT = 'Maintenance-incident coordinator'
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
            "demo: edge collect on a throwaway sample project, then control show"
        ],
        "./run.sh edge collect --node-name n --projects-root DIR --out FILE",
        "./run.sh control show snapshot.json"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-OPS-AGENT architecture",
    "role": {
        "en": "**HYDRA-UMC-OPS-AGENT** is the maintenance-incident coordinator of the ecosystem. It owns one lifecycle (evidence, diagnosis, human-approved change, canary deploy through `HYDRA-UMC-UPDATER`, verification) and reimplements neither inference, updates nor the safety logic of the controllers.",
        "es": "**HYDRA-UMC-OPS-AGENT** es el coordinador de incidencias de mantenimiento del ecosistema. Es dueño de un solo ciclo de vida (pruebas, diagnóstico, cambio aprobado por una persona, despliegue canario con `HYDRA-UMC-UPDATER`, verificación) y no reimplementa ni la inferencia, ni las actualizaciones, ni la lógica de seguridad de los controladores.",
        "de": "**HYDRA-UMC-OPS-AGENT** ist der Koordinator für Wartungsvorfälle im Ökosystem. Er besitzt genau einen Lebenszyklus (Belege, Diagnose, von Menschen genehmigte Änderung, Canary-Auslieferung über `HYDRA-UMC-UPDATER`, Verifikation) und implementiert weder Inferenz noch Updates noch die Sicherheitslogik der Steuerungen neu.",
        "fr": "**HYDRA-UMC-OPS-AGENT** est le coordinateur des incidents de maintenance de l'écosystème. Il possède un seul cycle de vie (preuves, diagnostic, changement approuvé par une personne, déploiement canari via `HYDRA-UMC-UPDATER`, vérification) et ne réimplémente ni l'inférence, ni les mises à jour, ni la logique de sécurité des contrôleurs.",
        "it": "**HYDRA-UMC-OPS-AGENT** è il coordinatore degli incidenti di manutenzione dell'ecosistema. Possiede un solo ciclo di vita (prove, diagnosi, modifica approvata da una persona, rilascio canary tramite `HYDRA-UMC-UPDATER`, verifica) e non reimplementa né l'inferenza, né gli aggiornamenti, né la logica di sicurezza dei controllori.",
        "ja": "**HYDRA-UMC-OPS-AGENT** はエコシステムの保守インシデントのコーディネーターです。証拠、診断、人が承認した変更、`HYDRA-UMC-UPDATER` によるカナリアデプロイ、検証という 1 つのライフサイクルを担い、推論、更新、コントローラーの安全ロジックは再実装しません。",
        "zh": "**HYDRA-UMC-OPS-AGENT** 是生态系统的维护事件协调者。它负责唯一的生命周期（证据、诊断、人工批准的变更、通过 `HYDRA-UMC-UPDATER` 的金丝雀部署、验证），不重新实现推理、更新或控制器的安全逻辑。",
        "pt": "O **HYDRA-UMC-OPS-AGENT** é o coordenador de incidentes de manutenção do ecossistema. É dono de um único ciclo de vida (provas, diagnóstico, alteração aprovada por uma pessoa, implantação canário pelo `HYDRA-UMC-UPDATER`, verificação) e não reimplementa nem a inferência, nem as atualizações, nem a lógica de segurança dos controladores."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
