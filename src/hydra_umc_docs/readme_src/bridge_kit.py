# HYDRA-UMC-DOCS - readme_src/bridge_kit.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""The sentences that the READMEs of the HYDRA-UMC bridges and of the other small Python services repeat, in the eight languages."""
from __future__ import annotations

from ..readme_kit import P, table, code, pick

# ------------------------------------------------------------------ the HYDRA_MQTT_* variables of the shared MQTT client
MQTT_ENV_ROWS = [
    ("`HYDRA_MQTT_USERNAME`", P("none", "ninguno", "keiner", "aucun", "nessuno", "なし", "无", "nenhum"),
     P("The MQTT user name; the broker binds it to a client-ID prefix", "El usuario MQTT; el broker lo liga a un prefijo de ID de cliente", "Der MQTT-Benutzername; der Broker bindet ihn an ein Client-ID-Präfix",
       "Le nom d'utilisateur MQTT ; le broker le lie à un préfixe d'identifiant client", "Il nome utente MQTT; il broker lo lega a un prefisso di ID client",
       "MQTT のユーザー名。ブローカーはクライアント ID のプレフィックスに結び付けます", "MQTT 用户名；代理将其绑定到客户端 ID 前缀", "O nome de utilizador MQTT; o broker liga-o a um prefixo de ID de cliente")),
    ("`HYDRA_MQTT_PASSWORD`", P("none", "ninguno", "keiner", "aucun", "nessuno", "なし", "无", "nenhum"),
     P("The password; only valid together with the user name", "La contraseña; solo vale junto con el usuario", "Das Passwort; nur zusammen mit dem Benutzernamen gültig",
       "Le mot de passe ; valable seulement avec le nom d'utilisateur", "La password; valida solo insieme al nome utente", "パスワード。ユーザー名と一緒にのみ有効です", "密码；只能与用户名一起使用", "A palavra-passe; só vale em conjunto com o nome de utilizador")),
    ("`HYDRA_MQTT_PASSWORD_FILE`", P("none", "ninguno", "keiner", "aucun", "nessuno", "なし", "无", "nenhum"),
     P("The password read from a file (a Docker or systemd secret); ignored when `HYDRA_MQTT_PASSWORD` is set", "La contraseña leída de un fichero (secreto de Docker o systemd); se ignora si hay `HYDRA_MQTT_PASSWORD`",
       "Das Passwort aus einer Datei (Docker- oder systemd-Secret); wird ignoriert, wenn `HYDRA_MQTT_PASSWORD` gesetzt ist", "Le mot de passe lu dans un fichier (secret Docker ou systemd) ; ignoré si `HYDRA_MQTT_PASSWORD` est défini",
       "La password letta da un file (segreto Docker o systemd); ignorata se `HYDRA_MQTT_PASSWORD` è impostata", "ファイルから読むパスワード（Docker や systemd のシークレット）。`HYDRA_MQTT_PASSWORD` があれば無視されます",
       "从文件读取的密码（Docker 或 systemd 机密）；设置了 `HYDRA_MQTT_PASSWORD` 时忽略", "A palavra-passe lida de um ficheiro (segredo do Docker ou do systemd); ignorada se `HYDRA_MQTT_PASSWORD` estiver definida")),
    ("`HYDRA_MQTT_TLS_CA`", P("none", "ninguno", "keiner", "aucun", "nessuno", "なし", "无", "nenhum"),
     P("The CA file that signed the broker's certificate: the connection is TLS and the certificate is verified", "El fichero de la CA que firmó el certificado del broker: la conexión es TLS y se verifica el certificado",
       "Die CA-Datei, die das Zertifikat des Brokers signiert hat: Die Verbindung ist TLS und das Zertifikat wird geprüft", "Le fichier de l'AC qui a signé le certificat du broker : la connexion est en TLS et le certificat est vérifié",
       "Il file della CA che ha firmato il certificato del broker: la connessione è TLS e il certificato viene verificato", "ブローカーの証明書に署名した CA のファイル。接続は TLS になり、証明書が検証されます",
       "签署代理证书的 CA 文件：连接使用 TLS 并验证证书", "O ficheiro da CA que assinou o certificado do broker: a ligação é TLS e o certificado é verificado")),
    ("`HYDRA_MQTT_TLS`", P("off", "desactivado", "aus", "désactivé", "disattivato", "オフ", "关闭", "desativado"),
     P("`1` turns TLS on, verified against the system's trusted CAs", "`1` activa TLS, verificado con las CA de confianza del sistema", "`1` schaltet TLS ein, geprüft gegen die vertrauenswürdigen CAs des Systems",
       "`1` active TLS, vérifié avec les AC de confiance du système", "`1` attiva TLS, verificato con le CA fidate del sistema", "`1` で TLS を有効にし、システムの信頼する CA で検証します", "`1` 启用 TLS，并用系统信任的 CA 验证", "`1` ativa o TLS, verificado com as CA de confiança do sistema")),
    ("`HYDRA_MQTT_TLS_CERT` / `HYDRA_MQTT_TLS_KEY`", P("none", "ninguno", "keiner", "aucun", "nessuno", "なし", "无", "nenhum"),
     P("The client certificate and its key for a broker that demands mutual TLS; both are needed", "El certificado de cliente y su clave para un broker que exige TLS mutuo; hacen falta los dos",
       "Das Clientzertifikat und sein Schlüssel für einen Broker mit gegenseitigem TLS; beide sind nötig", "Le certificat client et sa clé pour un broker qui exige du TLS mutuel ; les deux sont requis",
       "Il certificato client e la sua chiave per un broker che richiede TLS reciproco; servono entrambi", "相互 TLS を求めるブローカー用のクライアント証明書とその鍵。両方が必要です",
       "用于要求双向 TLS 的代理的客户端证书及其密钥；两者都需要", "O certificado de cliente e a sua chave para um broker que exige TLS mútuo; são precisos os dois")),
]

BUILD_ROWS = [
    ("`HYDRA_UMC_SDK_ROOT`", P("`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`", "`../HYDRA-UMC-SDK`"),
     P("Where the build and test scripts look for the SDK checkout", "Dónde buscan los scripts de compilación y pruebas la copia del SDK", "Wo die Build- und Testskripte nach dem SDK-Checkout suchen",
       "Où les scripts de build et de test cherchent la copie du SDK", "Dove gli script di build e test cercano la copia dell'SDK", "ビルドとテストのスクリプトが SDK のチェックアウトを探す場所", "构建和测试脚本查找 SDK 副本的位置", "Onde os scripts de compilação e testes procuram a cópia do SDK")),
]

