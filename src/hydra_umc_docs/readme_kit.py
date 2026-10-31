# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/readme_kit.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Small helpers shared by the README sources of the repositories: a text in eight languages, tables, code blocks, the pictures and the words every README repeats."""
from __future__ import annotations

import re
from pathlib import Path

LGS = ["en", "es", "de", "fr", "it", "ja", "zh", "pt"]
VERBATIM = Path(__file__).resolve().parent / "readme_src" / "verbatim"


def P(en, es, de, fr, it, ja, zh, pt):
    """One text in the eight languages (the order of the arguments is the order of LGS)."""
    return dict(zip(LGS, (en, es, de, fr, it, ja, zh, pt), strict=False))


def pick(value, lg):
    """A text that is the same in every language (a string) or one per language (a mapping)."""
    return value[lg] if isinstance(value, dict) else value


def apply_addenda(body: dict, addenda: dict, lg: str) -> dict:
    """Adds the paragraph of each section in `addenda` (section -> {language: text}) after what the section already has, or makes the section."""
    for key, texts in addenda.items():
        text = pick(texts, lg).strip()
        current = (body.get(key) or "").strip()
        body[key] = (current + "\n\n" + text) if current else text
    return body


def verbatim(repo: str, lg: str, key: str, **fields) -> str:
    """A prose file kept from the earlier READMEs (already translated); {name} placeholders are filled from `fields`."""
    text = (VERBATIM / repo / lg / f"{key}.txt").read_text(encoding="utf-8").strip("\n")
    from .readme_src.fixes import FIXES
    for old, new in FIXES.get(lg, []):
        text = text.replace(old, new)
    for name, value in fields.items():
        text = text.replace("{" + name + "}", str(value))
    return re.sub(r"\n{3,}", "\n\n", text)


def has_verbatim(repo: str, lg: str, key: str) -> bool:
    return (VERBATIM / repo / lg / f"{key}.txt").is_file()


# --------------------------------------------------------------------------- the 22 sections
ROLE_NAME = P("Role in HYDRA-UMC", "Papel en HYDRA-UMC", "Rolle in HYDRA-UMC", "Rôle dans HYDRA-UMC", "Ruolo in HYDRA-UMC", "HYDRA-UMC での役割", "在 HYDRA-UMC 中的角色", "Papel no HYDRA-UMC")
JUMP = P("**Jump to:**", "**Ir a:**", "**Springe zu:**", "**Aller à :**", "**Vai a:**", "**移動：**", "**跳转：**", "**Ir para:**")
SUMMARY_DIAGRAM = P("Text version of the diagram (Mermaid)", "Versión en texto del diagrama (Mermaid)", "Textversion des Diagramms (Mermaid)", "Version texte du diagramme (Mermaid)",
                    "Versione testuale del diagramma (Mermaid)", "図のテキスト版（Mermaid）", "图表的文本版本（Mermaid）", "Versão em texto do diagrama (Mermaid)")
SUMMARY_TREE = P("Text version of the tree", "Versión en texto del árbol", "Textversion des Baums", "Version texte de l'arborescence", "Versione testuale dell'albero",
                 "ツリーのテキスト版", "目录树的文本版本", "Versão em texto da árvore")
LIMITS = P("**Known limits today**", "**Límites conocidos hoy**", "**Bekannte Grenzen heute**", "**Limites connues aujourd'hui**", "**Limiti noti oggi**", "**現時点の既知の制限**",
           "**当前已知限制**", "**Limites conhecidos hoje**")
WHY = P("**Why it is built this way**", "**Por qué está hecho así**", "**Warum es so gebaut ist**", "**Pourquoi il est construit ainsi**", "**Perché è fatto così**", "**この作りにした理由**",
        "**为什么这样构建**", "**Porque é construído assim**")
DOES = P("**What it does**", "**Qué hace**", "**Was es tut**", "**Ce qu'il fait**", "**Cosa fa**", "**できること**", "**它做什么**", "**O que faz**")
DOES_NOT = P("**What it does not do**", "**Qué no hace**", "**Was es nicht tut**", "**Ce qu'il ne fait pas**", "**Cosa non fa**", "**できないこと**", "**它不做什么**", "**O que não faz**")

