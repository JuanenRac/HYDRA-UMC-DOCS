<!--
=============================================================================
HYDRA-UMC-DOCS - Interfaces and who owns each contract
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# Interfaces and ownership

This page does not copy the contracts: it says which repository **owns** each one, where it is written down, who produces and who consumes it, and how much of it is checked by a machine. A contract that is only prose is marked as such.

The rule of the ecosystem (`HYDRA-UMC-SDK/docs/CONTRACTS.md`): a service depends on a versioned contract, never on the database, private queue or source tree of another service. A contract is defined once, as JSON Schema, OpenAPI or Protobuf, according to its use.

## 1. The contracts of the SDK

Owner: **HYDRA-UMC-SDK** (`contracts/json-schema/v1/`, with a conformance fixture pair, one accepted and one rejected, for each in `conformance/fixtures/v1/`). `tools/verify_contract_matrix.py` fails when a schema has no reference-validator entry or a fixture is accepted or rejected the wrong way.

| Contract | Producer | Consumer | Notes |
|---|---|---|---|
| `DeviceDescriptor` | OS agent, MCU and URTC adapters | Server, Studio, Updater | The OS agent emits it today (read-only) |
| `HealthReport` | OS agent, services | Server, Node Healing, Studio | |
| `SafetyState` | MCU adapter, safety service | Server, UIs, Job Dispatcher | `READY`, `INHIBITED`, `FAULT`, `SAFE_STOP`; the producers on the MCU side do not exist yet |
| `UpdateManifest` | Updater registry | OS agent, updater client | Requires an `https://` artifact URL and a SHA-256; it has **no signature field** (see the [security baseline](SECURITY_BASELINE.md)) |
| `ServerDiscovery` | Server, `GET /api/hydra-info` | Studio, Suite, mobile clients, Updater | Checked against the live server by `tools/verify_discovery_contract.mjs` of the server |
| `EventEnvelope` | Services | Event consumers, DataLake | |
| `ScenarioOutcome` | Scenario runners | OPS-AGENT, Node Healing | |
| `Operation` | Server, Orchestrator, Dev Server | UIs, Job Dispatcher | A lifecycle with evidence-based success |
| `Capability` | Targets and their descriptors | Orchestrator, Job Dispatcher | |
| `ProjectManifest` | Every repository (`hydra-umc.project.json`, `urtc.project.json`) | Updater, the profile dashboard | A closed schema: a typo in a field name fails early |

Planned in the SDK and **without a schema yet**: `ToolDescriptor` and `TelemetrySample`. Protobuf is not published by the SDK.

