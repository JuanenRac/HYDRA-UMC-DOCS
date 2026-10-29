# HYDRA-UMC-DOCS - readme_src/service_kit.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""The parts of the README that the services, libraries and tools of the family share, in the eight languages, and the function that puts a source together.

A source gives its role, its quick-start commands and its test command; the prose that the earlier README already had (overview, design, build, roadmap,
related projects) is read from `readme_src/verbatim/<REPO>/<language>/<part>.txt` so that nothing unique is lost.
"""
from __future__ import annotations

from ..readme_kit import P, SUMMARY_DIAGRAM, LIMITS, code, pick
from .. import readme_kit as K

# ------------------------------------------------------------------ what each toolchain needs
INSTALL = {
    "python": P("Requires Python {req} or newer.", "Requiere Python {req} o superior.", "Benötigt Python {req} oder neuer.", "Nécessite Python {req} ou plus récent.",
                "Richiede Python {req} o successivo.", "Python {req} 以上が必要です。", "需要 Python {req} 或更高版本。", "Requer Python {req} ou superior."),
    "node": P("Requires Node.js {req} or newer with npm.", "Requiere Node.js {req} o superior con npm.", "Benötigt Node.js {req} oder neuer mit npm.", "Nécessite Node.js {req} ou plus récent avec npm.",
              "Richiede Node.js {req} o successivo con npm.", "Node.js {req} 以上と npm が必要です。", "需要 Node.js {req} 或更高版本及 npm。", "Requer Node.js {req} ou superior com npm."),
    "go": P("Requires Go {req} or newer.", "Requiere Go {req} o superior.", "Benötigt Go {req} oder neuer.", "Nécessite Go {req} ou plus récent.",
            "Richiede Go {req} o successivo.", "Go {req} 以上が必要です。", "需要 Go {req} 或更高版本。", "Requer Go {req} ou superior."),
    "rust": P("Requires the stable Rust toolchain (edition {req}) with `cargo`.", "Requiere la cadena de herramientas estable de Rust (edición {req}) con `cargo`.",
              "Benötigt die stabile Rust-Toolchain (Edition {req}) mit `cargo`.", "Nécessite la chaîne d'outils Rust stable (édition {req}) avec `cargo`.",
              "Richiede la toolchain Rust stabile (edizione {req}) con `cargo`.", "安定版の Rust ツールチェーン（エディション {req}）と `cargo` が必要です。",
              "需要稳定版 Rust 工具链（{req} 版）及 `cargo`。", "Requer a cadeia de ferramentas Rust estável (edição {req}) com `cargo`."),
    "flutter": P("Requires the stable Flutter SDK ({req}) with Linux desktop support.", "Requiere el SDK estable de Flutter ({req}) con soporte de escritorio Linux.",
                 "Benötigt das stabile Flutter-SDK ({req}) mit Linux-Desktop-Unterstützung.", "Nécessite le SDK Flutter stable ({req}) avec la prise en charge du bureau Linux.",
                 "Richiede l'SDK Flutter stabile ({req}) con supporto desktop Linux.", "Linux デスクトップ対応の安定版 Flutter SDK（{req}）が必要です。",
                 "需要支持 Linux 桌面的稳定版 Flutter SDK（{req}）。", "Requer o SDK Flutter estável ({req}) com suporte para ambiente de trabalho Linux."),
}
BUILD_SCRIPTS = P("`build.sh` / `build.bat` prepare the environment and run the checks; they never change the version.",
                  "`build.sh` / `build.bat` preparan el entorno y ejecutan las comprobaciones; nunca cambian la versión.",
                  "`build.sh` / `build.bat` richten die Umgebung ein und führen die Prüfungen aus; sie ändern nie die Version.",
                  "`build.sh` / `build.bat` préparent l'environnement et lancent les vérifications ; ils ne changent jamais la version.",
                  "`build.sh` / `build.bat` preparano l'ambiente ed eseguono i controlli; non cambiano mai la versione.",
                  "`build.sh` / `build.bat` は環境を整えて検査を実行します。バージョンは変更しません。",
                  "`build.sh` / `build.bat` 准备环境并运行检查；它们从不改变版本。",
                  "`build.sh` / `build.bat` preparam o ambiente e executam as verificações; nunca mudam a versão.")

TESTING = P(
    "{n} automated tests run with `{cmd}`.{note}",
    "{n} pruebas automáticas se ejecutan con `{cmd}`.{note}",
    "{n} automatische Tests laufen mit `{cmd}`.{note}",
    "{n} tests automatiques s'exécutent avec `{cmd}`.{note}",
    "{n} test automatici si eseguono con `{cmd}`.{note}",
    "`{cmd}` で自動テスト {n} 件を実行します。{note}",
    "运行 `{cmd}` 会执行 {n} 个自动测试。{note}",
    "{n} testes automáticos correm com `{cmd}`.{note}",
)
NO_HARDWARE = P(" They need no hardware and nothing outside this machine.", " No necesitan hardware ni nada fuera de esta máquina.",
                " Sie brauchen weder Hardware noch etwas außerhalb dieses Rechners.", " Ils n'ont besoin ni de matériel ni de rien en dehors de cette machine.",
                " Non richiedono hardware né nulla al di fuori di questa macchina.", " ハードウェアも、このマシンの外にあるものも必要ありません。",
                " 不需要硬件，也不需要这台机器以外的任何东西。", " Não precisam de hardware nem de nada fora desta máquina.")
CI_PLAIN = P(
    "The CI runs `HYDRA_UMC_CI=1 python tools/ci_validate.py`, which checks the manifest, the documents, the eight READMEs and the pictures.",
    "El CI ejecuta `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que comprueba el manifiesto, los documentos, los ocho README y las imágenes.",
    "Die CI führt `HYDRA_UMC_CI=1 python tools/ci_validate.py` aus; das prüft das Manifest, die Dokumente, die acht READMEs und die Bilder.",
    "La CI exécute `HYDRA_UMC_CI=1 python tools/ci_validate.py`, qui vérifie le manifeste, les documents, les huit README et les images.",
    "La CI esegue `HYDRA_UMC_CI=1 python tools/ci_validate.py`, che controlla il manifesto, i documenti, gli otto README e le immagini.",
    "CI は `HYDRA_UMC_CI=1 python tools/ci_validate.py` を実行し、マニフェスト、文書、8 つの README、図を検査します。",
    "CI 运行 `HYDRA_UMC_CI=1 python tools/ci_validate.py`，检查清单、文档、八个 README 和图片。",
    "A CI executa `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que verifica o manifesto, os documentos, os oito README e as imagens.",
)


def docs_items(lg: str, ctx) -> list[str]:
    """The documents of the repository that the earlier README listed (one Markdown bullet per line in the `docs` part), without the bullet mark."""
    if not ctx.has(lg, "docs"):
        return []
    return [line[2:].strip() for line in ctx.v(lg, "docs").split("\n") if line.startswith(("- ", "* "))]


def arch_details(lg: str, alt: str, ctx) -> str:
    """The picture, the Mermaid text of the earlier README inside <details> (when it had one) and the design notes that went with it."""
    out = [f'<p align="center">\n  <img src="images/architecture.svg" alt="{alt}" width="100%">\n</p>']
    if ctx.has(lg, "mermaid"):
        out.append(f"<details>\n<summary>{SUMMARY_DIAGRAM[lg]}</summary>\n\n{ctx.v(lg, 'mermaid')}\n\n</details>")
    if ctx.has(lg, "design"):
        out.append(ctx.v(lg, "design"))
    return "\n\n".join(out)


def quickstart(lg: str, stack: str, req: str, lines, intro=None, after=None) -> str:
    """Prerequisite sentence, then the commands (a list for `code`), then an optional closing text (a mapping of eight languages)."""
    first = pick(intro, lg) if intro is not None else INSTALL[stack][lg].replace("{req}", req)
    parts = [first, code(lg, lines, "bash")]
    if after is not None:
        parts.append(pick(after, lg))
    return "\n\n".join(parts)


def testing(lg: str, n: int, cmd: str, note=None) -> str:
    extra = pick(note, lg) if note is not None else NO_HARDWARE[lg]
    return TESTING[lg].replace("{n}", str(n)).replace("{cmd}", cmd).replace("{note}", extra) + "\n\n" + CI_PLAIN[lg]


def make_body(lg: str, ctx, spec: dict) -> dict:
    """The sections a service or library source gives. `spec`: role, alt, stack, req, quick (+ quick_intro, quick_after), test_cmd (+ test_note)."""
    out = {}
    if ctx.has(lg, "overview"):
        out["overview"] = ctx.v(lg, "overview")
    out["role"] = pick(spec["role"], lg)
    out["architecture"] = arch_details(lg, spec["alt"], ctx)
    out["quickstart"] = quickstart(lg, spec["stack"], spec.get("req", ""), spec["quick"], spec.get("quick_intro"), spec.get("quick_after"))
    out["testing"] = testing(lg, ctx.tests, spec["test_cmd"], spec.get("test_note"))
    if ctx.has(lg, "build"):
        out["build"] = ctx.v(lg, "build")
    if ctx.has(lg, "roadmap"):
        out["roadmap"] = LIMITS[lg] + "\n\n" + ctx.v(lg, "roadmap")
    out["related"] = ctx.v(lg, "related")
    return out