# ------------------------------------------------------------------ role
ROLE_SHARED_MQTT = P(
    "Every bridge speaks the shared safety contract of `HYDRA-UMC-SDK`: a job is accepted only after the shared `evaluate_job()` gate says so, and the gate fails closed. The parent project is `HYDRA-UMC-SERVER`; this bridge does not call it, it answers over MQTT through `HYDRA-UMC-MQTT-BROKER` to whoever commands the cell.",
    "Todos los bridges hablan el contrato de seguridad compartido de `HYDRA-UMC-SDK`: un trabajo solo se acepta cuando la puerta compartida `evaluate_job()` lo permite, y esa puerta falla cerrada. El proyecto padre es `HYDRA-UMC-SERVER`; este bridge no lo llama, responde por MQTT, a través de `HYDRA-UMC-MQTT-BROKER`, a quien manda en la celda.",
    "Jeder Bridge spricht den gemeinsamen Sicherheitsvertrag von `HYDRA-UMC-SDK`: Ein Auftrag wird nur angenommen, wenn das gemeinsame Tor `evaluate_job()` zustimmt, und das Tor schließt im Zweifel. Das Elternprojekt ist `HYDRA-UMC-SERVER`; dieser Bridge ruft es nicht auf, er antwortet über MQTT und `HYDRA-UMC-MQTT-BROKER` dem, der die Zelle steuert.",
    "Chaque bridge parle le contrat de sécurité partagé de `HYDRA-UMC-SDK` : un travail n'est accepté que si la porte partagée `evaluate_job()` le permet, et cette porte échoue en position fermée. Le projet parent est `HYDRA-UMC-SERVER` ; ce bridge ne l'appelle pas, il répond en MQTT, via `HYDRA-UMC-MQTT-BROKER`, à celui qui commande la cellule.",
    "Ogni bridge parla il contratto di sicurezza condiviso di `HYDRA-UMC-SDK`: un lavoro viene accettato solo se la porta condivisa `evaluate_job()` lo permette, e quella porta fallisce chiusa. Il progetto padre è `HYDRA-UMC-SERVER`; questo bridge non lo chiama, risponde via MQTT, attraverso `HYDRA-UMC-MQTT-BROKER`, a chi comanda la cella.",
    "すべてのブリッジは `HYDRA-UMC-SDK` の共通の安全契約に従います。ジョブは共通の `evaluate_job()` ゲートが許可したときだけ受け付けられ、ゲートは安全側（閉）に倒れます。親プロジェクトは `HYDRA-UMC-SERVER` で、このブリッジはそれを呼び出さず、`HYDRA-UMC-MQTT-BROKER` 経由の MQTT でセルを指令する側に応答します。",
    "所有桥接都遵循 `HYDRA-UMC-SDK` 的共同安全契约：只有共用的 `evaluate_job()` 关口放行，任务才会被接受，而该关口在失败时保持关闭。父项目是 `HYDRA-UMC-SERVER`；本桥接不调用它，而是通过 `HYDRA-UMC-MQTT-BROKER` 以 MQTT 回应指挥该单元的一方。",
    "Todos os bridges falam o contrato de segurança partilhado do `HYDRA-UMC-SDK`: um trabalho só é aceite quando a porta partilhada `evaluate_job()` o permite, e essa porta falha fechada. O projeto pai é o `HYDRA-UMC-SERVER`; este bridge não o chama, responde por MQTT, através do `HYDRA-UMC-MQTT-BROKER`, a quem comanda a célula.",
)

# ------------------------------------------------------------------ quick start
INSTALL_SDK = P(
    "Requires Python 3.11 or newer. The tests and the build scripts expect `HYDRA-UMC-SDK` checked out next to this repository (`../HYDRA-UMC-SDK`) or pointed at with `HYDRA_UMC_SDK_ROOT`.",
    "Requiere Python 3.11 o superior. Las pruebas y los scripts de compilación esperan `HYDRA-UMC-SDK` clonado junto a este repositorio (`../HYDRA-UMC-SDK`) o indicado con `HYDRA_UMC_SDK_ROOT`.",
    "Benötigt Python 3.11 oder neuer. Die Tests und die Build-Skripte erwarten `HYDRA-UMC-SDK` neben diesem Repository (`../HYDRA-UMC-SDK`) oder über `HYDRA_UMC_SDK_ROOT` angegeben.",
    "Nécessite Python 3.11 ou plus récent. Les tests et les scripts de build attendent `HYDRA-UMC-SDK` cloné à côté de ce dépôt (`../HYDRA-UMC-SDK`) ou indiqué par `HYDRA_UMC_SDK_ROOT`.",
    "Richiede Python 3.11 o successivo. I test e gli script di build si aspettano `HYDRA-UMC-SDK` clonato accanto a questo repository (`../HYDRA-UMC-SDK`) o indicato con `HYDRA_UMC_SDK_ROOT`.",
    "Python 3.11 以上が必要です。テストとビルドスクリプトは、このリポジトリの隣にある `HYDRA-UMC-SDK`（`../HYDRA-UMC-SDK`）、または `HYDRA_UMC_SDK_ROOT` で指定した場所を前提にします。",
    "需要 Python 3.11 或更高版本。测试和构建脚本期望 `HYDRA-UMC-SDK` 位于本仓库旁边（`../HYDRA-UMC-SDK`），或由 `HYDRA_UMC_SDK_ROOT` 指定。",
    "Requer Python 3.11 ou superior. Os testes e os scripts de compilação esperam o `HYDRA-UMC-SDK` clonado ao lado deste repositório (`../HYDRA-UMC-SDK`) ou indicado com `HYDRA_UMC_SDK_ROOT`.",
)
TRY_IT = P("Try it without hardware (this checks the whole bridge against its emulators and fakes):", "Pruébalo sin hardware (esto comprueba todo el bridge contra sus emuladores y dobles de prueba):",
           "Ohne Hardware ausprobieren (das prüft den ganzen Bridge gegen seine Emulatoren und Attrappen):", "Essayez-le sans matériel (cela vérifie tout le bridge avec ses émulateurs et ses doubles de test) :",
           "Provalo senza hardware (questo verifica tutto il bridge con i suoi emulatori e test double):", "ハードウェアなしで試す（エミュレーターと模擬部品でブリッジ全体を確認します）：",
           "无需硬件即可试用（用模拟器和替身检查整个桥接）：", "Experimente sem hardware (isto verifica todo o bridge com os seus emuladores e dublês de teste):")