# the column headings that the tables of every README share
HEAD = {
    "threat": P(["Threat", "Defence", "Where"], ["Amenaza", "Defensa", "Dónde"], ["Bedrohung", "Abwehr", "Wo"], ["Menace", "Défense", "Où"], ["Minaccia", "Difesa", "Dove"],
                ["脅威", "防御", "場所"], ["威胁", "防御", "位置"], ["Ameaça", "Defesa", "Onde"]),
    "trouble": P(["You see", "Because", "Do"], ["Ves", "Porque", "Haz"], ["Du siehst", "Weil", "Tu"], ["Vous voyez", "Parce que", "Faites"], ["Vedi", "Perché", "Fai"],
                 ["表示", "原因", "対処"], ["你看到", "原因", "处理"], ["Vê", "Porque", "Faça"]),
    "tests": P(["Test file", "Tests", "What it covers"], ["Fichero de pruebas", "Pruebas", "Qué cubre"], ["Testdatei", "Tests", "Was sie abdeckt"],
               ["Fichier de tests", "Tests", "Ce qu'il couvre"], ["File di test", "Test", "Cosa copre"], ["テストファイル", "テスト数", "対象"],
               ["测试文件", "测试数", "覆盖内容"], ["Ficheiro de testes", "Testes", "O que cobre"]),
    "config": P(["Variable", "Default", "What it sets"], ["Variable", "Por defecto", "Qué fija"], ["Variable", "Standard", "Was sie festlegt"],
                ["Variable", "Par défaut", "Ce qu'elle définit"], ["Variabile", "Predefinito", "Cosa imposta"], ["変数", "既定値", "設定する内容"],
                ["变量", "默认值", "设置内容"], ["Variável", "Predefinição", "O que define"]),
    "topic": P(["Topic or route", "What it carries"], ["Topic o ruta", "Qué lleva"], ["Topic oder Route", "Was es trägt"], ["Topic ou route", "Ce qu'il porte"], ["Topic o rotta", "Cosa porta"],
               ["トピックまたはルート", "内容"], ["主题或路由", "内容"], ["Tópico ou rota", "O que leva"]),
    "item": P(["Item", "What it is"], ["Elemento", "Qué es"], ["Element", "Was es ist"], ["Élément", "Ce que c'est"], ["Elemento", "Cos'è"], ["項目", "内容"], ["项目", "说明"], ["Elemento", "O que é"]),
    "limit": P(["Limit", "Value"], ["Límite", "Valor"], ["Grenze", "Wert"], ["Limite", "Valeur"], ["Limite", "Valore"], ["上限", "値"], ["限制", "值"], ["Limite", "Valor"]),
    "talks": P(["It talks to", "How", "What for"], ["Habla con", "Cómo", "Para qué"], ["Er spricht mit", "Wie", "Wozu"], ["Il parle à", "Comment", "Pour quoi faire"],
               ["Parla con", "Come", "A che scopo"], ["連携先", "方法", "目的"], ["对话对象", "方式", "用途"], ["Fala com", "Como", "Para quê"]),
}


def table(lg: str, head, rows) -> str:
    """A Markdown table. `head` is a key of HEAD or a list of column titles; each cell is a string or a mapping with the eight languages."""
    titles = HEAD[head][lg] if isinstance(head, str) else [pick(h, lg) for h in head]
    lines = ["| " + " | ".join(titles) + " |", "|" + "---|" * len(titles)]
    for row in rows:
        lines.append("| " + " | ".join(str(pick(cell, lg)).replace("\n", " ").replace("|", "\\|") for cell in row) + " |")
    return "\n".join(lines)


def code(lg: str, lines, shell: str = "bash") -> str:
    """A code block. Each line is a command, or (command, comment) where the comment is a string or one per language; the comments line up."""
    items = [(line, "") if isinstance(line, str) else (line[0], pick(line[1], lg)) for line in lines]
    width = max([len(cmd) for cmd, note in items if note] or [0]) + 2
    body = "\n".join((cmd.ljust(width) + "# " + note) if note else cmd for cmd, note in items)
    return "```" + shell + "\n" + body + "\n```"


