# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_GATEWAY_INDUSTRIAL.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-GATEWAY-INDUSTRIAL."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🌐'
COMMENT = 'Single status surface in front of the industrial bridges'
BADGES = [('Standard', 'Industry%204.0', 'blue'), ('Security', 'TLS%20and%20mTLS%20optional%2C%20off%20by%20default', 'orange'), ('Protocols', 'OPC--UA%20%2F%20MQTT%20%2F%20MTConnect', 'orange')]
NO_UI = True

SPEC = {
    "stack": "node",
    "req": "20",
    "quick": [
        "npm install",
        "npm test",
        "npm run build",
        "npm start"
    ],
    "test_cmd": "npm test",
    "alt": "HYDRA-UMC-GATEWAY-INDUSTRIAL architecture",
    "role": {
        "en": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** is the single status surface in front of `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` and `HYDRA-UMC-MTCONNECT-ADAPTER`: it checks that each answers and accepts only an allow-listed set of commands whose effect is a reachability check. It never moves a machine.",
        "es": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** es la superficie de estado única delante de `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` y `HYDRA-UMC-MTCONNECT-ADAPTER`: comprueba que cada uno responde y acepta solo un conjunto permitido de órdenes cuyo efecto es una comprobación de alcance. Nunca mueve una máquina.",
        "de": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** ist die einzige Statusfläche vor `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` und `HYDRA-UMC-MTCONNECT-ADAPTER`: Er prüft, ob jeder antwortet, und nimmt nur freigegebene Befehle an, deren Wirkung eine Erreichbarkeitsprüfung ist. Er bewegt nie eine Maschine.",
        "fr": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** est la surface d'état unique devant `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` et `HYDRA-UMC-MTCONNECT-ADAPTER` : il vérifie que chacun répond et n'accepte qu'un ensemble autorisé de commandes dont l'effet est un test de joignabilité. Il ne déplace jamais une machine.",
        "it": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** è l'unica superficie di stato davanti a `HYDRA-UMC-OPCUA-SERVER`, `HYDRA-UMC-MQTT-BROKER` e `HYDRA-UMC-MTCONNECT-ADAPTER`: verifica che ognuno risponda e accetta solo un insieme ammesso di comandi il cui effetto è un controllo di raggiungibilità. Non muove mai una macchina.",
        "ja": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** は `HYDRA-UMC-OPCUA-SERVER`、`HYDRA-UMC-MQTT-BROKER`、`HYDRA-UMC-MTCONNECT-ADAPTER` の手前にある単一のステータス窓口です。それぞれが応答するかを確認し、効果が到達性の確認だけに限られる許可リストのコマンドしか受け付けません。機械を動かすことはありません。",
        "zh": "**HYDRA-UMC-GATEWAY-INDUSTRIAL** 是 `HYDRA-UMC-OPCUA-SERVER`、`HYDRA-UMC-MQTT-BROKER` 和 `HYDRA-UMC-MTCONNECT-ADAPTER` 前面唯一的状态窗口：它检查各自是否应答，并且只接受效果仅为可达性检查的允许列表命令。它从不移动机器。",
        "pt": "O **HYDRA-UMC-GATEWAY-INDUSTRIAL** é a superfície de estado única à frente do `HYDRA-UMC-OPCUA-SERVER`, do `HYDRA-UMC-MQTT-BROKER` e do `HYDRA-UMC-MTCONNECT-ADAPTER`: verifica se cada um responde e aceita apenas um conjunto permitido de comandos cujo efeito é uma verificação de alcance. Nunca move uma máquina."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'configuration': {'en': "The listen port is read from `HYDRA_UMC_GATEWAY_PORT` first. The shared `PORT` still works as a last resort and prints a warning, so an environment file shared by several services cannot move the gateway onto another service's port by accident; the container health check follows the same order.", 'es': 'El puerto de escucha se lee primero de `HYDRA_UMC_GATEWAY_PORT`. El `PORT` compartido sigue valiendo como último recurso y avisa por consola, de modo que un fichero de entorno compartido por varios servicios no pueda mover la pasarela al puerto de otro servicio por accidente; el control de salud del contenedor sigue el mismo orden.', 'de': 'Der Listen-Port wird zuerst aus `HYDRA_UMC_GATEWAY_PORT` gelesen. Das gemeinsame `PORT` gilt weiter als letzter Ausweg und gibt eine Warnung aus, damit eine von mehreren Diensten geteilte Umgebungsdatei das Gateway nicht versehentlich auf den Port eines anderen Dienstes verschiebt; die Health-Prüfung des Containers folgt derselben Reihenfolge.', 'fr': "Le port d'écoute est lu d'abord dans `HYDRA_UMC_GATEWAY_PORT`. Le `PORT` partagé reste valable en dernier recours et affiche un avertissement, de sorte qu'un fichier d'environnement partagé par plusieurs services ne puisse pas déplacer la passerelle sur le port d'un autre service par accident ; le contrôle de santé du conteneur suit le même ordre.", 'it': 'La porta di ascolto viene letta prima da `HYDRA_UMC_GATEWAY_PORT`. Il `PORT` condiviso vale ancora come ultima risorsa e stampa un avviso, così che un file di ambiente condiviso da più servizi non possa spostare il gateway sulla porta di un altro servizio per errore; il controllo di salute del container segue lo stesso ordine.', 'ja': '待ち受けポートは、まず `HYDRA_UMC_GATEWAY_PORT` から読み取ります。共有の `PORT` は最後の手段として引き続き使え、警告を表示します。そのため、複数のサービスで共有する環境ファイルがゲートウェイを他のサービスのポートへうっかり移すことはありません。コンテナのヘルスチェックも同じ順序に従います。', 'zh': '监听端口首先从 `HYDRA_UMC_GATEWAY_PORT` 读取。共享的 `PORT` 仍可作为最后手段并会打印警告，这样多个服务共用的环境文件就不会意外把网关移到另一个服务的端口上；容器健康检查遵循相同的顺序。', 'pt': 'A porta de escuta é lida primeiro de `HYDRA_UMC_GATEWAY_PORT`. O `PORT` partilhado continua a valer como último recurso e mostra um aviso, para que um ficheiro de ambiente partilhado por vários serviços não possa mudar o gateway para a porta de outro serviço por acidente; a verificação de saúde do contentor segue a mesma ordem.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):  # type: ignore[no-redef]
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)

_NEW_CONFIGURATION_TEXT = {
 "en": "A Modbus TCP adapter, off until `GATEWAY_MODBUS_MAP_FILE` names a declarative map of devices and registers: `POST /command` with the protocol `Modbus` reads a register by its name (`modbus:<device>/<register>`), scaled to engineering units. Writing is separate and stricter: it needs `GATEWAY_WRITES=1`, a register the map lists as writable with its own minimum and maximum, the two steps and the cell-state check of the write gate, the `admin` role in the token, and the value is read back from the device; a value that does not come back is reported as `write_unverified`, never as accepted. `GATEWAY_JOURNAL_URL` sends every order to HYDRA-UMC-DATALAKE as a queryable timeline (`GET /command/journal` lists the newest), and `GATEWAY_STATUS_STREAM=1` serves `GET /status/stream`, which pushes a change of reachability as a Server-Sent Event instead of making clients poll.",
 "es": "Un adaptador Modbus TCP, desactivado hasta que `GATEWAY_MODBUS_MAP_FILE` indique un mapa declarativo de dispositivos y registros: `POST /command` con el protocolo `Modbus` lee un registro por su nombre (`modbus:<dispositivo>/<registro>`), escalado a unidades de ingeniería. Escribir es distinto y más estricto: exige `GATEWAY_WRITES=1`, un registro que el mapa declare escribible con su propio mínimo y máximo, los dos pasos y la comprobación del estado de la celda de la puerta de escritura, el rol `admin` en el token, y el valor se lee de vuelta del dispositivo; un valor que no vuelve se notifica como `write_unverified`, nunca como aceptado. `GATEWAY_JOURNAL_URL` envía cada orden a HYDRA-UMC-DATALAKE como una línea de tiempo consultable (`GET /command/journal` lista las últimas), y `GATEWAY_STATUS_STREAM=1` sirve `GET /status/stream`, que empuja un cambio de alcanzabilidad como evento Server-Sent en vez de obligar a sondear.",
 "de": "Ein Modbus-TCP-Adapter, aus, bis `GATEWAY_MODBUS_MAP_FILE` eine deklarative Karte von Geräten und Registern nennt: `POST /command` mit dem Protokoll `Modbus` liest ein Register über seinen Namen (`modbus:<Gerät>/<Register>`), skaliert auf technische Einheiten. Schreiben ist getrennt und strenger: Es braucht `GATEWAY_WRITES=1`, ein Register, das die Karte mit eigenem Minimum und Maximum als beschreibbar führt, die zwei Schritte und die Zellenzustandsprüfung des Schreib-Gates, die Rolle `admin` im Token, und der Wert wird vom Gerät zurückgelesen; ein Wert, der nicht zurückkommt, wird als `write_unverified` gemeldet, nie als angenommen. `GATEWAY_JOURNAL_URL` sendet jeden Auftrag als abfragbare Zeitleiste an HYDRA-UMC-DATALAKE (`GET /command/journal` listet die neuesten), und `GATEWAY_STATUS_STREAM=1` liefert `GET /status/stream`, das eine Änderung der Erreichbarkeit als Server-Sent Event meldet, statt Clients pollen zu lassen.",
 "fr": "Un adaptateur Modbus TCP, désactivé tant que `GATEWAY_MODBUS_MAP_FILE` ne désigne pas une carte déclarative d'appareils et de registres : `POST /command` avec le protocole `Modbus` lit un registre par son nom (`modbus:<appareil>/<registre>`), mis à l'échelle en unités d'ingénierie. L'écriture est distincte et plus stricte : elle exige `GATEWAY_WRITES=1`, un registre que la carte déclare inscriptible avec son propre minimum et maximum, les deux étapes et le contrôle de l'état de la cellule de la porte d'écriture, le rôle `admin` dans le jeton, et la valeur est relue depuis l'appareil ; une valeur qui ne revient pas est signalée `write_unverified`, jamais acceptée. `GATEWAY_JOURNAL_URL` envoie chaque ordre à HYDRA-UMC-DATALAKE comme une chronologie interrogeable (`GET /command/journal` liste les plus récents), et `GATEWAY_STATUS_STREAM=1` sert `GET /status/stream`, qui pousse un changement d'accessibilité comme événement Server-Sent au lieu de faire scruter les clients.",
 "it": "Un adattatore Modbus TCP, disattivato finché `GATEWAY_MODBUS_MAP_FILE` non indica una mappa dichiarativa di dispositivi e registri: `POST /command` con il protocollo `Modbus` legge un registro per nome (`modbus:<dispositivo>/<registro>`), scalato in unità ingegneristiche. La scrittura è distinta e più rigida: richiede `GATEWAY_WRITES=1`, un registro che la mappa dichiara scrivibile con un proprio minimo e massimo, i due passi e il controllo dello stato della cella della porta di scrittura, il ruolo `admin` nel token, e il valore viene riletto dal dispositivo; un valore che non torna è segnalato come `write_unverified`, mai come accettato. `GATEWAY_JOURNAL_URL` invia ogni ordine a HYDRA-UMC-DATALAKE come cronologia interrogabile (`GET /command/journal` elenca i più recenti), e `GATEWAY_STATUS_STREAM=1` serve `GET /status/stream`, che spinge un cambio di raggiungibilità come evento Server-Sent invece di far fare polling ai client.",
 "ja": "Modbus TCP アダプターは、`GATEWAY_MODBUS_MAP_FILE` が機器とレジスターの宣言的なマップを指すまでオフです。プロトコル `Modbus` の `POST /command` は、名前（`modbus:<機器>/<レジスター>`）でレジスターを読み、工学単位に換算します。書き込みは別扱いでより厳格です。`GATEWAY_WRITES=1`、マップが固有の最小値・最大値付きで書き込み可能と宣言したレジスター、書き込みゲートの 2 段階とセル状態の確認、トークンの `admin` ロールが必要で、書いた値は機器から読み戻されます。戻ってこない値は受理ではなく `write_unverified` と報告されます。`GATEWAY_JOURNAL_URL` は各命令を照会可能なタイムラインとして HYDRA-UMC-DATALAKE に送り（`GET /command/journal` が最新を一覧）、`GATEWAY_STATUS_STREAM=1` は `GET /status/stream` を提供して、到達性の変化をクライアントのポーリングの代わりに Server-Sent Event で通知します。",
 "zh": "Modbus TCP 适配器在 `GATEWAY_MODBUS_MAP_FILE` 指向设备与寄存器的声明式映射之前保持关闭：协议为 `Modbus` 的 `POST /command` 按名称（`modbus:<设备>/<寄存器>`）读取寄存器，并换算为工程单位。写入是分开的，也更严格：需要 `GATEWAY_WRITES=1`、映射中声明为可写且带有各自最小值和最大值的寄存器、写入门的两个步骤和单元状态检查、令牌中的 `admin` 角色，并且写入的值会从设备读回；未能读回的值报告为 `write_unverified`，绝不算作已接受。`GATEWAY_JOURNAL_URL` 把每条指令作为可查询的时间线发送到 HYDRA-UMC-DATALAKE（`GET /command/journal` 列出最新的），`GATEWAY_STATUS_STREAM=1` 提供 `GET /status/stream`，以 Server-Sent Event 推送可达性变化，而不必让客户端轮询。",
 "pt": "Um adaptador Modbus TCP, desativado até `GATEWAY_MODBUS_MAP_FILE` indicar um mapa declarativo de dispositivos e registos: `POST /command` com o protocolo `Modbus` lê um registo pelo nome (`modbus:<dispositivo>/<registo>`), escalado para unidades de engenharia. Escrever é diferente e mais rigoroso: exige `GATEWAY_WRITES=1`, um registo que o mapa declare escrevível com o seu próprio mínimo e máximo, os dois passos e a verificação do estado da célula da porta de escrita, o papel `admin` no token, e o valor é lido de volta do dispositivo; um valor que não volta é indicado como `write_unverified`, nunca como aceite. `GATEWAY_JOURNAL_URL` envia cada ordem para o HYDRA-UMC-DATALAKE como uma cronologia consultável (`GET /command/journal` lista as mais recentes), e `GATEWAY_STATUS_STREAM=1` serve `GET /status/stream`, que empurra uma alteração de alcançabilidade como evento Server-Sent em vez de obrigar os clientes a sondar."
}
for _lg, _text in _NEW_CONFIGURATION_TEXT.items():
    ADDENDA['configuration'][_lg] = ADDENDA['configuration'].get(_lg, '') + '\n\n' + _text
