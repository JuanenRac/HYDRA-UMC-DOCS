<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | <a href="README_spa.md">🇪🇸 Español</a> | <a href="README_fra.md">🇫🇷 Français</a> | <a href="README_ita.md">🇮🇹 Italiano</a> | 🇩🇪 <b>Deutsch</b> | <a href="README_zho.md">🇨🇳 简体中文</a> | <a href="README_jpn.md">🇯🇵 日本語</a> | <a href="README_por.md">🇵🇹 Português</a></p>

### Architektur, Schnittstellen, Sicherheitsbasis und die Wahrheit über das, was belegt ist

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.0.4-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**Ehrlichkeitsprüfung - was heute wirklich läuft:** dieses Repository enthält Dokumente und kleine Werkzeuge. Die Werkzeuge (der Katalog-Generator, der Marken-Generator, der README-Generator, die Veröffentlichungsprüfung und die Familienprüfung) sind echt und haben Unit-Tests, die in der CI laufen; der nächtliche Workflow führt sie gegen die übrigen Repositories der Familie aus. Die Dokumente sind aus den READMEs, Manifesten, Änderungsprotokollen und Dokumenten dieser Repositories geschrieben, wie sie für diese Version gelesen wurden, und eine Aussage, die sich nicht auf ein Repository zurückführen ließ, ist als solche gekennzeichnet. Nichts davon ist ein Hardwaretest: Die Fähigkeitenmatrix sagt für jede Fähigkeit, ob sie nur simuliert, auf einem Computer getestet oder auf echter Hardware ausgeführt wurde, und das Firmware-Repository gibt an, dass noch keine bestückte Platine existiert.

---

> **Stand von Sicherheit (Safety) und Security:** Dieses Ökosystem ist kein zertifiziertes Sicherheitssystem. Es gibt noch keinen Hardware-E-STOP-Pfad, keine von der Firmware durchgesetzten Grenzen oder Verriegelungen und keinen verifizierten Bewegungsbefehl; Firmware-Images werden mit CRC32 und einem HMAC-SHA256 mit gemeinsamem Schlüssel geprüft, nicht mit einer asymmetrischen Signatur; TLS und gegenseitiges TLS sind optional und standardmäßig aus; noch keine eigene Platine wurde bestückt oder getestet. Lesen Sie die [Sicherheitsbasis](docs/SECURITY_BASELINE.md) und das [Bedrohungsmodell](docs/THREAT_MODEL.md), bevor Sie sich für die Sicherheit einer Person auf eine Aussage hier verlassen.

## 📋 Auf einen Blick

| | |
|---|---|
| Version | `0.0.4` |
| Reifegrad | Gerüst |
| Technik | Markdown / Mermaid / Python / SVG |
| Ziel | Der PC der Person, die es benutzt |
| Auf echter Hardware | Nicht zutreffend: nichts hiervon läuft auf Hardware |

## 🚦 Projektstatus

Jede Zeile ist ein Teil dieses Repositorys, und die Ampel sagt, wie weit er heute ist. Sie beruht auf dem, was das Repository zeigen kann (Tests, Builds, Läufe), nicht auf dem, was geplant ist.

🟢 Fertig und überprüft · 🟡 Funktioniert, mit bekannten Grenzen · 🟠 Teilweise fertig oder noch nicht überprüft · 🔴 Nicht gemacht oder funktioniert nicht

| Bereich | Stand | Was das hier bedeutet |
|---|---|---|
| Software | 🟠 | Nur Struktur und erste Teile; der größte Teil der Arbeit steht noch aus |
| Tests | 🟠 | Für dieses Repository ist noch keine Testanzahl vermerkt |
| Echte Hardware | 🟢 | Nicht zutreffend: nichts hiervon läuft auf Hardware |
| Dokumentation | 🟢 | README in acht Sprachen, bei jeder Änderung gegen das Manifest geprüft |

## 🎯 Überblick

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

Das Bild unten zeigt die Familien von Repositories und die Datenflüsse, die ihre Dokumente behaupten.

* [Architektur](docs/ARCHITECTURE.md): Schichten, Datenflüsse, Ports und Vertrauensgrenzen.
* [Schnittstellen](docs/INTERFACES.md): wem jeder Vertrag gehört und wo er dokumentiert ist.
* [Fähigkeitenmatrix](docs/CAPABILITY_MATRIX.md): was in Software belegt ist und was Hardware braucht, Projekt für Projekt.
* [Sicherheitsbasis](docs/SECURITY_BASELINE.md): was der Code durchsetzt und was noch fehlt; und das [Bedrohungsmodell](docs/THREAT_MODEL.md).
* [Erster vertikaler Schnitt](docs/FIRST_VERTICAL_SLICE.md): der kleinste durchgehende Pfad, den es heute gibt.
* [Projektkatalog](docs/PROJECT_CATALOG.md): jedes Repository der Familie, aus seinem eigenen Manifest geschrieben.
* **Werkzeuge:** `make_catalog.py` schreibt den Katalog, `make_brand.py` das Banner, das Symbol und die Familienkarte, `make_readmes.py` die acht READMEs dieses Repositorys, `publication_check.py` sucht vor einer Veröffentlichung nach allem Privaten, und `check_all.sh` führt die eigenen Prüfungen jedes Repositorys der Familie aus und gibt je eine Zeile PASS, FAIL oder SKIP aus. `make_glance.py` schreibt die Tabelle Auf einen Blick jedes Repositorys aus dessen Manifest und aus `data/glance.json` (`--check` vergleicht, `--apply` schreibt); nach einer Versionserhöhung aktualisiert `python tools/make_glance.py --apply --repo NAME` die Tabelle dieses Repositorys. `check_claims.py` liest das englische README jedes Repositorys der Familie und schlägt fehl, wenn ein Satz ein Risikowort enthält (E-STOP, Verriegelung, Echtzeit, signiert, mTLS, FDCAN, YOLO, KI-gesteuert, autonom, zertifiziert, ...) und daneben keine Statusmarkierung steht (geplant, nicht implementiert, optional, standardmäßig aus, simuliert, getestet, ...), es sei denn, eine Person hat diese Zeile neben dem Code gelesen und in `data/claims_reviewed.json` eingetragen.

