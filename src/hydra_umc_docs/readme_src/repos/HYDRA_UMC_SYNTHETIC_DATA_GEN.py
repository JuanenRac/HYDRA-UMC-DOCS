# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_SYNTHETIC_DATA_GEN.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-SYNTHETIC-DATA-GEN."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '📸'
COMMENT = 'Procedural training datasets with exact labels'
BADGES = [('Format', 'YOLO%20%2F%20COCO', 'FF6F00'), ('Target', 'Vision%20AI%20Node', 'green')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh generate --out ./out --count 10 --seed 42",
        "./run.sh generate --out ./out --format yolo --defect-rate 0.3"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-SYNTHETIC-DATA-GEN architecture",
    "role": {
        "en": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** writes small training datasets for the vision nodes: random scenes of components, with the bounding boxes taken from the same coordinates that drew them, exported as YOLO or COCO together with a manifest of how the set was made. Today the scenes are flat 2D shapes; rendering through the Digital Twin is planned.",
        "es": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** escribe pequeños conjuntos de entrenamiento para los nodos de visión: escenas aleatorias de componentes, con las cajas delimitadoras tomadas de las mismas coordenadas que las dibujaron, exportadas como YOLO o COCO junto con un manifiesto de cómo se hizo el conjunto. Hoy las escenas son formas 2D planas; el renderizado con el Digital Twin está previsto.",
        "de": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** schreibt kleine Trainingsdatensätze für die Vision-Knoten: zufällige Szenen aus Bauteilen, deren Begrenzungsrahmen aus denselben Koordinaten stammen, mit denen sie gezeichnet wurden, exportiert als YOLO oder COCO zusammen mit einem Manifest, wie der Satz entstand. Heute sind die Szenen flache 2D-Formen; das Rendern über den Digital Twin ist geplant.",
        "fr": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** écrit de petits jeux d'entraînement pour les nœuds de vision : des scènes aléatoires de composants, dont les boîtes englobantes viennent des mêmes coordonnées que celles qui les ont dessinées, exportées en YOLO ou COCO avec un manifeste de la façon dont le jeu a été fait. Aujourd'hui les scènes sont des formes 2D plates ; le rendu via le Digital Twin est prévu.",
        "it": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** scrive piccoli insiemi di addestramento per i nodi di visione: scene casuali di componenti, con i riquadri presi dalle stesse coordinate che le hanno disegnate, esportati come YOLO o COCO insieme a un manifesto di come è stato fatto l'insieme. Oggi le scene sono forme 2D piatte; il rendering tramite il Digital Twin è previsto.",
        "ja": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** はビジョンノード向けの小さな学習データセットを書き出します。部品のランダムな場面で、バウンディングボックスは描画に使った同じ座標から取られ、YOLO または COCO 形式で、作り方を記録したマニフェストとともに出力されます。現在の場面は平面の 2D 図形で、Digital Twin 経由のレンダリングは計画中です。",
        "zh": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** 为视觉节点写出小型训练数据集：随机的元件场景，边界框取自绘制它们的同一组坐标，以 YOLO 或 COCO 导出，并附带说明数据集如何生成的清单。目前场景是平面的 2D 形状；通过 Digital Twin 渲染还在计划中。",
        "pt": "O **HYDRA-UMC-SYNTHETIC-DATA-GEN** escreve pequenos conjuntos de treino para os nós de visão: cenas aleatórias de componentes, com as caixas delimitadoras tiradas das mesmas coordenadas que as desenharam, exportadas como YOLO ou COCO com um manifesto de como o conjunto foi feito. Hoje as cenas são formas 2D planas; a renderização através do Digital Twin está prevista."
    }
}


from ... import readme_kit as K

EXTRAS: Any = {}


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