def arch(lg: str, alt: str, mermaid: str | None = None, before: str = "", after: str = "") -> str:
    """The Architecture section: the picture and, when the repository had one, the Mermaid text inside <details>."""
    out = []
    if before.strip():
        out.append(before.strip())
    out.append(f'<p align="center">\n  <img src="images/architecture.svg" alt="{alt}" width="100%">\n</p>')
    if mermaid:
        out.append(f"<details>\n<summary>{SUMMARY_DIAGRAM[lg]}</summary>\n\n```mermaid\n{mermaid.strip()}\n```\n\n</details>")
    if after.strip():
        out.append(after.strip())
    return "\n\n".join(out)


def github_anchor(heading: str) -> str:
    """The anchor GitHub gives to a heading: lower case, only letters, digits, underscores, hyphens and spaces, spaces turned into hyphens."""
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


# --------------------------------------------------------------------------- sentences every HYDRA README repeats
LANGUAGES_TEXT = P(
    "This README and the documents of the repository exist in eight languages: English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese (Portugal). They are written together and checked in the CI so that the eight files have the same sections and the same links.",
    "Este README y los documentos del repositorio existen en ocho idiomas: inglés, español, alemán, francés, italiano, japonés, chino y portugués (Portugal). Se escriben a la vez y el CI comprueba que los ocho ficheros tengan las mismas secciones y los mismos enlaces.",
    "Diese README und die Dokumente des Repositorys gibt es in acht Sprachen: Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und Portugiesisch (Portugal). Sie entstehen gemeinsam, und die CI prüft, dass die acht Dateien dieselben Abschnitte und dieselben Links haben.",
    "Ce README et les documents du dépôt existent en huit langues : anglais, espagnol, allemand, français, italien, japonais, chinois et portugais (Portugal). Ils sont écrits ensemble et la CI vérifie que les huit fichiers ont les mêmes sections et les mêmes liens.",
    "Questo README e i documenti del repository esistono in otto lingue: inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese (Portogallo). Sono scritti insieme e la CI verifica che gli otto file abbiano le stesse sezioni e gli stessi link.",
    "この README とリポジトリの文書は、英語・スペイン語・ドイツ語・フランス語・イタリア語・日本語・中国語・ポルトガル語（ポルトガル）の 8 言語で提供されています。8 つのファイルは同時に書かれ、同じ節と同じリンクを持つことを CI が確認します。",
    "本 README 和仓库文档提供八种语言：英语、西班牙语、德语、法语、意大利语、日语、中文和葡萄牙语（葡萄牙）。它们同时编写，并由 CI 检查八个文件拥有相同的章节和相同的链接。",
    "Este README e os documentos do repositório existem em oito idiomas: inglês, espanhol, alemão, francês, italiano, japonês, chinês e português (Portugal). São escritos em conjunto e a CI verifica que os oito ficheiros têm as mesmas secções e as mesmas ligações.",
)
NO_UI = P(
    "This repository has no screen or message catalogue of its own, so there are no interface strings to translate.",
    "Este repositorio no tiene pantalla ni catálogo de mensajes propios, así que no hay cadenas de interfaz que traducir.",
    "Dieses Repository hat weder eine eigene Oberfläche noch einen eigenen Meldungskatalog, es gibt also keine Oberflächentexte zu übersetzen.",
    "Ce dépôt n'a ni écran ni catalogue de messages propre, il n'y a donc aucune chaîne d'interface à traduire.",
    "Questo repository non ha uno schermo né un catalogo di messaggi propri, quindi non ci sono stringhe di interfaccia da tradurre.",
    "このリポジトリには独自の画面もメッセージカタログもないため、翻訳すべきインターフェース文字列はありません。",
    "本仓库没有自己的界面或消息目录，因此没有需要翻译的界面文字。",
    "Este repositório não tem ecrã nem catálogo de mensagens próprios, por isso não há textos de interface para traduzir.",
)
DOC_CHANGELOG = P("Changelog of this repository", "Historial de cambios de este repositorio", "Änderungsprotokoll dieses Repositorys", "Journal des modifications de ce dépôt",
                  "Registro delle modifiche di questo repository", "このリポジトリの変更履歴", "本仓库的更新日志", "Registo de alterações deste repositório")
