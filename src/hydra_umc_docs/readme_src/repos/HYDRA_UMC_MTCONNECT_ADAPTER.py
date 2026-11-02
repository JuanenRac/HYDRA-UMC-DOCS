# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_MTCONNECT_ADAPTER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-MTCONNECT-ADAPTER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🏭'
COMMENT = 'MTConnect probe/current/sample endpoints'
BADGES = [('Standard', 'MTConnect', 'blue'), ('Format', 'XML%20%2F%20HTTP', 'orange')]
NO_UI = True

SPEC = {
    "stack": "node",
    "req": "20",
    "quick": [
        "npm install",
        "npm test",
        "npm run build",
        "npm start",
        "curl http://127.0.0.1:5000/probe"
    ],
    "test_cmd": "npm test",
    "alt": "HYDRA-UMC-MTCONNECT-ADAPTER architecture",
    "role": {
        "en": "**HYDRA-UMC-MTCONNECT-ADAPTER** shows the robots to factory monitoring software as MTConnect devices: read-only XML over HTTP (`/probe`, `/current`, `/sample`), fed from `HYDRA-UMC-SERVER`. It sends no command to any machine.",
        "es": "**HYDRA-UMC-MTCONNECT-ADAPTER** muestra los robots al software de supervisión de fábrica como dispositivos MTConnect: XML de solo lectura sobre HTTP (`/probe`, `/current`, `/sample`), alimentado desde `HYDRA-UMC-SERVER`. No envía ninguna orden a ninguna máquina.",
        "de": "**HYDRA-UMC-MTCONNECT-ADAPTER** zeigt die Roboter der Fabrik-Überwachungssoftware als MTConnect-Geräte: XML nur lesend über HTTP (`/probe`, `/current`, `/sample`), gespeist aus `HYDRA-UMC-SERVER`. Er sendet keinen Befehl an eine Maschine.",
        "fr": "**HYDRA-UMC-MTCONNECT-ADAPTER** présente les robots aux logiciels de supervision d'usine comme des appareils MTConnect : du XML en lecture seule sur HTTP (`/probe`, `/current`, `/sample`), alimenté depuis `HYDRA-UMC-SERVER`. Il n'envoie aucune commande à aucune machine.",
        "it": "**HYDRA-UMC-MTCONNECT-ADAPTER** mostra i robot al software di monitoraggio di fabbrica come dispositivi MTConnect: XML in sola lettura su HTTP (`/probe`, `/current`, `/sample`), alimentato da `HYDRA-UMC-SERVER`. Non invia alcun comando ad alcuna macchina.",
        "ja": "**HYDRA-UMC-MTCONNECT-ADAPTER** は、工場の監視ソフトウェアに対してロボットを MTConnect デバイスとして見せます。`HYDRA-UMC-SERVER` から取得した状態を、読み取り専用の XML over HTTP（`/probe`、`/current`、`/sample`）で提供します。どの機械にもコマンドを送りません。",
        "zh": "**HYDRA-UMC-MTCONNECT-ADAPTER** 把机器人以 MTConnect 设备的形式呈现给工厂监控软件：通过 HTTP 提供只读 XML（`/probe`、`/current`、`/sample`），数据来自 `HYDRA-UMC-SERVER`。它不会向任何机器发送命令。",
        "pt": "O **HYDRA-UMC-MTCONNECT-ADAPTER** mostra os robôs ao software de monitorização de fábrica como dispositivos MTConnect: XML só de leitura sobre HTTP (`/probe`, `/current`, `/sample`), alimentado a partir do `HYDRA-UMC-SERVER`. Não envia nenhum comando a nenhuma máquina."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'configuration': {'en': "The listen port is read from `HYDRA_UMC_MTCONNECT_PORT` first (5000 by default). The shared `PORT` still works as a last resort and prints a warning, so an environment file shared by several services cannot move the agent onto another service's port by accident; a value that is set but is not a valid port stops the start, and the container health check follows the same order.", 'es': 'El puerto de escucha se lee primero de `HYDRA_UMC_MTCONNECT_PORT` (5000 por defecto). El `PORT` compartido sigue valiendo como último recurso y avisa por consola, de modo que un fichero de entorno compartido por varios servicios no pueda mover el agente al puerto de otro servicio por accidente; un valor definido pero que no es un puerto válido detiene el arranque, y el control de salud del contenedor sigue el mismo orden.', 'de': 'Der Listen-Port wird zuerst aus `HYDRA_UMC_MTCONNECT_PORT` gelesen (standardmäßig 5000). Das gemeinsame `PORT` gilt weiter als letzter Ausweg und gibt eine Warnung aus, damit eine von mehreren Diensten geteilte Umgebungsdatei den Agenten nicht versehentlich auf den Port eines anderen Dienstes verschiebt; ein gesetzter, aber ungültiger Port stoppt den Start, und die Health-Prüfung des Containers folgt derselben Reihenfolge.', 'fr': "Le port d'écoute est lu d'abord dans `HYDRA_UMC_MTCONNECT_PORT` (5000 par défaut). Le `PORT` partagé reste valable en dernier recours et affiche un avertissement, de sorte qu'un fichier d'environnement partagé par plusieurs services ne puisse pas déplacer l'agent sur le port d'un autre service par accident ; une valeur définie mais qui n'est pas un port valide arrête le démarrage, et le contrôle de santé du conteneur suit le même ordre.", 'it': "La porta di ascolto viene letta prima da `HYDRA_UMC_MTCONNECT_PORT` (5000 per impostazione predefinita). Il `PORT` condiviso vale ancora come ultima risorsa e stampa un avviso, così che un file di ambiente condiviso da più servizi non possa spostare l'agente sulla porta di un altro servizio per errore; un valore impostato ma non valido come porta ferma l'avvio, e il controllo di salute del container segue lo stesso ordine.", 'ja': '待ち受けポートは、まず `HYDRA_UMC_MTCONNECT_PORT` から読み取ります（既定は 5000）。共有の `PORT` は最後の手段として引き続き使え、警告を表示します。そのため、複数のサービスで共有する環境ファイルがエージェントを他のサービスのポートへうっかり移すことはありません。設定されていても有効なポートでない値は起動を止め、コンテナのヘルスチェックも同じ順序に従います。', 'zh': '监听端口首先从 `HYDRA_UMC_MTCONNECT_PORT` 读取（默认 5000）。共享的 `PORT` 仍可作为最后手段并会打印警告，这样多个服务共用的环境文件就不会意外把代理移到另一个服务的端口上；已设置但不是有效端口的值会终止启动，容器健康检查遵循相同的顺序。', 'pt': 'A porta de escuta é lida primeiro de `HYDRA_UMC_MTCONNECT_PORT` (5000 por predefinição). O `PORT` partilhado continua a valer como último recurso e mostra um aviso, para que um ficheiro de ambiente partilhado por vários serviços não possa mudar o agente para a porta de outro serviço por acidente; um valor definido mas que não é uma porta válida interrompe o arranque, e a verificação de saúde do contentor segue a mesma ordem.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):  # type: ignore[no-redef]
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)

_NEW_CONFIGURATION_TEXT = {
 "en": "`HYDRA_UMC_MTCONNECT_SHDR_PORT` (7878 is the usual port) serves the same observations as SHDR to an agent such as cppagent. Two more sources, each off until its address is set: `HYDRA_UMC_MTCONNECT_JOBS_URL` (HYDRA-UMC-JOB-DISPATCHER, with `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`) feeds `PartCount` (the jobs it finished) and `Program` (the job on a robot now), and `HYDRA_UMC_MTCONNECT_FAULTS_URL` (with `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`) feeds two conditions, `mcu_condition` and `urtc_condition`, from the active faults of the controllers and of the tool heads. A feed that is down turns only its own DataItems UNAVAILABLE, and the two sources serve the single device `HydraNode_1` (they are refused together with one Device per robot). `docs/adapter-manifest.json` describes this adapter for the connector hub.",
 "es": "`HYDRA_UMC_MTCONNECT_SHDR_PORT` (7878 es el puerto habitual) sirve las mismas observaciones como SHDR a un agente como cppagent. Dos fuentes más, cada una desactivada hasta que se indique su dirección: `HYDRA_UMC_MTCONNECT_JOBS_URL` (HYDRA-UMC-JOB-DISPATCHER, con `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`) alimenta `PartCount` (los trabajos que terminó) y `Program` (el trabajo que un robot tiene ahora), y `HYDRA_UMC_MTCONNECT_FAULTS_URL` (con `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`) alimenta dos condiciones, `mcu_condition` y `urtc_condition`, con los fallos activos de los controladores y de los cabezales. Una fuente caída pone en UNAVAILABLE solo sus propios DataItems, y las dos fuentes sirven el dispositivo único `HydraNode_1` (se rechazan junto con un Device por robot). `docs/adapter-manifest.json` describe este adaptador para el hub de conectores.",
 "de": "`HYDRA_UMC_MTCONNECT_SHDR_PORT` (7878 ist der übliche Port) liefert dieselben Beobachtungen als SHDR an einen Agenten wie cppagent. Zwei weitere Quellen, jede aus, bis ihre Adresse gesetzt ist: `HYDRA_UMC_MTCONNECT_JOBS_URL` (HYDRA-UMC-JOB-DISPATCHER, mit `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`) speist `PartCount` (die abgeschlossenen Aufträge) und `Program` (den Auftrag, an dem ein Roboter gerade arbeitet), und `HYDRA_UMC_MTCONNECT_FAULTS_URL` (mit `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`) speist zwei Conditions, `mcu_condition` und `urtc_condition`, aus den aktiven Fehlern der Steuerungen und der Werkzeugköpfe. Eine ausgefallene Quelle setzt nur ihre eigenen DataItems auf UNAVAILABLE, und beide Quellen bedienen das einzelne Gerät `HydraNode_1` (zusammen mit einem Device je Roboter werden sie abgelehnt). `docs/adapter-manifest.json` beschreibt diesen Adapter für den Connector-Hub.",
 "fr": "`HYDRA_UMC_MTCONNECT_SHDR_PORT` (7878 est le port habituel) sert les mêmes observations en SHDR à un agent tel que cppagent. Deux sources de plus, chacune désactivée tant que son adresse n'est pas donnée : `HYDRA_UMC_MTCONNECT_JOBS_URL` (HYDRA-UMC-JOB-DISPATCHER, avec `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`) alimente `PartCount` (les travaux terminés) et `Program` (le travail en cours sur un robot), et `HYDRA_UMC_MTCONNECT_FAULTS_URL` (avec `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`) alimente deux conditions, `mcu_condition` et `urtc_condition`, à partir des défauts actifs des contrôleurs et des têtes d'outil. Une source en panne ne rend UNAVAILABLE que ses propres DataItems, et les deux sources servent l'appareil unique `HydraNode_1` (elles sont refusées avec un Device par robot). `docs/adapter-manifest.json` décrit cet adaptateur pour le hub de connecteurs.",
 "it": "`HYDRA_UMC_MTCONNECT_SHDR_PORT` (7878 è la porta abituale) serve le stesse osservazioni come SHDR a un agente come cppagent. Altre due fonti, ciascuna disattivata finché non si imposta il suo indirizzo: `HYDRA_UMC_MTCONNECT_JOBS_URL` (HYDRA-UMC-JOB-DISPATCHER, con `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`) alimenta `PartCount` (i lavori terminati) e `Program` (il lavoro in corso su un robot), e `HYDRA_UMC_MTCONNECT_FAULTS_URL` (con `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`) alimenta due condizioni, `mcu_condition` e `urtc_condition`, dai guasti attivi dei controller e delle teste utensile. Una fonte non raggiungibile rende UNAVAILABLE solo i propri DataItem, e le due fonti servono il dispositivo unico `HydraNode_1` (sono rifiutate insieme a un Device per robot). `docs/adapter-manifest.json` descrive questo adattatore per l'hub dei connettori.",
 "ja": "`HYDRA_UMC_MTCONNECT_SHDR_PORT`（通常は 7878）を設定すると、同じ観測値を cppagent などのエージェントへ SHDR として提供します。さらに二つの情報源があり、それぞれアドレスを設定するまでオフです。`HYDRA_UMC_MTCONNECT_JOBS_URL`（HYDRA-UMC-JOB-DISPATCHER、`HYDRA_UMC_MTCONNECT_JOBS_TOKEN` と併用）は `PartCount`（完了したジョブ数）と `Program`（ロボットが今実行中のジョブ）を、`HYDRA_UMC_MTCONNECT_FAULTS_URL`（`HYDRA_UMC_MTCONNECT_FAULTS_TOKEN` と併用）はコントローラーとツールヘッドの有効な故障から二つのコンディション `mcu_condition` と `urtc_condition` を供給します。停止した情報源は自分の DataItem だけを UNAVAILABLE にし、二つの情報源は単一デバイス `HydraNode_1` を対象とします（ロボットごとの Device とは併用できません）。`docs/adapter-manifest.json` はこのアダプターをコネクターハブ向けに記述します。",
 "zh": "`HYDRA_UMC_MTCONNECT_SHDR_PORT`（常用端口为 7878）以 SHDR 向 cppagent 之类的代理提供相同的观测数据。另有两个数据源，各自在设置地址之前保持关闭：`HYDRA_UMC_MTCONNECT_JOBS_URL`（HYDRA-UMC-JOB-DISPATCHER，配合 `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`）提供 `PartCount`（已完成的作业数）和 `Program`（机器人当前执行的作业），`HYDRA_UMC_MTCONNECT_FAULTS_URL`（配合 `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`）根据控制器和工具头的活动故障提供两个状态 `mcu_condition` 和 `urtc_condition`。停止的数据源只会让它自己的 DataItem 变为 UNAVAILABLE，且这两个数据源服务于单一设备 `HydraNode_1`（与每个机器人一个 Device 的模式同时使用会被拒绝）。`docs/adapter-manifest.json` 为连接器中心描述该适配器。",
 "pt": "`HYDRA_UMC_MTCONNECT_SHDR_PORT` (7878 é a porta habitual) serve as mesmas observações em SHDR a um agente como o cppagent. Mais duas fontes, cada uma desativada até o seu endereço ser definido: `HYDRA_UMC_MTCONNECT_JOBS_URL` (HYDRA-UMC-JOB-DISPATCHER, com `HYDRA_UMC_MTCONNECT_JOBS_TOKEN`) alimenta `PartCount` (os trabalhos terminados) e `Program` (o trabalho que um robô tem agora), e `HYDRA_UMC_MTCONNECT_FAULTS_URL` (com `HYDRA_UMC_MTCONNECT_FAULTS_TOKEN`) alimenta duas condições, `mcu_condition` e `urtc_condition`, com as falhas ativas dos controladores e das cabeças de ferramenta. Uma fonte em baixo põe UNAVAILABLE apenas os seus DataItems, e as duas fontes servem o dispositivo único `HydraNode_1` (são recusadas junto com um Device por robô). `docs/adapter-manifest.json` descreve este adaptador para o hub de conectores."
}
for _lg, _text in _NEW_CONFIGURATION_TEXT.items():
    ADDENDA['configuration'][_lg] = ADDENDA['configuration'].get(_lg, '') + '\n\n' + _text
