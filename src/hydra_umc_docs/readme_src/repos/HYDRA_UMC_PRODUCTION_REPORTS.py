# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_PRODUCTION_REPORTS.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-PRODUCTION-REPORTS."""
from __future__ import annotations

from .. import service_kit as S

ICON = '📑'
COMMENT = 'KPI and OEE reports built from the datalake'
BADGES = [('Metrics', 'OEE%20%2F%20KPI%20%2F%20Cycle--Time', 'green'), ('Export', 'CSV%20%2F%20JSON', 'blue')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh --datalake-url http://localhost:8095",
        "curl http://127.0.0.1:8099/reports/oee?..."
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-PRODUCTION-REPORTS architecture",
    "role": {
        "en": "**HYDRA-UMC-PRODUCTION-REPORTS** builds OEE and availability reports for plant managers from the history that `HYDRA-UMC-DATALAKE` holds. It keeps no store of its own: every request queries a running datalake, and the same range and filters always give the same bytes, with the sources, the window and the formula version recorded next to the numbers.",
        "es": "**HYDRA-UMC-PRODUCTION-REPORTS** construye informes de OEE y de disponibilidad para los responsables de planta a partir del historial que guarda `HYDRA-UMC-DATALAKE`. No tiene almacén propio: cada petición consulta un datalake en marcha, y el mismo rango y los mismos filtros dan siempre los mismos bytes, con las fuentes, la ventana y la versión de la fórmula anotadas junto a las cifras.",
        "de": "**HYDRA-UMC-PRODUCTION-REPORTS** erstellt OEE- und Verfügbarkeitsberichte für Werksleiter aus der Historie, die `HYDRA-UMC-DATALAKE` hält. Er hat keinen eigenen Speicher: Jede Anfrage fragt einen laufenden Datalake ab, und derselbe Bereich und dieselben Filter ergeben immer dieselben Bytes, mit Quellen, Zeitfenster und Formelversion neben den Zahlen.",
        "fr": "**HYDRA-UMC-PRODUCTION-REPORTS** construit des rapports d'OEE et de disponibilité pour les responsables d'usine à partir de l'historique que garde `HYDRA-UMC-DATALAKE`. Il n'a pas de stockage propre : chaque requête interroge un datalake en marche, et la même plage et les mêmes filtres donnent toujours les mêmes octets, avec les sources, la fenêtre et la version de la formule notées à côté des chiffres.",
        "it": "**HYDRA-UMC-PRODUCTION-REPORTS** costruisce rapporti di OEE e di disponibilità per i responsabili di stabilimento a partire dallo storico che conserva `HYDRA-UMC-DATALAKE`. Non ha un archivio proprio: ogni richiesta interroga un datalake in funzione, e lo stesso intervallo e gli stessi filtri danno sempre gli stessi byte, con fonti, finestra e versione della formula annotate accanto ai numeri.",
        "ja": "**HYDRA-UMC-PRODUCTION-REPORTS** は、`HYDRA-UMC-DATALAKE` が保持する履歴から、工場管理者向けの OEE と稼働率のレポートを作ります。独自のストアは持たず、リクエストのたびに稼働中のデータレイクへ問い合わせます。同じ範囲とフィルターなら常に同じバイト列になり、数値の隣にソース、期間、計算式のバージョンが記録されます。",
        "zh": "**HYDRA-UMC-PRODUCTION-REPORTS** 根据 `HYDRA-UMC-DATALAKE` 保存的历史数据，为工厂管理者生成 OEE 和可用率报告。它没有自己的存储：每个请求都会查询一个正在运行的数据湖，相同的范围和过滤条件总是得到相同的字节，数字旁边记录着来源、时间窗口和公式版本。",
        "pt": "O **HYDRA-UMC-PRODUCTION-REPORTS** constrói relatórios de OEE e de disponibilidade para os responsáveis de fábrica a partir do histórico que o `HYDRA-UMC-DATALAKE` guarda. Não tem armazenamento próprio: cada pedido consulta um datalake em funcionamento, e o mesmo intervalo e os mesmos filtros dão sempre os mesmos bytes, com as fontes, a janela e a versão da fórmula registadas junto dos números."
    }
}


from ... import readme_kit as K

