# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_OPCUA_SERVER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-OPCUA-SERVER."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🏭'
COMMENT = 'OPC-UA address space of the robot roster'
BADGES = [('Standard', 'OPC--UA', 'orange'), ('Feature', 'Address%20Space%20Modeling', 'blue')]
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
    "alt": "HYDRA-UMC-OPCUA-SERVER architecture",
    "role": {
        "en": "**HYDRA-UMC-OPCUA-SERVER** publishes the robot roster of `HYDRA-UMC-SERVER` as an OPC-UA address space that SCADA and automation software can browse. Sessions carry OPC UA roles and no role may write: no node controls a joint or an effector.",
        "es": "**HYDRA-UMC-OPCUA-SERVER** publica la lista de robots de `HYDRA-UMC-SERVER` como un espacio de direcciones OPC-UA que el software SCADA y de automatización puede explorar. Las sesiones llevan roles OPC UA y ningún rol puede escribir: ningún nodo controla una articulación ni un efector.",
        "de": "**HYDRA-UMC-OPCUA-SERVER** veröffentlicht die Roboterliste von `HYDRA-UMC-SERVER` als OPC-UA-Adressraum, den SCADA- und Automatisierungssoftware durchsuchen kann. Sitzungen tragen OPC-UA-Rollen, und keine Rolle darf schreiben: Kein Knoten steuert ein Gelenk oder einen Effektor.",
        "fr": "**HYDRA-UMC-OPCUA-SERVER** publie la liste des robots de `HYDRA-UMC-SERVER` comme un espace d'adressage OPC-UA que les logiciels SCADA et d'automatisation peuvent parcourir. Les sessions portent des rôles OPC UA et aucun rôle ne peut écrire : aucun nœud ne commande une articulation ni un effecteur.",
        "it": "**HYDRA-UMC-OPCUA-SERVER** pubblica l'elenco dei robot di `HYDRA-UMC-SERVER` come spazio di indirizzi OPC-UA che il software SCADA e di automazione può esplorare. Le sessioni portano ruoli OPC UA e nessun ruolo può scrivere: nessun nodo controlla un giunto o un effettore.",
        "ja": "**HYDRA-UMC-OPCUA-SERVER** は `HYDRA-UMC-SERVER` のロボット一覧を、SCADA やオートメーションのソフトウェアが閲覧できる OPC-UA アドレス空間として公開します。セッションは OPC UA のロールを持ち、書き込みできるロールはありません。関節やエンドエフェクターを制御するノードはありません。",
        "zh": "**HYDRA-UMC-OPCUA-SERVER** 把 `HYDRA-UMC-SERVER` 的机器人列表发布为 OPC-UA 地址空间，供 SCADA 和自动化软件浏览。会话带有 OPC UA 角色，任何角色都不能写入：没有任何节点控制关节或末端执行器。",
        "pt": "O **HYDRA-UMC-OPCUA-SERVER** publica a lista de robôs do `HYDRA-UMC-SERVER` como um espaço de endereços OPC-UA que o software SCADA e de automação pode explorar. As sessões trazem funções OPC UA e nenhuma função pode escrever: nenhum nó controla uma articulação nem um efetor."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'configuration': {'en': "The listen port is read from `HYDRA_UMC_OPCUA_PORT` first (4840 by default). The shared `PORT` still works as a last resort and prints a warning, so an environment file shared by several services cannot move the server onto another service's port by accident; a value that is set but is not a valid port stops the start, and the container health check follows the same order.", 'es': 'El puerto de escucha se lee primero de `HYDRA_UMC_OPCUA_PORT` (4840 por defecto). El `PORT` compartido sigue valiendo como último recurso y avisa por consola, de modo que un fichero de entorno compartido por varios servicios no pueda mover el servidor al puerto de otro servicio por accidente; un valor definido pero que no es un puerto válido detiene el arranque, y el control de salud del contenedor sigue el mismo orden.', 'de': 'Der Listen-Port wird zuerst aus `HYDRA_UMC_OPCUA_PORT` gelesen (standardmäßig 4840). Das gemeinsame `PORT` gilt weiter als letzter Ausweg und gibt eine Warnung aus, damit eine von mehreren Diensten geteilte Umgebungsdatei den Server nicht versehentlich auf den Port eines anderen Dienstes verschiebt; ein gesetzter, aber ungültiger Port stoppt den Start, und die Health-Prüfung des Containers folgt derselben Reihenfolge.', 'fr': "Le port d'écoute est lu d'abord dans `HYDRA_UMC_OPCUA_PORT` (4840 par défaut). Le `PORT` partagé reste valable en dernier recours et affiche un avertissement, de sorte qu'un fichier d'environnement partagé par plusieurs services ne puisse pas déplacer le serveur sur le port d'un autre service par accident ; une valeur définie mais qui n'est pas un port valide arrête le démarrage, et le contrôle de santé du conteneur suit le même ordre.", 'it': "La porta di ascolto viene letta prima da `HYDRA_UMC_OPCUA_PORT` (4840 per impostazione predefinita). Il `PORT` condiviso vale ancora come ultima risorsa e stampa un avviso, così che un file di ambiente condiviso da più servizi non possa spostare il server sulla porta di un altro servizio per errore; un valore impostato ma non valido come porta ferma l'avvio, e il controllo di salute del container segue lo stesso ordine.", 'ja': '待ち受けポートは、まず `HYDRA_UMC_OPCUA_PORT` から読み取ります（既定は 4840）。共有の `PORT` は最後の手段として引き続き使え、警告を表示します。そのため、複数のサービスで共有する環境ファイルがサーバーを他のサービスのポートへうっかり移すことはありません。設定されていても有効なポートでない値は起動を止め、コンテナのヘルスチェックも同じ順序に従います。', 'zh': '监听端口首先从 `HYDRA_UMC_OPCUA_PORT` 读取（默认 4840）。共享的 `PORT` 仍可作为最后手段并会打印警告，这样多个服务共用的环境文件就不会意外把服务器移到另一个服务的端口上；已设置但不是有效端口的值会终止启动，容器健康检查遵循相同的顺序。', 'pt': 'A porta de escuta é lida primeiro de `HYDRA_UMC_OPCUA_PORT` (4840 por predefinição). O `PORT` partilhado continua a valer como último recurso e mostra um aviso, para que um ficheiro de ambiente partilhado por vários serviços não possa mudar o servidor para a porta de outro serviço por acidente; um valor definido mas que não é uma porta válida interrompe o arranque, e a verificação de saúde do contentor segue a mesma ordem.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
