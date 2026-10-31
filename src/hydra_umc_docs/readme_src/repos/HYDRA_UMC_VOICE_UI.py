# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_VOICE_UI.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-VOICE-UI."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '🎙️'
COMMENT = 'Local speech-to-action front end'
BADGES = [('STT', 'Whisper%20Local', 'FF6F00'), ('Platform', 'Hailo--10', 'green')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh analyze-audio clip.wav",
        "./run.sh parse-intent \"stop robot one\"",
        "./run.sh serve --port 8091"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-VOICE-UI architecture",
    "role": {
        "en": "**HYDRA-UMC-VOICE-UI** is the voice front end of the cognitive node: it detects voice in a WAV file, parses already-recognised text into an intent with rules, and offers a bounded HTTP gateway for the watch flow that asks for a confirmation before anything is handed on. It does not recognise speech yet and never sends a physical command.",
        "es": "**HYDRA-UMC-VOICE-UI** es la entrada de voz del nodo cognitivo: detecta voz en un fichero WAV, analiza con reglas un texto ya reconocido para sacar una intención y ofrece una pasarela HTTP acotada para el flujo del reloj que pide una confirmación antes de pasar nada. Todavía no reconoce el habla y nunca envía una orden física.",
        "de": "**HYDRA-UMC-VOICE-UI** ist das Sprach-Frontend des kognitiven Knotens: Es erkennt Stimme in einer WAV-Datei, zerlegt bereits erkannten Text regelbasiert in eine Absicht und bietet ein begrenztes HTTP-Gateway für den Uhren-Ablauf, das vor jeder Weitergabe eine Bestätigung verlangt. Es erkennt noch keine Sprache und sendet nie einen physischen Befehl.",
        "fr": "**HYDRA-UMC-VOICE-UI** est l'entrée vocale du nœud cognitif : il détecte la voix dans un fichier WAV, analyse par règles un texte déjà reconnu pour en tirer une intention et propose une passerelle HTTP bornée pour le flux de la montre, qui demande une confirmation avant de transmettre quoi que ce soit. Il ne reconnaît pas encore la parole et n'envoie jamais de commande physique.",
        "it": "**HYDRA-UMC-VOICE-UI** è il front end vocale del nodo cognitivo: rileva la voce in un file WAV, analizza con regole un testo già riconosciuto per ricavarne un'intenzione e offre un gateway HTTP limitato per il flusso dell'orologio, che chiede una conferma prima di passare qualsiasi cosa. Non riconosce ancora il parlato e non invia mai un comando fisico.",
        "ja": "**HYDRA-UMC-VOICE-UI** は認知ノードの音声フロントエンドです。WAV ファイル内の音声を検出し、認識済みのテキストをルールで意図に解析し、何かを引き渡す前に確認を求める、ウォッチ用の上限付き HTTP ゲートウェイを提供します。音声認識はまだ行わず、物理的なコマンドは送りません。",
        "zh": "**HYDRA-UMC-VOICE-UI** 是认知节点的语音前端：它检测 WAV 文件中的语音，用规则把已识别的文本解析为意图，并为手表流程提供有界的 HTTP 网关，在转交任何内容之前先要求确认。它目前还不识别语音，也从不发送物理指令。",
        "pt": "O **HYDRA-UMC-VOICE-UI** é a entrada de voz do nó cognitivo: deteta voz num ficheiro WAV, analisa com regras um texto já reconhecido para obter uma intenção e oferece um gateway HTTP limitado para o fluxo do relógio, que pede uma confirmação antes de passar o que quer que seja. Ainda não reconhece fala e nunca envia um comando físico."
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