The SDK also publishes a first OpenAPI v1 slice of the server (`contracts/openapi/v1/server.openapi.json`: discovery, sign-in, settings and command routes, a subset of the server's own file) and reference clients in Python, Go, TypeScript and Rust that enforce the schemas.

## 2. The HTTP and WebSocket API of the server

Owner: **HYDRA-UMC-SERVER**. Written in `docs/REMOTE_API.md` (the prose, the single source for every client) and `docs/openapi.json` (an OpenAPI 3.1 inventory of the 51 routes: path, method, the access each one demands, the status codes and the names of the body fields; it does **not** describe field types or response bodies, and the server's test run fails when it is out of date). Default port 3000; the REST endpoints and the `/ws` WebSocket share it.

| Area | Routes | Access |
|---|---|---|
| Discovery | `GET /api/hydra-info` | public; gated per client type by `X-Hydra-Client` |
| Sign-in | `POST /api/login`, `/api/refresh`, `/api/logout` | public (rate limited) |
| State | `GET /api/settings`, `POST /api/settings`, `/ws` | read: any account; write: admin; `/ws` needs the token |
| Robots | `POST /api/robot/:id/command`, `/claim`, `/release`, `POST /api/stop-all` | any signed-in account |
| Accounts | `GET/POST /api/users`, `PUT/DELETE /api/users/:username` | admin |
| Cameras | `POST /api/camera/ticket`, `GET /api/camera/:id/stream`, snapshots, recordings, PTZ | ticket or Bearer; PTZ and path discovery admin |
| Hardware | `POST /api/hardware/canota/flash`, `GET /api/hardware/canota/version` | flashing admin |
| Voice and AI | `POST /api/voice/turn`, `/api/ai/:service/*`, `GET /api/adapters` | signed-in account |
| Operations | `/api/ecosystem/status`, `/api/ecosystem/service/:unit/:action`, `/api/admin/*`, `/api/system/*` | mixed: see the file; `reboot` and `shutdown` accept only a plain request from the device itself |
| Observability | `GET /metrics` (Prometheus), `/api/system/metrics`, `/api/telemetry/*` | public unless `HYDRA_UMC_INFO_AUTH=required`; telemetry signed-in |

The version of the transport is `remoteApiVersion` in the discovery answer, independent of the application version: a client checks it, not the version, before it assumes a feature.

## 3. MQTT

Owner of the broker: **HYDRA-UMC-MQTT-BROKER**; owner of the topic catalogue: its `docs/BRIDGE_TOPICS.md`; owner of the job contract that travels on it: **HYDRA-UMC-SDK** (`docs/BRIDGE_CONTRACT.md`).

| Topic | Direction | Producer and consumer |
|---|---|---|
| `hydra/bridges/<name>/cmd/job` | to the bridge | a `BridgeJob` (`job_id`, `idempotency_key`, `source`, `phase`, claimed `machine_state`, string parameters) from the orchestrator or any authorised publisher |
| `hydra/bridges/<name>/cmd/job/result` | from the bridge | the gate decision `{allowed, reason}`; a malformed payload always answers `allowed: false` |
| `hydra/bridges/<name>/state` | from the bridge, retained | `cnc`, `laser`, `printer3d`, `ros2` publish a state; `openpnp` has none |
| `hydra/bridges/cnc/cmd/status`, `feed_hold`, `soft_reset`, `cycle_start_resume` | to the bridge | GRBL real-time controls; no G-code program is ever streamed |
| `hydra/bridges/laser/cmd/status` | to the bridge | re-reads the three safeguards; no command can arm or fire |
| `hydra/bridges/openpnp/cmd/handoff` | to the bridge | a traceable hand-off whose result is always tagged `simulation-only` |
| `hydra/bridges/printer3d/cmd/status`, `start`, `pause`, `resume`, `cancel` | to the bridge | Moonraker calls on an already uploaded file |
| `hydra/bridges/ros2/cmd/safe_stop` | to the bridge | a `std_srvs/Trigger` call |

`<name>` is `cnc`, `laser`, `openpnp`, `printer3d` or `ros2`. The catalogue covers these five; the AMR bridge speaks VDA 5050 topics to the fleet manager and the UAV bridge speaks MAVLink to the autopilot, each as its own README documents. `hydra/swarm/<robot>/...` appears in the broker README as the intended future shape and is **not** wired.

Rules that belong to the contract, not to a repository: a retained message is not a request (`JobIntake` ignores it); a key is handled once (`IdempotencyStore`, SQLite when given a file); the gate uses the machine state that the bridge observes and ignores the claim in the message; `ABORT` is always forwarded to the authorised safety path. The ACL of the broker scopes each bridge to `hydra/bridges/<name>/#` by client-id prefix.

## 4. HTTP APIs of the other services

Each is a small JSON/HTTP surface owned by the repository that serves it; the port is in the [architecture](ARCHITECTURE.md). The routes below are the ones the READMEs name.

| Repository | Routes | Contract |
|---|---|---|
| HYDRA-UMC-JOB-DISPATCHER | `POST /robots`, `POST /jobs`, `POST /jobs/submit`, `GET /health` | prose in the README; idempotent `DedupKey` submission |
| HYDRA-UMC-ORCHESTRATOR | `POST /nodes/:node/recover`, `GET /health` | prose; the mission state machine is in `src/mission.rs` |
| HYDRA-UMC-GATEWAY-INDUSTRIAL | `GET /health`, `GET /status`, `POST /command {protocol, operation, target}` | default-deny allowlist, `403`, `429` and `504` behaviours in the README |
| HYDRA-UMC-DATALAKE | `POST /ingest`, `GET /query`, `GET /aggregate`, `GET /stats`, `/retention*` | prose |
| HYDRA-UMC-TELEMETRY-COLLECTOR | `/ingest/...`, `GET /stats`, `GET /metrics` | prose; a network bind needs a bearer token |
| HYDRA-UMC-PRODUCTION-REPORTS | `GET /reports/oee`, `/reports/availability` and their `/export` | prose; CSV only, no PDF |
| HYDRA-UMC-SAFETY-ZONES | `POST /check`, `GET /stats` | prose |
| HYDRA-UMC-VISUAL-SERVOING-API | `POST /correct`, `POST /request`, `GET /stats` | prose |
| HYDRA-UMC-DETECTION-HEF | `GET /registry`, `/registry/latest`, `/registry/load`, `GET /stats` | prose; model compatibility gate |
| HYDRA-UMC-VOICE-UI | `POST /v1/voice/turn`, `POST /v1/voice/confirm`, `GET /health` | prose; HMAC-signed, single-use confirmation token |
| HYDRA-UMC-SEMANTIC-PLANNER | `POST /decompose`, `/recover`, `/release`, `GET /stats` | prose |
| HYDRA-UMC-SWARM-SYNC | `POST /reconcile`, `GET /state`, `GET /stats` | prose; optional shared-secret authentication |
| HYDRA-UMC-TWIN, -HIL-BRIDGE | `GET /family-status`, `GET /family-sync`; `POST /route`, `POST /mirror` | prose |
| HYDRA-UMC-DOCS-QA | `GET /query?q=...&top_k=N`, `GET /stats` | `docs/CLI_REFERENCE.md` of that repository |

## 5. gRPC and Protobuf

Owner: **HYDRA-UMC-ORCHESTRATOR**, `proto/hydra_common.proto`: `HealthService.Check(Empty) returns (HealthReport)` with a `NodeIdentity`, a `HealthState` and open key/value metrics. Its own comment says that **no node serves it over gRPC yet**: HYDRA-UMC-NODE-HEALING probes each node's HTTP health route today, and its tests make real gRPC round trips over loopback sockets. There is no other `.proto` file in the family.

## 6. Firmware

| Interface | Owner | Written in |
|---|---|---|
| CAN-OTA between the H745, the G474 boards and the URTC head | HYDRA-UMC | `docs/CANBUS_STM32H745.TXT`, `docs/CANBUS_STM32G474.TXT`: classic frames, at most 8 bytes, about 1 Mbit/s |
| SPI-OTA and the 128-byte telemetry frame between the CM5 and the H745 | HYDRA-UMC | `README.md` section 10, `src/cm5_host/ipc_driver`, `src/cm5_host/spi_bridge` |
| The relay (`RELAY_SEND` / `RELAY_RECV`) to the tool head | HYDRA-UMC | `docs/architecture.md` sections 1 and 5 |
| `firmware_manifest.json` with the CRC32 of each image | HYDRA-UMC (written by `build_firmware.sh`) | the build scripts; read by STUDIO and SUITE to download firmware |

## 7. Files that other tools read

* `hydra-umc.project.json` in every repository: read by HYDRA-UMC-UPDATER, by the profile dashboard (GitHub raw content, no fixed list) and by the [catalogue](PROJECT_CATALOG.md) of this repository. Schema and rules: `HYDRA-UMC-SDK/docs/PROJECT_MANIFEST.md`.
* `schemas/adapter-manifest.v1.schema.json` (HYDRA-UMC-CONNECTOR-HUB): declarative adapters for external machines; the server proxies `GET /api/adapters` to it when `HYDRA_UMC_CONNECTOR_HUB_URL` is set.
* `contracts/*.schema.json` (HYDRA-UMC-LOCAL-TECHNICIAN): the evidence bundle, the maintenance proposal and the patch verification report.

## What is not an interface yet

* A telemetry sample contract (planned in the SDK, no schema).
* A signed update manifest (the OS update model asks for a signature; the SDK contract has none).
* MQTT topics for the server's own state.
* A gRPC service that any node actually serves.
