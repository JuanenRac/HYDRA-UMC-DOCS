<!--
=============================================================================
HYDRA-UMC-DOCS - Project catalogue of the HYDRA-UMC ecosystem
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# Project catalogue

Every repository of the family, written by `tools/make_catalog.py` from the `hydra-umc.project.json` of each repository found next to this one, so that no version, maturity or role in the tables can be behind its project. Nothing between the two markers is typed by hand; the text around them is.

* **Family** is the `family` of the manifest. **Parent** is its `parent`: the repository that is the integration parent of the family, `-` for a root.
* **Maturity** follows the SDK's definition (`HYDRA-UMC-SDK/docs/PROJECT_MANIFEST.md`): *scaffolding* is real, tested code not yet exercised in its real context; *functional* has been exercised against some real target; *established* has seen sustained real use in this ecosystem's deployment; *production* is a continuous, unattended deployment with no known open gap, and no repository claims it. How far each capability is proven is the [capability matrix](CAPABILITY_MATRIX.md), not this column.
* **What it is** is a sentence written for this catalogue from the manifest and README of each repository (`src/hydra_umc_docs/descriptions.py`); a repository without one shows the start of the notes of its manifest.
* The firmware repository is called exactly `HYDRA-UMC`. `URTC` and its tools are an independent ecosystem with its own manifest (`urtc.project.json`), and `ELECTRO-HOBBY-3D-UPDATER` belongs to none of the three ecosystems: it dispatches to the updaters of HYDRA-UMC, URTC and A.R.M.O.R. Neither is in the tables.
* Regenerate with `python tools/make_catalog.py` (the repositories must sit next to this one); `--check` fails when the table is stale and `--check-structure` fails only when a repository appeared or disappeared or changed kind.

<!-- catalog:begin -->
**56 repositories** in 13 families: 1 scaffolding, 21 functional, 34 established.

### Cognitive AI Node

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE) | 0.1.4 | Functional | service | python | cm5 | - | Integration hub of the Hailo-10 cognitive family; reports the readiness of its four children. |
| [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA) | 0.1.3 | Established | api | python | cm5 | HYDRA-UMC-COGNITIVE-NODE | Stdlib-only TF-IDF search over the ecosystem's own Markdown documents, with citations; lexical, not semantic. |
| [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN) | 0.1.6 | Functional | service | python | cm5 | HYDRA-UMC-COGNITIVE-NODE | Read-only diagnostic assistant with a fixed risk-level policy and tool allowlist; a retrieved document can never trigger a tool call. |
| [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER) | 0.1.2 | Established | service | python | cm5 | HYDRA-UMC-COGNITIVE-NODE | Rule-based task decomposition and semantic recovery over MCU error codes. |
| [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE) | 0.1.6 | Established | service | python | cm5 | HYDRA-UMC-COGNITIVE-NODE | Action-token encoding and decoding and trajectory generation for a vision-language-action model. |
| [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI) | 0.1.5 | Established | service | python | cm5 | HYDRA-UMC-COGNITIVE-NODE | Voice front end: voice-activity detection, rule-based intent parsing and a confirmation-gated Watch relay. |

### Complementary Tools

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI) | 0.1.4 | Established | ui | node | cm5 | - | Text summaries of DATALAKE history (min, max, average, trend) and anomaly highlighting, with a statistical fallback when no AI provider is configured. |
| [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI) | 0.1.4 | Established | cli | go | user-pc | - | Command-line client: version, status, robots, doctor and a dry-run configuration apply. |
| [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH) | 0.2.4 | Functional | ui | android | wearable | - | Wear OS companion with haptic alert patterns and a voice-command capture. |

### Core Backend & Clients

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER) | 0.8.0.9 | Established | api | node | cm5 | - | Headless Node.js/TypeScript backend: REST and WebSocket API, authentication, mDNS discovery and the global stop. |
| [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL) | 0.6.8 | Established | ui | android | mobile | HYDRA-UMC-SERVER | Native Android control app with biometric login, a client of HYDRA-UMC-SERVER. |
| [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI) | 0.2.4 | Established | ui | flutter | cm5 | HYDRA-UMC-SERVER | Flutter touch interface for the onboard 7 inch DSI display of the CM5. |
| [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL) | 0.1.5 | Functional | tool | python | user-pc | HYDRA-UMC-STUDIO | Desktop STL editor for the model libraries shared by STUDIO and SUITE. |
| [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF) | 0.1.3 | Established | tool | python | user-pc | HYDRA-UMC-STUDIO | Desktop URDF creator and editor that pushes finished models into the shared model catalogue. |
| [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL) | 0.2.4 | Established | ui | flutter | mobile | HYDRA-UMC-SERVER | Flutter control app for iOS and iPadOS with a real-time WebSocket link to HYDRA-UMC-SERVER. |
| [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO) | 0.7.9 | Established | ui | node | cm5 | HYDRA-UMC-SERVER | Web control dashboard (React) with 3D multi-robot visualisation, a client of HYDRA-UMC-SERVER. |
| [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE) | 0.6.7 | Established | ui | python | user-pc | HYDRA-UMC-SERVER | Desktop (PySide6) command centre for several servers at once. |

