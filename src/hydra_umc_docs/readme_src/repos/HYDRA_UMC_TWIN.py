# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_TWIN.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-TWIN."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🪞'
COMMENT = 'Digital Twin integration hub'
BADGES = [('\x01', 'Rust', 'orange'), ('Feature', 'HIL%20Ready', 'green'), ('Stage', 'Functional%20v0', 'yellow')]
NO_UI = True

SPEC = {
    "stack": "rust",
    "req": "2021",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh family-status",
        "./run.sh family-sync",
        "./run.sh serve --port 8111",
        "./run.sh keygen --key-file twin.key"
    ],
    "test_cmd": "cargo test",
    "alt": "HYDRA-UMC-TWIN architecture",
    "role": {
        "en": "**HYDRA-UMC-TWIN** is the integration parent of the Digital Twin family. It reads the manifests of its three children, reports whether the family is ready and in step, probes their health, and signs interlock certificates that tell the hardware-in-the-loop bridge a risk report came from the twin. The physics engine itself is still planned.",
        "es": "**HYDRA-UMC-TWIN** es el padre de integración de la familia Digital Twin. Lee los manifiestos de sus tres hijos, informa de si la familia está lista y sincronizada, comprueba su salud y firma certificados de interbloqueo que indican al puente hardware-in-the-loop que un informe de riesgo procede del gemelo. El motor de física sigue previsto.",
        "de": "**HYDRA-UMC-TWIN** ist der Integrationsknoten der Digital-Twin-Familie. Er liest die Manifeste seiner drei Kinder, meldet, ob die Familie bereit und im Gleichschritt ist, prüft deren Gesundheit und signiert Interlock-Zertifikate, die der Hardware-in-the-Loop-Brücke sagen, dass ein Risikobericht vom Twin stammt. Die Physik-Engine selbst ist noch geplant.",
        "fr": "**HYDRA-UMC-TWIN** est le parent d'intégration de la famille Digital Twin. Il lit les manifestes de ses trois enfants, indique si la famille est prête et en phase, sonde leur santé et signe des certificats d'interverrouillage qui disent au pont hardware-in-the-loop qu'un rapport de risque vient du jumeau. Le moteur physique lui-même reste prévu.",
        "it": "**HYDRA-UMC-TWIN** è il genitore di integrazione della famiglia Digital Twin. Legge i manifesti dei suoi tre figli, indica se la famiglia è pronta e allineata, ne verifica lo stato di salute e firma certificati di interblocco che dicono al ponte hardware-in-the-loop che un rapporto di rischio proviene dal gemello. Il motore fisico vero e proprio è ancora previsto.",
        "ja": "**HYDRA-UMC-TWIN** は Digital Twin ファミリーの統合の親です。3 つの子のマニフェストを読み、ファミリーが準備できて揃っているかを報告し、その健全性を確認し、リスクレポートがツインから来たことをハードウェア・イン・ザ・ループのブリッジに伝えるインターロック証明書に署名します。物理エンジン自体は計画中です。",
        "zh": "**HYDRA-UMC-TWIN** 是 Digital Twin 系列的集成父项目。它读取三个子项目的清单，报告系列是否就绪且同步，探测其健康状况，并签署互锁证书，告诉硬件在环桥接某份风险报告来自孪生体。物理引擎本身仍在计划中。",
        "pt": "O **HYDRA-UMC-TWIN** é o pai de integração da família Digital Twin. Lê os manifestos dos seus três filhos, indica se a família está pronta e em sintonia, verifica a sua saúde e assina certificados de interbloqueio que dizem à ponte hardware-in-the-loop que um relatório de risco veio do gémeo. O motor de física em si continua previsto."
    }
}


from ... import readme_kit as K

