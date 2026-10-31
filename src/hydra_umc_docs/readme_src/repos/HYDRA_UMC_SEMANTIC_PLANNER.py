# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_SEMANTIC_PLANNER.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-SEMANTIC-PLANNER."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '🧭'
COMMENT = 'Rule-based mission planner and semantic error recovery'
BADGES: Any = []
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh decompose \"assemble the pcb\"",
        "./run.sh recover --component gripper --error-code TIMEOUT",
        "./run.sh serve --port 8110"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-SEMANTIC-PLANNER architecture",
    "role": {
        "en": "**HYDRA-UMC-SEMANTIC-PLANNER** turns a high-level goal into a plan made of a closed vocabulary of robot primitives and proposes a recovery when a step fails. Today it is rule-based, not a language model; a plan is only a proposal until a named person approves that exact plan.",
        "es": "**HYDRA-UMC-SEMANTIC-PLANNER** convierte un objetivo de alto nivel en un plan hecho con un vocabulario cerrado de primitivas del robot y propone una recuperación cuando falla un paso. Hoy se basa en reglas, no en un modelo de lenguaje; un plan es solo una propuesta hasta que una persona con nombre aprueba ese plan exacto.",
        "de": "**HYDRA-UMC-SEMANTIC-PLANNER** macht aus einem übergeordneten Ziel einen Plan aus einem geschlossenen Vokabular von Roboter-Primitiven und schlägt eine Wiederherstellung vor, wenn ein Schritt scheitert. Heute arbeitet er regelbasiert, nicht mit einem Sprachmodell; ein Plan ist nur ein Vorschlag, bis eine benannte Person genau diesen Plan freigibt.",
        "fr": "**HYDRA-UMC-SEMANTIC-PLANNER** transforme un objectif de haut niveau en un plan fait d'un vocabulaire fermé de primitives du robot et propose une reprise quand une étape échoue. Aujourd'hui il est fondé sur des règles, pas sur un modèle de langage ; un plan n'est qu'une proposition tant qu'une personne nommée n'a pas approuvé ce plan exact.",
        "it": "**HYDRA-UMC-SEMANTIC-PLANNER** trasforma un obiettivo di alto livello in un piano fatto di un vocabolario chiuso di primitive del robot e propone un ripristino quando un passo fallisce. Oggi è basato su regole, non su un modello linguistico; un piano è solo una proposta finché una persona con nome non approva quel piano esatto.",
        "ja": "**HYDRA-UMC-SEMANTIC-PLANNER** は高レベルの目標を、閉じたロボットプリミティブの語彙で作られた計画に変換し、ステップが失敗したときの回復案を提案します。現在はルールベースで言語モデルではなく、計画は名前のある担当者がその計画そのものを承認するまで提案にすぎません。",
        "zh": "**HYDRA-UMC-SEMANTIC-PLANNER** 把高层目标转换为由封闭的机器人原语词汇组成的计划，并在某一步失败时提出恢复方案。目前它基于规则而不是语言模型；在具名人员批准这份确切的计划之前，计划只是建议。",
        "pt": "O **HYDRA-UMC-SEMANTIC-PLANNER** transforma um objetivo de alto nível num plano feito de um vocabulário fechado de primitivas do robô e propõe uma recuperação quando um passo falha. Hoje baseia-se em regras, não num modelo de linguagem; um plano é apenas uma proposta até uma pessoa identificada aprovar esse plano exato."
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

ADDENDA = {'configuration': {'en': 'Plan simulation (off by default): with `plan_simulation.enabled` set to `true` in the configuration file, `POST /plan/simulate` checks a list of steps against declared constraints (workspace box, catalogue of locations, robots available, maximum step and plan time, resources held by one step at a time, order of dependencies, the gripper of each robot) and walks it on a simulated clock. It answers a verdict that lists EVERY broken rule with its step, value and limit and, where one follows, a deterministic suggestion; it never executes or releases anything, and an input it cannot understand is a 400, never an "accepted". With the switch off the route answers 404 as before. See `docs/PLAN_SIMULATION.md`.', 'es': 'Simulación de planes (apagada por defecto): con `plan_simulation.enabled` en `true` en el fichero de configuración, `POST /plan/simulate` comprueba una lista de pasos contra restricciones declaradas (caja del espacio de trabajo, catálogo de ubicaciones, robots disponibles, tiempo máximo por paso y por plan, recursos que solo un paso puede tener a la vez, orden de las dependencias, la pinza de cada robot) y la recorre con un reloj simulado. Responde un veredicto que lista TODAS las reglas incumplidas con su paso, valor y límite y, cuando se deduce, una sugerencia determinista; nunca ejecuta ni libera nada, y una entrada que no entiende es un 400, nunca un «aceptado». Con el interruptor apagado la ruta responde 404 como antes. Véase `docs/PLAN_SIMULATION.md`.', 'de': 'Plansimulation (standardmäßig aus): Ist in der Konfigurationsdatei `plan_simulation.enabled` auf `true` gesetzt, prüft `POST /plan/simulate` eine Schrittliste gegen deklarierte Randbedingungen (Arbeitsraumquader, Katalog der Orte, verfügbare Roboter, maximale Schritt- und Plandauer, Ressourcen, die nur ein Schritt zugleich halten darf, Reihenfolge der Abhängigkeiten, der Greifer jedes Roboters) und spielt sie auf einer simulierten Uhr durch. Die Antwort ist ein Urteil, das JEDE verletzte Regel mit Schritt, Wert und Grenze auflistet und, wo sich eines ergibt, einen deterministischen Korrekturvorschlag; sie führt nie etwas aus und gibt nie etwas frei, und eine nicht verständliche Eingabe ergibt 400, nie ein „akzeptiert“. Bei ausgeschaltetem Schalter antwortet die Route wie zuvor mit 404. Siehe `docs/PLAN_SIMULATION.md`.', 'fr': "Simulation de plans (désactivée par défaut) : avec `plan_simulation.enabled` à `true` dans le fichier de configuration, `POST /plan/simulate` vérifie une liste d'étapes par rapport à des contraintes déclarées (boîte de l'espace de travail, catalogue de positions, robots disponibles, durée maximale par étape et par plan, ressources qu'une seule étape peut tenir à la fois, ordre des dépendances, pince de chaque robot) et la déroule sur une horloge simulée. Elle répond par un verdict qui liste CHAQUE règle enfreinte avec son étape, sa valeur et sa limite et, quand il y en a une, une suggestion déterministe ; elle n'exécute ni ne libère jamais rien, et une entrée qu'elle ne comprend pas donne un 400, jamais un « accepté ». Interrupteur éteint, la route répond 404 comme avant. Voir `docs/PLAN_SIMULATION.md`.", 'it': "Simulazione dei piani (spenta per impostazione predefinita): con `plan_simulation.enabled` impostato su `true` nel file di configurazione, `POST /plan/simulate` verifica un elenco di passi rispetto a vincoli dichiarati (riquadro dello spazio di lavoro, catalogo delle posizioni, robot disponibili, tempo massimo per passo e per piano, risorse che un solo passo può tenere alla volta, ordine delle dipendenze, la pinza di ogni robot) e lo percorre con un orologio simulato. Risponde con un verdetto che elenca OGNI regola violata con il suo passo, valore e limite e, quando ne discende una, un suggerimento deterministico; non esegue né rilascia mai nulla, e un input che non capisce dà un 400, mai un «accettato». Con l'interruttore spento la route risponde 404 come prima. Vedi `docs/PLAN_SIMULATION.md`.", 'ja': '計画のシミュレーション（既定ではオフ）：設定ファイルで `plan_simulation.enabled` を `true` にすると、`POST /plan/simulate` は宣言された制約（作業空間の範囲、場所のカタログ、利用可能なロボット、ステップと計画の最大時間、同時に 1 つのステップしか保持できないリソース、依存関係の順序、各ロボットのグリッパー）に対してステップの一覧を検査し、シミュレートされた時計の上で順に進めます。応答は、破られた規則を「すべて」、そのステップ・値・限界とともに列挙した判定で、該当する場合は決定的な修正案も付きます。何かを実行したり解放したりすることはなく、理解できない入力は 400 になり、「承認」になることはありません。スイッチがオフのときは、これまでどおりルートは 404 を返します。`docs/PLAN_SIMULATION.md` を参照してください。', 'zh': '计划模拟（默认关闭）：在配置文件中把 `plan_simulation.enabled` 设为 `true` 后，`POST /plan/simulate` 会根据已声明的约束（工作空间范围、位置目录、可用机器人、单步和整个计划的最长时间、同一时刻只能由一步占用的资源、依赖顺序、每个机器人的夹爪）检查一组步骤，并在模拟时钟上逐步走一遍。它返回的结论会列出每一条被违反的规则及其步骤、数值和限值，并在可推导时给出确定性的修正建议；它从不执行或放行任何东西，无法理解的输入返回 400，绝不会是“通过”。开关关闭时，该路由与以前一样返回 404。参见 `docs/PLAN_SIMULATION.md`。', 'pt': 'Simulação de planos (desligada por predefinição): com `plan_simulation.enabled` a `true` no ficheiro de configuração, `POST /plan/simulate` verifica uma lista de passos contra restrições declaradas (caixa do espaço de trabalho, catálogo de localizações, robôs disponíveis, tempo máximo por passo e por plano, recursos que só um passo pode ter de cada vez, ordem das dependências, a garra de cada robô) e percorre-a com um relógio simulado. Responde com um veredicto que lista TODAS as regras violadas com o seu passo, valor e limite e, quando se deduz, uma sugestão determinista; nunca executa nem liberta nada, e uma entrada que não entende dá um 400, nunca um «aceite». Com o interruptor desligado, a rota responde 404 como antes. Veja `docs/PLAN_SIMULATION.md`.'}, 'security': {'en': 'Approvals can be signed (off by default): `serve --approval-key-file FILE --robot-id ROBOT` makes `POST /release` require `robot_id`, `issued_at_ms`, `expires_at_ms` and an HMAC-SHA256 `signature` over the plan fingerprint, the approver, the robot and a time window of one hour at most, so an unsigned, altered, expired or other-robot approval releases nothing; `sign-approval` produces the fields. The key (at least 16 bytes) lives in a file of the installation, never in the repository.', 'es': 'Las aprobaciones pueden firmarse (apagado por defecto): `serve --approval-key-file FICHERO --robot-id ROBOT` hace que `POST /release` exija `robot_id`, `issued_at_ms`, `expires_at_ms` y una `signature` HMAC-SHA256 sobre la huella del plan, el aprobador, el robot y una ventana de tiempo de una hora como máximo, de modo que una aprobación sin firma, alterada, caducada o de otro robot no libera nada; `sign-approval` produce los campos. La clave (al menos 16 bytes) vive en un fichero de la instalación, nunca en el repositorio.', 'de': 'Freigaben können signiert werden (standardmäßig aus): `serve --approval-key-file DATEI --robot-id ROBOT` lässt `POST /release` `robot_id`, `issued_at_ms`, `expires_at_ms` und eine HMAC-SHA256-`signature` über den Plan-Fingerabdruck, den Freigebenden, den Roboter und ein Zeitfenster von höchstens einer Stunde verlangen; eine unsignierte, veränderte, abgelaufene oder für einen anderen Roboter gedachte Freigabe gibt nichts frei; `sign-approval` erzeugt die Felder. Der Schlüssel (mindestens 16 Bytes) liegt in einer Datei der Installation, nie im Repository.', 'fr': "Les approbations peuvent être signées (désactivé par défaut) : `serve --approval-key-file FICHIER --robot-id ROBOT` fait exiger à `POST /release` `robot_id`, `issued_at_ms`, `expires_at_ms` et une `signature` HMAC-SHA256 portant sur l'empreinte du plan, l'approbateur, le robot et une fenêtre de temps d'une heure au plus ; une approbation non signée, altérée, expirée ou destinée à un autre robot ne libère rien ; `sign-approval` produit les champs. La clé (au moins 16 octets) se trouve dans un fichier de l'installation, jamais dans le dépôt.", 'it': "Le approvazioni possono essere firmate (spento per impostazione predefinita): `serve --approval-key-file FILE --robot-id ROBOT` fa sì che `POST /release` richieda `robot_id`, `issued_at_ms`, `expires_at_ms` e una `signature` HMAC-SHA256 sull'impronta del piano, l'approvatore, il robot e una finestra di tempo di al massimo un'ora; un'approvazione non firmata, alterata, scaduta o di un altro robot non rilascia nulla; `sign-approval` produce i campi. La chiave (almeno 16 byte) sta in un file dell'installazione, mai nel repository.", 'ja': '承認には署名を付けられます（既定ではオフ）。`serve --approval-key-file FILE --robot-id ROBOT` を指定すると、`POST /release` は `robot_id`、`issued_at_ms`、`expires_at_ms`、そして計画のフィンガープリント・承認者・ロボット・最長 1 時間の有効時間にわたる HMAC-SHA256 の `signature` を要求します。署名のない、改変された、期限切れの、または別のロボット向けの承認では何も解放されません。`sign-approval` がこれらのフィールドを生成します。鍵（16 バイト以上）はインストール先のファイルに置き、リポジトリには決して置きません。', 'zh': '批准可以签名（默认关闭）：`serve --approval-key-file 文件 --robot-id ROBOT` 会让 `POST /release` 要求 `robot_id`、`issued_at_ms`、`expires_at_ms`，以及对计划指纹、批准人、机器人和最长一小时的时间窗口计算的 HMAC-SHA256 `signature`；未签名、被篡改、已过期或属于其他机器人的批准不会放行任何内容；`sign-approval` 用于生成这些字段。密钥（至少 16 字节）放在安装目录中的文件里，绝不放进仓库。', 'pt': 'As aprovações podem ser assinadas (desligado por predefinição): `serve --approval-key-file FICHEIRO --robot-id ROBOT` faz com que `POST /release` exija `robot_id`, `issued_at_ms`, `expires_at_ms` e uma `signature` HMAC-SHA256 sobre a impressão digital do plano, o aprovador, o robô e uma janela de tempo de uma hora no máximo, pelo que uma aprovação sem assinatura, alterada, expirada ou de outro robô não liberta nada; `sign-approval` produz os campos. A chave (pelo menos 16 bytes) fica num ficheiro da instalação, nunca no repositório.'}}

_BODY_BASE = BODY


def BODY(lg, ctx):  # type: ignore[no-redef]
    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