EXTRAS = {'configuration': {'rows': [['`--addr`', '`127.0.0.1`', {'en': 'address the API binds to; another address needs a token or `--allow-anonymous`', 'es': 'dirección en la que escucha la API; otra dirección exige un token o `--allow-anonymous`', 'de': 'Adresse, an die sich die API bindet; eine andere Adresse braucht ein Token oder `--allow-anonymous`', 'fr': "adresse sur laquelle l'API écoute ; une autre adresse exige un jeton ou `--allow-anonymous`", 'it': "indirizzo su cui ascolta l'API; un altro indirizzo richiede un token o `--allow-anonymous`", 'ja': 'API が待ち受けるアドレス。それ以外にはトークンか `--allow-anonymous` が必要', 'zh': 'API 绑定的地址；其他地址需要令牌或 `--allow-anonymous`', 'pt': 'endereço onde a API escuta; outro endereço exige um token ou `--allow-anonymous`'}], ['`--port`', '`8099`', {'en': 'port of the API', 'es': 'puerto de la API', 'de': 'Port der API', 'fr': "port de l'API", 'it': "porta dell'API", 'ja': 'API のポート', 'zh': 'API 端口', 'pt': 'porta da API'}], ['`--datalake-url`', '`http://localhost:8095`', {'en': 'datalake that every request queries', 'es': 'datalake que consulta cada petición', 'de': 'Datalake, den jede Anfrage abfragt', 'fr': 'datalake interrogé par chaque requête', 'it': 'datalake interrogato da ogni richiesta', 'ja': '各リクエストが問い合わせるデータレイク', 'zh': '每个请求所查询的数据湖', 'pt': 'datalake consultado por cada pedido'}], ['`--token` / `PRODUCTION_REPORTS_TOKEN`', {'en': 'none', 'es': 'ninguno', 'de': 'keiner', 'fr': 'aucun', 'it': 'nessuno', 'ja': 'なし', 'zh': '无', 'pt': 'nenhum'}, {'en': 'bearer token that every route except `GET /health` requires', 'es': 'token Bearer que exige toda ruta salvo `GET /health`', 'de': 'Bearer-Token, das jede Route außer `GET /health` verlangt', 'fr': 'jeton Bearer exigé par toute route sauf `GET /health`', 'it': 'token Bearer richiesto da ogni rotta tranne `GET /health`', 'ja': '`GET /health` 以外のすべてのルートが要求する Bearer トークン', 'zh': '除 `GET /health` 外所有路由都需要的 Bearer 令牌', 'pt': 'token Bearer exigido por todas as rotas exceto `GET /health`'}], ['`--max-concurrent-reports`', '`4`', {'en': 'reports built at the same time; beyond that a request gets 503', 'es': 'informes construidos a la vez; más allá una petición recibe 503', 'de': 'gleichzeitig erstellte Berichte; darüber hinaus erhält eine Anfrage 503', 'fr': 'rapports construits en même temps ; au-delà une requête reçoit 503', 'it': 'rapporti costruiti contemporaneamente; oltre una richiesta riceve 503', 'ja': '同時に作るレポート数。超えると 503 になる', 'zh': '同时生成的报告数；超过后请求得到 503', 'pt': 'relatórios construídos ao mesmo tempo; além disso um pedido recebe 503'}], ['`--job-dispatcher-url` / `PRODUCTION_REPORTS_JOB_DISPATCHER_URL`', 'none', {'en': 'job dispatcher whose robot registry gives the cell of each robot for `groupBy=cell`', 'es': 'despachador de trabajos cuyo registro de robots da la celda de cada robot para `groupBy=cell`', 'de': 'Job-Dispatcher, dessen Roboterregister für `groupBy=cell` die Zelle jedes Roboters liefert', 'fr': 'répartiteur de tâches dont le registre des robots donne la cellule de chaque robot pour `groupBy=cell`', 'it': 'dispatcher dei lavori il cui registro dei robot dà la cella di ogni robot per `groupBy=cell`', 'ja': '`groupBy=cell` のために、ロボット登録簿から各ロボットのセルを得るジョブディスパッチャー', 'zh': '其机器人登记簿为 `groupBy=cell` 提供每个机器人所在单元的作业调度器', 'pt': 'despachante de trabalhos cujo registo de robôs dá a célula de cada robô para `groupBy=cell`'}], ['`--job-dispatcher-token-file`', 'none', {'en': 'file whose first line is the bearer token of the job dispatcher', 'es': 'fichero cuya primera línea es el token del despachador de trabajos', 'de': 'Datei, deren erste Zeile das Bearer-Token des Job-Dispatchers ist', 'fr': 'fichier dont la première ligne est le jeton du répartiteur de tâches', 'it': 'file la cui prima riga è il token del dispatcher dei lavori', 'ja': '1 行目がジョブディスパッチャーのベアラートークンであるファイル', 'zh': '第一行为作业调度器承载令牌的文件', 'pt': 'ficheiro cuja primeira linha é o token do despachante de trabalhos'}]]}, 'troubleshooting': [['HTTP 503', {'en': 'Four reports are already being built (each can bring up to two queries of 200,000 points into memory)', 'es': 'Ya se están construyendo cuatro informes (cada uno puede traer a memoria hasta dos consultas de 200 000 puntos)', 'de': 'Es werden schon vier Berichte erstellt (jeder kann bis zu zwei Abfragen mit 200 000 Punkten in den Speicher holen)', 'fr': "Quatre rapports sont déjà en cours (chacun peut charger en mémoire jusqu'à deux requêtes de 200 000 points)", 'it': 'Quattro rapporti sono già in costruzione (ciascuno può portare in memoria fino a due interrogazioni da 200 000 punti)', 'ja': 'すでに 4 件のレポートを作成中（それぞれ最大 2 回、200,000 点のクエリをメモリに読み込む）', 'zh': '已有四份报告正在生成（每份最多可把两次各 200,000 点的查询载入内存）', 'pt': 'Já estão a ser construídos quatro relatórios (cada um pode trazer para a memória até duas consultas de 200 000 pontos)'}, {'en': 'Retry shortly, or raise `--max-concurrent-reports` if the machine has the memory', 'es': 'Reintenta en un momento, o sube `--max-concurrent-reports` si la máquina tiene memoria', 'de': 'Kurz danach erneut versuchen oder `--max-concurrent-reports` erhöhen, wenn der Rechner genug Speicher hat', 'fr': 'Réessayez dans un instant, ou augmentez `--max-concurrent-reports` si la machine a la mémoire', 'it': 'Riprova a breve, o aumenta `--max-concurrent-reports` se la macchina ha memoria', 'ja': '少し待って再試行するか、メモリに余裕があれば `--max-concurrent-reports` を増やします', 'zh': '稍后重试，或在机器内存足够时调大 `--max-concurrent-reports`', 'pt': 'Tente de novo daqui a pouco, ou aumente `--max-concurrent-reports` se a máquina tiver memória'}], ['exit status 2 at start', {'en': 'The address is not loopback and there is neither a token nor `--allow-anonymous`', 'es': 'La dirección no es de bucle local y no hay token ni `--allow-anonymous`', 'de': 'Die Adresse ist nicht Loopback und es gibt weder Token noch `--allow-anonymous`', 'fr': "L'adresse n'est pas locale et il n'y a ni jeton ni `--allow-anonymous`", 'it': "L'indirizzo non è loopback e non c'è né token né `--allow-anonymous`", 'ja': 'ループバック以外のアドレスで、トークンも `--allow-anonymous` も無い', 'zh': '地址不是回环，且既没有令牌也没有 `--allow-anonymous`', 'pt': 'O endereço não é de loopback e não há token nem `--allow-anonymous`'}, {'en': 'Set `PRODUCTION_REPORTS_TOKEN` (or `--token`), or use `--allow-anonymous` in a lab', 'es': 'Define `PRODUCTION_REPORTS_TOKEN` (o `--token`), o usa `--allow-anonymous` en un laboratorio', 'de': '`PRODUCTION_REPORTS_TOKEN` (oder `--token`) setzen oder im Labor `--allow-anonymous` verwenden', 'fr': 'Définissez `PRODUCTION_REPORTS_TOKEN` (ou `--token`), ou utilisez `--allow-anonymous` en laboratoire', 'it': 'Imposta `PRODUCTION_REPORTS_TOKEN` (o `--token`), oppure usa `--allow-anonymous` in laboratorio', 'ja': '`PRODUCTION_REPORTS_TOKEN`（または `--token`）を設定するか、実験環境では `--allow-anonymous` を使います', 'zh': '设置 `PRODUCTION_REPORTS_TOKEN`（或 `--token`），或在实验室使用 `--allow-anonymous`', 'pt': 'Defina `PRODUCTION_REPORTS_TOKEN` (ou `--token`), ou use `--allow-anonymous` num laboratório'}]]}

