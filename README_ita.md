<!-- =============================================================================
HYDRA-UMC-DOCS - Architecture, interfaces, security baseline and what is proven
Copyright (C) JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
GPL-3.0-or-later - see LICENSE
============================================================================= -->

<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | <a href="README_spa.md">🇪🇸 Español</a> | <a href="README_fra.md">🇫🇷 Français</a> | 🇮🇹 <b>Italiano</b> | <a href="README_deu.md">🇩🇪 Deutsch</a> | <a href="README_zho.md">🇨🇳 简体中文</a> | <a href="README_jpn.md">🇯🇵 日本語</a> | <a href="README_por.md">🇵🇹 Português</a></p>

### Architettura, interfacce, base di sicurezza e la verità su ciò che è provato

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-172%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.0.6-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**Verifica di onestà - cosa funziona davvero oggi:** questo repository contiene documenti e piccoli strumenti. Gli strumenti (il generatore del catalogo, quello del marchio, quello dei README, il controllo di pubblicazione e il controllo della famiglia) sono reali e hanno test unitari eseguiti in CI; il workflow notturno li esegue sugli altri repository della famiglia. I documenti sono scritti a partire dai README, manifesti, registri delle modifiche e documenti di quei repository così come sono stati letti per questa versione, e un'affermazione che non si è potuta ricondurre a un repository è segnalata come tale. Nulla qui è un test hardware: la matrice delle capacità dice, per ogni capacità, se è stata solo simulata, provata su un computer o eseguita su hardware reale, e il repository del firmware dichiara che non esiste ancora alcuna scheda assemblata.

---

> **Stato di sicurezza (safety e security):** questo ecosistema non è un sistema di sicurezza certificato. Non esiste ancora un percorso E-STOP hardware, né limiti o interblocchi imposti dal firmware, né un comando di movimento verificato; le immagini firmware sono controllate con CRC-32 e una firma Ed25519, e una compilazione di rilascio rifiuta le chiavi di sviluppo pubblicate (le teste utensile e le schede di espansione dietro il relè usano ancora i bootloader di URTC, che accettano un HMAC-SHA256 a chiave condivisa invece di una firma); TLS e TLS reciproco sono opzionali e disattivati per impostazione predefinita; nessuna scheda propria è stata ancora assemblata o provata. Leggi la [base di sicurezza](docs/SECURITY_BASELINE.md) e il [modello delle minacce](docs/THREAT_MODEL.md) prima di fidarti di qualsiasi affermazione qui per la sicurezza di una persona.

---

## 📋 In breve

| | |
|---|---|
| Versione | `0.0.6` |
| Maturità | Impalcatura |
| Test | 172 (`python -m pytest tests -q`) |
| Tecnologia | Markdown / Mermaid / Python / SVG |
| Destinazione | Il PC di chi lo usa |
| Su hardware reale | Non applicabile: nulla qui gira su hardware |

