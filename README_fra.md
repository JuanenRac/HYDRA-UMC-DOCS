<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | <a href="README_spa.md">🇪🇸 Español</a> | 🇫🇷 <b>Français</b> | <a href="README_ita.md">🇮🇹 Italiano</a> | <a href="README_deu.md">🇩🇪 Deutsch</a> | <a href="README_zho.md">🇨🇳 简体中文</a> | <a href="README_jpn.md">🇯🇵 日本語</a> | <a href="README_por.md">🇵🇹 Português</a></p>

### Architecture, interfaces, socle de sécurité et la vérité sur ce qui est prouvé

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.0.3-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**Vérification d'honnêteté - ce qui fonctionne réellement aujourd'hui :** ce dépôt contient des documents et de petits outils. Les outils (le générateur du catalogue, celui de la marque, celui des README, la vérification de publication et la vérification de la famille) sont réels et ont des tests unitaires exécutés en CI ; le workflow nocturne les exécute sur les autres dépôts de la famille. Les documents sont écrits à partir des README, manifestes, journaux de modifications et documents de ces dépôts tels qu'ils ont été lus pour cette version, et une affirmation qui n'a pu être reliée à un dépôt est signalée comme telle. Rien ici n'est un test matériel : la matrice des capacités indique, pour chaque capacité, si elle a seulement été simulée, testée sur un ordinateur ou exécutée sur du matériel réel, et le dépôt du firmware indique qu'aucune carte assemblée n'existe encore.

---

> **État de la sûreté et de la cybersécurité :** cet écosystème n'est pas un système de sécurité certifié. Il n'existe pas encore de chaîne d'E-STOP matérielle, ni de limites ou de verrouillages imposés par le firmware, ni de commande de mouvement vérifiée ; les images de firmware sont contrôlées par CRC32 et un HMAC-SHA256 à clé partagée, pas par une signature asymétrique ; TLS et TLS mutuel sont optionnels et désactivés par défaut ; aucune carte propre n'a encore été assemblée ni testée. Lisez la [base de sécurité](docs/SECURITY_BASELINE.md) et le [modèle de menaces](docs/THREAT_MODEL.md) avant de vous fier à une affirmation d'ici pour la sécurité d'une personne.

## 📋 En un coup d'œil

| | |
|---|---|
| Version | `0.0.3` |
| Maturité | Ébauche |
| Technologie | Markdown / Mermaid / Python / SVG |
| Cible | Le PC de la personne qui l'utilise |
| Sur matériel réel | Sans objet : rien ici ne s'exécute sur du matériel |

## 🚦 État du projet

Chaque ligne est une partie de ce dépôt et le feu dit où elle en est aujourd'hui. Elle est écrite d'après ce que le dépôt peut montrer (tests, compilations, exécutions), pas d'après ce qui est prévu.

🟢 Fait et vérifié · 🟡 Fonctionne, avec des limites connues · 🟠 À moitié fait ou pas encore vérifié · 🔴 Pas fait ou ne fonctionne pas

| Domaine | État | Ce que cela veut dire ici |
|---|---|---|
| Logiciel | 🟠 | Seulement la structure et les premières pièces ; l'essentiel du travail reste à faire |
| Tests | 🟠 | Aucun nombre de tests n'est encore consigné pour ce dépôt |
| Matériel réel | 🟢 | Sans objet : rien ici ne s'exécute sur du matériel |
| Documentation | 🟢 | README en huit langues, vérifié par rapport au manifeste à chaque modification |

## 🎯 Vue d'ensemble

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

L'image ci-dessous montre les familles de dépôts et les flux qu'affirment leurs documents.

