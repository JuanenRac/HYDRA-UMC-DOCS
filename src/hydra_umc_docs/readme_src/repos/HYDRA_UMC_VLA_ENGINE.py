# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_VLA_ENGINE.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-VLA-ENGINE."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '🤖'
COMMENT = 'Vision-language-action engine contracts'
BADGES = [('Model', 'OpenVLA%20%2F%20RT--2', 'orange'), ('Acceleration', 'Hailo--10', 'green')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh tokens encode --action 0.02,0.00,-0.01,0.0,0.0,0.05,1.0",
        "./run.sh trajectory integrate --start 0,0,0,0,0,0 --actions actions.json",
        "./run.sh status",
        "./run.sh serve --port 8098"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-VLA-ENGINE architecture",
    "role": {
        "en": "**HYDRA-UMC-VLA-ENGINE** holds the parts of a vision-language-action engine that do not need a model: turning actions into discrete tokens and back, integrating the predicted steps into a trajectory, and a guard that clamps or rejects a trajectory against the work volume, speed limits, safety zones and the gripper range. No model runs yet; the Hailo-10 boundary only reports what is present.",
        "es": "**HYDRA-UMC-VLA-ENGINE** contiene las partes de un motor visión-lenguaje-acción que no necesitan un modelo: convertir acciones en tokens discretos y viceversa, integrar los pasos predichos en una trayectoria y una guarda que recorta o rechaza una trayectoria según el volumen de trabajo, los límites de velocidad, las zonas de seguridad y el rango de la pinza. Aún no se ejecuta ningún modelo; la frontera con Hailo-10 solo informa de lo que hay.",
        "de": "**HYDRA-UMC-VLA-ENGINE** enthält die Teile einer Vision-Language-Action-Engine, die kein Modell brauchen: Aktionen in diskrete Tokens und zurück umwandeln, die vorhergesagten Schritte zu einer Trajektorie integrieren und eine Schutzprüfung, die eine Trajektorie anhand von Arbeitsvolumen, Geschwindigkeitsgrenzen, Sicherheitszonen und Greiferbereich beschneidet oder ablehnt. Noch läuft kein Modell; die Hailo-10-Grenze meldet nur, was vorhanden ist.",
        "fr": "**HYDRA-UMC-VLA-ENGINE** contient les parties d'un moteur vision-langage-action qui n'ont pas besoin d'un modèle : convertir des actions en jetons discrets et inversement, intégrer les pas prédits en une trajectoire, et une garde qui rogne ou rejette une trajectoire selon le volume de travail, les limites de vitesse, les zones de sécurité et la plage de la pince. Aucun modèle ne tourne encore ; la frontière Hailo-10 indique seulement ce qui est présent.",
        "it": "**HYDRA-UMC-VLA-ENGINE** contiene le parti di un motore visione-linguaggio-azione che non richiedono un modello: convertire azioni in token discreti e viceversa, integrare i passi previsti in una traiettoria, e una guardia che ritaglia o rifiuta una traiettoria rispetto al volume di lavoro, ai limiti di velocità, alle zone di sicurezza e all'intervallo della pinza. Nessun modello gira ancora; il confine con Hailo-10 riferisce solo ciò che è presente.",
        "ja": "**HYDRA-UMC-VLA-ENGINE** は、モデルを必要としない視覚・言語・行動エンジンの部分を収めています。行動と離散トークンの相互変換、予測ステップの軌道への積分、作業空間・速度制限・安全ゾーン・グリッパー範囲に対して軌道を切り詰めるか拒否するガードです。モデルはまだ動かず、Hailo-10 との境界は存在するものを報告するだけです。",
        "zh": "**HYDRA-UMC-VLA-ENGINE** 包含视觉-语言-动作引擎中不需要模型的部分：把动作转换为离散令牌并还原，把预测的步骤积分成轨迹，以及根据工作空间、速度限制、安全区域和夹爪范围裁剪或拒绝轨迹的守卫。目前还没有模型运行；Hailo-10 边界只报告现有的东西。",
        "pt": "O **HYDRA-UMC-VLA-ENGINE** contém as partes de um motor visão-linguagem-ação que não precisam de um modelo: converter ações em tokens discretos e vice-versa, integrar os passos previstos numa trajetória e uma guarda que corta ou rejeita uma trajetória segundo o volume de trabalho, os limites de velocidade, as zonas de segurança e o intervalo da pinça. Ainda não corre nenhum modelo; a fronteira com o Hailo-10 só indica o que está presente."
    }
}


from ... import readme_kit as K

EXTRAS: Any = {}


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

# Text added for recent changes of the repository (section -> language -> paragraph), appended to what the section already says.
from ... import readme_kit as _K