## 🧩 Rolle in HYDRA-UMC

HYDRA-UMC-DOCS ist das Gedächtnis des Ökosystems: der Ort, an dem Architektur, Schnittstellen, Sicherheitsbasis und Fähigkeitenmatrix liegen und an dem die Werkzeuge aufbewahrt werden, die alle Repositories nebeneinander vergleichen. Jedes Repository behält sein eigenes README, seine Tests und seinen Vertrag; dieses sagt, wie sie zusammenpassen und was wirklich belegt wurde.

## 📂 Repository-Struktur

```text
HYDRA-UMC-DOCS/
├── docs/     Architektur, Schnittstellen, Fähigkeitenmatrix, Sicherheitsbasis, Bedrohungsmodell, erster Schnitt, erzeugter Katalog
├── data/     die geprüften Aussagen und die Daten der Tabellen Auf einen Blick
├── src/      die Werkzeuge als Paket (Katalog, Marke, READMEs, Veröffentlichungsprüfung)
├── tools/    dünne Skripte über dem Paket, check_all.sh und die gemeinsamen CI-Prüfungen des Ökosystems
├── tests/    Unit-Tests der Werkzeuge
├── images/   Banner und Karte der Familien
├── brand/    das Symbol
├── build.sh / build.bat, build-test.sh / build-test.bat, run.sh / run.bat
└── hydra-umc.project.json, pyproject.toml, CHANGELOG.md, LICENSE, LICENSE.md
```

## 🛠️ BUILD & AUSFÜHRUNG

**Voraussetzungen:** Python 3.10 oder neuer; pytest für die Tests

```bash
python tools/make_catalog.py --check             # der Katalog ist aktuell (braucht die Repositories neben diesem)
python tools/make_brand.py --check               # Banner, Symbol und Karte sind aktuell
python tools/make_readmes.py --check             # die acht READMEs sind aktuell
python tools/make_glance.py --check              # die Tabellen Auf einen Blick der Familie sind aktuell (braucht die Repositories neben diesem)
python tools/publication_check.py                # nichts Privates würde mit einer Veröffentlichung hinausgehen
python tools/check_claims.py --require-siblings  # kein README nennt eine riskante Fähigkeit ohne ihren Status (braucht die Repositorys neben diesem)
bash tools/check_all.sh                          # die Prüfungen jedes Repositorys, eine Zeile je Repository
python -m pytest tests -q                        # die Unit-Tests der Werkzeuge
```

`build.sh` / `build.bat` erhöhen die Version um einen Schritt (der Kilometerzähler des Ökosystems), installieren das Paket und führen die Tests aus; `build-test.sh` / `build-test.bat` prüfen, ohne eine Version zu ändern.

## 🔗 Verwandte Projekte

HYDRA-UMC besteht aus unabhängigen Repositories mit jeweils eigener Version, eigenen Tests und eigenem README. Das ist die Familie, nach Gruppen:

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (dieses Repository), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**Über HYDRA-UMC hinaus:**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - dieselbe Idee für das Sicherheits-Ökosystem A.R.M.O.R.
* **[URTC](https://github.com/JuanenRac/URTC)** - der universelle Roboter-Werkzeugcontroller, ein eigenständiges Produkt, das über das SDK angebunden ist
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - das Profil und das Status-Dashboard aller Ökosysteme

## 📚 Dokumentation & Community

Wo man mehr liest:

* [Fähigkeitenmatrix: was belegt ist und was nicht](docs/CAPABILITY_MATRIX.md)
* [Projektkatalog: Versionen und Arten der Repositories](docs/PROJECT_CATALOG.md)
* [Änderungsprotokoll dieses Repositorys](CHANGELOG.md)
* [Lizenz (GPL-3.0-or-later)](LICENSE)
* Fragen, Ideen und Meldungen: electrohobby3d@gmail.com

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LIZENZ

Software: GPL-3.0-or-later - siehe [LICENSE](LICENSE). Dokumentation: CC BY-SA 4.0 - siehe [LICENSE.md](LICENSE.md).
