<!--
=============================================================================
HYDRA-UMC-DOCS - Capability matrix of the HYDRA-UMC ecosystem
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# Capability matrix

What each capability is *today*, said the same way for every repository. It is written from what each repository's own README, changelog and manifest state; this repository has no measurement record of its own, so a row never says more than its source does. When two documents of the same repository disagree, the row follows the more cautious one and says so.

## Levels

| Level | Meaning |
|---|---|
| **Absent** | Nothing exists: the repository says it is not written, or it is planned only. |
| **Builds** | The code compiles or analyses clean and its helper logic may have host tests, but it has not run on the target it is for. |
| **Local** | Works and is tested on a computer (unit, integration or end-to-end tests against a live instance of the same software), with no real device on the other end. |
| **Emulated** | Tested against a fake, a recorded protocol or a hand-written emulator of the external machine. It proves the handling of a *simulated* condition, never that the real machine behaves so. |
| **In use** | The manifest of the repository says `established`, which the SDK defines as sustained real use in this ecosystem's own deployment (a CM5 on the owner's network, or a real desktop or phone). This repository holds no log of that use. |
| **Verified** | Measured on the real target, and the source says so in words. |

The four kinds of evidence are kept apart on purpose (`HYDRA-UMC-SDK/docs/PROJECT_MANIFEST.md`): a unit test, a loopback test against a real running process, an emulation and a physical-bench result are different claims, and a lighter one never stands in for a heavier one.

**The one fact that colours every row:** the custom boards of HYDRA-UMC do not exist as populated hardware yet. The firmware repository, the web client, the desktop client and the operating-system layer all say so. Nothing in the family has been measured on those boards, and no firmware has run on an STM32 of the final design. What has met real devices is stated row by row: real IP cameras (VISION-STREAMER), and the CM5 of the owner for the services that are `established`.

## Firmware: HYDRA-UMC

| Capability | Level | Evidence and limits |
|---|---|---|
| Bootloaders of the G474, the H745 CM7 and the H745 CM4 (CAN-OTA / SPI-OTA, CRC-32 and Ed25519 signature verified into a backup slot before the copy) | Builds | Compile and link clean with the ARM toolchain; not run on real silicon. Helper logic with host tests: flash geometry, the data-length helpers, relay reassembly, source guards |
| G474 Robot Controller Board application: status responder and the FDCAN2 relay to the tool head | Builds | Real code (`RobotControllerRelay.c`); no board |
| H745 CM4 application: FDCAN1 "STACK A" master (round-robin status queries over eight slots, watchdog refresh) | Builds | Real code; no board |
| H745 CM7 application | Absent | Still a FreeRTOS smoke-test stub |
| Six-axis motion generation and S-curve profiles | Absent | The README describes the design; "real 6-axis motion generation (both G474 and CM7) is still not written" |
| E-STOP path, software limits, safety interlocks, power-loss dump to FRAM | Absent | The repository says so in its safety note: nothing may rely on them yet |
| CAN FD | Absent | The silicon and the transceivers allow it; the protocols in use are classic frames of at most eight bytes |
| Bus-off recovery on the CM4 | Absent | Planned |
| Read-out protection of the chips | Absent | A known, accepted gap: the key of the local integrity check (HMAC-SHA256) is shared per board type, so physical access to one board exposes it; the board holds only the public half of the update signing key |
| CM5 SPI-OTA bridge in Python (`spi_bridge`) | Local | Unit-tested against fakes; one SPI operation at a time |
| CM5 IPC driver for the telemetry frame | Builds | Defaults to 10 MHz because the slave-side configuration has not been checked against hardware |
| Build on Windows and on Linux with a pinned HAL | Verified | The README states a run end to end on a Windows machine with matching CRC32s |

## Server

| Capability | Level | Evidence and limits |
|---|---|---|
| REST and WebSocket API, robot ownership, atomic commands | Local, In use | Tests run against a live instance of the same server; the manifest says `established` |
| Authentication: JWT, rotating refresh tokens, scrypt, two roles, login rate limit | Local | Negative-authentication and refresh-token scripts against a live instance |
| Global stop `POST /api/stop-all` | Local | Stops every robot and switches every valve and pump off in the server's state and persists it; the path from there to a physical output is the unbuilt one above |
| TLS (HTTPS and WSS) | Local | Real and optional, off by default; a set but unreadable certificate stops the start |
| mDNS `_hydra._tcp` discovery and `GET /api/hydra-info` | Local | Tested; discovery gated per client type |
| Production start policy | Local | Refuses an example JWT secret, a short secret or bootstrap password |
| Relay of flashing to the SPI bridge, CAN-OTA relay | Local | Exercised through the API layer only: "no physical CM5/STM32 to close that last hop" |
| Voice relay to the loopback gateway, `/api/ai/*` proxy, connector-hub relay | Local | With error paths; the AI services behind them are rows of their own |
| Prometheus metrics and the Grafana stack | Local | Real and optional, off by default |

