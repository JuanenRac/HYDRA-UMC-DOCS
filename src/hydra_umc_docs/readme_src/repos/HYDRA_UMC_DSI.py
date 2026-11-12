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
        "en": "**HYDRA-UMC-DSI** is the touch screen of the CM5 itself: a native Flutter app for the 5\"/7\" DSI panel that talks to `HYDRA-UMC-SERVER` over its REST and WebSocket interface, next to the browser interface of `HYDRA-UMC-STUDIO`. It holds no robot logic of its own; the server decides what is allowed. It runs on the touch display of the CM5 pilot bench today. In the target design the DSI display hangs from the STM32H757, which is meant to run the complete interface on screen, so that the H757 and the display keep working (stop, status, control) even if the Jetson hangs, while the Jetson hosts vision, AI and the server. That design has not been built or tested, and this Flutter app stays the one of the CM5 pilot bench.",
        "es": "**HYDRA-UMC-DSI** es la pantalla táctil de la propia CM5: una aplicación nativa de Flutter para el panel DSI de 5\"/7\" que habla con `HYDRA-UMC-SERVER` por su interfaz REST y WebSocket, junto a la interfaz de navegador de `HYDRA-UMC-STUDIO`. No tiene lógica de robots propia; el servidor decide qué se permite. Hoy se ejecuta en la pantalla táctil del banco piloto con la CM5. En el diseño objetivo la pantalla DSI cuelga del STM32H757, que debe ejecutar la interfaz completa en pantalla, de modo que el H757 y la pantalla sigan funcionando (parada, estado, control) aunque la Jetson se bloquee, mientras la Jetson aloja la visión, la IA y el servidor. Ese diseño no se ha construido ni probado, y esta app Flutter sigue siendo la del banco piloto con la CM5.",
        "de": "**HYDRA-UMC-DSI** ist der Touchscreen der CM5 selbst: eine native Flutter-App für das 5\"/7\"-DSI-Panel, die über REST und WebSocket mit `HYDRA-UMC-SERVER` spricht, neben der Browseroberfläche von `HYDRA-UMC-STUDIO`. Sie hat keine eigene Robotiklogik; der Server entscheidet, was erlaubt ist. Heute läuft sie auf dem Touch-Display des CM5-Pilotprüfstands. Im Zielentwurf hängt das DSI-Display am STM32H757, der die vollständige Oberfläche auf dem Bildschirm ausführen soll, damit H757 und Display (Stopp, Status, Steuerung) auch bei einem Hänger des Jetson weiterarbeiten, während der Jetson Bildverarbeitung, KI und den Server beherbergt. Dieser Entwurf ist weder gebaut noch getestet, und diese Flutter-App bleibt die des CM5-Pilotprüfstands.",
        "fr": "**HYDRA-UMC-DSI** est l'écran tactile de la CM5 elle-même : une application Flutter native pour la dalle DSI 5\"/7\" qui parle à `HYDRA-UMC-SERVER` par son interface REST et WebSocket, à côté de l'interface navigateur de `HYDRA-UMC-STUDIO`. Elle n'a aucune logique de robot propre ; le serveur décide de ce qui est permis. Elle tourne aujourd'hui sur l'écran tactile du banc pilote CM5. Dans la conception visée, l'écran DSI est branché au STM32H757, qui doit exécuter l'interface complète à l'écran, afin que le H757 et l'écran continuent de fonctionner (arrêt, état, commande) même si le Jetson se bloque, tandis que le Jetson héberge la vision, l'IA et le serveur. Cette conception n'est ni construite ni testée, et cette application Flutter reste celle du banc pilote CM5.",
        "it": "**HYDRA-UMC-DSI** è il touchscreen della CM5 stessa: un'app Flutter nativa per il pannello DSI da 5\"/7\" che parla con `HYDRA-UMC-SERVER` tramite la sua interfaccia REST e WebSocket, accanto all'interfaccia browser di `HYDRA-UMC-STUDIO`. Non ha logica robotica propria; è il server a decidere cosa è consentito. Oggi gira sul display touch del banco pilota CM5. Nel progetto di destinazione il display DSI è collegato allo STM32H757, che dovrebbe eseguire l'interfaccia completa a schermo, in modo che H757 e display continuino a funzionare (arresto, stato, controllo) anche se il Jetson si blocca, mentre il Jetson ospita visione, IA e server. Questo progetto non è costruito né provato, e questa app Flutter resta quella del banco pilota CM5.",
        "ja": "**HYDRA-UMC-DSI** は CM5 自身のタッチ画面です。5\"/7\" の DSI パネル向けのネイティブ Flutter アプリで、`HYDRA-UMC-STUDIO` のブラウザー UI と並んで、REST と WebSocket で `HYDRA-UMC-SERVER` と通信します。ロボットのロジックは持たず、何が許されるかはサーバーが決めます。現在は CM5 試験用ベンチのタッチディスプレイで動作します。目標設計では DSI ディスプレイは STM32H757 に接続され、H757 が画面上の完全なインターフェースを実行する想定です。これにより Jetson がハングしても H757 とディスプレイは動作（停止、状態、制御）を続け、Jetson はビジョン、AI、サーバーを担当します。この設計は製作も試験もされておらず、この Flutter アプリは引き続き CM5 試験用ベンチのものです。",
        "zh": "**HYDRA-UMC-DSI** 是 CM5 自带的触摸屏：一个面向 5\"/7\" DSI 面板的原生 Flutter 应用，通过 REST 和 WebSocket 与 `HYDRA-UMC-SERVER` 通信，与 `HYDRA-UMC-STUDIO` 的浏览器界面并存。它没有自己的机器人逻辑；允许什么由服务器决定。目前它运行在 CM5 试验台的触摸屏上。在目标设计中，DSI 显示屏接在 STM32H757 上，由 H757 在屏幕上运行完整界面，这样即使 Jetson 卡死，H757 和显示屏也能继续工作（停止、状态、控制），而 Jetson 承载视觉、AI 和服务器。该设计尚未制造或测试，本 Flutter 应用仍是 CM5 试验台的应用。",
        "pt": "O **HYDRA-UMC-DSI** é o ecrã tátil da própria CM5: uma aplicação Flutter nativa para o painel DSI de 5\"/7\" que fala com o `HYDRA-UMC-SERVER` pela sua interface REST e WebSocket, ao lado da interface de navegador do `HYDRA-UMC-STUDIO`. Não tem lógica de robôs própria; o servidor decide o que é permitido. Hoje corre no ecrã tátil do banco piloto com a CM5. No desenho objetivo, o ecrã DSI liga-se ao STM32H757, que deverá executar a interface completa no ecrã, de modo que o H757 e o ecrã continuem a funcionar (paragem, estado, controlo) mesmo que a Jetson bloqueie, enquanto a Jetson aloja a visão, a IA e o servidor. Esse desenho não foi construído nem testado, e esta app Flutter continua a ser a do banco piloto com a CM5."
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