EXTRAS = {'security': {'rows': [[{'en': 'A report of risk written by the one who wants the robot to move', 'es': 'Un informe de riesgo escrito por quien quiere que el robot se mueva', 'de': 'Ein Risikobericht, geschrieben von dem, der den Roboter bewegen will', 'fr': 'Un rapport de risque écrit par celui qui veut faire bouger le robot', 'it': 'Un rapporto di rischio scritto da chi vuole muovere il robot', 'ja': 'ロボットを動かしたい本人が書いたリスクレポート', 'zh': '由想让机器人动起来的人自己写的风险报告', 'pt': 'Um relatório de risco escrito por quem quer que o robô se mova'}, {'en': "The report travels as a certificate signed with the twin's Ed25519 key; the bridge holds only the public half, so nobody who can reach it can mint one", 'es': 'El informe viaja como un certificado firmado con la clave Ed25519 del gemelo; el puente solo tiene la mitad pública, así que nadie que lo alcance puede fabricar uno', 'de': 'Der Bericht reist als Zertifikat, signiert mit dem Ed25519-Schlüssel des Twins; die Brücke hält nur den öffentlichen Teil, wer sie erreicht, kann also keines ausstellen', 'fr': "Le rapport voyage comme un certificat signé avec la clé Ed25519 du jumeau ; le pont n'a que la moitié publique, donc personne qui l'atteint ne peut en fabriquer un", 'it': 'Il rapporto viaggia come certificato firmato con la chiave Ed25519 del gemello; il ponte ha solo la metà pubblica, quindi nessuno che lo raggiunga può crearne uno', 'ja': 'レポートはツインの Ed25519 鍵で署名された証明書として運ばれます。ブリッジは公開鍵だけを持つため、到達できる人でも証明書は作れません', 'zh': '报告以孪生体的 Ed25519 密钥签名的证书形式传递；桥接只持有公钥，因此能访问它的人也无法伪造证书', 'pt': 'O relatório viaja como um certificado assinado com a chave Ed25519 do gémeo; a ponte só tem a metade pública, por isso quem lhe chega não pode fabricar um'}, '`src/certificate.rs`, `docs/INTERLOCK_CERTIFICATE.md`'], [{'en': 'Anyone asking the twin to sign', 'es': 'Cualquiera pidiendo al gemelo que firme', 'de': 'Jeder, der den Twin um eine Signatur bittet', 'fr': "N'importe qui demandant au jumeau de signer", 'it': 'Chiunque chieda al gemello di firmare', 'ja': '誰でもツインに署名を依頼できてしまう', 'zh': '任何人都可以要求孪生体签名', 'pt': 'Qualquer pessoa a pedir ao gémeo que assine'}, {'en': '`POST /interlock/certify` exists only when the twin starts with a signing key and a certify token; its body is limited to 4 KiB and `keygen` never overwrites a file and writes it with mode 0600 on Unix', 'es': '`POST /interlock/certify` existe solo si el gemelo arranca con una clave de firma y un token de certificación; su cuerpo se limita a 4 KiB y `keygen` nunca sobrescribe un fichero y lo escribe con modo 0600 en Unix', 'de': '`POST /interlock/certify` gibt es nur, wenn der Twin mit Signaturschlüssel und Zertifizierungs-Token startet; sein Body ist auf 4 KiB begrenzt und `keygen` überschreibt nie eine Datei und schreibt sie unter Unix mit Modus 0600', 'fr': "`POST /interlock/certify` n'existe que si le jumeau démarre avec une clé de signature et un jeton de certification ; son corps est limité à 4 KiB et `keygen` n'écrase jamais un fichier et l'écrit en mode 0600 sous Unix", 'it': '`POST /interlock/certify` esiste solo se il gemello parte con una chiave di firma e un token di certificazione; il suo corpo è limitato a 4 KiB e `keygen` non sovrascrive mai un file e lo scrive con modo 0600 su Unix', 'ja': '`POST /interlock/certify` は、署名鍵と認証トークンを付けてツインを起動したときにだけ存在します。本文は 4 KiB までで、`keygen` はファイルを上書きせず、Unix ではモード 0600 で書きます', 'zh': '只有孪生体带着签名密钥和认证令牌启动时才存在 `POST /interlock/certify`；其请求体限制为 4 KiB，`keygen` 从不覆盖文件，在 Unix 上以 0600 权限写入', 'pt': '`POST /interlock/certify` só existe quando o gémeo arranca com uma chave de assinatura e um token de certificação; o seu corpo está limitado a 4 KiB e `keygen` nunca sobrescreve um ficheiro e escreve-o com modo 0600 em Unix'}, '`src/server.rs`, `src/main.rs`']], 'never': {'en': '**What it never does:** simulate physics yet. Until the engine exists, the twin signs the report of the caller that holds the certify token, so a certificate is as good as the source of the report.', 'es': '**Lo que nunca hace:** simular física todavía. Hasta que exista el motor, el gemelo firma el informe de quien tiene el token de certificación, así que un certificado vale lo que valga la fuente del informe.', 'de': '**Was er nie tut:** Physik simulieren, noch nicht. Bis die Engine existiert, signiert der Twin den Bericht des Aufrufers mit Zertifizierungs-Token; ein Zertifikat ist also so gut wie die Quelle des Berichts.', 'fr': "**Ce qu'il ne fait jamais :** simuler la physique, pas encore. Tant que le moteur n'existe pas, le jumeau signe le rapport de l'appelant qui détient le jeton de certification ; un certificat vaut donc ce que vaut la source du rapport.", 'it': '**Cosa non fa mai:** simulare la fisica, per ora. Finché il motore non esiste, il gemello firma il rapporto di chi ha il token di certificazione; un certificato vale quanto la fonte del rapporto.', 'ja': '**まだしないこと：** 物理シミュレーション。エンジンができるまで、ツインは認証トークンを持つ呼び出し側のレポートに署名するため、証明書の信頼性はレポートの出どころ次第です。', 'zh': '**目前不做的事：** 物理仿真。在引擎出现之前，孪生体为持有认证令牌的调用方的报告签名，因此证书的可信度取决于报告的来源。', 'pt': '**O que ainda não faz:** simular física. Até o motor existir, o gémeo assina o relatório de quem tem o token de certificação, por isso um certificado vale o que vale a fonte do relatório.'}}, 'configuration': {'rows': [['`--addr`', '`127.0.0.1`', {'en': 'address of the HTTP API', 'es': 'dirección de la API HTTP', 'de': 'Adresse der HTTP-API', 'fr': "adresse de l'API HTTP", 'it': "indirizzo dell'API HTTP", 'ja': 'HTTP API のアドレス', 'zh': 'HTTP API 的地址', 'pt': 'endereço da API HTTP'}], ['`--port`', '`8111`', {'en': 'port of the HTTP API', 'es': 'puerto de la API HTTP', 'de': 'Port der HTTP-API', 'fr': "port de l'API HTTP", 'it': "porta dell'API HTTP", 'ja': 'HTTP API のポート', 'zh': 'HTTP API 的端口', 'pt': 'porta da API HTTP'}], ['`--workspace`', {'en': 'the folder that holds this repository', 'es': 'la carpeta que contiene este repositorio', 'de': 'der Ordner, der dieses Repository enthält', 'fr': 'le dossier qui contient ce dépôt', 'it': 'la cartella che contiene questo repository', 'ja': 'このリポジトリを含むフォルダー', 'zh': '包含本仓库的文件夹', 'pt': 'a pasta que contém este repositório'}, {'en': 'where the sibling repositories are looked for', 'es': 'dónde se buscan los repositorios hermanos', 'de': 'wo die Geschwister-Repositories gesucht werden', 'fr': "où l'on cherche les dépôts frères", 'it': 'dove si cercano i repository fratelli', 'ja': '兄弟リポジトリを探す場所', 'zh': '在哪里查找同级仓库', 'pt': 'onde se procuram os repositórios irmãos'}], ['`--physics-replica-bin` / `HYDRA_UMC_TWIN_PHYSICS_REPLICA_BIN`', {'en': 'none', 'es': 'ninguno', 'de': 'keiner', 'fr': 'aucun', 'it': 'nessuno', 'ja': 'なし', 'zh': '无', 'pt': 'nenhum'}, {'en': 'binary of the physics replica that the health check starts', 'es': 'binario de la réplica de física que arranca la comprobación de salud', 'de': 'Binärdatei des Physik-Replikats, die die Gesundheitsprüfung startet', 'fr': 'binaire de la réplique physique que lance la vérification de santé', 'it': 'binario della replica fisica avviato dal controllo di salute', 'ja': 'ヘルスチェックが起動する物理レプリカのバイナリ', 'zh': '健康检查所启动的物理副本的可执行文件', 'pt': 'binário da réplica de física que a verificação de saúde arranca'}], ['`--hil-bridge-addr` / `HYDRA_UMC_TWIN_HIL_ADDR`', {'en': 'none', 'es': 'ninguno', 'de': 'keiner', 'fr': 'aucun', 'it': 'nessuno', 'ja': 'なし', 'zh': '无', 'pt': 'nenhum'}, {'en': 'host:port of the hardware-in-the-loop bridge to probe', 'es': 'host:puerto del puente hardware-in-the-loop que se sondea', 'de': 'Host:Port der Hardware-in-the-Loop-Brücke, die geprüft wird', 'fr': 'hôte:port du pont hardware-in-the-loop sondé', 'it': 'host:porta del ponte hardware-in-the-loop sondato', 'ja': '確認する HIL ブリッジの host:port', 'zh': '要探测的硬件在环桥接的 主机:端口', 'pt': 'host:porta da ponte hardware-in-the-loop sondada'}], ['`--timeout-ms`', '`5000`', {'en': 'time allowed to each health probe', 'es': 'tiempo que se concede a cada sondeo de salud', 'de': 'Zeit, die jede Gesundheitsprüfung hat', 'fr': 'temps accordé à chaque sonde de santé', 'it': 'tempo concesso a ogni sonda di salute', 'ja': '各ヘルス確認に与える時間', 'zh': '每次健康探测允许的时间', 'pt': 'tempo concedido a cada sonda de saúde'}], ['`--signing-key-file` / `HYDRA_UMC_TWIN_SIGNING_KEY_FILE`', {'en': 'none', 'es': 'ninguno', 'de': 'keiner', 'fr': 'aucun', 'it': 'nessuno', 'ja': 'なし', 'zh': '无', 'pt': 'nenhum'}, {'en': 'Ed25519 key that turns on certificate signing', 'es': 'clave Ed25519 que activa la firma de certificados', 'de': 'Ed25519-Schlüssel, der das Signieren von Zertifikaten einschaltet', 'fr': 'clé Ed25519 qui active la signature de certificats', 'it': 'chiave Ed25519 che attiva la firma dei certificati', 'ja': '証明書の署名を有効にする Ed25519 鍵', 'zh': '启用证书签名的 Ed25519 密钥', 'pt': 'chave Ed25519 que ativa a assinatura de certificados'}], ['`--certify-token-file` / `HYDRA_UMC_TWIN_CERTIFY_TOKEN`', {'en': 'none', 'es': 'ninguno', 'de': 'keiner', 'fr': 'aucun', 'it': 'nessuno', 'ja': 'なし', 'zh': '无', 'pt': 'nenhum'}, {'en': 'token that `POST /interlock/certify` requires', 'es': 'token que exige `POST /interlock/certify`', 'de': 'Token, den `POST /interlock/certify` verlangt', 'fr': 'jeton exigé par `POST /interlock/certify`', 'it': 'token richiesto da `POST /interlock/certify`', 'ja': '`POST /interlock/certify` が要求するトークン', 'zh': '`POST /interlock/certify` 所需的令牌', 'pt': 'token exigido por `POST /interlock/certify`'}]]}}


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

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'security': {'en': 'The `?workspace=` override of the HTTP API is bounded by default to the served workspace, so a request cannot make the API probe other directories of the machine; `--strict-workspace-root PATH` picks another root and `--allow-any-workspace` brings back the earlier, unbounded behaviour.', 'es': 'El parámetro `?workspace=` de la API HTTP queda acotado por defecto al espacio de trabajo servido, de modo que una petición no puede hacer que la API examine otros directorios de la máquina; `--strict-workspace-root RUTA` elige otra raíz y `--allow-any-workspace` recupera el comportamiento anterior, sin límite.', 'de': 'Die Überschreibung `?workspace=` der HTTP-API ist standardmäßig auf den bereitgestellten Arbeitsbereich begrenzt, sodass eine Anfrage die API nicht andere Verzeichnisse des Rechners untersuchen lassen kann; `--strict-workspace-root PFAD` wählt eine andere Wurzel, und `--allow-any-workspace` bringt das frühere, unbegrenzte Verhalten zurück.', 'fr': "Le paramètre `?workspace=` de l'API HTTP est limité par défaut à l'espace de travail servi, de sorte qu'une requête ne puisse pas faire explorer à l'API d'autres répertoires de la machine ; `--strict-workspace-root CHEMIN` choisit une autre racine et `--allow-any-workspace` rétablit l'ancien comportement, sans limite.", 'it': "Il parametro `?workspace=` dell'API HTTP è limitato per impostazione predefinita all'area di lavoro servita, così che una richiesta non possa far esaminare all'API altre directory della macchina; `--strict-workspace-root PERCORSO` sceglie un'altra radice e `--allow-any-workspace` ripristina il comportamento precedente, senza limiti.", 'ja': 'HTTP API の `?workspace=` による上書きは、既定では配信中のワークスペースに限定されるため、リクエストによって API がマシン上の他のディレクトリを調べることはできません。`--strict-workspace-root PATH` で別のルートを選べ、`--allow-any-workspace` で以前の無制限の動作に戻せます。', 'zh': 'HTTP API 的 `?workspace=` 覆盖默认限制在所提供的工作区内，因此请求无法让 API 探查机器上的其他目录；`--strict-workspace-root 路径` 可选择另一个根目录，`--allow-any-workspace` 则恢复之前不受限制的行为。', 'pt': 'O parâmetro `?workspace=` da API HTTP fica limitado por predefinição ao espaço de trabalho servido, pelo que um pedido não pode fazer a API examinar outras pastas da máquina; `--strict-workspace-root CAMINHO` escolhe outra raiz e `--allow-any-workspace` repõe o comportamento anterior, sem limite.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):  # type: ignore[no-redef]
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