## Platform

| Capability | Level | Evidence and limits |
|---|---|---|
| SDK: ten JSON Schema v1 contracts, conformance fixtures, the compatibility matrix gate, a differential test of the Python validator | Local | CI of the SDK |
| SDK reference clients: Python, Go, TypeScript, Rust | Local | Enforce the published schemas |
| SDK bridge helpers: job gate, idempotency store, intake, Operation lifecycle, capability checks, promotion journal | Local | Used by the eight bridges |
| SDK shared CI checks (documentation boundary, README parity, version tools) and their sync scripts | Local | Propagated byte for byte to every repository |
| OS: read-only device agent (`DeviceDescriptor`, `HealthReport`) | Local | Unit tests; no CM5 run in the document that states the boundary |
| OS: preflight, rollback and Wi-Fi provisioning state machine | Local | Idempotence, negative paths and a partial-failure rollback checked; the Wi-Fi machine against a fake NetworkManager and one loopback round trip |
| OS: image builder, Debian packages | Absent | The image builder is documentation only; the package metadata has not been built into a `.deb` |
| CONNECTOR-HUB: adapter manifest registry and validator | Local | Part of its tests skip without the optional SDK |

## Clients

| Capability | Level | Evidence and limits |
|---|---|---|
| STUDIO: robot dashboard and 3D view | Local, In use | Vitest over the kinematics and examples; the manifest says `established` |
| STUDIO: CAN-OTA flasher and tester | Emulated | The README says the transport runs against a full built-in simulation until firmware runs on real boards |
| SUITE: discovery, REST and WebSocket, forward kinematics checked against STUDIO's, MJPEG cameras | Local, In use | Offline verify scripts and smoke tests against a running server and a real GPU context |
| DSI: networking and state layers, six screens | Local | The Linux release build was launched under WSL2 on x86_64 only; never on the CM5's aarch64; the kiosk unit has never run on a real Linux machine |
| ANDROID-CONTROL: kinematics, state, commands, voice relay, WebSocket, MJPEG parsing, update channel | Local | JVM and Robolectric tests. The Keystore-backed storage, the biometric prompt, the Bluetooth GATT transport and the hardware image decoder path are stated as not verified on a device in that README |
| IOS-CONTROL | Local | Built and run on Windows with Flutter; an `.ipa` needs Xcode on a Mac, which the repository does not have |
| WATCH: haptic patterns, sync codec, relay policy | Local | JUnit on a plain JVM; nothing on a physical Wear OS watch. The wireless E-STOP and a direct link to the server are planned only |
| EDITOR-URDF: parser, writer, DOF validation, kinematics, mesh resolution | Local | The pure-logic core is tested; the Qt and OpenGL layer is checked by hand |
| EDITOR-STL, TOOL-CLI | Local | TOOL-CLI is a client of a live server and has a fixed exit-code contract; fleet-wide deploy and a live configuration apply are future work |

## Bridges to external machines

All eight go through the SDK gate. **None of them has touched a real machine, a real broker or a real controller**; each README says so for itself.

| Bridge | Level | What the tests stand in for |
|---|---|---|
| CNC | Emulated | A hand-written GRBL v1.1 emulator; serial and MQTT not on real devices |
| LASER | Emulated | A GPIO and MQTT emulator; it cannot arm or fire by design |
| OPENPNP | Emulated | A fake broker client; results are always tagged simulation-only |
| PRINTER3D | Emulated | A local HTTP fixture in place of Moonraker |
| ROS2 | Emulated | The `rclpy` transport is lazily imported and has not met a ROS 2 installation |
| AMR | Emulated | A VDA 5050 AGV emulator and a fake MQTT client |
| DROIDS | Emulated | A Spot emulator; the vendor client is replaced by fakes |
| UAV | Emulated | A MAVLink autopilot emulator |

## Industrial gateway

| Capability | Level | Evidence and limits |
|---|---|---|
| MQTT broker: TCP listener, authentication, topic ACL, payload limit, retained TTL, WebSocket and TLS listeners | Local, In use | A real MQTT client over a real socket against a real Aedes broker |
| MQTT: the server's own state on `hydra/swarm/...` | Absent | Planned; only the bridge topics are wired |
| MQTT: mDNS and Home Assistant discovery | Absent | Planned |
| OPC UA address space | Local | Checked with a real OPC UA client over the binary protocol; subscriptions are not tested |
| MTConnect `/probe` and `/current` | Local | Shape checked against the specification with real HTTP tests |
| Gateway: allowlisted command route with backpressure and timeout | Local | It stops short of a protocol-level write: none of its three children exposes a command API |

## Orchestration

