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


def BODY(lg, ctx):
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
