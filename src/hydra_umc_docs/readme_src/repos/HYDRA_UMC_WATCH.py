# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_WATCH.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-WATCH."""
from __future__ import annotations

from .. import service_kit as S

ICON = '⌚'
COMMENT = 'Wear OS companion: status cards, haptic alerts and a voice relay'
BADGES = [('Platform', 'Wear%20OS', '4285F4'), ('Feature', 'Voice%20%26%20haptics', 'blue')]
NO_UI = False

SPEC = {
    "stack": "android",
    "req": "",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        [
            "./run.sh",
            "installs the debug app on the connected watch and starts it"
        ],
        [
            "./update-from-github.sh",
            "installs the newest release by ADB, without Google Play"
        ]
    ],
    "test_cmd": "./gradlew testDebugUnitTest",
    "alt": "HYDRA-UMC-WATCH architecture",
    "role": {
        "en": "**HYDRA-UMC-WATCH** is the Wear OS companion of the HYDRA-UMC controller apps: it shows the last known system status with its age, plays a distinct vibration for each alert severity, and relays a voice request through the paired phone. It holds no server credential and offers no wireless emergency stop.",
        "es": "**HYDRA-UMC-WATCH** es el acompañante Wear OS de las aplicaciones de control de HYDRA-UMC: muestra el último estado conocido del sistema con su antigüedad, reproduce una vibración distinta para cada gravedad de alerta y retransmite una petición de voz por el teléfono emparejado. No guarda ninguna credencial del servidor y no ofrece parada de emergencia inalámbrica.",
        "de": "**HYDRA-UMC-WATCH** ist der Wear-OS-Begleiter der HYDRA-UMC-Steuerungs-Apps: Er zeigt den letzten bekannten Systemstatus mit seinem Alter, spielt für jede Alarmstufe ein eigenes Vibrationsmuster ab und leitet eine Sprachanfrage über das gekoppelte Telefon weiter. Er hält keine Server-Zugangsdaten und bietet keinen drahtlosen Not-Halt.",
        "fr": "**HYDRA-UMC-WATCH** est le compagnon Wear OS des applications de contrôle HYDRA-UMC : il affiche le dernier état connu du système avec son âge, joue une vibration distincte pour chaque gravité d'alerte et relaie une demande vocale via le téléphone appairé. Il ne détient aucun identifiant du serveur et n'offre pas d'arrêt d'urgence sans fil.",
        "it": "**HYDRA-UMC-WATCH** è il compagno Wear OS delle app di controllo HYDRA-UMC: mostra l'ultimo stato noto del sistema con la sua età, riproduce una vibrazione distinta per ogni gravità di allarme e inoltra una richiesta vocale tramite il telefono abbinato. Non conserva alcuna credenziale del server e non offre un arresto di emergenza wireless.",
        "ja": "**HYDRA-UMC-WATCH** は HYDRA-UMC コントローラーアプリの Wear OS コンパニオンです。最後に分かっているシステム状態をその経過時間とともに表示し、警報の重大度ごとに異なる振動を再生し、ペアリングしたスマートフォン経由で音声リクエストを中継します。サーバーの認証情報は持たず、無線の非常停止も提供しません。",
        "zh": "**HYDRA-UMC-WATCH** 是 HYDRA-UMC 控制应用的 Wear OS 配套应用：它显示最后已知的系统状态及其时效，为每个警报级别播放不同的振动，并通过配对的手机转发语音请求。它不保存任何服务器凭据，也不提供无线紧急停止。",
        "pt": "O **HYDRA-UMC-WATCH** é o companheiro Wear OS das aplicações de controlo HYDRA-UMC: mostra o último estado conhecido do sistema com a sua idade, reproduz uma vibração distinta para cada gravidade de alerta e reencaminha um pedido de voz através do telemóvel emparelhado. Não guarda nenhuma credencial do servidor e não oferece paragem de emergência sem fios."
    },
    "quick_intro": {
        "en": "Requires the Android SDK with a JDK that the bundled Gradle wrapper accepts, and a Wear OS 3 or newer watch or emulator.",
        "es": "Requiere el SDK de Android con un JDK que acepte el contenedor de Gradle incluido, y un reloj o emulador con Wear OS 3 o superior.",
        "de": "Benötigt das Android-SDK mit einem JDK, das der mitgelieferte Gradle-Wrapper akzeptiert, und eine Uhr oder einen Emulator mit Wear OS 3 oder neuer.",
        "fr": "Nécessite le SDK Android avec un JDK accepté par l'enveloppe Gradle fournie, et une montre ou un émulateur sous Wear OS 3 ou plus récent.",
        "it": "Richiede l'SDK Android con un JDK accettato dal wrapper Gradle incluso, e un orologio o emulatore con Wear OS 3 o successivo.",
        "ja": "同梱の Gradle ラッパーが受け付ける JDK を備えた Android SDK と、Wear OS 3 以降のウォッチまたはエミュレーターが必要です。",
        "zh": "需要带有随附 Gradle 包装器可接受的 JDK 的 Android SDK，以及运行 Wear OS 3 或更高版本的手表或模拟器。",
        "pt": "Requer o SDK do Android com um JDK que o wrapper do Gradle incluído aceite, e um relógio ou emulador com Wear OS 3 ou superior."
    }
}