DOC_SECURITY = P("How to report a vulnerability and the security focus areas of this project", "Cómo informar de una vulnerabilidad y las áreas de seguridad de este proyecto",
                 "Wie man eine Schwachstelle meldet und die Sicherheitsschwerpunkte dieses Projekts", "Comment signaler une vulnérabilité et les axes de sécurité de ce projet",
                 "Come segnalare una vulnerabilità e le aree di sicurezza di questo progetto", "脆弱性の報告方法と、このプロジェクトのセキュリティ上の重点", "如何报告漏洞，以及本项目的安全重点",
                 "Como comunicar uma vulnerabilidade e as áreas de segurança deste projeto")
DOC_SUPPORT = P("Where to ask questions and report bugs", "Dónde hacer preguntas e informar de errores", "Wo man Fragen stellt und Fehler meldet", "Où poser des questions et signaler des bogues",
                "Dove fare domande e segnalare errori", "質問とバグ報告の窓口", "在哪里提问和报告错误", "Onde fazer perguntas e comunicar erros")
DOC_SECURITY_BASELINE = P("Security baseline of the ecosystem", "Base de seguridad del ecosistema", "Sicherheitsgrundlage des Ökosystems", "Base de sécurité de l'écosystème",
                          "Base di sicurezza dell'ecosistema", "エコシステムのセキュリティ基準", "生态系统的安全基线", "Base de segurança do ecossistema")
DOC_THREAT_MODEL = P("Threat model of the ecosystem", "Modelo de amenazas del ecosistema", "Bedrohungsmodell des Ökosystems", "Modèle de menaces de l'écosystème",
                     "Modello delle minacce dell'ecosistema", "エコシステムの脅威モデル", "生态系统的威胁模型", "Modelo de ameaças do ecossistema")