ADDENDA = {'security': {'en': 'Trajectory proposals can be signed (off by default): `serve --proposal-key-file FILE --robot-id ROBOT [--proposal-valid-seconds N]` adds `robot_id`, `issued_at_ms`, `expires_at_ms` and an HMAC-SHA256 `signature` to what `POST /trajectory/integrate` returns (valid 60 seconds by default, 600 at most), and `verify_proposal()` refuses an altered, expired, future-dated or other-robot proposal. A proposal is still never an order. The key (at least 16 bytes) lives in a file of the installation, never in the repository.', 'es': 'Las propuestas de trayectoria pueden firmarse (apagado por defecto): `serve --proposal-key-file FICHERO --robot-id ROBOT [--proposal-valid-seconds N]` añade `robot_id`, `issued_at_ms`, `expires_at_ms` y una `signature` HMAC-SHA256 a lo que devuelve `POST /trajectory/integrate` (válida 60 segundos por defecto, 600 como máximo), y `verify_proposal()` rechaza una propuesta alterada, caducada, con fecha futura o de otro robot. Una propuesta sigue sin ser nunca una orden. La clave (al menos 16 bytes) vive en un fichero de la instalación, nunca en el repositorio.', 'de': 'Trajektorienvorschläge können signiert werden (standardmäßig aus): `serve --proposal-key-file DATEI --robot-id ROBOT [--proposal-valid-seconds N]` fügt dem, was `POST /trajectory/integrate` liefert, `robot_id`, `issued_at_ms`, `expires_at_ms` und eine HMAC-SHA256-`signature` hinzu (standardmäßig 60 Sekunden gültig, höchstens 600), und `verify_proposal()` lehnt einen veränderten, abgelaufenen, in der Zukunft datierten oder für einen anderen Roboter gedachten Vorschlag ab. Ein Vorschlag ist weiterhin nie ein Befehl. Der Schlüssel (mindestens 16 Bytes) liegt in einer Datei der Installation, nie im Repository.', 'fr': "Les propositions de trajectoire peuvent être signées (désactivé par défaut) : `serve --proposal-key-file FICHIER --robot-id ROBOT [--proposal-valid-seconds N]` ajoute `robot_id`, `issued_at_ms`, `expires_at_ms` et une `signature` HMAC-SHA256 à ce que renvoie `POST /trajectory/integrate` (valable 60 secondes par défaut, 600 au plus), et `verify_proposal()` refuse une proposition altérée, expirée, datée du futur ou destinée à un autre robot. Une proposition n'est toujours jamais un ordre. La clé (au moins 16 octets) se trouve dans un fichier de l'installation, jamais dans le dépôt.", 'it': "Le proposte di traiettoria possono essere firmate (spento per impostazione predefinita): `serve --proposal-key-file FILE --robot-id ROBOT [--proposal-valid-seconds N]` aggiunge `robot_id`, `issued_at_ms`, `expires_at_ms` e una `signature` HMAC-SHA256 a ciò che restituisce `POST /trajectory/integrate` (valida 60 secondi per impostazione predefinita, 600 al massimo), e `verify_proposal()` rifiuta una proposta alterata, scaduta, con data futura o di un altro robot. Una proposta non è comunque mai un ordine. La chiave (almeno 16 byte) sta in un file dell'installazione, mai nel repository.", 'ja': '軌道の提案には署名を付けられます（既定ではオフ）。`serve --proposal-key-file FILE --robot-id ROBOT [--proposal-valid-seconds N]` を指定すると、`POST /trajectory/integrate` が返す内容に `robot_id`、`issued_at_ms`、`expires_at_ms`、HMAC-SHA256 の `signature` が加わります（有効時間は既定 60 秒、最長 600 秒）。`verify_proposal()` は、改変された、期限切れの、未来の日時の、または別のロボット向けの提案を拒否します。提案は依然として命令ではありません。鍵（16 バイト以上）はインストール先のファイルに置き、リポジトリには決して置きません。', 'zh': '轨迹提案可以签名（默认关闭）：`serve --proposal-key-file 文件 --robot-id ROBOT [--proposal-valid-seconds N]` 会在 `POST /trajectory/integrate` 返回的内容中加入 `robot_id`、`issued_at_ms`、`expires_at_ms` 和 HMAC-SHA256 `signature`（默认有效 60 秒，最长 600 秒），`verify_proposal()` 会拒绝被篡改、已过期、日期在未来或属于其他机器人的提案。提案仍然不是命令。密钥（至少 16 字节）放在安装目录中的文件里，绝不放进仓库。', 'pt': 'As propostas de trajetória podem ser assinadas (desligado por predefinição): `serve --proposal-key-file FICHEIRO --robot-id ROBOT [--proposal-valid-seconds N]` acrescenta `robot_id`, `issued_at_ms`, `expires_at_ms` e uma `signature` HMAC-SHA256 ao que `POST /trajectory/integrate` devolve (válida 60 segundos por predefinição, 600 no máximo), e `verify_proposal()` recusa uma proposta alterada, expirada, com data futura ou de outro robô. Uma proposta continua a nunca ser uma ordem. A chave (pelo menos 16 bytes) fica num ficheiro da instalação, nunca no repositório.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):  # type: ignore[no-redef]
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
