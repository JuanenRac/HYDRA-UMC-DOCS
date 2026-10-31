# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_DSI.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-DSI."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🖥️'
COMMENT = 'Native touch UI for the CM5 DSI screen'
BADGES = [('Framework', 'Flutter%203.x', '02569B'), ('Language', 'Dart', '0175C2'), ('Platform', 'Linux%20%7C%20CM5', 'E34F26')]
NO_UI = False

SPEC = {
    "stack": "flutter",
    "req": "3.x",
    "quick": [
        [
            "flutter pub get",
            ""
        ],
        [
            "./run_dev.sh",
            "desktop simulation, no hardware (run_dev.bat on Windows)"
        ],
        [
            "./build_linux.sh",
            "on a Linux machine or the CM5: the real target"
        ]
    ],
    "test_cmd": "flutter test",
    "alt": "HYDRA-UMC-DSI architecture",
    "role": {
        "en": "**HYDRA-UMC-DSI** is the touch screen of the CM5 itself: a native Flutter app for the 5\"/7\" DSI panel that talks to `HYDRA-UMC-SERVER` over its REST and WebSocket interface, next to the browser interface of `HYDRA-UMC-STUDIO`. It holds no robot logic of its own; the server decides what is allowed.",
        "es": "**HYDRA-UMC-DSI** es la pantalla táctil de la propia CM5: una aplicación nativa de Flutter para el panel DSI de 5\"/7\" que habla con `HYDRA-UMC-SERVER` por su interfaz REST y WebSocket, junto a la interfaz de navegador de `HYDRA-UMC-STUDIO`. No tiene lógica de robots propia; el servidor decide qué se permite.",
        "de": "**HYDRA-UMC-DSI** ist der Touchscreen der CM5 selbst: eine native Flutter-App für das 5\"/7\"-DSI-Panel, die über REST und WebSocket mit `HYDRA-UMC-SERVER` spricht, neben der Browseroberfläche von `HYDRA-UMC-STUDIO`. Sie hat keine eigene Robotiklogik; der Server entscheidet, was erlaubt ist.",
        "fr": "**HYDRA-UMC-DSI** est l'écran tactile de la CM5 elle-même : une application Flutter native pour la dalle DSI 5\"/7\" qui parle à `HYDRA-UMC-SERVER` par son interface REST et WebSocket, à côté de l'interface navigateur de `HYDRA-UMC-STUDIO`. Elle n'a aucune logique de robot propre ; le serveur décide de ce qui est permis.",
        "it": "**HYDRA-UMC-DSI** è il touchscreen della CM5 stessa: un'app Flutter nativa per il pannello DSI da 5\"/7\" che parla con `HYDRA-UMC-SERVER` tramite la sua interfaccia REST e WebSocket, accanto all'interfaccia browser di `HYDRA-UMC-STUDIO`. Non ha logica robotica propria; è il server a decidere cosa è consentito.",
        "ja": "**HYDRA-UMC-DSI** は CM5 自身のタッチ画面です。5\"/7\" の DSI パネル向けのネイティブ Flutter アプリで、`HYDRA-UMC-STUDIO` のブラウザー UI と並んで、REST と WebSocket で `HYDRA-UMC-SERVER` と通信します。ロボットのロジックは持たず、何が許されるかはサーバーが決めます。",
        "zh": "**HYDRA-UMC-DSI** 是 CM5 自带的触摸屏：一个面向 5\"/7\" DSI 面板的原生 Flutter 应用，通过 REST 和 WebSocket 与 `HYDRA-UMC-SERVER` 通信，与 `HYDRA-UMC-STUDIO` 的浏览器界面并存。它没有自己的机器人逻辑；允许什么由服务器决定。",
        "pt": "O **HYDRA-UMC-DSI** é o ecrã tátil da própria CM5: uma aplicação Flutter nativa para o painel DSI de 5\"/7\" que fala com o `HYDRA-UMC-SERVER` pela sua interface REST e WebSocket, ao lado da interface de navegador do `HYDRA-UMC-STUDIO`. Não tem lógica de robôs própria; o servidor decide o que é permitido."
    }
}


APPEND = {'build': 'versioning'}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    body = S.make_body(lg, ctx, SPEC)
    for key, src in APPEND.items():
        if ctx.has(lg, src):
            body[key] = body[key] + "\n\n" + ctx.v(lg, src)
    return body
