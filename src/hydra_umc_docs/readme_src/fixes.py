# HYDRA-UMC-DOCS - readme_src/fixes.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""Names of sections that the earlier READMEs quoted in their prose, mapped to the names the universal layout gives them, per language."""

FIXES: dict[str, list[tuple[str, str]]] = {
    "en": [('"Current Status & Next Steps"', '"Roadmap & Known limits"'), ("see BUILD & RUN below", "see Build & Release below"), ('"ROADMAP"', '"Roadmap & Known limits"'),
           ('"BUILD & RUN"', '"Build & Release"'), ('"BUILD & RUN GUIDE"', '"Build & Release"')],
    "es": [("ver COMPILACIÓN Y EJECUCIÓN más abajo", "ver Compilación y publicación más abajo")],
    "de": [("siehe BUILD & AUSFÜHRUNG unten", "siehe Build und Veröffentlichung unten")],
    "fr": [("« État actuel et prochaines étapes »", "« Feuille de route et limites connues »"), ("voir COMPILATION & EXÉCUTION ci-dessous", "voir Compilation et publication ci-dessous")],
    "it": [('"Stato attuale e prossimi passi"', '"Roadmap e limiti noti"'), ("vedi COMPILAZIONE ED ESECUZIONE più sotto", "vedi Compilazione e rilascio più sotto")],
    "ja": [("「現状と次のステップ」", "「ロードマップと既知の制限」"), ("「ビルドと実行」", "「ビルドとリリース」")],
    "zh": [('"构建与运行"', '"构建与发布"')],
    "pt": [("«Estado atual e próximos passos»", "«Roteiro e limites conhecidos»"), ("ver COMPILAR E EXECUTAR abaixo", "ver Compilação e publicação abaixo")],
}
