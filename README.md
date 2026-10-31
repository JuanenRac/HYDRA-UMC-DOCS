<!-- =============================================================================
HYDRA-UMC-DOCS - Architecture, interfaces, security baseline and what is proven
Copyright (C) JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
GPL-3.0-or-later - see LICENSE
============================================================================= -->

<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center">🇺🇸 <b>English</b> | <a href="README_spa.md">🇪🇸 Español</a> | <a href="README_fra.md">🇫🇷 Français</a> | <a href="README_ita.md">🇮🇹 Italiano</a> | <a href="README_deu.md">🇩🇪 Deutsch</a> | <a href="README_zho.md">🇨🇳 简体中文</a> | <a href="README_jpn.md">🇯🇵 日本語</a> | <a href="README_por.md">🇵🇹 Português</a></p>

### Architecture, interfaces, security baseline and the truth about what is proven

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-172%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.0.6-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**Honesty check - what actually runs today:** this repository holds documents and small tools. The tools (the catalogue generator, the brand generator, the README generator, the publication check and the family check) are real and have unit tests that run in CI; the nightly workflow runs them against the other repositories of the family. The documents are written from the READMEs, manifests, changelogs and documents of those repositories as they were read for this version, and a statement that could not be traced to a repository is marked as such. Nothing here is a hardware test: the capability matrix says, for each capability, whether it was only simulated, tested on a computer or run on real hardware, and the firmware repository states that no populated board exists yet.

---

> **Safety and security status:** this ecosystem is not a certified safety system. There is no hardware E-STOP path, no firmware-enforced limits or interlocks and no verified motion command yet; firmware images are checked with CRC-32 and an Ed25519 signature, and a release build refuses the published development keys (the tool heads and expansion boards behind the relay still run URTC bootloaders, which take a shared-key HMAC-SHA256 instead of a signature); TLS and mutual TLS are optional and off by default; no custom board has been populated or tested yet. Read the [security baseline](docs/SECURITY_BASELINE.md) and the [threat model](docs/THREAT_MODEL.md) before relying on any statement here for the safety of a person.

---

## 📋 At a glance

| | |
|---|---|
| Version | `0.0.6` |
| Maturity | Scaffolding |
| Tests | 172 (`python -m pytest tests -q`) |
| Stack | Markdown / Mermaid / Python / SVG |
| Target | The PC of the person using it |
| On real hardware | Not applicable: nothing here runs on hardware |