START_SERVICE = P("Start the service (there is no console script: the service is the `run_forever()` of the MQTT transport, which you call from your own start-up code):",
                  "Arranca el servicio (no hay un script de consola: el servicio es el `run_forever()` del transporte MQTT, que llamas desde tu propio código de arranque):",
                  "Den Dienst starten (es gibt kein Konsolenskript: Der Dienst ist das `run_forever()` des MQTT-Transports, das du aus deinem eigenen Startcode aufrufst):",
                  "Démarrer le service (il n'y a pas de script de console : le service est le `run_forever()` du transport MQTT, que vous appelez depuis votre propre code de démarrage) :",
                  "Avviare il servizio (non c'è uno script da console: il servizio è il `run_forever()` del trasporto MQTT, che chiami dal tuo codice di avvio):",
                  "サービスを起動する（コンソールスクリプトはありません。サービスは MQTT トランスポートの `run_forever()` で、自分の起動コードから呼び出します）：",
                  "启动服务（没有控制台脚本：服务就是 MQTT 传输的 `run_forever()`，由你自己的启动代码调用）：",
                  "Arrancar o serviço (não há um script de consola: o serviço é o `run_forever()` do transporte MQTT, que chama a partir do seu próprio código de arranque):")
CREDENTIALS_NOTE = P("The user name, the password and the TLS files come from the `HYDRA_MQTT_*` variables (see Configuration); the code above needs no credentials of its own.",
                     "El usuario, la contraseña y los ficheros TLS salen de las variables `HYDRA_MQTT_*` (ver Configuración); el código de arriba no necesita credenciales propias.",
                     "Benutzername, Passwort und TLS-Dateien kommen aus den Variablen `HYDRA_MQTT_*` (siehe Konfiguration); der Code oben braucht keine eigenen Zugangsdaten.",
                     "Le nom d'utilisateur, le mot de passe et les fichiers TLS viennent des variables `HYDRA_MQTT_*` (voir Configuration) ; le code ci-dessus n'a besoin d'aucun identifiant propre.",
                     "Nome utente, password e file TLS vengono dalle variabili `HYDRA_MQTT_*` (vedi Configurazione); il codice sopra non ha bisogno di credenziali proprie.",
                     "ユーザー名、パスワード、TLS ファイルは `HYDRA_MQTT_*` 変数から読まれます（設定を参照）。上のコード自体に認証情報は不要です。",
                     "用户名、密码和 TLS 文件来自 `HYDRA_MQTT_*` 变量（见“配置”）；上面的代码本身不需要凭据。",
                     "O nome de utilizador, a palavra-passe e os ficheiros TLS vêm das variáveis `HYDRA_MQTT_*` (ver Configuração); o código acima não precisa de credenciais próprias.")

# ------------------------------------------------------------------ testing
TESTING_INTRO = P(
    "{n} automated `unittest` cases run with `python tools/build_test.py` (it also compiles every module). The tests need no hardware, no network and no optional package: the ones that would need `paho-mqtt`, `pyserial` or a vendor library use a stand-in or are skipped when the package is missing.",
    "{n} casos automáticos de `unittest` se ejecutan con `python tools/build_test.py` (que también compila cada módulo). Las pruebas no necesitan hardware, red ni paquetes opcionales: las que necesitarían `paho-mqtt`, `pyserial` o una biblioteca del fabricante usan un sustituto o se saltan si falta el paquete.",
    "{n} automatische `unittest`-Fälle laufen mit `python tools/build_test.py` (das kompiliert auch jedes Modul). Die Tests brauchen weder Hardware noch Netz noch optionale Pakete: Die, die `paho-mqtt`, `pyserial` oder eine Herstellerbibliothek bräuchten, nutzen einen Ersatz oder werden übersprungen, wenn das Paket fehlt.",
    "{n} cas `unittest` automatiques s'exécutent avec `python tools/build_test.py` (qui compile aussi chaque module). Les tests n'ont besoin ni de matériel, ni de réseau, ni de paquet optionnel : ceux qui exigeraient `paho-mqtt`, `pyserial` ou une bibliothèque de fabricant utilisent un substitut ou sont ignorés si le paquet manque.",
    "{n} casi `unittest` automatici si eseguono con `python tools/build_test.py` (che compila anche ogni modulo). I test non richiedono hardware, rete né pacchetti opzionali: quelli che richiederebbero `paho-mqtt`, `pyserial` o una libreria del produttore usano un sostituto o vengono saltati se il pacchetto manca.",
    "`python tools/build_test.py` で自動 `unittest` {n} 件を実行します（各モジュールのコンパイルも行います）。テストにハードウェア、ネットワーク、オプションのパッケージは不要で、`paho-mqtt`・`pyserial`・ベンダーのライブラリが必要なものは代用品を使うか、パッケージがなければスキップされます。",
    "运行 `python tools/build_test.py` 会执行 {n} 个自动 `unittest` 用例（同时编译每个模块）。测试不需要硬件、网络或可选软件包：需要 `paho-mqtt`、`pyserial` 或厂商库的用例使用替身，缺少软件包时则跳过。",
    "{n} casos `unittest` automáticos correm com `python tools/build_test.py` (que também compila cada módulo). Os testes não precisam de hardware, rede nem pacotes opcionais: os que precisariam de `paho-mqtt`, `pyserial` ou de uma biblioteca do fabricante usam um substituto ou são saltados se o pacote faltar.",
)
CI_LINE = P(
    "The CI runs `HYDRA_UMC_CI=1 python tools/ci_validate.py`, which checks the manifest, the documents, the eight READMEs and the pictures, and runs the tests with an SDK checkout.",
    "El CI ejecuta `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que comprueba el manifiesto, los documentos, los ocho README y las imágenes, y ejecuta las pruebas con una copia del SDK.",
    "Die CI führt `HYDRA_UMC_CI=1 python tools/ci_validate.py` aus; das prüft das Manifest, die Dokumente, die acht READMEs und die Bilder und führt die Tests mit einem SDK-Checkout aus.",
    "La CI exécute `HYDRA_UMC_CI=1 python tools/ci_validate.py`, qui vérifie le manifeste, les documents, les huit README et les images, et lance les tests avec une copie du SDK.",
    "La CI esegue `HYDRA_UMC_CI=1 python tools/ci_validate.py`, che controlla il manifesto, i documenti, gli otto README e le immagini, ed esegue i test con una copia dell'SDK.",
    "CI は `HYDRA_UMC_CI=1 python tools/ci_validate.py` を実行し、マニフェスト、文書、8 つの README、図を検査し、SDK のチェックアウトを使ってテストを実行します。",
    "CI 运行 `HYDRA_UMC_CI=1 python tools/ci_validate.py`，检查清单、文档、八个 README 和图片，并使用 SDK 副本运行测试。",
    "A CI executa `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que verifica o manifesto, os documentos, os oito README e as imagens, e corre os testes com uma cópia do SDK.",
)