EXTRAS["configuration"]["rows"] += [
    ["`python -m hydra_umc_production_reports.scheduled --config FILE --period daily|weekly`", "`enabled: false`", {
        "en": "writes the OEE and availability of the last complete day or week as CSV/HTML plus a manifest with the sha256 of every file; run by the example systemd timers; nothing is written until `enabled` is true in the file, and every tunable value (sources, planned time, formats, time zone) lives in that file",
        "es": "escribe el OEE y la disponibilidad del último día o semana completos como CSV/HTML más un manifiesto con el sha256 de cada fichero; lo ejecutan los timers de systemd de ejemplo; no escribe nada hasta que `enabled` sea true en el fichero, y todo valor ajustable (fuentes, tiempo planificado, formatos, zona horaria) vive en ese fichero",
        "de": "schreibt OEE und Verfügbarkeit des letzten vollständigen Tages oder der letzten Woche als CSV/HTML plus ein Manifest mit dem sha256 jeder Datei; wird von den systemd-Beispiel-Timern gestartet; es wird nichts geschrieben, bis `enabled` in der Datei true ist, und jeder einstellbare Wert (Quellen, geplante Zeit, Formate, Zeitzone) steht in dieser Datei",
        "fr": "écrit l'OEE et la disponibilité du dernier jour ou de la dernière semaine complets en CSV/HTML, avec un manifeste contenant le sha256 de chaque fichier ; lancé par les timers systemd d'exemple ; rien n'est écrit tant que `enabled` n'est pas true dans le fichier, et chaque valeur réglable (sources, temps planifié, formats, fuseau horaire) vit dans ce fichier",
        "it": "scrive l'OEE e la disponibilità dell'ultimo giorno o settimana completi come CSV/HTML più un manifesto con lo sha256 di ogni file; lo avviano i timer systemd di esempio; non scrive nulla finché `enabled` non è true nel file, e ogni valore regolabile (fonti, tempo pianificato, formati, fuso orario) sta in quel file",
        "ja": "直近の完全な日または週の OEE と稼働率を CSV/HTML とし、各ファイルの sha256 を記したマニフェストとともに書き出します。例示の systemd タイマーから実行されます。設定ファイルで `enabled` が true になるまで何も書き込まず、調整可能な値（ソース、計画時間、形式、タイムゾーン）はすべてそのファイルにあります",
        "zh": "把最近一个完整的日或周的 OEE 和可用率写成 CSV/HTML，并附带记录每个文件 sha256 的清单；由示例 systemd 定时器运行；配置文件中的 `enabled` 为 true 之前不会写入任何内容，所有可调值（来源、计划时间、格式、时区）都在该文件中",
        "pt": "escreve o OEE e a disponibilidade do último dia ou semana completos em CSV/HTML, mais um manifesto com o sha256 de cada ficheiro; é executado pelos timers systemd de exemplo; não escreve nada até `enabled` ser true no ficheiro, e todo o valor ajustável (fontes, tempo planeado, formatos, fuso horário) vive nesse ficheiro",
    }],
    ["`GET /reports/availability?mode=state`", "`mode=gaps`", {
        "en": "availability from explicit up/down events (1 = up, 0 = down) instead of gaps in a telemetry stream; `lookbackMs` says how far back the state at the start of the window is looked for; time with no event to prove the state counts as downtime and is shown as `unknown_ms`",
        "es": "disponibilidad a partir de eventos explícitos up/down (1 = activo, 0 = caído) en lugar de huecos en un flujo de telemetría; `lookbackMs` indica hasta dónde se busca el estado al inicio de la ventana; el tiempo sin evento que pruebe el estado cuenta como parada y se muestra como `unknown_ms`",
        "de": "Verfügbarkeit aus expliziten Up/Down-Ereignissen (1 = up, 0 = down) statt aus Lücken in einem Telemetriestrom; `lookbackMs` legt fest, wie weit zurück der Zustand am Fensteranfang gesucht wird; Zeit ohne Ereignis, das den Zustand belegt, zählt als Ausfall und wird als `unknown_ms` ausgewiesen",
        "fr": "disponibilité à partir d'événements up/down explicites (1 = actif, 0 = arrêté) au lieu des trous d'un flux de télémétrie ; `lookbackMs` dit jusqu'où on cherche l'état au début de la fenêtre ; le temps sans événement prouvant l'état compte comme arrêt et apparaît comme `unknown_ms`",
        "it": "disponibilità da eventi up/down espliciti (1 = attivo, 0 = fermo) invece che dai vuoti in un flusso di telemetria; `lookbackMs` indica fin dove si cerca lo stato all'inizio della finestra; il tempo senza un evento che provi lo stato conta come fermo e compare come `unknown_ms`",
        "ja": "テレメトリの途切れではなく、明示的な up/down イベント（1 = 稼働、0 = 停止）から稼働率を求めます。`lookbackMs` はウィンドウ開始時の状態をどこまで遡って探すかを指定し、状態を示すイベントがない時間は停止として数え、`unknown_ms` に示されます",
        "zh": "根据明确的 up/down 事件（1 = 运行，0 = 停止）而不是遥测流中的空缺来计算可用率；`lookbackMs` 指定向前回溯多远来查找窗口起点的状态；没有事件证明状态的时间按停机计算，并显示为 `unknown_ms`",
        "pt": "disponibilidade a partir de eventos up/down explícitos (1 = ativo, 0 = parado) em vez de lacunas num fluxo de telemetria; `lookbackMs` indica até onde se procura o estado no início da janela; o tempo sem evento que prove o estado conta como paragem e aparece como `unknown_ms`",
    }],
]



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
