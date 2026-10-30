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


def BODY(lg, ctx):
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