# ------------------------------------------------------------------ troubleshooting rows shared by the Python services
TROUBLE_SDK = ("`ModuleNotFoundError: hydra_umc_sdk`",
               P("The SDK is not installed or not next to this repository", "El SDK no está instalado ni junto a este repositorio", "Das SDK ist nicht installiert oder liegt nicht neben diesem Repository",
                 "Le SDK n'est ni installé ni à côté de ce dépôt", "L'SDK non è installato né accanto a questo repository", "SDK がインストールされておらず、このリポジトリの隣にもありません", "未安装 SDK，且不在本仓库旁边", "O SDK não está instalado nem ao lado deste repositório"),
               P("Check out `HYDRA-UMC-SDK` next to this repository or set `HYDRA_UMC_SDK_ROOT`", "Clona `HYDRA-UMC-SDK` junto a este repositorio o define `HYDRA_UMC_SDK_ROOT`", "`HYDRA-UMC-SDK` neben dieses Repository klonen oder `HYDRA_UMC_SDK_ROOT` setzen",
                 "Clonez `HYDRA-UMC-SDK` à côté de ce dépôt ou définissez `HYDRA_UMC_SDK_ROOT`", "Clona `HYDRA-UMC-SDK` accanto a questo repository o imposta `HYDRA_UMC_SDK_ROOT`", "`HYDRA-UMC-SDK` をこのリポジトリの隣に置くか、`HYDRA_UMC_SDK_ROOT` を設定します",
                 "把 `HYDRA-UMC-SDK` 克隆到本仓库旁边，或设置 `HYDRA_UMC_SDK_ROOT`", "Clone o `HYDRA-UMC-SDK` ao lado deste repositório ou defina `HYDRA_UMC_SDK_ROOT`"))
TROUBLE_PAHO = ("`paho-mqtt is not installed`",
                P("The MQTT client is an optional extra", "El cliente MQTT es un extra opcional", "Der MQTT-Client ist ein optionales Extra", "Le client MQTT est un extra optionnel", "Il client MQTT è un extra opzionale", "MQTT クライアントはオプションの追加パッケージです", "MQTT 客户端是可选附加包", "O cliente MQTT é um extra opcional"),
                P("`pip install \".[mqtt]\"` (it needs `paho-mqtt` 2.1 or newer, below 3)", "`pip install \".[mqtt]\"` (necesita `paho-mqtt` 2.1 o superior, menor que 3)", "`pip install \".[mqtt]\"` (braucht `paho-mqtt` ab 2.1, unter 3)",
                  "`pip install \".[mqtt]\"` (il faut `paho-mqtt` 2.1 ou plus, avant 3)", "`pip install \".[mqtt]\"` (serve `paho-mqtt` 2.1 o successivo, inferiore a 3)", "`pip install \".[mqtt]\"`（`paho-mqtt` 2.1 以上 3 未満が必要）",
                  "`pip install \".[mqtt]\"`（需要 `paho-mqtt` 2.1 或更高，低于 3）", "`pip install \".[mqtt]\"` (precisa de `paho-mqtt` 2.1 ou superior, inferior a 3)"))
TROUBLE_CREDS = ("`password was given without a username`",
                 P("MQTT credentials need both parts", "Las credenciales MQTT necesitan las dos partes", "MQTT-Zugangsdaten brauchen beide Teile", "Les identifiants MQTT exigent les deux parties", "Le credenziali MQTT richiedono entrambe le parti", "MQTT の認証情報にはユーザー名とパスワードの両方が必要です", "MQTT 凭据需要两部分", "As credenciais MQTT precisam das duas partes"),
                 P("Set `HYDRA_MQTT_USERNAME` as well as the password", "Define `HYDRA_MQTT_USERNAME` además de la contraseña", "Setze auch `HYDRA_MQTT_USERNAME`, nicht nur das Passwort", "Définissez aussi `HYDRA_MQTT_USERNAME`, pas seulement le mot de passe",
                   "Imposta anche `HYDRA_MQTT_USERNAME`, non solo la password", "パスワードに加えて `HYDRA_MQTT_USERNAME` も設定します", "除密码外还要设置 `HYDRA_MQTT_USERNAME`", "Defina também `HYDRA_MQTT_USERNAME`, não só a palavra-passe"))


def trouble_table(lg, rows):
    return table(lg, "trouble", [[r[0], r[1], r[2]] for r in rows])


def global_stop_row(variable, *texts):
    """The row of the configuration table for the switch that makes a bridge follow the global stop of the server; `texts` are the eight descriptions."""
    return (f"`{variable}`", P("off", "desactivado", "aus", "désactivé", "disattivato", "オフ", "关闭", "desativado"), P(*texts))


def mqtt_env_table(lg):
    return table(lg, "config", MQTT_ENV_ROWS)


def talks(lg, rows):
    return table(lg, "talks", rows)


# ------------------------------------------------------------------ the rows of the security table that every MQTT bridge shares
def _row(threat, defence, where):
    return [threat, defence, where]


