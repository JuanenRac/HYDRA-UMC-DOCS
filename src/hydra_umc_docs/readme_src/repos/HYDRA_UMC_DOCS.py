# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_DOCS.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-DOCS.

The words of the hub live in `readme_text.py` (one block per language) and the claim-hygiene sentences in `readme_claims_text.py`; the list of
related projects is read from `readme_family.py`. This source puts them in the order of the universal layout, so it has no prose files.
"""
from __future__ import annotations

from ... import readme_kit as K
from ...readme_claims_text import COMMENT as CLAIMS_COMMENT, NOTE as CLAIMS_NOTE, TOOLS as CLAIMS_TOOLS
from ...readme_family import FAMILY_REPOS
from ...readme_text import TEXT
from .. import service_kit as S

ICON = "📚"
COMMENT = "Architecture, interfaces, security baseline and what is proven"
BADGES = [("Format", "Markdown", "083fa1"), ("Languages", "8", "00E5FF")]
NO_UI = True
# this source has no prose files: it writes these parts itself from the words of the hub
OWN_PROSE = ("tagline", "honesty", "overview", "roadmap", "related")
NAME = "HYDRA-UMC-DOCS"
URL = "https://github.com/JuanenRac/{name}"


def T(*texts):
    return K.P(*texts)


ARCH_NOTE = T(
    "The documents describe every family of the ecosystem. The picture below is this repository itself: the tools read the manifests and the READMEs of the sibling repositories and write the catalogue, the At a glance tables, the banner and the eight READMEs, and two checks refuse what should not be published.",
    "Los documentos describen cada familia del ecosistema. La imagen de abajo es este mismo repositorio: las herramientas leen los manifiestos y los README de los repositorios hermanos y escriben el catálogo, las tablas De un vistazo, el banner y los ocho README, y dos comprobaciones rechazan lo que no debe publicarse.",
    "Die Dokumente beschreiben jede Familie des Ökosystems. Das Bild unten ist dieses Repository selbst: Die Werkzeuge lesen die Manifeste und READMEs der Geschwister-Repositories und schreiben den Katalog, die Auf-einen-Blick-Tabellen, das Banner und die acht READMEs, und zwei Prüfungen weisen ab, was nicht veröffentlicht werden darf.",
    "Les documents décrivent chaque famille de l'écosystème. L'image ci-dessous est ce dépôt lui-même : les outils lisent les manifestes et les README des dépôts frères et écrivent le catalogue, les tableaux En un coup d'œil, la bannière et les huit README, et deux contrôles refusent ce qui ne doit pas être publié.",
    "I documenti descrivono ogni famiglia dell'ecosistema. L'immagine qui sotto è questo stesso repository: gli strumenti leggono i manifesti e i README dei repository fratelli e scrivono il catalogo, le tabelle In breve, il banner e gli otto README, e due controlli rifiutano ciò che non deve essere pubblicato.",
    "文書はエコシステムの各ファミリーを説明します。下の図はこのリポジトリ自身です。ツールは兄弟リポジトリのマニフェストと README を読み、カタログ、At a glance の表、バナー、8 つの README を書き、2 つの検査が公開してはならないものを拒否します。",
    "文档描述生态系统的每个系列。下图就是这个仓库本身：工具读取同级仓库的清单和 README，写出目录、一览表、横幅和八个 README，两项检查拒绝不应发布的内容。",
    "Os documentos descrevem cada família do ecossistema. A imagem abaixo é este próprio repositório: as ferramentas leem os manifestos e os README dos repositórios irmãos e escrevem o catálogo, as tabelas Num relance, o banner e os oito README, e duas verificações recusam o que não deve ser publicado.")

SECURITY_ROWS = [
    [T("A README that states a risky capability (an emergency stop, an interlock) without saying how far it is proven", "Un README que afirma una capacidad de riesgo (una parada de emergencia, un enclavamiento) sin decir hasta dónde está probada", "Ein README, das eine riskante Fähigkeit (Not-Halt, Verriegelung) behauptet, ohne zu sagen, wie weit sie belegt ist", "Un README qui affirme une capacité à risque (un arrêt d'urgence, un verrouillage) sans dire jusqu'où elle est prouvée", "Un README che dichiara una capacità a rischio (un arresto di emergenza, un interblocco) senza dire fino a dove è provata", "非常停止やインターロックなど危険を伴う機能が、どこまで実証されているかを書かずに記述される README", "声称具备有风险能力（紧急停止、互锁）却不说明验证到什么程度的 README", "Um README que afirma uma capacidade de risco (uma paragem de emergência, um interbloqueio) sem dizer até onde está provada"),
     T("`check_claims.py` reads the English README of every repository and fails on a sentence with a risk word that has no status marker and was not reviewed (`data/claims_reviewed.json`)", "`check_claims.py` lee el README en inglés de cada repositorio y falla ante una frase con una palabra de riesgo que no tiene marca de estado y no fue revisada (`data/claims_reviewed.json`)", "`check_claims.py` liest das englische README jedes Repositorys und schlägt bei einem Satz mit Risikowort fehl, der keine Statusmarkierung hat und nicht geprüft wurde (`data/claims_reviewed.json`)", "`check_claims.py` lit le README anglais de chaque dépôt et échoue sur une phrase contenant un mot à risque sans marque d'état et non relue (`data/claims_reviewed.json`)", "`check_claims.py` legge il README inglese di ogni repository e fallisce su una frase con una parola di rischio senza indicatore di stato e non rivista (`data/claims_reviewed.json`)", "`check_claims.py` は各リポジトリの英語 README を読み、リスク語を含み、状態の印も確認済みの記録も無い文があると失敗します（`data/claims_reviewed.json`）", "`check_claims.py` 读取每个仓库的英文 README，对含有风险词、既无状态标记又未经审阅的句子报错（`data/claims_reviewed.json`）", "`check_claims.py` lê o README em inglês de cada repositório e falha numa frase com uma palavra de risco sem marca de estado e sem revisão (`data/claims_reviewed.json`)"),
     "`tools/check_claims.py`"],
    [T("Something private leaving with a publication", "Algo privado saliendo con una publicación", "Etwas Privates verlässt das Haus mit einer Veröffentlichung", "Quelque chose de privé qui part avec une publication", "Qualcosa di privato che esce con una pubblicazione", "公開物と一緒に非公開のものが外に出る", "私有内容随发布一起流出", "Algo privado a sair com uma publicação"),
     T("`publication_check.py` looks for anything private in the files and the history before a publication", "`publication_check.py` busca cualquier cosa privada en los ficheros y en el historial antes de una publicación", "`publication_check.py` sucht vor einer Veröffentlichung in den Dateien und im Verlauf nach allem Privaten", "`publication_check.py` cherche tout ce qui est privé dans les fichiers et dans l'historique avant une publication", "`publication_check.py` cerca qualsiasi cosa privata nei file e nella cronologia prima di una pubblicazione", "`publication_check.py` は公開前に、ファイルと履歴に非公開のものが無いか調べます", "`publication_check.py` 在发布前检查文件和历史中是否有私有内容", "`publication_check.py` procura qualquer coisa privada nos ficheiros e no histórico antes de uma publicação"),
     "`tools/publication_check.py`"],
    [T("A statement that nobody can trace to a repository", "Una afirmación que nadie puede rastrear hasta un repositorio", "Eine Aussage, die niemand auf ein Repository zurückführen kann", "Une affirmation que personne ne peut rattacher à un dépôt", "Un'affermazione che nessuno può ricondurre a un repository", "どのリポジトリにもたどれない記述", "无法追溯到任何仓库的说法", "Uma afirmação que ninguém consegue ligar a um repositório"),
     T("The documents are written from the READMEs, manifests, changelogs and documents of the repositories, and a statement that could not be traced is marked as such", "Los documentos se escriben a partir de los README, manifiestos, historiales de cambios y documentos de los repositorios, y una afirmación que no se pudo rastrear se marca como tal", "Die Dokumente entstehen aus READMEs, Manifesten, Änderungsprotokollen und Dokumenten der Repositories, und eine nicht rückführbare Aussage wird als solche gekennzeichnet", "Les documents sont écrits à partir des README, manifestes, journaux et documents des dépôts, et une affirmation introuvable est marquée comme telle", "I documenti sono scritti a partire da README, manifesti, registri delle modifiche e documenti dei repository, e un'affermazione non rintracciabile è segnata come tale", "文書はリポジトリの README、マニフェスト、変更履歴、文書から書かれ、たどれなかった記述はその旨が明記されます", "文档根据各仓库的 README、清单、更新日志和文档编写，无法追溯的说法会被如实标注", "Os documentos são escritos a partir dos README, manifestos, registos de alterações e documentos dos repositórios, e uma afirmação que não se conseguiu rastrear é marcada como tal"),
     "`docs/CAPABILITY_MATRIX.md`"],
]

ROADMAP = T(
    "This repository is documents and small tools. The checks that read the other repositories (the catalogue, the At a glance tables, the claims) need those repositories checked out next to this one. It proves nothing about hardware: the capability matrix says, for each capability, whether it was only simulated or tried for real.",
    "Este repositorio son documentos y pequeñas herramientas. Las comprobaciones que leen los demás repositorios (el catálogo, las tablas De un vistazo, las afirmaciones) necesitan esos repositorios descargados junto a este. No prueba nada sobre hardware: la matriz de capacidades dice, para cada capacidad, si solo se simuló o se probó de verdad.",
    "Dieses Repository besteht aus Dokumenten und kleinen Werkzeugen. Die Prüfungen, die die anderen Repositories lesen (der Katalog, die Auf-einen-Blick-Tabellen, die Aussagen), brauchen diese Repositories neben diesem ausgecheckt. Es belegt nichts über Hardware: Die Fähigkeitsmatrix sagt für jede Fähigkeit, ob sie nur simuliert oder wirklich erprobt wurde.",
    "Ce dépôt est fait de documents et de petits outils. Les contrôles qui lisent les autres dépôts (le catalogue, les tableaux En un coup d'œil, les affirmations) exigent ces dépôts récupérés à côté de celui-ci. Il ne prouve rien sur le matériel : la matrice des capacités dit, pour chaque capacité, si elle a seulement été simulée ou réellement essayée.",
    "Questo repository è fatto di documenti e piccoli strumenti. I controlli che leggono gli altri repository (il catalogo, le tabelle In breve, le affermazioni) richiedono quei repository scaricati accanto a questo. Non prova nulla sull'hardware: la matrice delle capacità dice, per ogni capacità, se è stata solo simulata o provata davvero.",
    "このリポジトリは文書と小さなツールでできています。他のリポジトリを読む検査（カタログ、At a glance の表、記述の確認）には、それらのリポジトリをこのリポジトリの隣にチェックアウトしておく必要があります。ハードウェアについては何も証明しません。機能マトリクスが、各機能について、シミュレーションのみか実際に試したかを示します。",
    "本仓库由文档和小工具组成。读取其他仓库的检查（目录、一览表、说法核对）需要把那些仓库检出到本仓库旁边。它不证明任何硬件方面的事：能力矩阵会逐项说明某项能力只是模拟过，还是真正试过。",
    "Este repositório é feito de documentos e pequenas ferramentas. As verificações que leem os outros repositórios (o catálogo, as tabelas Num relance, as afirmações) precisam desses repositórios descarregados ao lado deste. Não prova nada sobre hardware: a matriz de capacidades diz, para cada capacidade, se foi apenas simulada ou testada a sério.")

COMMANDS = ("python tools/make_catalog.py --check", "python tools/make_brand.py --check", "python tools/make_readmes.py --check", "python tools/make_glance.py --check",
            "python tools/publication_check.py", "python tools/check_claims.py --require-siblings", "bash tools/check_all.sh", "python -m pytest tests -q")


def TAGLINE(lg, ctx):
    return TEXT[lg]["subtitle"]


def HONESTY(lg, ctx):
    text = TEXT[lg]
    return f"**{text['honesty_label']}** {text['honesty']}\n\n---\n\n{CLAIMS_NOTE[lg]}"


def _overview(lg):
    text = TEXT[lg]
    picture = '<p align="center">\n  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">\n</p>'
    items = [f"* [{label}]({path}): {description}" for label, path, description in text["overview"]]
    items.append(f"* **{text['tools_label']}** {text['tools']}{CLAIMS_TOOLS[lg]}")
    return picture + "\n\n" + str(text["overview_intro"]) + "\n\n" + "\n".join(items)


def _related(lg):
    text = TEXT[lg]
    lines = [str(text["related_intro"]), ""]
    for family_name, names in FAMILY_REPOS:
        entries = [f"**{name}** ({text['related_this']})" if name == NAME else f"[{name}]({URL.format(name=name)})" for name in names]
        lines.append(f"* **{family_name}:** " + ", ".join(entries))
    lines += ["", f"**{text['related_beyond']}**", ""]
    lines += [f"* **[{name}]({url})** - {description}" for name, url, description in text["beyond"]]
    return "\n".join(lines)


def DOCS(lg, ctx):
    return [f"[{label}]({path})" for label, path in TEXT[lg]["docs_links"] if path not in ("CHANGELOG.md", "LICENSE")]


def BODY(lg, ctx):
    text = TEXT[lg]
    comments = list(text["dev_comments"])
    comments.insert(5, CLAIMS_COMMENT[lg])
    quick = [(command, comment) for command, comment in zip(COMMANDS, comments)]
    return {
        "overview": _overview(lg),
        "role": str(text["role"]),
        "architecture": K.pick(ARCH_NOTE, lg) + '\n\n<p align="center">\n  <img src="images/architecture.svg" alt="HYDRA-UMC-DOCS architecture" width="100%">\n</p>',
        "security": K.table(lg, "threat", SECURITY_ROWS),
        "quickstart": str(text["dev_requirements"]) + "\n\n" + K.code(lg, quick, "bash"),
        "testing": S.testing(lg, ctx.tests, "python -m pytest tests -q"),
        "build": str(text["dev_note"]),
        "roadmap": K.LIMITS[lg] + "\n\n" + K.pick(ROADMAP, lg),
        "related": _related(lg),
    }
