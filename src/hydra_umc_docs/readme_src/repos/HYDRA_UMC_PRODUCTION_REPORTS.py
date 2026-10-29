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

EXTRAS = {'configuration': {'rows': [['`--addr`', '`127.0.0.1`', {'en': 'address the API binds to; another address needs a token or `--allow-anonymous`', 'es': 'dirección en la que escucha la API; otra dirección exige un token o `--allow-anonymous`', 'de': 'Adresse, an die sich die API bindet; eine andere Adresse braucht ein Token oder `--allow-anonymous`', 'fr': "adresse sur laquelle l'API écoute ; une autre adresse exige un jeton ou `--allow-anonymous`", 'it': "indirizzo su cui ascolta l'API; un altro indirizzo richiede un token o `--allow-anonymous`", 'ja': 'API が待ち受けるアドレス。それ以外にはトークンか `--allow-anonymous` が必要', 'zh': 'API 绑定的地址；其他地址需要令牌或 `--allow-anonymous`', 'pt': 'endereço onde a API escuta; outro endereço exige um token ou `--allow-anonymous`'}], ['`--port`', '`8099`', {'en': 'port of the API', 'es': 'puerto de la API', 'de': 'Port der API', 'fr': "port de l'API", 'it': "porta dell'API", 'ja': 'API のポート', 'zh': 'API 端口', 'pt': 'porta da API'}], ['`--datalake-url`', '`http://localhost:8095`', {'en': 'datalake that every request queries', 'es': 'datalake que consulta cada petición', 'de': 'Datalake, den jede Anfrage abfragt', 'fr': 'datalake interrogé par chaque requête', 'it': 'datalake interrogato da ogni richiesta', 'ja': '各リクエストが問い合わせるデータレイク', 'zh': '每个请求所查询的数据湖', 'pt': 'datalake consultado por cada pedido'}], ['`--token` / `PRODUCTION_REPORTS_TOKEN`', {'en': 'none', 'es': 'ninguno', 'de': 'keiner', 'fr': 'aucun', 'it': 'nessuno', 'ja': 'なし', 'zh': '无', 'pt': 'nenhum'}, {'en': 'bearer token that every route except `GET /health` requires', 'es': 'token Bearer que exige toda ruta salvo `GET /health`', 'de': 'Bearer-Token, das jede Route außer `GET /health` verlangt', 'fr': 'jeton Bearer exigé par toute route sauf `GET /health`', 'it': 'token Bearer richiesto da ogni rotta tranne `GET /health`', 'ja': '`GET /health` 以外のすべてのルートが要求する Bearer トークン', 'zh': '除 `GET /health` 外所有路由都需要的 Bearer 令牌', 'pt': 'token Bearer exigido por todas as rotas exceto `GET /health`'}], ['`--max-concurrent-reports`', '`4`', {'en': 'reports built at the same time; beyond that a request gets 503', 'es': 'informes construidos a la vez; más allá una petición recibe 503', 'de': 'gleichzeitig erstellte Berichte; darüber hinaus erhält eine Anfrage 503', 'fr': 'rapports construits en même temps ; au-delà une requête reçoit 503', 'it': 'rapporti costruiti contemporaneamente; oltre una richiesta riceve 503', 'ja': '同時に作るレポート数。超えると 503 になる', 'zh': '同时生成的报告数；超过后请求得到 503', 'pt': 'relatórios construídos ao mesmo tempo; além disso um pedido recebe 503'}]]}, 'troubleshooting': [['HTTP 503', {'en': 'Four reports are already being built (each can bring up to two queries of 200,000 points into memory)', 'es': 'Ya se están construyendo cuatro informes (cada uno puede traer a memoria hasta dos consultas de 200 000 puntos)', 'de': 'Es werden schon vier Berichte erstellt (jeder kann bis zu zwei Abfragen mit 200 000 Punkten in den Speicher holen)', 'fr': "Quatre rapports sont déjà en cours (chacun peut charger en mémoire jusqu'à deux requêtes de 200 000 points)", 'it': 'Quattro rapporti sono già in costruzione (ciascuno può portare in memoria fino a due interrogazioni da 200 000 punti)', 'ja': 'すでに 4 件のレポートを作成中（それぞれ最大 2 回、200,000 点のクエリをメモリに読み込む）', 'zh': '已有四份报告正在生成（每份最多可把两次各 200,000 点的查询载入内存）', 'pt': 'Já estão a ser construídos quatro relatórios (cada um pode trazer para a memória até duas consultas de 200 000 pontos)'}, {'en': 'Retry shortly, or raise `--max-concurrent-reports` if the machine has the memory', 'es': 'Reintenta en un momento, o sube `--max-concurrent-reports` si la máquina tiene memoria', 'de': 'Kurz danach erneut versuchen oder `--max-concurrent-reports` erhöhen, wenn der Rechner genug Speicher hat', 'fr': 'Réessayez dans un instant, ou augmentez `--max-concurrent-reports` si la machine a la mémoire', 'it': 'Riprova a breve, o aumenta `--max-concurrent-reports` se la macchina ha memoria', 'ja': '少し待って再試行するか、メモリに余裕があれば `--max-concurrent-reports` を増やします', 'zh': '稍后重试，或在机器内存足够时调大 `--max-concurrent-reports`', 'pt': 'Tente de novo daqui a pouco, ou aumente `--max-concurrent-reports` se a máquina tiver memória'}], ['exit status 2 at start', {'en': 'The address is not loopback and there is neither a token nor `--allow-anonymous`', 'es': 'La dirección no es de bucle local y no hay token ni `--allow-anonymous`', 'de': 'Die Adresse ist nicht Loopback und es gibt weder Token noch `--allow-anonymous`', 'fr': "L'adresse n'est pas locale et il n'y a ni jeton ni `--allow-anonymous`", 'it': "L'indirizzo non è loopback e non c'è né token né `--allow-anonymous`", 'ja': 'ループバック以外のアドレスで、トークンも `--allow-anonymous` も無い', 'zh': '地址不是回环，且既没有令牌也没有 `--allow-anonymous`', 'pt': 'O endereço não é de loopback e não há token nem `--allow-anonymous`'}, {'en': 'Set `PRODUCTION_REPORTS_TOKEN` (or `--token`), or use `--allow-anonymous` in a lab', 'es': 'Define `PRODUCTION_REPORTS_TOKEN` (o `--token`), o usa `--allow-anonymous` en un laboratorio', 'de': '`PRODUCTION_REPORTS_TOKEN` (oder `--token`) setzen oder im Labor `--allow-anonymous` verwenden', 'fr': 'Définissez `PRODUCTION_REPORTS_TOKEN` (ou `--token`), ou utilisez `--allow-anonymous` en laboratoire', 'it': 'Imposta `PRODUCTION_REPORTS_TOKEN` (o `--token`), oppure usa `--allow-anonymous` in laboratorio', 'ja': '`PRODUCTION_REPORTS_TOKEN`（または `--token`）を設定するか、実験環境では `--allow-anonymous` を使います', 'zh': '设置 `PRODUCTION_REPORTS_TOKEN`（或 `--token`），或在实验室使用 `--allow-anonymous`', 'pt': 'Defina `PRODUCTION_REPORTS_TOKEN` (ou `--token`), ou use `--allow-anonymous` num laboratório'}]]}


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