SEC_GATE = _row(
    P("A job for a cell or machine that is not in a safe state", "Un trabajo para una celda o máquina que no está en estado seguro", "Ein Auftrag für eine Zelle oder Maschine, die nicht sicher ist", "Un travail pour une cellule ou une machine qui n'est pas en état sûr",
      "Un lavoro per una cella o macchina che non è in stato sicuro", "安全でない状態のセルや機械へのジョブ", "对处于不安全状态的单元或机器下达任务", "Um trabalho para uma célula ou máquina que não está em estado seguro"),
    P("Every job goes through the shared `evaluate_job()` gate of the SDK, which fails closed; the bridge has no accept/reject logic of its own",
      "Todo trabajo pasa por la puerta compartida `evaluate_job()` del SDK, que falla cerrada; el bridge no tiene lógica propia de aceptar o rechazar",
      "Jeder Auftrag läuft durch das gemeinsame Tor `evaluate_job()` des SDK, das im Zweifel schließt; der Bridge hat keine eigene Annahmelogik",
      "Chaque travail passe par la porte partagée `evaluate_job()` du SDK, qui échoue en position fermée ; le bridge n'a aucune logique propre d'acceptation",
      "Ogni lavoro passa dalla porta condivisa `evaluate_job()` dell'SDK, che fallisce chiusa; il bridge non ha una logica propria di accettazione",
      "すべてのジョブは SDK の共通 `evaluate_job()` ゲートを通り、ゲートは安全側に倒れます。ブリッジ自身に受理・拒否のロジックはありません",
      "每个任务都经过 SDK 共用的 `evaluate_job()` 关口，该关口失败时保持关闭；桥接本身没有接受/拒绝逻辑",
      "Todo o trabalho passa pela porta partilhada `evaluate_job()` do SDK, que falha fechada; o bridge não tem lógica própria de aceitar ou recusar"),
    "SDK `bridge_contract`")
SEC_LIMITS = _row(
    P("Oversized or unbounded job data", "Datos de trabajo desmesurados", "Überlange oder unbegrenzte Auftragsdaten", "Données de travail démesurées", "Dati di lavoro smisurati", "過大なジョブデータ", "过大的任务数据", "Dados de trabalho desmesurados"),
    P("At most 32 parameters, keys up to 64 characters, values up to 1024, identifiers up to 128 (`MAX_PARAMETERS`, `MAX_PARAMETER_KEY_CHARS`, `MAX_PARAMETER_VALUE_CHARS`, `MAX_IDENTIFIER_CHARS`)",
      "Como máximo 32 parámetros, claves de hasta 64 caracteres, valores de hasta 1024, identificadores de hasta 128 (`MAX_PARAMETERS`, `MAX_PARAMETER_KEY_CHARS`, `MAX_PARAMETER_VALUE_CHARS`, `MAX_IDENTIFIER_CHARS`)",
      "Höchstens 32 Parameter, Schlüssel bis 64 Zeichen, Werte bis 1024, Bezeichner bis 128 (`MAX_PARAMETERS`, `MAX_PARAMETER_KEY_CHARS`, `MAX_PARAMETER_VALUE_CHARS`, `MAX_IDENTIFIER_CHARS`)",
      "Au plus 32 paramètres, clés jusqu'à 64 caractères, valeurs jusqu'à 1024, identifiants jusqu'à 128 (`MAX_PARAMETERS`, `MAX_PARAMETER_KEY_CHARS`, `MAX_PARAMETER_VALUE_CHARS`, `MAX_IDENTIFIER_CHARS`)",
      "Al massimo 32 parametri, chiavi fino a 64 caratteri, valori fino a 1024, identificatori fino a 128 (`MAX_PARAMETERS`, `MAX_PARAMETER_KEY_CHARS`, `MAX_PARAMETER_VALUE_CHARS`, `MAX_IDENTIFIER_CHARS`)",
      "パラメーターは最大 32 個、キーは 64 文字、値は 1024 文字、識別子は 128 文字まで（`MAX_PARAMETERS`、`MAX_PARAMETER_KEY_CHARS`、`MAX_PARAMETER_VALUE_CHARS`、`MAX_IDENTIFIER_CHARS`）",
      "最多 32 个参数，键最长 64 个字符，值最长 1024，标识符最长 128（`MAX_PARAMETERS`、`MAX_PARAMETER_KEY_CHARS`、`MAX_PARAMETER_VALUE_CHARS`、`MAX_IDENTIFIER_CHARS`）",
      "No máximo 32 parâmetros, chaves até 64 carateres, valores até 1024, identificadores até 128 (`MAX_PARAMETERS`, `MAX_PARAMETER_KEY_CHARS`, `MAX_PARAMETER_VALUE_CHARS`, `MAX_IDENTIFIER_CHARS`)"),
    "SDK `bridge_contract`")
SEC_IDEM = _row(
    P("A repeated or replayed order", "Una orden repetida o reenviada", "Ein wiederholter oder erneut gesendeter Befehl", "Un ordre répété ou rejoué", "Un ordine ripetuto o rinviato", "繰り返された、または再送された命令", "重复或重放的命令", "Uma ordem repetida ou reenviada"),
    P("An `IdempotencyStore` remembers each key for 24 hours and at most 10 000 entries; a repeat gets the first answer instead of being evaluated again",
      "Un `IdempotencyStore` recuerda cada clave 24 horas y como máximo 10 000 entradas; una repetición recibe la primera respuesta en vez de evaluarse otra vez",
      "Ein `IdempotencyStore` merkt sich jeden Schlüssel 24 Stunden und höchstens 10 000 Einträge; eine Wiederholung bekommt die erste Antwort, statt neu bewertet zu werden",
      "Un `IdempotencyStore` retient chaque clé 24 heures et au plus 10 000 entrées ; une répétition reçoit la première réponse au lieu d'être réévaluée",
      "Un `IdempotencyStore` ricorda ogni chiave per 24 ore e al massimo 10 000 voci; una ripetizione riceve la prima risposta invece di essere valutata di nuovo",
      "`IdempotencyStore` は各キーを 24 時間、最大 10 000 件まで記憶し、再送には再評価せず最初の応答を返します",
      "`IdempotencyStore` 将每个键记住 24 小时、最多 10 000 条；重复请求得到第一次的答复而不是重新评估",
      "Um `IdempotencyStore` lembra cada chave durante 24 horas e no máximo 10 000 entradas; uma repetição recebe a primeira resposta em vez de ser avaliada de novo"),
    "SDK `job_intake`")
