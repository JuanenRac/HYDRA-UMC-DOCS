# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_VLA_ENGINE.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-VLA-ENGINE."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🤖'
COMMENT = 'Vision-language-action engine contracts'
BADGES = [('Model', 'OpenVLA%20%2F%20RT--2', 'orange'), ('Acceleration', 'Hailo--10', 'green')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh tokens encode --action 0.02,0.00,-0.01,0.0,0.0,0.05,1.0",
        "./run.sh trajectory integrate --start 0,0,0,0,0,0 --actions actions.json",
        "./run.sh status",
        "./run.sh serve --port 8098"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-VLA-ENGINE architecture",
    "role": {
        "en": "**HYDRA-UMC-VLA-ENGINE** holds the parts of a vision-language-action engine that do not need a model: turning actions into discrete tokens and back, integrating the predicted steps into a trajectory, and a guard that clamps or rejects a trajectory against the work volume, speed limits, safety zones and the gripper range. No model runs yet; the Hailo-10 boundary only reports what is present.",
        "es": "**HYDRA-UMC-VLA-ENGINE** contiene las partes de un motor visión-lenguaje-acción que no necesitan un modelo: convertir acciones en tokens discretos y viceversa, integrar los pasos predichos en una trayectoria y una guarda que recorta o rechaza una trayectoria según el volumen de trabajo, los límites de velocidad, las zonas de seguridad y el rango de la pinza. Aún no se ejecuta ningún modelo; la frontera con Hailo-10 solo informa de lo que hay.",
        "de": "**HYDRA-UMC-VLA-ENGINE** enthält die Teile einer Vision-Language-Action-Engine, die kein Modell brauchen: Aktionen in diskrete Tokens und zurück umwandeln, die vorhergesagten Schritte zu einer Trajektorie integrieren und eine Schutzprüfung, die eine Trajektorie anhand von Arbeitsvolumen, Geschwindigkeitsgrenzen, Sicherheitszonen und Greiferbereich beschneidet oder ablehnt. Noch läuft kein Modell; die Hailo-10-Grenze meldet nur, was vorhanden ist.",
        "fr": "**HYDRA-UMC-VLA-ENGINE** contient les parties d'un moteur vision-langage-action qui n'ont pas besoin d'un modèle : convertir des actions en jetons discrets et inversement, intégrer les pas prédits en une trajectoire, et une garde qui rogne ou rejette une trajectoire selon le volume de travail, les limites de vitesse, les zones de sécurité et la plage de la pince. Aucun modèle ne tourne encore ; la frontière Hailo-10 indique seulement ce qui est présent.",
        "it": "**HYDRA-UMC-VLA-ENGINE** contiene le parti di un motore visione-linguaggio-azione che non richiedono un modello: convertire azioni in token discreti e viceversa, integrare i passi previsti in una traiettoria, e una guardia che ritaglia o rifiuta una traiettoria rispetto al volume di lavoro, ai limiti di velocità, alle zone di sicurezza e all'intervallo della pinza. Nessun modello gira ancora; il confine con Hailo-10 riferisce solo ciò che è presente.",
        "ja": "**HYDRA-UMC-VLA-ENGINE** は、モデルを必要としない視覚・言語・行動エンジンの部分を収めています。行動と離散トークンの相互変換、予測ステップの軌道への積分、作業空間・速度制限・安全ゾーン・グリッパー範囲に対して軌道を切り詰めるか拒否するガードです。モデルはまだ動かず、Hailo-10 との境界は存在するものを報告するだけです。",
        "zh": "**HYDRA-UMC-VLA-ENGINE** 包含视觉-语言-动作引擎中不需要模型的部分：把动作转换为离散令牌并还原，把预测的步骤积分成轨迹，以及根据工作空间、速度限制、安全区域和夹爪范围裁剪或拒绝轨迹的守卫。目前还没有模型运行；Hailo-10 边界只报告现有的东西。",
        "pt": "O **HYDRA-UMC-VLA-ENGINE** contém as partes de um motor visão-linguagem-ação que não precisam de um modelo: converter ações em tokens discretos e vice-versa, integrar os passos previstos numa trajetória e uma guarda que corta ou rejeita uma trajetória segundo o volume de trabalho, os limites de velocidade, as zonas de segurança e o intervalo da pinça. Ainda não corre nenhum modelo; a fronteira com o Hailo-10 só indica o que está presente."
    }
}


from ... import readme_kit as K

EXTRAS = {}


def EXTRA(lg):
    out = {}
    sec = EXTRAS.get("security")
    if sec:
        out["security"] = K.table(lg, "threat", sec["rows"]) + ("\n\n" + K.pick(sec["never"], lg) if sec.get("never") else "")
    cfg = EXTRAS.get("configuration")
    if cfg:
        out["configuration"] = (K.pick(cfg["intro"], lg) + "\n\n" if cfg.get("intro") else "") + K.table(lg, "config", cfg["rows"])
    trb = EXTRAS.get("troubleshooting")
    if trb:
        out["troubleshooting"] = K.table(lg, "trouble", trb)
    rdm = EXTRAS.get("roadmap")
    if rdm:
        out["roadmap"] = K.pick(rdm, lg)
    itf = EXTRAS.get("interfaces")
    if itf:
        out["interfaces"] = K.table(lg, itf["head"], itf["rows"]) if isinstance(itf["head"], str) else K.table(lg, [K.pick(h, lg) for h in itf["head"]], itf["rows"])
    return out


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    body = S.make_body(lg, ctx, SPEC)
    body.update(EXTRA(lg))
    return body
