# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/descriptions.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""One sober sentence per repository, for the generated project catalogue.

Each sentence says what the repository's own manifest and README say it does,
without the claims that only hardware could prove. A repository missing from
this table still appears in the catalogue (with the start of the notes of its
manifest) and the structure check of the nightly run reports it.
"""
from __future__ import annotations

DESCRIPTIONS: dict[str, str] = {
    "HYDRA-UMC": "Motion-control firmware (STM32H745 and STM32G474, six components with bootloaders) and the CM5 SPI-OTA bridge; not yet run on a real board.",
    "HYDRA-UMC-ANDROID-CONTROL": "Native Android control app with biometric login, a client of HYDRA-UMC-SERVER.",
    "HYDRA-UMC-ANOMALY-DETECTOR": "FFT and statistical-baseline anomaly detector over DATALAKE history, with drift monitoring (no machine-learning model).",
    "HYDRA-UMC-BRIDGE-AMR": "Coordination boundary for AGV/AMR fleets: frame transform and a VDA 5050 style order vocabulary behind the shared safety gate.",
    "HYDRA-UMC-BRIDGE-CNC": "CNC cell coordinator with GRBL status and real-time control bytes; never streams a G-code program.",
    "HYDRA-UMC-BRIDGE-DROIDS": "Coordination boundary for legged and humanoid droids: a small named action vocabulary behind the shared safety gate.",
    "HYDRA-UMC-BRIDGE-LASER": "Laser cell coordinator that reads three safeguards (key, enclosure, interlock) and cannot arm or fire.",
    "HYDRA-UMC-BRIDGE-OPENPNP": "Board hand-off coordinator for OpenPnP; its results are tagged simulation-only.",
    "HYDRA-UMC-BRIDGE-PRINTER3D": "Coordination boundary for Moonraker/Klipper 3D printers: readiness, start, pause, resume and cancel of an uploaded file.",
    "HYDRA-UMC-BRIDGE-ROS2": "ROS 2 coordination boundary with a plan-only dispatch and an optional rclpy transport.",
    "HYDRA-UMC-BRIDGE-UAV": "Coordination boundary for camera-equipped UAVs: a flight-request vocabulary and a heartbeat/link-loss failsafe watchdog.",
    "HYDRA-UMC-COGNITIVE-NODE": "Integration hub of the Hailo-10 cognitive family; reports the readiness of its four children.",
    "HYDRA-UMC-CONNECTOR-HUB": "Registry and validator of declarative adapter manifests for external machines.",
    "HYDRA-UMC-DASHBOARD-AI": "Text summaries of DATALAKE history (min, max, average, trend) and anomaly highlighting, with a statistical fallback when no AI provider is configured.",
    "HYDRA-UMC-DATALAKE": "SQLite time-series store with an HTTP ingest and query API.",
    "HYDRA-UMC-DETECTION-HEF": "Registry of compiled detection models with schema, Hailo-architecture and checksum checks before loading.",
    "HYDRA-UMC-DEV-SERVER": "Reproducible development host: policy-gated configuration and manifest inventory; no task has deploy permission.",
    "HYDRA-UMC-DOCS": "This repository: architecture, interfaces, security baseline, capability matrix and cross-repository tooling.",
    "HYDRA-UMC-DOCS-QA": "Stdlib-only TF-IDF search over the ecosystem's own Markdown documents, with citations; lexical, not semantic.",
    "HYDRA-UMC-DSI": "Flutter touch interface for the onboard 7 inch DSI display of the CM5.",
    "HYDRA-UMC-EDITOR-STL": "Desktop STL editor for the model libraries shared by STUDIO and SUITE.",
    "HYDRA-UMC-EDITOR-URDF": "Desktop URDF creator and editor that pushes finished models into the shared model catalogue.",
    "HYDRA-UMC-MESHES": "The shared 3D meshes (STL and GLB) of STUDIO and SUITE, published once as a release package with a SHA-256 manifest.",
    "HYDRA-UMC-GATEWAY-INDUSTRIAL":"Integration hub for the industrial protocols, with a default-deny command allowlist, a concurrency limit and a timeout.",
    "HYDRA-UMC-HIL-BRIDGE": "Hardware-in-the-loop routing with an interlock that blocks commands to real hardware in the wrong mode.",
    "HYDRA-UMC-IOS-CONTROL": "Flutter control app for iOS and iPadOS with a real-time WebSocket link to HYDRA-UMC-SERVER.",
    "HYDRA-UMC-JOB-DISPATCHER": "Priority job queue with tool-aware routing, dependencies and de-duplication, over an HTTP API; optional SQLite persistence.",
    "HYDRA-UMC-LOCAL-TECHNICIAN": "Read-only diagnostic assistant with a fixed risk-level policy and tool allowlist; a retrieved document can never trigger a tool call.",
    "HYDRA-UMC-MQTT-BROKER": "Aedes-based MQTT broker with per-client authentication, topic ACLs, optional TLS and WebSocket listeners.",
    "HYDRA-UMC-MTCONNECT-ADAPTER": "MTConnect probe and current XML endpoints for machine and robot state.",
    "HYDRA-UMC-NODE-HEALING": "Health watchdog (gRPC or HTTP) with guarded recovery and identity-mismatch detection.",
    "HYDRA-UMC-OPCUA-SERVER": "OPC UA address space for the robot state, checked with a real binary-protocol client.",
    "HYDRA-UMC-OPS-AGENT": "Maintenance-incident coordinator: a sanitised snapshot, a read-only control plane and an AI-provider diagnosis proposal.",
    "HYDRA-UMC-ORCHESTRATOR": "Mission state machine with persistence and an outbox, an HTTP client to JOB-DISPATCHER and its own JSON/HTTP server.",
    "HYDRA-UMC-OS": "Product layer on Raspberry Pi OS for the CM5: read-only device agent, preflight, rollback and Wi-Fi provisioning; not a new distribution.",
    "HYDRA-UMC-OS-REBUILDER": "Desktop tool that builds a ready-to-flash CM5 image with the current versions of the ecosystem; the image build is Linux-only, remotely over SSH from Windows.",
    "HYDRA-UMC-PATH-PLANNER-3D": "RRT 3D path planner with obstacle and workspace collision validation.",
    "HYDRA-UMC-PHYSICS-REPLICA": "Forward kinematics and joint-limit validation over a documented URDF subset.",
    "HYDRA-UMC-PRODUCTION-REPORTS": "OEE and availability reports over DATALAKE history, with reproducible CSV export.",
    "HYDRA-UMC-SAFETY-ZONES": "Zone-breach checking and E-STOP requesting over axis-aligned zones, with calibration-freshness enforcement.",
    "HYDRA-UMC-SDK": "Versioned JSON Schema and OpenAPI contracts, conformance fixtures, reference clients (Python, Go, TypeScript, Rust) and the shared CI checks.",
    "HYDRA-UMC-SEMANTIC-PLANNER": "Rule-based task decomposition and semantic recovery over MCU error codes.",
    "HYDRA-UMC-SERVER": "Headless Node.js/TypeScript backend: REST and WebSocket API, authentication, mDNS discovery and the global stop.",
    "HYDRA-UMC-STUDIO": "Web control dashboard (React) with 3D multi-robot visualisation, a client of HYDRA-UMC-SERVER.",
    "HYDRA-UMC-SUITE": "Desktop (PySide6) command centre for several servers at once.",
    "HYDRA-UMC-SWARM-SYNC": "CRDT last-writer-wins state synchronisation, property-tested for convergence.",
    "HYDRA-UMC-SYNTHETIC-DATA-GEN": "Procedural 2D scene generator with YOLO and COCO annotation export.",
    "HYDRA-UMC-TELEMETRY-COLLECTOR": "CAN and WebSocket ingestion with a bounded buffer, retry on outage and a DATALAKE sink.",
    "HYDRA-UMC-TOOL-CLI": "Command-line client: version, status, robots, doctor and a dry-run configuration apply.",
    "HYDRA-UMC-TWIN": "Integration hub of the digital-twin family with a version-compatibility check of its children.",
    "HYDRA-UMC-UPDATER": "Detects, installs and updates the ecosystem's repositories from their manifests (clone, stage, verify, promote).",
    "HYDRA-UMC-VISION-NODE": "Integration hub of the Hailo-8 vision family with a per-stage readiness check.",
    "HYDRA-UMC-VISION-STREAMER": "GStreamer pipeline and MediaMTX configuration generator with a HailoRT boundary.",
    "HYDRA-UMC-VISUAL-SERVOING-API": "Position-based visual-servoing correction law, gated on the state of the safety zones.",
    "HYDRA-UMC-VLA-ENGINE": "Action-token encoding and decoding and trajectory generation for a vision-language-action model.",
    "HYDRA-UMC-VOICE-UI": "Voice front end: voice-activity detection, rule-based intent parsing and a confirmation-gated Watch relay.",
    "HYDRA-UMC-WATCH": "Wear OS companion with haptic alert patterns and a voice-command capture.",
}