SEC_PAYLOAD = _row(
    P("A huge or hostile MQTT payload", "Una carga MQTT enorme u hostil", "Eine riesige oder feindliche MQTT-Nutzlast", "Une charge MQTT énorme ou hostile", "Un payload MQTT enorme o ostile", "巨大または悪意のある MQTT ペイロード", "巨大或恶意的 MQTT 负载", "Uma carga MQTT enorme ou hostil"),
    P("A payload over 16 KiB, unreadable or deeply nested JSON and any unexpected failure are answered with a refusal on the result topic and never end the loop",
      "Una carga de más de 16 KiB, un JSON ilegible o muy anidado y cualquier fallo inesperado se responden con un rechazo en el topic de resultado y nunca terminan el bucle",
      "Eine Nutzlast über 16 KiB, unlesbares oder tief verschachteltes JSON und jeder unerwartete Fehler werden mit einer Ablehnung auf dem Ergebnis-Topic beantwortet und beenden die Schleife nie",
      "Une charge de plus de 16 KiB, un JSON illisible ou très imbriqué et tout échec inattendu reçoivent un refus sur le topic de résultat et ne terminent jamais la boucle",
      "Un payload oltre 16 KiB, un JSON illeggibile o molto annidato e qualsiasi errore imprevisto ricevono un rifiuto sul topic di risultato e non terminano mai il ciclo",
      "16 KiB を超えるペイロード、読めない・深く入れ子になった JSON、想定外の失敗は、結果トピックで拒否として応答され、ループを終わらせません",
      "超过 16 KiB 的负载、不可读或嵌套过深的 JSON 以及任何意外故障，都会在结果主题上得到拒绝答复，且不会终止循环",
      "Uma carga acima de 16 KiB, um JSON ilegível ou muito aninhado e qualquer falha inesperada recebem uma recusa no tópico de resultado e nunca terminam o ciclo"),
    "`mqtt_transport.py`")
TROUBLE_REFUSED = ("`\"allowed\": false` + `reason`",
                   P("The shared gate or a guard refused the order", "La puerta compartida o una guarda rechazó la orden", "Das gemeinsame Tor oder eine Sperre hat den Befehl abgelehnt", "La porte partagée ou une garde a refusé l'ordre",
                     "La porta condivisa o una guardia ha rifiutato l'ordine", "共通ゲートまたはガードが命令を拒否しました", "共用关口或某项保护拒绝了命令", "A porta partilhada ou uma guarda recusou a ordem"),
                   P("Read `reason` and fix the cause; do not retry blindly", "Lee `reason` y arregla la causa; no reintentes a ciegas", "Lies `reason` und behebe die Ursache; nicht blind wiederholen", "Lisez `reason` et corrigez la cause ; ne réessayez pas à l'aveugle",
                     "Leggi `reason` e correggi la causa; non riprovare alla cieca", "`reason` を読んで原因を直します。やみくもに再試行しないでください", "阅读 `reason` 并排除原因；不要盲目重试", "Leia `reason` e corrija a causa; não repita às cegas"))
NEVER = P("**What it never does:**", "**Lo que nunca hace:**", "**Was er nie tut:**", "**Ce qu'il ne fait jamais :**", "**Cosa non fa mai:**", "**絶対にしないこと：**", "**它绝不做的事：**", "**O que nunca faz:**")
NEVER_PLAIN = P("**What it never does:**", "**Lo que nunca hace:**", "**Was es nie tut:**", "**Ce qu'il ne fait jamais :**", "**Cosa non fa mai:**", "**絶対にしないこと：**", "**它绝不做的事：**", "**O que nunca faz:**")


def security(lg, rows, never, common=("gate", "limits", "idem", "payload")):
    """The threat table (the common rows first, then `rows`) and the sentence of what the bridge never does."""
    chosen = {"gate": SEC_GATE, "limits": SEC_LIMITS, "idem": SEC_IDEM, "payload": SEC_PAYLOAD}
    all_rows = [chosen[name] for name in common] + list(rows)
    return table(lg, "threat", all_rows) + "\n\n" + (NEVER[lg] + " " + pick(never, lg))


def testing(lg, n, rows):
    return TESTING_INTRO[lg].replace("{n}", str(n)) + "\n\n" + table(lg, "tests", rows) + "\n\n" + CI_LINE[lg]


def quickstart(lg, snippet, service=True, note=True):
    parts = [INSTALL_SDK[lg], TRY_IT[lg], code(lg, ["py -3 tools/build_test.py          # Windows", "python3 tools/build_test.py         # Linux, macOS"], "bash")]
    if service:
        parts += [START_SERVICE[lg], code(lg, snippet, "python")]
        if note:
            parts.append(CREDENTIALS_NOTE[lg])
    return "\n\n".join(parts)


def docs_item(lg, path, desc):
    return f"[{path}]({path}) - {pick(desc, lg)}"

TROUBLE_REACH = ("`could not reach the MQTT broker after N attempts`",
                 P("The broker is down, the address is wrong or the port is closed", "El broker está caído, la dirección es errónea o el puerto está cerrado", "Der Broker ist aus, die Adresse falsch oder der Port geschlossen", "Le broker est arrêté, l'adresse est fausse ou le port est fermé",
                   "Il broker è spento, l'indirizzo è sbagliato o la porta è chiusa", "ブローカーが停止している、アドレスが違う、またはポートが閉じています", "代理未运行、地址错误或端口已关闭", "O broker está em baixo, o endereço está errado ou a porta está fechada"),
                 P("Start `HYDRA-UMC-MQTT-BROKER`, check the host and port given to the transport (it tries 5 times, 2 seconds apart); a TLS handshake failure is not retried", "Arranca `HYDRA-UMC-MQTT-BROKER` y revisa el host y el puerto dados al transporte (lo intenta 5 veces, con 2 segundos de pausa); un fallo del handshake TLS no se reintenta",
                   "Starte `HYDRA-UMC-MQTT-BROKER` und prüfe Host und Port des Transports (5 Versuche im Abstand von 2 Sekunden); ein TLS-Handshake-Fehler wird nicht wiederholt", "Démarrez `HYDRA-UMC-MQTT-BROKER` et vérifiez l'hôte et le port donnés au transport (5 essais à 2 secondes d'écart) ; un échec de la poignée de main TLS n'est pas réessayé",
                   "Avvia `HYDRA-UMC-MQTT-BROKER` e controlla host e porta dati al trasporto (5 tentativi a 2 secondi di distanza); un errore dell'handshake TLS non viene ritentato", "`HYDRA-UMC-MQTT-BROKER` を起動し、トランスポートに渡したホストとポートを確認します（2 秒間隔で 5 回試行。TLS ハンドシェイクの失敗は再試行しません）",
                   "启动 `HYDRA-UMC-MQTT-BROKER`，检查传给传输层的主机和端口（每隔 2 秒试 5 次；TLS 握手失败不会重试）", "Arranque o `HYDRA-UMC-MQTT-BROKER` e verifique o anfitrião e a porta dados ao transporte (5 tentativas com 2 segundos de intervalo); uma falha do handshake TLS não é repetida"))
