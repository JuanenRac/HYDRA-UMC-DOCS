<!-- =============================================================================
HYDRA-UMC-DOCS - The universal README layout in this ecosystem
Copyright (C) JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
GPL-3.0-or-later - see LICENSE
============================================================================= -->

# The universal README layout

Every repository of the four families ends up with the same README: 22 sections with a fixed name, a fixed icon and a fixed order, in eight languages. `tools/universal_readme_check.py` (a copy of the shared checker) says what differs; it is a warning in the CI of every repository until its family has finished moving.

## How a HYDRA-UMC repository gets its README

* **One source per repository** in `src/hydra_umc_docs/readme_src/repos/<NAME>.py`: its icon, its badges, and a `BODY(language, context)` that returns the Markdown of each section that the repository has. The words that every README repeats (the names of the sections, the column heads of the tables, the sentences of Languages and Contributing) live once, in eight languages, in `readme_kit.py` and `readme_src/bridge_kit.py`.
* **`service_kit.py`** holds what the services, libraries and tools share besides the bridges (the sentence that says what the toolchain needs, the testing paragraph, the Architecture block with the Mermaid text inside `<details>`) and `make_body` puts a source together from a few values (role, commands, test command).
* **Prose kept from the earlier READMEs** in `readme_src/verbatim/<NAME>/<language>/<part>.txt` (already translated). A part can carry `{tests}` and `{version}`, filled from `data/glance.json` and the manifest, so a number is never typed twice. `readme_src/fixes.py` renames the sections that this prose quotes.
* **`readme_universal.py`** writes the eight files: the header, At a glance and Project status (from `glance.py` and `status.py`, the same code `make_glance.py` uses, so the two always agree), the sections of the source, Repository Structure (from `docs/structure.json` of the repository), Languages, Documentation, Contributing, AUTHOR and LICENSE.
* **`glance_jump.py`** adds the "Jump to" line that closes At a glance, built from the sections the README really has. `glance.py` and `status.py` are shared line by line with the other documentation hub, so the line is added around them and they are not changed.

```bash
python tools/make_readmes.py --repo HYDRA-UMC-BRIDGE-CNC     # write the eight files of one repository (it must be next to this one)
python tools/make_readmes.py --check                          # this repository and every sibling that has a source
python tools/make_glance.py --apply --repo HYDRA-UMC-BRIDGE-CNC
```

A repository that has no source yet keeps its README as it is; `make_glance.py` writes its tables exactly as before.

## The two pictures

`docs/architecture.json` draws `images/architecture.svg` and `docs/structure.json` draws `images/repository-structure.svg` and the text tree of the README. Both come from the shared tools `make_architecture.py`, `make_structure.py` and `_readme_svg.py` (a copy in the `tools/` of every repository), and the repository's `tools/extra_checks.py` runs their `--check` from `ci_validate.py`. The Mermaid text that the README had stays inside a `<details>` under the picture.