### Core Hardware

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC) | 0.2.1 | Functional | firmware | firmware-c | user-pc | - | Motion-control firmware (STM32H745 and STM32G474, six components with bootloaders) and the CM5 SPI-OTA bridge; not yet run on a real board. |

### Data & Analytics

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE) | 0.1.7 | Established | api | python | cm5 | - | SQLite time-series store with an HTTP ingest and query API. |
| [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR) | 0.1.6 | Established | api | python | cm5 | HYDRA-UMC-DATALAKE | FFT and statistical-baseline anomaly detector over DATALAKE history, with drift monitoring (no machine-learning model). |
| [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS) | 0.1.4 | Established | api | python | cm5 | HYDRA-UMC-DATALAKE | OEE and availability reports over DATALAKE history, with reproducible CSV export. |
| [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR) | 0.1.6 | Established | api | go | cm5 | HYDRA-UMC-DATALAKE | CAN and WebSocket ingestion with a bounded buffer, retry on outage and a DATALAKE sink. |

### Digital Twin & Simulation

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN) | 0.0.8 | Established | service | rust | cm5 | - | Integration hub of the digital-twin family with a version-compatibility check of its children. |
| [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE) | 0.0.9 | Functional | service | rust | cm5 | HYDRA-UMC-TWIN | Hardware-in-the-loop routing with an interlock that blocks commands to real hardware in the wrong mode. |
| [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA) | 0.0.7 | Established | library | rust | cm5 | HYDRA-UMC-TWIN | Forward kinematics and joint-limit validation over a documented URDF subset. |
| [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN) | 0.1.0 | Established | tool | python | user-pc | HYDRA-UMC-TWIN | Procedural 2D scene generator with YOLO and COCO annotation export. |

### Ecosystem Operations

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER) | 0.1.8 | Functional | service | python | dev-server | - | Reproducible development host: policy-gated configuration and manifest inventory; no task has deploy permission. |
| [HYDRA-UMC-DOCS](https://github.com/JuanenRac/HYDRA-UMC-DOCS) | 0.0.2 | Scaffolding | tool | python | user-pc | - | This repository: architecture, interfaces, security baseline, capability matrix and cross-repository tooling. |
| [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT) | 0.1.8 | Functional | service | python | cm5 | - | Maintenance-incident coordinator: a sanitised snapshot, a read-only control plane and an AI-provider diagnosis proposal. |
| [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER) | 0.4.8 | Established | tool | python | user-pc | - | Detects, installs and updates the ecosystem's repositories from their manifests (clone, stage, verify, promote). |
| [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER) | 0.3.1 | Functional | tool | python | user-pc | HYDRA-UMC-OS | Desktop tool that builds a ready-to-flash CM5 image with the current versions of the ecosystem; the image build is Linux-only, remotely over SSH from Windows. |

### External Automation Bridges

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC) | 0.1.9 | Functional | service | python | cm5 | HYDRA-UMC-SERVER | CNC cell coordinator with GRBL status and real-time control bytes; never streams a G-code program. |
| [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER) | 0.1.7 | Functional | service | python | cm5 | HYDRA-UMC-SERVER | Laser cell coordinator that reads three safeguards (key, enclosure, interlock) and cannot arm or fire. |
| [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP) | 0.1.9 | Functional | service | python | cm5 | HYDRA-UMC-SERVER | Board hand-off coordinator for OpenPnP; its results are tagged simulation-only. |
| [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D) | 0.1.8 | Functional | service | python | cm5 | HYDRA-UMC-SERVER | Coordination boundary for Moonraker/Klipper 3D printers: readiness, start, pause, resume and cancel of an uploaded file. |
| [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2) | 0.1.2 | Functional | service | python | cm5 | HYDRA-UMC-SERVER | ROS 2 coordination boundary with a plan-only dispatch and an optional rclpy transport. |