| Capability | Level | Evidence and limits |
|---|---|---|
| ORCHESTRATOR: mission state machine, persistence, outbox, HTTP client to the dispatcher | Local | No live multi-node fleet has ever run; planned layers (PTP-synced dispatch, PATH-PLANNER and SWARM-SYNC wiring) are intent only |
| JOB-DISPATCHER: priority queue, tool-aware routing, dependencies, de-duplication, SQLite persistence | Local | Persistence checked against a killed and relaunched process. Known gap: the tool a robot claims is not confirmed over CAN |
| NODE-HEALING: watchdog, bounded retry, recovery requests | Local | Real gRPC round trips over loopback; the node registry is a static file |
| PATH-PLANNER-3D: single-agent RRT with obstacle checks | Local | Deterministic, with case minimisation; not RRT* |
| SWARM-SYNC: CRDT LWW map, Lamport clock | Local | Property-tested convergence and a four-cell simulation; crash-safe state checked with a killed process |

## Vision AI

| Capability | Level | Evidence and limits |
|---|---|---|
| VISION-STREAMER: configuration validation, GStreamer and MediaMTX configuration generation, buffer and reconnect policy | Local | |
| VISION-STREAMER: `stream serve` reading a camera | Verified | Against real IP cameras on the local network. Not against a physically connected USB camera |
| VISION-STREAMER: the GStreamer pipeline itself and Hailo-8 inference | Absent | Only the description is generated; no Hailo-8 module in the environment |
| DETECTION-HEF: model registry and safe-load gate | Local | The export, quantisation and packaging that would produce models are future work |
| SAFETY-ZONES: zone breach checking, E-STOP requesting, calibration freshness | Local | Takes object positions from a file: the spatial pipeline that would produce them does not exist |
| VISUAL-SERVOING-API: correction law and authorisation gated on the zones | Local | Integration test against SAFETY-ZONES; no pose estimation from a camera, no gRPC feed |
| VISION-NODE: family readiness and frame validation | Local | Runs no Hailo-8 runtime itself |

## Cognitive AI

| Capability | Level | Evidence and limits |
|---|---|---|
| COGNITIVE-NODE: family readiness | Local | Runs no model; the compose file has never run as one stack |
| VLA-ENGINE: action-token coding, trajectory integration, honest hardware status | Local | No model chosen, no Hailo-10 inference |
| VOICE-UI: voice-activity detection, intent parsing, signed single-use confirmation, authenticated gateway | Local | No microphone, speech model or NPU is needed or used |
| SEMANTIC-PLANNER: rule-based decomposition and recovery | Local | Rules over a small vocabulary; no language model |
| DOCS-QA: TF-IDF retrieval with citations | Local | Lexical; no embeddings, no language-model answer |
| LOCAL-TECHNICIAN: read-only observation tools under a risk policy | Local | Adversarial tests show that retrieved text cannot trigger a tool call |

## Data and analytics

| Capability | Level | Evidence and limits |
|---|---|---|
| DATALAKE: SQLite time series, aggregation, retention, migrations | Local, In use | Tested over real HTTP |
| TELEMETRY-COLLECTOR: CAN and WebSocket parsing, bounded buffer, de-duplication, DATALAKE sink | Local | |
| ANOMALY-DETECTOR: FFT, statistical baseline, drift | Local | Signal processing, not a trained model |
| PRODUCTION-REPORTS: OEE and availability, shifts, CSV export | Local | No PDF export exists |
| DASHBOARD-AI: summaries, anomaly highlighting, provider gate | Local | A language-model provider and trend prediction are future work |

## Twin and simulation

| Capability | Level | Evidence and limits |
|---|---|---|
| TWIN: family readiness and version compatibility | Local | Runs no physics engine |
| HIL-BRIDGE: route and mirror with an interlock on an imminent collision | Local | |
| PHYSICS-REPLICA: forward kinematics and joint limits | Local | A documented partial URDF subset |
| SYNTHETIC-DATA-GEN: 2D scenes, YOLO and COCO export | Local | Flat-shaded rectangles, not photorealistic |

## Operations

| Capability | Level | Evidence and limits |
|---|---|---|
| UPDATER: discovery from manifests, clone, stage, verify, promote | Local, In use | Tested against a fixture HTTP server and temporary git repositories; the Qt and Tk windows have no automated test |
| UPDATER: optional signature gate on the candidate commit | Local | Off unless `HYDRA_UMC_UPDATER_REQUIRE_SIGNED=1` |
| OS-REBUILDER: remote image build over SSH | Local | The README says the remote path was exercised against the CM5's own checkout; the loop-mount and chroot pipeline is Linux-only |
| OPS-AGENT: sanitised snapshot, read-only control plane, AI-provider diagnosis | Local | |
| DEV-SERVER: policy-gated configuration and manifest inventory | Local | A task runner is future work; no task has deploy permission |
| DOCS (this repository): catalogue, brand, READMEs, publication check, family check | Local | Unit tests in CI; the nightly comparison of all repositories has not run over time |

## How a row moves

A row moves up only with evidence a person can reproduce from a clean checkout, written in the changelog of the repository that owns it: what was run, where, and what came out (`PROJECT_MANIFEST.md`, "Promotion evidence"). A failure or an out-of-scope part stays visible; it is never edited out to make a change look more complete.