DOC_LICENSE = P("License of this repository", "Licencia de este repositorio", "Lizenz dieses Repositorys", "Licence de ce dépôt", "Licenza di questo repository", "このリポジトリのライセンス", "本仓库的许可证", "Licença deste repositório")
DOCS_INTRO = P("Where to read more:", "Dónde leer más:", "Hier steht mehr:", "Où lire la suite :", "Dove leggere di più:", "さらに読むには：", "更多阅读：", "Onde ler mais:")
CONTRIB = P(
    ["Before a pull request run `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (or `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): it must print `CI_VALIDATION=PASS`. Do not run `build.sh` or `build.bat` for this check; building is not a check.",
     "The eight READMEs are written from one source in HYDRA-UMC-DOCS; do not edit them by hand. Change the source and write them again with `tools/make_readmes.py`.",
     "Do not state in a README what has not run: say \"simulated\" or \"not tried on hardware\" where that is the truth.",
     "See [CONTRIBUTING.md](CONTRIBUTING.md), the [code of conduct](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) and [SUPPORT.md](SUPPORT.md)."],
    ["Antes de un pull request ejecuta `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (o `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): debe imprimir `CI_VALIDATION=PASS`. No ejecutes `build.sh` ni `build.bat` para esta comprobación; compilar no es comprobar.",
     "Los ocho README se escriben desde una sola fuente en HYDRA-UMC-DOCS; no los edites a mano. Cambia la fuente y vuelve a escribirlos con `tools/make_readmes.py`.",
     "No afirmes en un README lo que no se ha ejecutado: di «simulado» o «sin probar en hardware» cuando esa sea la verdad.",
     "Mira [CONTRIBUTING.md](CONTRIBUTING.md), el [código de conducta](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) y [SUPPORT.md](SUPPORT.md)."],
    ["Führe vor einem Pull Request `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (oder `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`) aus: Es muss `CI_VALIDATION=PASS` ausgeben. Führe dafür nicht `build.sh` oder `build.bat` aus; Bauen ist keine Prüfung.",
     "Die acht READMEs entstehen aus einer einzigen Quelle in HYDRA-UMC-DOCS; bearbeite sie nicht von Hand. Ändere die Quelle und schreibe sie mit `tools/make_readmes.py` neu.",
     "Behaupte in einer README nichts, was nicht gelaufen ist: Schreibe „simuliert“ oder „nicht auf Hardware erprobt“, wo das stimmt.",
     "Siehe [CONTRIBUTING.md](CONTRIBUTING.md), den [Verhaltenskodex](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) und [SUPPORT.md](SUPPORT.md)."],
    ["Avant une pull request, exécutez `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (ou `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`) : il doit afficher `CI_VALIDATION=PASS`. N'exécutez pas `build.sh` ni `build.bat` pour cette vérification ; compiler n'est pas vérifier.",
     "Les huit README sont écrits à partir d'une source unique dans HYDRA-UMC-DOCS ; ne les modifiez pas à la main. Changez la source et réécrivez-les avec `tools/make_readmes.py`.",
     "N'affirmez pas dans un README ce qui n'a pas tourné : écrivez « simulé » ou « non essayé sur matériel » quand c'est la vérité.",
     "Voir [CONTRIBUTING.md](CONTRIBUTING.md), le [code de conduite](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) et [SUPPORT.md](SUPPORT.md)."],
    ["Prima di una pull request esegui `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (oppure `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): deve stampare `CI_VALIDATION=PASS`. Non eseguire `build.sh` né `build.bat` per questa verifica; compilare non è verificare.",
     "I otto README sono scritti da un'unica fonte in HYDRA-UMC-DOCS; non modificarli a mano. Cambia la fonte e riscrivili con `tools/make_readmes.py`.",
     "Non affermare in un README ciò che non è stato eseguito: scrivi «simulato» o «non provato su hardware» quando è la verità.",
     "Vedi [CONTRIBUTING.md](CONTRIBUTING.md), il [codice di condotta](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) e [SUPPORT.md](SUPPORT.md)."],
    ["プルリクエストの前に `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py`（または `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`）を実行してください。`CI_VALIDATION=PASS` と表示される必要があります。この確認に `build.sh` や `build.bat` は使わないでください。ビルドは検査ではありません。",
     "8 つの README は HYDRA-UMC-DOCS の 1 つのソースから書かれます。手で編集しないでください。ソースを変更し、`tools/make_readmes.py` で書き直します。",
     "実行していないことを README に書かないでください。事実であれば「シミュレーションのみ」「実機では未確認」と書きます。",
     "[CONTRIBUTING.md](CONTRIBUTING.md)、[行動規範](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md)、[SUPPORT.md](SUPPORT.md) を参照してください。"],
    ["提交 pull request 之前，请运行 `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py`（或 `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`）：它必须输出 `CI_VALIDATION=PASS`。此检查不要运行 `build.sh` 或 `build.bat`；构建不是检查。",
     "八个 README 由 HYDRA-UMC-DOCS 中的同一个源生成；请勿手工编辑。修改源文件，再用 `tools/make_readmes.py` 重新生成。",
     "不要在 README 中声称尚未运行过的内容：属实时请写“仅模拟”或“尚未在硬件上试过”。",
     "请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)、[行为准则](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md) 和 [SUPPORT.md](SUPPORT.md)。"],
    ["Antes de um pull request execute `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (ou `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): tem de imprimir `CI_VALIDATION=PASS`. Não execute `build.sh` nem `build.bat` para esta verificação; compilar não é verificar.",
     "Os oito README são escritos a partir de uma única fonte em HYDRA-UMC-DOCS; não os edite à mão. Altere a fonte e escreva-os de novo com `tools/make_readmes.py`.",
     "Não afirme num README o que não foi executado: diga «simulado» ou «não testado em hardware» quando for a verdade.",
     "Consulte [CONTRIBUTING.md](CONTRIBUTING.md), o [código de conduta](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) e [SUPPORT.md](SUPPORT.md)."],
)


def h3_split(text: str):
    """Split a prose file at its `### ` headings: (the text before the first one, [(title, body), ...])."""
    pieces = re.split(r"(?m)^### (.*)\n", text)
    pre = pieces[0].strip("\n")
    return pre, [(pieces[i].strip(), pieces[i + 1].strip("\n")) for i in range(1, len(pieces) - 1, 2)]