from ... import readme_kit as K

EXTRAS = {'security': {'rows': [[{'en': "Another app or a stranger's phone sending messages to the watch", 'es': 'Otra aplicación o el teléfono de un desconocido enviando mensajes al reloj', 'de': 'Eine andere App oder das Telefon eines Fremden sendet Nachrichten an die Uhr', 'fr': "Une autre application ou le téléphone d'un inconnu envoyant des messages à la montre", 'it': "Un'altra app o il telefono di uno sconosciuto che invia messaggi all'orologio", 'ja': '別のアプリや他人のスマートフォンがウォッチにメッセージを送る', 'zh': '其他应用或陌生人的手机向手表发送消息', 'pt': 'Outra aplicação ou o telemóvel de um desconhecido a enviar mensagens ao relógio'}, {'en': 'The relay uses the Wear OS Data Layer, which only carries traffic between APKs with the same package name and signing certificate; the target is chosen by a capability query, never by guessing a connected node', 'es': 'El relé usa la capa de datos de Wear OS, que solo lleva tráfico entre APK con el mismo nombre de paquete y certificado de firma; el destino se elige con una consulta de capacidad, nunca adivinando un nodo conectado', 'de': 'Das Relay nutzt die Wear-OS-Data-Layer, die nur Verkehr zwischen APKs mit gleichem Paketnamen und Signaturzertifikat trägt; das Ziel wird per Capability-Abfrage gewählt, nie durch Raten eines verbundenen Knotens', 'fr': 'Le relais utilise la Data Layer de Wear OS, qui ne transporte que le trafic entre APK de même nom de paquet et de même certificat de signature ; la cible est choisie par une requête de capacité, jamais en devinant un nœud connecté', 'it': 'Il relay usa il Data Layer di Wear OS, che trasporta solo traffico tra APK con lo stesso nome di pacchetto e certificato di firma; la destinazione si sceglie con una query di capacità, mai indovinando un nodo connesso', 'ja': '中継には Wear OS の Data Layer を使います。これは同じパッケージ名と署名証明書を持つ APK 同士の通信だけを運び、宛先は接続中のノードを推測するのではなく capability の問い合わせで選びます', 'zh': '中继使用 Wear OS 数据层，它只在包名和签名证书相同的 APK 之间传输；目标通过能力查询选择，从不猜测已连接的节点', 'pt': 'O reencaminhamento usa a Data Layer do Wear OS, que só transporta tráfego entre APK com o mesmo nome de pacote e certificado de assinatura; o destino escolhe-se por uma consulta de capacidade, nunca adivinhando um nó ligado'}, '`WatchRelayTransport.kt`'], [{'en': 'A stolen or lost watch giving access to the server', 'es': 'Un reloj robado o perdido que da acceso al servidor', 'de': 'Eine gestohlene oder verlorene Uhr, die Zugriff auf den Server gibt', 'fr': 'Une montre volée ou perdue qui donne accès au serveur', 'it': 'Un orologio rubato o perso che dà accesso al server', 'ja': '盗難または紛失したウォッチからサーバーに入られる', 'zh': '被盗或丢失的手表获得服务器访问权', 'pt': 'Um relógio roubado ou perdido que dá acesso ao servidor'}, {'en': 'The watch never holds a server credential: the paired phone app authenticates and the watch only relays bounded protocol messages', 'es': 'El reloj nunca guarda una credencial del servidor: la aplicación del teléfono emparejado se autentica y el reloj solo retransmite mensajes de protocolo acotados', 'de': 'Die Uhr hält nie Server-Zugangsdaten: Die App des gekoppelten Telefons authentifiziert sich und die Uhr leitet nur begrenzte Protokollnachrichten weiter', 'fr': "La montre ne détient jamais d'identifiant du serveur : l'application du téléphone appairé s'authentifie et la montre ne relaie que des messages de protocole bornés", 'it': "L'orologio non conserva mai una credenziale del server: l'app del telefono abbinato si autentica e l'orologio inoltra solo messaggi di protocollo limitati", 'ja': 'ウォッチはサーバーの認証情報を持ちません。認証はペアリングしたスマートフォンのアプリが行い、ウォッチは上限付きのプロトコルメッセージを中継するだけです', 'zh': '手表从不持有服务器凭据：由配对手机上的应用完成认证，手表只转发有界的协议消息', 'pt': 'O relógio nunca guarda uma credencial do servidor: a aplicação do telemóvel emparelhado autentica-se e o relógio só reencaminha mensagens de protocolo limitadas'}, '`SyncMessage.kt`, `docs/VOICE_AI_PROTOCOL.md`'], [{'en': 'An action offered while the phone is out of reach, then failing later', 'es': 'Una acción ofrecida cuando el teléfono está fuera de alcance, que luego falla', 'de': 'Eine Aktion, die angeboten wird, während das Telefon außer Reichweite ist, und später scheitert', 'fr': 'Une action proposée alors que le téléphone est hors de portée, puis qui échoue', 'it': "Un'azione offerta mentre il telefono è fuori portata, che poi fallisce", 'ja': 'スマートフォンが圏外のときに表示され、後で失敗する操作', 'zh': '在手机不在范围内时提供、随后失败的操作', 'pt': 'Uma ação oferecida quando o telemóvel está fora de alcance, e que depois falha'}, {'en': 'Without a recent message from the phone companion an action that goes through it is withheld; a refresh is never gated, since it is how the heartbeat is obtained, and an old status is shown marked as old, not hidden', 'es': 'Sin un mensaje reciente del teléfono acompañante se retiene la acción que pasa por él; una actualización nunca se bloquea, porque así se obtiene el latido, y un estado antiguo se muestra marcado como antiguo, no oculto', 'de': 'Ohne eine aktuelle Nachricht des Telefon-Begleiters wird eine Aktion über ihn zurückgehalten; ein Aktualisieren wird nie gesperrt, da so der Herzschlag entsteht, und ein alter Status wird als alt markiert gezeigt, nicht versteckt', 'fr': "Sans message récent du téléphone compagnon, une action qui passe par lui est retenue ; un rafraîchissement n'est jamais bloqué, car c'est ainsi qu'on obtient le signal de vie, et un ancien état est affiché comme ancien, pas caché", 'it': "Senza un messaggio recente dal telefono compagno un'azione che passa da esso viene trattenuta; un aggiornamento non è mai bloccato, perché è così che si ottiene il segnale di vita, e uno stato vecchio è mostrato come vecchio, non nascosto", 'ja': 'コンパニオンのスマートフォンから最近のメッセージが無い間は、それを経由する操作は表示されません。更新は生存確認を得る手段なので制限されず、古い状態は隠さず「古い」と示して表示されます', 'zh': '手机配套应用没有最近的消息时，经由它的操作会被隐藏；刷新从不受限，因为这正是获取心跳的方式；旧状态会标明为旧，而不是隐藏', 'pt': 'Sem uma mensagem recente do telemóvel companheiro, uma ação que passa por ele fica retida; uma atualização nunca é bloqueada, porque é assim que se obtém o sinal de vida, e um estado antigo mostra-se marcado como antigo, não escondido'}, '`CriticalActionGate.kt`, `LastKnownStateCache.kt`']], 'never': {'en': '**What it never does:** act as an emergency stop. A wireless E-STOP button and a direct link to the server are future work that needs hardware.', 'es': '**Lo que nunca hace:** actuar como parada de emergencia. Un botón de parada de emergencia inalámbrico y un enlace directo con el servidor son trabajo futuro que necesita hardware.', 'de': '**Was er nie tut:** als Not-Halt dienen. Ein drahtloser Not-Halt-Knopf und eine direkte Verbindung zum Server sind künftige Arbeit, die Hardware braucht.', 'fr': "**Ce qu'il ne fait jamais :** servir d'arrêt d'urgence. Un bouton d'arrêt d'urgence sans fil et une liaison directe avec le serveur sont des travaux futurs qui exigent du matériel.", 'it': '**Cosa non fa mai:** fare da arresto di emergenza. Un pulsante di arresto di emergenza wireless e un collegamento diretto al server sono lavoro futuro che richiede hardware.', 'ja': '**絶対にしないこと：** 非常停止の代わりになること。無線の非常停止ボタンとサーバーへの直接接続は、ハードウェアを必要とする今後の作業です。', 'zh': '**它绝不做的事：** 充当紧急停止。无线急停按钮和直连服务器是需要硬件的后续工作。', 'pt': '**O que nunca faz:** servir de paragem de emergência. Um botão de paragem de emergência sem fios e uma ligação direta ao servidor são trabalho futuro que precisa de hardware.'}}}


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
