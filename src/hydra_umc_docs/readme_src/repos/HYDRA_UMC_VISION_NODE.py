# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_VISION_NODE.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-VISION-NODE."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '👁️'
COMMENT = 'Integration parent of the Vision AI Node family'
BADGES = [('Hardware', 'CM5%20%2B%20Hailo--8', 'orange'), ('Performance', '26%20TOPS', 'green'), ('Stage', 'Functional%20v0', 'yellow')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh family-status",
        "./run.sh pipeline-status",
        "./run.sh validate-frame frame.raw --width 640 --height 480",
        "./run.sh serve --port 8105"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-VISION-NODE architecture",
    "role": {
        "en": "**HYDRA-UMC-VISION-NODE** is the integration parent of the Vision AI Node family. It does not run the camera, the accelerator or the detection itself: it checks that its four children are present and ready, describes the perception pipeline stage by stage, validates raw camera frames and reads DataMatrix codes.",
        "es": "**HYDRA-UMC-VISION-NODE** es el padre de integración de la familia Vision AI Node. No ejecuta la cámara, el acelerador ni la detección: comprueba que sus cuatro hijos están presentes y listos, describe la cadena de percepción etapa por etapa, valida fotogramas en bruto de la cámara y lee códigos DataMatrix.",
        "de": "**HYDRA-UMC-VISION-NODE** ist der Integrationsknoten der Vision-AI-Node-Familie. Er betreibt weder Kamera noch Beschleuniger oder Erkennung selbst: Er prüft, ob seine vier Kinder vorhanden und bereit sind, beschreibt die Wahrnehmungskette Stufe für Stufe, validiert rohe Kamerabilder und liest DataMatrix-Codes.",
        "fr": "**HYDRA-UMC-VISION-NODE** est le parent d'intégration de la famille Vision AI Node. Il ne fait tourner ni la caméra, ni l'accélérateur, ni la détection : il vérifie que ses quatre enfants sont présents et prêts, décrit la chaîne de perception étape par étape, valide des images brutes de caméra et lit des codes DataMatrix.",
        "it": "**HYDRA-UMC-VISION-NODE** è il genitore di integrazione della famiglia Vision AI Node. Non esegue la telecamera, l'acceleratore o il rilevamento: verifica che i suoi quattro figli siano presenti e pronti, descrive la catena di percezione fase per fase, convalida fotogrammi grezzi della telecamera e legge codici DataMatrix.",
        "ja": "**HYDRA-UMC-VISION-NODE** は Vision AI Node ファミリーの統合の親です。カメラやアクセラレーター、検出そのものは動かさず、4 つの子が揃って準備できているかを確認し、知覚パイプラインを段階ごとに説明し、生のカメラフレームを検証し、DataMatrix コードを読み取ります。",
        "zh": "**HYDRA-UMC-VISION-NODE** 是 Vision AI Node 系列的集成父项目。它自己不运行摄像头、加速器或检测：它检查四个子项目是否存在且就绪，逐级描述感知流水线，验证原始摄像头帧并读取 DataMatrix 码。",
        "pt": "O **HYDRA-UMC-VISION-NODE** é o pai de integração da família Vision AI Node. Não executa a câmara, o acelerador nem a deteção: verifica se os seus quatro filhos estão presentes e prontos, descreve a cadeia de perceção etapa a etapa, valida fotogramas em bruto da câmara e lê códigos DataMatrix."
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
