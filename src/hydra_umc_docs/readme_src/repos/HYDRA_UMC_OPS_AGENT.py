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

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'features': {'en': 'A promoted canary also leaves its change as a patch file, written with `git format-patch` to `<project>.canary-patches/<deploy-id>.patch` outside the checkout and reported as `patchPath` in the result and the audit record, so the local commit can be inspected and dropped knowingly. Writing it is best effort and never changes the result of the deploy.', 'es': 'Un canario promovido deja además su cambio como fichero de parche, escrito con `git format-patch` en `<proyecto>.canary-patches/<id-de-despliegue>.patch` fuera del checkout e informado como `patchPath` en el resultado y en el registro de auditoría, de modo que el commit local se pueda inspeccionar y descartar con conocimiento. Escribirlo es de mejor esfuerzo y nunca cambia el resultado del despliegue.', 'de': 'Ein übernommener Canary hinterlässt seine Änderung zusätzlich als Patch-Datei, mit `git format-patch` nach `<Projekt>.canary-patches/<Deploy-ID>.patch` außerhalb des Checkouts geschrieben und als `patchPath` im Ergebnis und im Audit-Eintrag gemeldet, sodass der lokale Commit geprüft und bewusst verworfen werden kann. Das Schreiben geschieht nach bestem Bemühen und ändert nie das Ergebnis des Deployments.', 'fr': "Un canari promu laisse aussi son changement sous forme de fichier de correctif, écrit avec `git format-patch` dans `<projet>.canary-patches/<id-de-déploiement>.patch` hors du checkout et indiqué comme `patchPath` dans le résultat et l'enregistrement d'audit, afin que le commit local puisse être examiné et abandonné en connaissance de cause. L'écriture se fait au mieux et ne change jamais le résultat du déploiement.", 'it': "Un canary promosso lascia anche la sua modifica come file di patch, scritto con `git format-patch` in `<progetto>.canary-patches/<id-distribuzione>.patch` fuori dal checkout e riportato come `patchPath` nel risultato e nel registro di audit, così che il commit locale possa essere ispezionato e scartato con cognizione di causa. La scrittura è al meglio delle possibilità e non cambia mai l'esito della distribuzione.", 'ja': '昇格したカナリアは、その変更をパッチファイルとしても残します。`git format-patch` でチェックアウトの外の `<プロジェクト>.canary-patches/<デプロイID>.patch` に書き出され、結果と監査記録に `patchPath` として報告されるため、ローカルのコミットを確認し、承知のうえで破棄できます。書き出しはベストエフォートで、デプロイの結果は変わりません。', 'zh': '被提升的金丝雀还会把其更改保存为补丁文件：用 `git format-patch` 写到检出目录之外的 `<项目>.canary-patches/<部署ID>.patch`，并在结果和审计记录中以 `patchPath` 报告，便于检查并在知情的情况下丢弃本地提交。写入尽力而为，绝不改变部署的结果。', 'pt': 'Um canário promovido deixa também a sua alteração como ficheiro de patch, escrito com `git format-patch` em `<projeto>.canary-patches/<id-de-implementação>.patch` fora do checkout e comunicado como `patchPath` no resultado e no registo de auditoria, para que o commit local possa ser inspecionado e descartado com conhecimento. A escrita é feita em esforço razoável e nunca altera o resultado da implementação.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
