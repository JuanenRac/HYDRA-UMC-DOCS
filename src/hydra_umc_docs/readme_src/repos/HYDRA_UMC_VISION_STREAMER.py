# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_VISION_STREAMER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-VISION-STREAMER."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '🎥'
COMMENT = 'Multi-camera capture pipeline for the Vision AI Node'
BADGES = [('Framework', 'GStreamer', '62B417'), ('Platform', 'Raspberry%20Pi%20CM5', 'BC1142'), ('Interface', '8x%20USB%203.0', 'blue'), ('Stage', 'Functional%20v0', 'green')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh config validate --config cameras.json",
        "./run.sh config gst --config cameras.json --camera cam0",
        "./run.sh config mediamtx --config cameras.json --out mediamtx.yml",
        "./run.sh stream --config cameras.json"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-VISION-STREAMER architecture",
    "role": {
        "en": "**HYDRA-UMC-VISION-STREAMER** is the capture side of the Vision AI Node: it validates the configuration of up to eight cameras, describes the GStreamer pipeline and the MediaMTX relay for each one, and serves an MJPEG stream with a bounded frame buffer and a reconnection policy. The Hailo-8 hand-off is a defined boundary that needs the real runtime.",
        "es": "**HYDRA-UMC-VISION-STREAMER** es el lado de captura del Vision AI Node: valida la configuración de hasta ocho cámaras, describe la cadena de GStreamer y el relé MediaMTX de cada una y sirve un flujo MJPEG con un búfer de fotogramas acotado y una política de reconexión. La entrega al Hailo-8 es una frontera definida que necesita el entorno real.",
        "de": "**HYDRA-UMC-VISION-STREAMER** ist die Aufnahmeseite des Vision AI Node: Er validiert die Konfiguration von bis zu acht Kameras, beschreibt je Kamera die GStreamer-Pipeline und das MediaMTX-Relay und liefert einen MJPEG-Strom mit begrenztem Bildpuffer und Wiederverbindungsregel. Die Übergabe an den Hailo-8 ist eine definierte Grenze, die die echte Laufzeit braucht.",
        "fr": "**HYDRA-UMC-VISION-STREAMER** est le côté capture du Vision AI Node : il valide la configuration de jusqu'à huit caméras, décrit le pipeline GStreamer et le relais MediaMTX de chacune et sert un flux MJPEG avec un tampon d'images borné et une politique de reconnexion. Le passage au Hailo-8 est une frontière définie qui exige l'environnement réel.",
        "it": "**HYDRA-UMC-VISION-STREAMER** è il lato di acquisizione del Vision AI Node: convalida la configurazione di fino a otto telecamere, descrive la pipeline GStreamer e il relay MediaMTX di ciascuna e serve un flusso MJPEG con un buffer di fotogrammi limitato e una politica di riconnessione. Il passaggio all'Hailo-8 è un confine definito che richiede il runtime reale.",
        "ja": "**HYDRA-UMC-VISION-STREAMER** は Vision AI Node のキャプチャ側です。最大 8 台のカメラの設定を検証し、それぞれの GStreamer パイプラインと MediaMTX リレーを記述し、上限付きのフレームバッファと再接続ポリシーを備えた MJPEG ストリームを配信します。Hailo-8 への受け渡しは、実際のランタイムを必要とする定義済みの境界です。",
        "zh": "**HYDRA-UMC-VISION-STREAMER** 是 Vision AI Node 的采集端：它验证最多八个摄像头的配置，描述每个摄像头的 GStreamer 流水线和 MediaMTX 中继，并提供带有限帧缓冲和重连策略的 MJPEG 流。向 Hailo-8 的交接是一个需要真实运行时的已定义边界。",
        "pt": "O **HYDRA-UMC-VISION-STREAMER** é o lado de captura do Vision AI Node: valida a configuração de até oito câmaras, descreve a cadeia GStreamer e o relé MediaMTX de cada uma e serve um fluxo MJPEG com um buffer de fotogramas limitado e uma política de reconexão. A entrega ao Hailo-8 é uma fronteira definida que precisa do ambiente real."
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