**Vai a:** [Panoramica](#-panoramica) · [Architettura](#-architettura) · [Sicurezza e protezione](#-sicurezza-e-protezione) · [Avvio rapido](#-avvio-rapido) · [Test](#-test) · [Struttura del repository](#-struttura-del-repository) · [Progetti correlati](#-progetti-correlati)

## 🚦 Stato del progetto

Ogni riga è una parte di questo repository e il semaforo dice a che punto è oggi. È scritta in base a ciò che il repository può mostrare (test, compilazioni, esecuzioni), non a ciò che è previsto.

🟢 Fatto e verificato · 🟡 Funziona, con limiti noti · 🟠 Fatto a metà o non ancora verificato · 🔴 Non fatto o non funzionante

| Area | Stato | Cosa significa qui |
|---|---|---|
| Software | 🟠 | Solo struttura e primi pezzi; gran parte del lavoro è ancora da fare |
| Test | 🟡 | 172 test automatici, eseguiti a ogni modifica |
| Hardware reale | 🟡 | Non applicabile: nulla qui gira su hardware |
| Documentazione | 🟡 | README in otto lingue, verificato rispetto al manifesto a ogni modifica |

## 🎯 Panoramica

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

L'immagine qui sotto mostra le famiglie di repository e i flussi che i loro documenti affermano.

* [Architettura](docs/ARCHITECTURE.md): livelli, flussi di dati, porte e confini di fiducia.
* [Interfacce](docs/INTERFACES.md): chi possiede ogni contratto e dove è documentato.
* [Matrice delle capacità](docs/CAPABILITY_MATRIX.md): cosa è provato in software e cosa richiede hardware, progetto per progetto.
* [Base di sicurezza](docs/SECURITY_BASELINE.md): cosa il codice impone e cosa manca ancora; e il [modello delle minacce](docs/THREAT_MODEL.md).
* [Prima fetta verticale](docs/FIRST_VERTICAL_SLICE.md): il più piccolo percorso da un capo all'altro che esiste oggi.
* [Catalogo dei progetti](docs/PROJECT_CATALOG.md): ogni repository della famiglia, scritto a partire dal proprio manifesto.
* **Strumenti:** `make_catalog.py` scrive il catalogo, `make_brand.py` il banner, l'icona e la mappa delle famiglie, `make_readmes.py` gli otto README di questo repository, `publication_check.py` cerca qualsiasi cosa privata prima di una pubblicazione e `check_all.sh` esegue i controlli propri di ogni repository della famiglia e stampa una riga PASS, FAIL o SKIP per ciascuno. `make_glance.py` scrive la tabella In breve di ogni repository dal suo manifesto e da `data/glance.json` (`--check` confronta, `--apply` scrive); dopo un aumento di versione, `python tools/make_glance.py --apply --repo NOME` aggiorna la tabella di quel repository. `check_claims.py` legge il README inglese di ogni repository della famiglia e fallisce quando una frase contiene una parola a rischio (E-STOP, interblocco, tempo reale, firmato, mTLS, FDCAN, YOLO, guidato dall'IA, autonomo, certificato, ...) senza un indicatore di stato accanto (previsto, non implementato, opzionale, disattivato per impostazione predefinita, simulato, provato, ...), a meno che una persona abbia letto quella riga accanto al codice e l'abbia inserita in `data/claims_reviewed.json`.

## 🧩 Ruolo in HYDRA-UMC

HYDRA-UMC-DOCS è la memoria dell'ecosistema: il luogo in cui vivono l'architettura, le interfacce, la base di sicurezza e la matrice delle capacità, e dove si conservano gli strumenti che confrontano tutti i repository fianco a fianco. Ogni repository conserva il proprio README, i propri test e il proprio contratto; questo dice come si incastrano e cosa è stato davvero provato.

## 🏛️ Architettura

I documenti descrivono ogni famiglia dell'ecosistema. L'immagine qui sotto è questo stesso repository: gli strumenti leggono i manifesti e i README dei repository fratelli e scrivono il catalogo, le tabelle In breve, il banner e gli otto README, e due controlli rifiutano ciò che non deve essere pubblicato.

<p align="center">
  <img src="images/architecture.svg" alt="HYDRA-UMC-DOCS architecture" width="100%">
</p>

## 🔒 Sicurezza e protezione

| Minaccia | Difesa | Dove |
|---|---|---|
| Un README che dichiara una capacità a rischio (un arresto di emergenza, un interblocco) senza dire fino a dove è provata | `check_claims.py` legge il README inglese di ogni repository e fallisce su una frase con una parola di rischio senza indicatore di stato e non rivista (`data/claims_reviewed.json`) | `tools/check_claims.py` |
| Qualcosa di privato che esce con una pubblicazione | `publication_check.py` cerca qualsiasi cosa privata nei file e nella cronologia prima di una pubblicazione | `tools/publication_check.py` |
| Un'affermazione che nessuno può ricondurre a un repository | I documenti sono scritti a partire da README, manifesti, registri delle modifiche e documenti dei repository, e un'affermazione non rintracciabile è segnata come tale | `docs/CAPABILITY_MATRIX.md` |

## 🚀 Avvio rapido

**Requisiti:** Python 3.10 o successivo; pytest per i test

```bash
python tools/make_catalog.py --check             # il catalogo è aggiornato (servono i repository accanto a questo)
python tools/make_brand.py --check               # il banner, l'icona e la mappa sono aggiornati
python tools/make_readmes.py --check             # gli otto README sono aggiornati
python tools/make_glance.py --check              # le tabelle In breve della famiglia sono aggiornate (servono i repository accanto a questo)
python tools/status_lights.py --check            # i semafori della tabella Stato del progetto restano entro ciò che il manifesto consente
python tools/publication_check.py                # nulla di privato uscirebbe con una pubblicazione
python tools/check_claims.py --require-siblings  # nessun README afferma una capacità a rischio senza il suo stato (richiede i repository accanto a questo)
bash tools/check_all.sh                          # i controlli di ogni repository, una riga ciascuno
python -m pytest tests -q                        # i test unitari degli strumenti
```