### Industrial Gateway

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL) | 0.1.5 | Functional | api | node | cm5 | - | Integration hub for the industrial protocols, with a default-deny command allowlist, a concurrency limit and a timeout. |
| [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER) | 0.1.5 | Established | service | node | cm5 | HYDRA-UMC-GATEWAY-INDUSTRIAL | Aedes-based MQTT broker with per-client authentication, topic ACLs, optional TLS and WebSocket listeners. |
| [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER) | 0.1.7 | Established | api | node | cm5 | HYDRA-UMC-GATEWAY-INDUSTRIAL | MTConnect probe and current XML endpoints for machine and robot state. |
| [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER) | 0.1.8 | Established | service | node | cm5 | HYDRA-UMC-GATEWAY-INDUSTRIAL | OPC UA address space for the robot state, checked with a real binary-protocol client. |

### Mobile & Autonomous Bridges

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR) | 0.1.3 | Functional | library | python | cm5 | HYDRA-UMC-SERVER | Coordination boundary for AGV/AMR fleets: frame transform and a VDA 5050 style order vocabulary behind the shared safety gate. |
| [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS) | 0.1.2 | Functional | library | python | cm5 | HYDRA-UMC-SERVER | Coordination boundary for legged and humanoid droids: a small named action vocabulary behind the shared safety gate. |
| [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV) | 0.1.3 | Functional | library | python | cm5 | HYDRA-UMC-SERVER | Coordination boundary for camera-equipped UAVs: a flight-request vocabulary and a heartbeat/link-loss failsafe watchdog. |

### Orchestration & Swarm

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR) | 0.1.7 | Established | service | rust | cm5 | - | Mission state machine with persistence and an outbox, an HTTP client to JOB-DISPATCHER and its own JSON/HTTP server. |
| [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER) | 0.2.1 | Established | api | go | cm5 | HYDRA-UMC-ORCHESTRATOR | Priority job queue with tool-aware routing, dependencies and de-duplication, over an HTTP API; optional SQLite persistence. |
| [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING) | 0.1.7 | Functional | service | go | cm5 | HYDRA-UMC-ORCHESTRATOR | Health watchdog (gRPC or HTTP) with guarded recovery and identity-mismatch detection. |
| [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D) | 0.0.9 | Established | library | rust | cm5 | HYDRA-UMC-ORCHESTRATOR | RRT 3D path planner with obstacle and workspace collision validation. |
| [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC) | 0.1.3 | Established | service | rust | cm5 | HYDRA-UMC-ORCHESTRATOR | CRDT last-writer-wins state synchronisation, property-tested for convergence. |

### Platform Foundation & Contracts

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB) | 0.1.4 | Functional | tool | python | user-pc | - | Registry and validator of declarative adapter manifests for external machines. |
| [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS) | 0.5.1 | Established | service | python | cm5 | - | Product layer on Raspberry Pi OS for the CM5: read-only device agent, preflight, rollback and Wi-Fi provisioning; not a new distribution. |
| [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK) | 0.3.3 | Established | library | python | user-pc | HYDRA-UMC-OS | Versioned JSON Schema and OpenAPI contracts, conformance fixtures, reference clients (Python, Go, TypeScript, Rust) and the shared CI checks. |

### Vision AI Node

| Repository | Version | Maturity | Role | Stack | Target | Parent | What it is |
|---|---|---|---|---|---|---|---|
| [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE) | 0.1.5 | Functional | service | python | cm5 | - | Integration hub of the Hailo-8 vision family with a per-stage readiness check. |
| [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF) | 0.1.3 | Established | library | python | cm5 | HYDRA-UMC-VISION-NODE | Registry of compiled detection models with schema, Hailo-architecture and checksum checks before loading. |
| [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES) | 0.1.3 | Established | service | python | cm5 | HYDRA-UMC-VISION-NODE | Zone-breach checking and E-STOP requesting over axis-aligned zones, with calibration-freshness enforcement. |
| [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER) | 0.2.0 | Established | service | python | cm5 | HYDRA-UMC-VISION-NODE | GStreamer pipeline and MediaMTX configuration generator with a HailoRT boundary. |
| [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API) | 0.1.8 | Established | api | python | cm5 | HYDRA-UMC-VISION-NODE | Position-based visual-servoing correction law, gated on the state of the safety zones. |
<!-- catalog:end -->