**Jump to:** [Overview](#-overview) · [Architecture](#-architecture) · [Security & Safety](#-security--safety) · [Quick start](#-quick-start) · [Testing](#-testing) · [Repository Structure](#-repository-structure) · [Related Projects](#-related-projects)

## 🚦 Project status

Each line is one part of this repository and the light says how far it is today. It is written from what the repository can show (tests, builds, runs), not from what is planned.

🟢 Done and verified · 🟡 Works, with known limits · 🟠 Partly done or not verified yet · 🔴 Not done or not working

| Area | State | What it means here |
|---|---|---|
| Software | 🟠 | Structure and first pieces only; most of the work is still to do |
| Tests | 🟡 | 172 automated tests, run on every change |
| Real hardware | 🟡 | Not applicable: nothing here runs on hardware |
| Documentation | 🟡 | README in eight languages, checked against the manifest on every change |

## 🎯 Overview

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

The picture below shows the families of repositories and the flows that their documents state.

* [Architecture](docs/ARCHITECTURE.md): layers, data flows, ports and trust boundaries.
* [Interfaces](docs/INTERFACES.md): who owns each contract and where it is documented.
* [Capability matrix](docs/CAPABILITY_MATRIX.md): what is proven in software and what needs hardware, project by project.
* [Security baseline](docs/SECURITY_BASELINE.md): what the code enforces and what is still missing; and the [threat model](docs/THREAT_MODEL.md).
* [First vertical slice](docs/FIRST_VERTICAL_SLICE.md): the smallest end-to-end path that exists today.
* [Project catalogue](docs/PROJECT_CATALOG.md): every repository of the family, written from its own manifest.
* **Tools:** `make_catalog.py` writes the catalogue, `make_brand.py` the banner, icon and family map, `make_readmes.py` the eight READMEs of this repository, `publication_check.py` looks for anything private before a publication, and `check_all.sh` runs the own checks of every repository of the family and prints one PASS, FAIL or SKIP line each. `make_glance.py` writes the At a glance table of every repository from its manifest and from `data/glance.json` (`--check` compares, `--apply` writes); after a version bump, `python tools/make_glance.py --apply --repo NAME` refreshes the table of that repository. `check_test_counts.py` counts the real tests of every repository next to this one and compares them with `data/glance.json` and with the Tests row of each README (`--apply` writes the exact counts back; Go, Rust, JavaScript, Dart and Kotlin suites are counted from the source and only reported). `i18n_cross_check.py` reads the language files of STUDIO, SUITE, ANDROID-CONTROL and WATCH into one shape, fails when a client lacks a key in any of the eight languages and lists the texts that read differently across clients (`--lang`, `--list`, `--json`). `check_claims.py` reads the English README of every repository of the family and fails when a sentence has a risk word (E-STOP, interlock, real-time, signed, mTLS, FDCAN, YOLO, AI-driven, autonomous, certified, ...) and no status marker next to it (planned, not implemented, optional, off by default, simulated, tested, ...), unless a person has read that line next to the code and put it in `data/claims_reviewed.json`.

## 🧩 Role in HYDRA-UMC

HYDRA-UMC-DOCS is the memory of the ecosystem: the place where the architecture, the interfaces, the security baseline and the capability matrix live, and where the tools that compare all the repositories side by side are kept. Each repository keeps its own README, tests and contract; this one says how they fit together and what has really been proven.

## 🏛️ Architecture

The documents describe every family of the ecosystem. The picture below is this repository itself: the tools read the manifests and the READMEs of the sibling repositories and write the catalogue, the At a glance tables, the banner and the eight READMEs, and two checks refuse what should not be published.

<p align="center">
  <img src="images/architecture.svg" alt="HYDRA-UMC-DOCS architecture" width="100%">
</p>

## 🔒 Security & Safety

| Threat | Defence | Where |
|---|---|---|
| A README that states a risky capability (an emergency stop, an interlock) without saying how far it is proven | `check_claims.py` reads the English README of every repository and fails on a sentence with a risk word that has no status marker and was not reviewed (`data/claims_reviewed.json`) | `tools/check_claims.py` |
| Something private leaving with a publication | `publication_check.py` looks for anything private in the files and the history before a publication | `tools/publication_check.py` |
| A statement that nobody can trace to a repository | The documents are written from the READMEs, manifests, changelogs and documents of the repositories, and a statement that could not be traced is marked as such | `docs/CAPABILITY_MATRIX.md` |

## 🚀 Quick start

**Requirements:** Python 3.10 or newer; pytest for the tests

```bash
python tools/make_catalog.py --check             # the catalogue is current (needs the repositories next to this one)
python tools/make_brand.py --check               # the banner, icon and map are current
python tools/make_readmes.py --check             # the eight READMEs are current
python tools/make_glance.py --check              # the At a glance tables of the family are current (needs the repositories next to this one)
python tools/status_lights.py --check            # the lights of the Project status table stay within what the manifest allows
python tools/publication_check.py                # nothing private would leave with a publication
python tools/check_claims.py --require-siblings  # no README states a risky capability without its status (needs the repositories next to this one)
bash tools/check_all.sh                          # the checks of every repository, one line each
python -m pytest tests -q                        # the unit tests of the tools
```

## 🧪 Testing

172 automated tests run with `python -m pytest tests -q`. They need no hardware and nothing outside this machine.

The CI runs `HYDRA_UMC_CI=1 python tools/ci_validate.py`, which checks the manifest, the documents, the eight READMEs and the pictures.

## 🏗️ Build & Release

`build.sh` / `build.bat` install the package and run the tests; they never change the version. `build-test.sh` / `build-test.bat` check without changing anything.

## 📂 Repository Structure

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of HYDRA-UMC-DOCS" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
HYDRA-UMC-DOCS/
├── docs/                                                                           architecture, interfaces, capability matrix, security baseline, threat model, first slice, generated catalogue
├── data/                                                                           the reviewed claims and the data of the At a glance tables
├── src/                                                                            the tools as a package (catalogue, brand, READMEs, publication check)
├── tools/                                                                          thin scripts over the package, check_all.sh, and the shared CI checks of the ecosystem
├── tests/                                                                          unit tests of the tools
├── images/                                                                         banner and map of the families
├── brand/                                                                          the icon
├── .github/                                                                        CI workflow and issue templates
├── build.sh / build.bat / build-test.sh / build-test.bat / run.sh / run.bat        builds and checks; never changes the version
├── hydra-umc.project.json / pyproject.toml / CHANGELOG.md / LICENSE / LICENSE.md   manifest: version, maturity, family
├── bump_manifest_version.py                                                        syncs the manifest version
├── bump_version.py                                                                 explicit version bump
└── test.sh                                                                         runs the tests
```

</details>

## 🗺️ Roadmap & Known limits

**Known limits today**

This repository is documents and small tools. The checks that read the other repositories (the catalogue, the At a glance tables, the claims) need those repositories checked out next to this one. It proves nothing about hardware: the capability matrix says, for each capability, whether it was only simulated or tried for real.

## 🌍 Languages

This README and the documents of the repository exist in eight languages: English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese (Portugal). They are written together and checked in the CI so that the eight files have the same sections and the same links. This repository has no screen or message catalogue of its own, so there are no interface strings to translate.

## 🔗 Related Projects

HYDRA-UMC is made of independent repositories, each with its own version, tests and README. This is the family, by group:

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-MESHES](https://github.com/JuanenRac/HYDRA-UMC-MESHES), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (this repository), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**Beyond HYDRA-UMC:**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - the same idea for the A.R.M.O.R. security ecosystem
* **[URTC](https://github.com/JuanenRac/URTC)** - the universal robot tool controller, an independent product connected through the SDK
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - the profile and the status dashboard of all the ecosystems

## 📚 Documentation

Where to read more:

* [Capability matrix: what is proven and what is not](docs/CAPABILITY_MATRIX.md)
* [Project catalogue: versions and kinds of the repositories](docs/PROJECT_CATALOG.md)
* [Security baseline of the ecosystem](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/SECURITY_BASELINE.md)
* [Threat model of the ecosystem](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/THREAT_MODEL.md)
* [Changelog of this repository](CHANGELOG.md)
* [License of this repository](LICENSE.md)

## 🤝 Contributing & Community

* Before a pull request run `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (or `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): it must print `CI_VALIDATION=PASS`. Do not run `build.sh` or `build.bat` for this check; building is not a check.
* The eight READMEs are written from one source in HYDRA-UMC-DOCS; do not edit them by hand. Change the source and write them again with `tools/make_readmes.py`.
* Do not state in a README what has not run: say "simulated" or "not tried on hardware" where that is the truth.
* See [CONTRIBUTING.md](CONTRIBUTING.md), the [code of conduct](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) and [SUPPORT.md](SUPPORT.md).

## 👤 AUTHOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENSE

GPL-3.0-or-later - [LICENSE](LICENSE).