## 🧪 Test

172 test automatici si eseguono con `python -m pytest tests -q`. Non richiedono hardware né nulla al di fuori di questa macchina.

La CI esegue `HYDRA_UMC_CI=1 python tools/ci_validate.py`, che controlla il manifesto, i documenti, gli otto README e le immagini.

## 🏗️ Compilazione e rilascio

`build.sh` / `build.bat` installano il pacchetto ed eseguono i test; non cambiano mai la versione. `build-test.sh` / `build-test.bat` controllano senza cambiare nulla.

## 📂 Struttura del repository

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of HYDRA-UMC-DOCS" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
HYDRA-UMC-DOCS/
├── docs/                                                                           architettura, interfacce, matrice delle capacità, base di sicurezza, modello delle minacce, prima fetta, catalogo generato
├── data/                                                                           le affermazioni verificate e i dati delle tabelle In breve
├── src/                                                                            gli strumenti come pacchetto (catalogo, marchio, README, controllo di pubblicazione)
├── tools/                                                                          script sottili sopra il pacchetto, check_all.sh e i controlli CI condivisi dell'ecosistema
├── tests/                                                                          test unitari degli strumenti
├── images/                                                                         banner e mappa delle famiglie
├── brand/                                                                          l'icona
├── .github/                                                                        workflow di CI e modelli di segnalazione
├── build.sh / build.bat / build-test.sh / build-test.bat / run.sh / run.bat        compila e controlla; non cambia mai la versione
├── hydra-umc.project.json / pyproject.toml / CHANGELOG.md / LICENSE / LICENSE.md   manifesto: versione, maturità, famiglia
├── bump_manifest_version.py                                                        sincronizza la versione del manifesto
├── bump_version.py                                                                 aumento di versione esplicito
└── test.sh                                                                         esegue i test
```

</details>

## 🗺️ Roadmap e limiti noti

**Limiti noti oggi**

Questo repository è fatto di documenti e piccoli strumenti. I controlli che leggono gli altri repository (il catalogo, le tabelle In breve, le affermazioni) richiedono quei repository scaricati accanto a questo. Non prova nulla sull'hardware: la matrice delle capacità dice, per ogni capacità, se è stata solo simulata o provata davvero.

## 🌍 Lingue

Questo README e i documenti del repository esistono in otto lingue: inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese (Portogallo). Sono scritti insieme e la CI verifica che gli otto file abbiano le stesse sezioni e gli stessi link. Questo repository non ha uno schermo né un catalogo di messaggi propri, quindi non ci sono stringhe di interfaccia da tradurre.

## 🔗 Progetti correlati

HYDRA-UMC è fatto di repository indipendenti, ciascuno con la propria versione, i propri test e il proprio README. Ecco la famiglia, per gruppi:

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (questo repository), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**Oltre HYDRA-UMC:**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - la stessa idea per l'ecosistema di sicurezza A.R.M.O.R.
* **[URTC](https://github.com/JuanenRac/URTC)** - il controller universale di utensile per robot, un prodotto indipendente collegato tramite l'SDK
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - il profilo e il pannello di stato di tutti gli ecosistemi

## 📚 Documentazione

Dove leggere di più:

* [Matrice delle capacità: cosa è provato e cosa no](docs/CAPABILITY_MATRIX.md)
* [Catalogo dei progetti: versioni e tipi dei repository](docs/PROJECT_CATALOG.md)
* [Base di sicurezza dell'ecosistema](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/SECURITY_BASELINE.md)
* [Modello delle minacce dell'ecosistema](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/THREAT_MODEL.md)
* [Registro delle modifiche di questo repository](CHANGELOG.md)
* [Licenza di questo repository](LICENSE.md)

## 🤝 Contribuire e comunità

* Prima di una pull request esegui `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (oppure `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): deve stampare `CI_VALIDATION=PASS`. Non eseguire `build.sh` né `build.bat` per questa verifica; compilare non è verificare.
* I otto README sono scritti da un'unica fonte in HYDRA-UMC-DOCS; non modificarli a mano. Cambia la fonte e riscrivili con `tools/make_readmes.py`.
* Non affermare in un README ciò che non è stato eseguito: scrivi «simulato» o «non provato su hardware» quando è la verità.
* Vedi [CONTRIBUTING.md](CONTRIBUTING.md), il [codice di condotta](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) e [SUPPORT.md](SUPPORT.md).

## 👤 AUTORE

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENZA

GPL-3.0-or-later - [LICENSE](LICENSE).