* [Architecture](docs/ARCHITECTURE.md): couches, flux de données, ports et frontières de confiance.
* [Interfaces](docs/INTERFACES.md): qui possède chaque contrat et où il est documenté.
* [Matrice des capacités](docs/CAPABILITY_MATRIX.md): ce qui est prouvé en logiciel et ce qui exige du matériel, projet par projet.
* [Socle de sécurité](docs/SECURITY_BASELINE.md): ce que le code impose et ce qui manque encore ; et le [modèle de menaces](docs/THREAT_MODEL.md).
* [Première tranche verticale](docs/FIRST_VERTICAL_SLICE.md): le plus petit chemin de bout en bout qui existe aujourd'hui.
* [Catalogue des projets](docs/PROJECT_CATALOG.md): chaque dépôt de la famille, écrit à partir de son propre manifeste.
* **Outils :** `make_catalog.py` écrit le catalogue, `make_brand.py` la bannière, l'icône et la carte des familles, `make_readmes.py` les huit README de ce dépôt, `publication_check.py` cherche tout ce qui serait privé avant une publication, et `check_all.sh` lance les vérifications propres à chaque dépôt de la famille et affiche une ligne PASS, FAIL ou SKIP pour chacun. `make_glance.py` écrit le tableau En un coup d'œil de chaque dépôt à partir de son manifeste et de `data/glance.json` (`--check` compare, `--apply` écrit) ; après un changement de version, `python tools/make_glance.py --apply --repo NOM` met à jour le tableau de ce dépôt. `check_claims.py` lit le README anglais de chaque dépôt de la famille et échoue lorsqu'une phrase contient un mot à risque (E-STOP, verrouillage, temps réel, signé, mTLS, FDCAN, YOLO, piloté par IA, autonome, certifié, ...) sans marqueur d'état à côté (prévu, non implémenté, optionnel, désactivé par défaut, simulé, testé, ...), sauf si une personne a lu cette ligne à côté du code et l'a inscrite dans `data/claims_reviewed.json`.

## 🧩 Rôle dans HYDRA-UMC

HYDRA-UMC-DOCS est la mémoire de l'écosystème : l'endroit où vivent l'architecture, les interfaces, le socle de sécurité et la matrice des capacités, et où sont gardés les outils qui comparent tous les dépôts côte à côte. Chaque dépôt garde son propre README, ses tests et son contrat ; celui-ci dit comment ils s'assemblent et ce qui a réellement été prouvé.

## 📂 Structure du dépôt

```text
HYDRA-UMC-DOCS/
├── docs/     architecture, interfaces, matrice des capacités, socle de sécurité, modèle de menaces, première tranche, catalogue généré
├── src/      les outils sous forme de paquet (catalogue, marque, README, vérification de publication)
├── tools/    scripts fins au-dessus du paquet, check_all.sh et les vérifications de CI partagées de l'écosystème
├── tests/    tests unitaires des outils
├── images/   bannière et carte des familles
├── brand/    l'icône
├── build.sh / build.bat, build-test.sh / build-test.bat, run.sh / run.bat
└── hydra-umc.project.json, pyproject.toml, CHANGELOG.md, LICENSE, LICENSE.md
```

## 🛠️ COMPILATION ET EXÉCUTION

**Prérequis :** Python 3.10 ou plus récent ; pytest pour les tests

```bash
python tools/make_catalog.py --check             # le catalogue est à jour (nécessite les dépôts à côté de celui-ci)
python tools/make_brand.py --check               # la bannière, l'icône et la carte sont à jour
python tools/make_readmes.py --check             # les huit README sont à jour
python tools/make_glance.py --check              # les tableaux En un coup d'œil de la famille sont à jour (nécessite les dépôts à côté de celui-ci)
python tools/publication_check.py                # rien de privé ne partirait avec une publication
python tools/check_claims.py --require-siblings  # aucun README n'affirme une capacité risquée sans son statut (nécessite les dépôts à côté de celui-ci)
bash tools/check_all.sh                          # les vérifications de chaque dépôt, une ligne chacun
python -m pytest tests -q                        # les tests unitaires des outils
```

`build.sh` / `build.bat` avancent la version d'un cran (le compteur kilométrique de l'écosystème), installent le paquet et lancent les tests ; `build-test.sh` / `build-test.bat` vérifient sans changer aucune version.

## 🔗 Projets liés

HYDRA-UMC est fait de dépôts indépendants, chacun avec sa version, ses tests et son README. Voici la famille, par groupes :

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (ce dépôt), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**Au-delà de HYDRA-UMC :**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - la même idée pour l'écosystème de sécurité A.R.M.O.R.
* **[URTC](https://github.com/JuanenRac/URTC)** - le contrôleur universel d'outil de robot, un produit indépendant relié par le SDK
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - le profil et le tableau d'état de tous les écosystèmes

## 📚 Documentation et communauté

Pour en savoir plus :

* [Matrice des capacités : ce qui est prouvé et ce qui ne l'est pas](docs/CAPABILITY_MATRIX.md)
* [Catalogue des projets : versions et types des dépôts](docs/PROJECT_CATALOG.md)
* [Journal des modifications de ce dépôt](CHANGELOG.md)
* [Licence (GPL-3.0-or-later)](LICENSE)
* Questions, idées et rapports : electrohobby3d@gmail.com

## 👤 AUTEUR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENCE

Logiciel : GPL-3.0-or-later - voir [LICENSE](LICENSE). Documentation : CC BY-SA 4.0 - voir [LICENSE.md](LICENSE.md).