TROUBLE_CONNREFUSED = ("`the MQTT broker refused the connection`",
                       P("The broker refused the credential (or did not answer within the time limit)", "El broker rechazó la credencial (o no respondió dentro del plazo)", "Der Broker hat die Zugangsdaten abgelehnt (oder nicht rechtzeitig geantwortet)", "Le broker a refusé l'identifiant (ou n'a pas répondu à temps)",
                         "Il broker ha rifiutato la credenziale (o non ha risposto entro il tempo limite)", "ブローカーが認証を拒否しました（または制限時間内に応答しませんでした）", "代理拒绝了凭据（或未在时限内应答）", "O broker recusou a credencial (ou não respondeu a tempo)"),
                       P("Check `HYDRA_MQTT_USERNAME` and the password; the client ID must start with the prefix the broker bound to the credential", "Revisa `HYDRA_MQTT_USERNAME` y la contraseña; el ID de cliente debe empezar por el prefijo que el broker ligó a la credencial", "Prüfe `HYDRA_MQTT_USERNAME` und das Passwort; die Client-ID muss mit dem Präfix beginnen, das der Broker an die Zugangsdaten gebunden hat",
                         "Vérifiez `HYDRA_MQTT_USERNAME` et le mot de passe ; l'identifiant client doit commencer par le préfixe que le broker a lié à l'identifiant", "Controlla `HYDRA_MQTT_USERNAME` e la password; l'ID client deve iniziare con il prefisso che il broker ha legato alla credenziale", "`HYDRA_MQTT_USERNAME` とパスワードを確認します。クライアント ID はブローカーが認証情報に結び付けたプレフィックスで始まる必要があります", "检查 `HYDRA_MQTT_USERNAME` 和密码；客户端 ID 必须以代理绑定到该凭据的前缀开头", "Verifique `HYDRA_MQTT_USERNAME` e a palavra-passe; o ID de cliente tem de começar pelo prefixo que o broker ligou à credencial"))

ROLE_TEMPLATE = P(
    "**{name}** sits between {what} and the robot cell. It reports what that side says, asks the shared gate before any auxiliary work and never takes over the authority of the machine it coordinates with.",
    "**{name}** está entre {what} y la celda de robots. Cuenta lo que dice ese lado, consulta la puerta compartida antes de cualquier trabajo auxiliar y nunca asume la autoridad de la máquina con la que coordina.",
    "**{name}** sitzt zwischen {what} und der Roboterzelle. Er meldet, was diese Seite sagt, fragt vor jeder Hilfsarbeit das gemeinsame Tor und übernimmt nie die Hoheit der Maschine, mit der er sich abstimmt.",
    "**{name}** se place entre {what} et la cellule de robots. Il rapporte ce que dit ce côté, interroge la porte partagée avant tout travail auxiliaire et ne prend jamais l'autorité de la machine avec laquelle il coordonne.",
    "**{name}** sta tra {what} e la cella di robot. Riferisce ciò che dice quel lato, interroga la porta condivisa prima di qualsiasi lavoro ausiliario e non assume mai l'autorità della macchina con cui si coordina.",
    "**{name}** は {what} とロボットセルの間に位置します。相手側の報告を伝え、補助作業の前に共通ゲートへ問い合わせ、協調する機械の権限を決して引き継ぎません。",
    "**{name}** 位于{what}与机器人单元之间。它转述对方所说的内容，在任何辅助作业前询问共用关口，且绝不接管所协调机器的决定权。",
    "O **{name}** fica entre {what} e a célula de robôs. Relata o que esse lado diz, consulta a porta partilhada antes de qualquer trabalho auxiliar e nunca assume a autoridade da máquina com que coordena.",
)


def role(lg, name, what, mqtt=True):
    """The Role section: one sentence with the thing the bridge stands next to (`what`, a text in eight languages), then the shared contract."""
    first = ROLE_TEMPLATE[lg].replace("{name}", name).replace("{what}", pick(what, lg))
    return first + ("\n\n" + ROLE_SHARED_MQTT[lg] if mqtt else "")


def trow(file, desc):
    """One row of the table of tests: the file or files and what they cover."""
    return [file, "-", desc]

