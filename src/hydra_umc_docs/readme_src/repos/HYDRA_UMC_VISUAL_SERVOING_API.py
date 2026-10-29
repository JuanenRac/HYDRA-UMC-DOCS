# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_VISUAL_SERVOING_API.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-VISUAL-SERVOING-API."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🎯'
COMMENT = 'Pose-correction law with zone-gated authorisation'
BADGES = [('Method', 'Eye--in--Hand%20%2F%20Eye--to--Hand', 'orange'), ('Sync', 'gRPC%20%2F%20SPI', 'yellow')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh correct --current 0.10,0.20,0.30,0.0,0.0,0.0 --target 0.15,0.20,0.25,0.0,0.0,0.10",
        "./run.sh serve --port 8106"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-VISUAL-SERVOING-API architecture",
    "role": {
        "en": "**HYDRA-UMC-VISUAL-SERVOING-API** turns the difference between a current and a target 6-DOF pose into a bounded velocity command, inside a session that remembers the loop. A request is only answered when its data is fresh enough, its confidence high enough and the safety state allows motion; limits can be made stricter by a caller, never looser. No pose comes from a camera yet.",
        "es": "**HYDRA-UMC-VISUAL-SERVOING-API** convierte la diferencia entre una pose actual y una objetivo de 6 grados de libertad en una orden de velocidad acotada, dentro de una sesión que recuerda el bucle. Una petición solo se atiende si sus datos son suficientemente recientes, su confianza suficientemente alta y el estado de seguridad permite el movimiento; un cliente puede endurecer los límites, nunca aflojarlos. Aún no llega ninguna pose de una cámara.",
        "de": "**HYDRA-UMC-VISUAL-SERVOING-API** macht aus der Differenz zwischen einer aktuellen und einer Zielpose mit 6 Freiheitsgraden einen begrenzten Geschwindigkeitsbefehl, innerhalb einer Sitzung, die die Regelschleife kennt. Eine Anfrage wird nur beantwortet, wenn ihre Daten frisch genug und ihre Konfidenz hoch genug sind und der Sicherheitszustand Bewegung erlaubt; ein Aufrufer kann Grenzen verschärfen, nie lockern. Noch kommt keine Pose von einer Kamera.",
        "fr": "**HYDRA-UMC-VISUAL-SERVOING-API** transforme l'écart entre une pose courante et une pose cible à 6 degrés de liberté en une commande de vitesse bornée, dans une session qui se souvient de la boucle. Une requête n'est traitée que si ses données sont assez fraîches, sa confiance assez haute et l'état de sécurité autorise le mouvement ; un appelant peut durcir les limites, jamais les assouplir. Aucune pose ne vient encore d'une caméra.",
        "it": "**HYDRA-UMC-VISUAL-SERVOING-API** trasforma la differenza tra una posa corrente e una posa obiettivo a 6 gradi di libertà in un comando di velocità limitato, dentro una sessione che ricorda il ciclo. Una richiesta riceve risposta solo se i suoi dati sono abbastanza freschi, la confidenza abbastanza alta e lo stato di sicurezza consente il movimento; un chiamante può irrigidire i limiti, mai allentarli. Nessuna posa arriva ancora da una telecamera.",
        "ja": "**HYDRA-UMC-VISUAL-SERVOING-API** は現在の 6 自由度姿勢と目標姿勢の差を、ループを記憶するセッションの中で上限付きの速度指令に変換します。リクエストは、データが十分新しく、信頼度が十分高く、安全状態が動作を許す場合にのみ処理されます。呼び出し側は制限を厳しくできても緩めることはできません。カメラからの姿勢はまだありません。",
        "zh": "**HYDRA-UMC-VISUAL-SERVOING-API** 把当前 6 自由度位姿与目标位姿之差转换为有界的速度指令，并在记住控制回路的会话中进行。只有当数据足够新、置信度足够高且安全状态允许运动时，请求才会得到回答；调用方可以收紧限制，但绝不能放宽。目前还没有来自摄像头的位姿。",
        "pt": "O **HYDRA-UMC-VISUAL-SERVOING-API** transforma a diferença entre uma pose atual e uma pose alvo de 6 graus de liberdade num comando de velocidade limitado, dentro de uma sessão que se lembra do ciclo. Um pedido só é atendido se os seus dados forem suficientemente recentes, a confiança suficientemente alta e o estado de segurança permitir movimento; um cliente pode apertar os limites, nunca afrouxá-los. Ainda não chega nenhuma pose de uma câmara."
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