TESTING_PLAIN = P(
    "{n} automated tests run with `python tools/build_test.py` (it also compiles every module). They need no hardware and no outside network: what they call is a local fixture or a real local process.",
    "{n} pruebas automáticas se ejecutan con `python tools/build_test.py` (que también compila cada módulo). No necesitan hardware ni red externa: lo que llaman es un montaje local o un proceso local real.",
    "{n} automatische Tests laufen mit `python tools/build_test.py` (das kompiliert auch jedes Modul). Sie brauchen weder Hardware noch ein äußeres Netz: Was sie aufrufen, ist ein lokales Fixture oder ein echter lokaler Prozess.",
    "{n} tests automatiques s'exécutent avec `python tools/build_test.py` (qui compile aussi chaque module). Ils n'ont besoin ni de matériel ni de réseau extérieur : ce qu'ils appellent est un banc local ou un vrai processus local.",
    "{n} test automatici si eseguono con `python tools/build_test.py` (che compila anche ogni modulo). Non richiedono hardware né rete esterna: ciò che chiamano è una fixture locale o un vero processo locale.",
    "`python tools/build_test.py` で自動テスト {n} 件を実行します（各モジュールのコンパイルも行います）。ハードウェアも外部ネットワークも不要で、呼び出す相手はローカルのフィクスチャか実際のローカルプロセスです。",
    "运行 `python tools/build_test.py` 会执行 {n} 个自动测试（同时编译每个模块）。测试不需要硬件和外部网络：它们调用的是本地夹具或真实的本地进程。",
    "{n} testes automáticos correm com `python tools/build_test.py` (que também compila cada módulo). Não precisam de hardware nem de rede externa: o que chamam é uma fixture local ou um processo local real.",
)
CI_PLAIN = P(
    "The CI runs `HYDRA_UMC_CI=1 python tools/ci_validate.py`, which checks the manifest, the documents, the eight READMEs and the pictures.",
    "El CI ejecuta `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que comprueba el manifiesto, los documentos, los ocho README y las imágenes.",
    "Die CI führt `HYDRA_UMC_CI=1 python tools/ci_validate.py` aus; das prüft das Manifest, die Dokumente, die acht READMEs und die Bilder.",
    "La CI exécute `HYDRA_UMC_CI=1 python tools/ci_validate.py`, qui vérifie le manifeste, les documents, les huit README et les images.",
    "La CI esegue `HYDRA_UMC_CI=1 python tools/ci_validate.py`, che controlla il manifesto, i documenti, gli otto README e le immagini.",
    "CI は `HYDRA_UMC_CI=1 python tools/ci_validate.py` を実行し、マニフェスト、文書、8 つの README、図を検査します。",
    "CI 运行 `HYDRA_UMC_CI=1 python tools/ci_validate.py`，检查清单、文档、八个 README 和图片。",
    "A CI executa `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que verifica o manifesto, os documentos, os oito README e as imagens.",
)
PY_ONLY = P(
    "Requires Python 3.11 or newer; the code uses only the standard library.",
    "Requiere Python 3.11 o superior; el código usa solo la biblioteca estándar.",
    "Benötigt Python 3.11 oder neuer; der Code nutzt nur die Standardbibliothek.",
    "Nécessite Python 3.11 ou plus récent ; le code n'utilise que la bibliothèque standard.",
    "Richiede Python 3.11 o successivo; il codice usa solo la libreria standard.",
    "Python 3.11 以上が必要です。コードは標準ライブラリだけを使います。",
    "需要 Python 3.11 或更高版本；代码只使用标准库。",
    "Requer Python 3.11 ou superior; o código usa apenas a biblioteca padrão.",
)


def testing_plain(lg, n, rows):
    return TESTING_PLAIN[lg].replace("{n}", str(n)) + "\n\n" + table(lg, "tests", rows) + "\n\n" + CI_PLAIN[lg]

BUILD_GENERIC = P(
    "There is nothing to compile for a release: `build.sh` / `build.bat` create the virtual environment, install the package in editable mode and run the tests, and `build-test` only checks. Building never changes the version; it is raised only by `python tools/hydra_project_tool.py bump`, which also moves the changelog. The version of the package, the manifest and the changelog must agree, and `ci_validate.py` fails when they do not.",
    "No hay nada que compilar para publicar: `build.sh` / `build.bat` crean el entorno virtual, instalan el paquete en modo editable y ejecutan las pruebas, y `build-test` solo comprueba. Compilar nunca cambia la versión; solo la sube `python tools/hydra_project_tool.py bump`, que también mueve el registro de cambios. La versión del paquete, la del manifiesto y la del registro de cambios deben coincidir, y `ci_validate.py` falla si no lo hacen.",
    "Für eine Veröffentlichung gibt es nichts zu kompilieren: `build.sh` / `build.bat` legen die virtuelle Umgebung an, installieren das Paket im editierbaren Modus und führen die Tests aus, `build-test` prüft nur. Bauen ändert nie die Version; sie wird nur von `python tools/hydra_project_tool.py bump` erhöht, das auch das Änderungsprotokoll fortschreibt. Die Version von Paket, Manifest und Änderungsprotokoll muss übereinstimmen, sonst schlägt `ci_validate.py` fehl.",
    "Il n'y a rien à compiler pour une publication : `build.sh` / `build.bat` créent l'environnement virtuel, installent le paquet en mode éditable et lancent les tests, et `build-test` ne fait que vérifier. Construire ne change jamais la version ; seul `python tools/hydra_project_tool.py bump` la monte, et il fait avancer aussi le journal des modifications. La version du paquet, du manifeste et du journal doit concorder, sinon `ci_validate.py` échoue.",
    "Per un rilascio non c'è nulla da compilare: `build.sh` / `build.bat` creano l'ambiente virtuale, installano il pacchetto in modalità modificabile ed eseguono i test, e `build-test` si limita a controllare. Compilare non cambia mai la versione; la alza soltanto `python tools/hydra_project_tool.py bump`, che sposta anche il registro delle modifiche. La versione del pacchetto, del manifesto e del registro deve coincidere, altrimenti `ci_validate.py` fallisce.",
    "リリースのためにコンパイルするものはありません。`build.sh` / `build.bat` は仮想環境を作り、パッケージを編集可能モードでインストールし、テストを実行します。`build-test` は検査だけです。ビルドでバージョンが変わることはなく、上げるのは `python tools/hydra_project_tool.py bump` だけで、変更履歴も一緒に進めます。パッケージ、マニフェスト、変更履歴のバージョンは一致する必要があり、一致しなければ `ci_validate.py` が失敗します。",
    "发布无需编译：`build.sh` / `build.bat` 创建虚拟环境、以可编辑模式安装包并运行测试，`build-test` 只做检查。构建从不改变版本；只有 `python tools/hydra_project_tool.py bump` 会提升版本，并同时推进更新日志。包、清单和更新日志的版本必须一致，否则 `ci_validate.py` 会失败。",
    "Não há nada para compilar numa publicação: `build.sh` / `build.bat` criam o ambiente virtual, instalam o pacote em modo editável e executam os testes, e `build-test` apenas verifica. Compilar nunca muda a versão; só a sobe `python tools/hydra_project_tool.py bump`, que também avança o registo de alterações. A versão do pacote, do manifesto e do registo tem de coincidir, senão o `ci_validate.py` falha.",
)