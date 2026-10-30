# CM5 test bench

This page records, for each HYDRA-UMC service that runs on the CM5, what is
**guaranteed by the installer**, what has been **tested on a real CM5** and what
has **not been tested**. The status lights in the READMEs and the maturity in
the project manifests depend on it: nothing counts as running on hardware
until a line of the table below says so, with the evidence next to it.

The table is empty on purpose. It is filled in only after a bench run on the
real board, by the person who ran it. Nothing here is marked as tested.

## How to read the columns

* **Installer guarantees**: what `HYDRA-UMC-OS/provisioning/install_<service>.sh` checks or
  enforces by itself (the service user, the unit, the secrets, the port, a refusal to start
  with an example value). It is taken from reading the script, not from a run.
* **Tested on a real CM5**: the service was installed with `--apply` on the board, started,
  answered its health path and survived a reboot. Write what was run, the version and the
  evidence (a log, a captured output).
* **Not tested**: what the bench did not cover (a camera, a Hailo accelerator, a robot, a
  second device).

Fill in a cell with a short sentence, or leave it empty if nothing is known.

## Services

The ports, health paths and units come from `HYDRA-UMC-OS/provisioning/ports.yaml`.

| Service | Port | Health path | Unit | Installer guarantees | Tested on a real CM5 | Not tested |
| --- | --- | --- | --- | --- | --- | --- |
| HYDRA-UMC-ANOMALY-DETECTOR | 8097 | `/stats` | `hydra-umc-anomaly-detector.service` |  |  |  |
| HYDRA-UMC-COGNITIVE-NODE | 8096 | `/stats` | `hydra-umc-cognitive-node.service` |  |  |  |
| HYDRA-UMC-DASHBOARD-AI | 8115 | `/` | `hydra-umc-dashboard-ai.service` |  |  |  |
| HYDRA-UMC-DATALAKE | 8095 | `/stats` | `hydra-umc-datalake.service` |  |  |  |
| HYDRA-UMC-DETECTION-HEF | 8093 | `/stats` | `hydra-umc-detection-hef.service` |  |  |  |
| HYDRA-UMC-DOCS-QA | 8110 | `/stats` | `hydra-umc-docs-qa.service` |  |  |  |
| HYDRA-UMC-GATEWAY-INDUSTRIAL | 8000 | `/health` | - |  |  |  |
| HYDRA-UMC-HIL-BRIDGE | 8113 | `/stats` | `hydra-umc-hil-bridge.service` |  |  |  |
| HYDRA-UMC-JOB-DISPATCHER | 8090 | `/health` | `hydra-umc-job-dispatcher.service` |  |  |  |
| HYDRA-UMC-MQTT-BROKER | 1883 | - | - |  |  |  |
| HYDRA-UMC-MTCONNECT-ADAPTER | 5000 | `/probe` | - |  |  |  |
| HYDRA-UMC-OPCUA-SERVER | 4840 | - | - |  |  |  |
| HYDRA-UMC-ORCHESTRATOR | 8114 | `/health` | `hydra-umc-orchestrator.service` |  |  |  |
| HYDRA-UMC-PRODUCTION-REPORTS | 8099 | `/health` | `hydra-umc-production-reports.service` |  |  |  |
| HYDRA-UMC-SAFETY-ZONES | 8108 | `/stats` | `hydra-umc-safety-zones.service` |  |  |  |
| HYDRA-UMC-SEMANTIC-PLANNER | 8109 | `/stats` | `hydra-umc-semantic-planner.service` |  |  |  |
| HYDRA-UMC-SERVER | 3000 | `/api/system/metrics` | `hydra-umc-server.service` |  |  |  |
| HYDRA-UMC-SWARM-SYNC | 8112 | `/health` | `hydra-umc-swarm-sync.service` |  |  |  |
| HYDRA-UMC-TELEMETRY-COLLECTOR | 8092 | `/stats` | `hydra-umc-telemetry-collector.service` |  |  |  |
| HYDRA-UMC-TWIN | 8111 | `/stats` | `hydra-umc-twin.service` |  |  |  |
| HYDRA-UMC-VISION-NODE | 8094 | `/stats` | `hydra-umc-vision-node.service` |  |  |  |
| HYDRA-UMC-VISUAL-SERVOING-API | 8116 | `/stats` | `hydra-umc-visual-servoing-api.service` |  |  |  |
| HYDRA-UMC-VLA-ENGINE | 8098 | `/health` | `hydra-umc-vla-engine.service` |  |  |  |
| HYDRA-UMC-VOICE-UI | 8091 | `/health` | - |  |  |  |

## Bench run

For each service, from the checkout that holds the repositories side by side:

1. Dry run: `sudo provisioning/install_<service>.sh` prints the plan and changes nothing.
2. Apply: `sudo provisioning/install_<service>.sh --apply`.
3. Check the unit (`systemctl status <unit>`) and the health path on its port.
4. Reboot the board and check again.
5. Run `provisioning/verify_cm5_runtime.sh` and keep its output.
6. Record the result in the table above, with the version of the service.

Take the order of the phases from `HYDRA-UMC-OS/provisioning/CM5_DEPLOYMENT_SEQUENCE.md`, one
gate at a time.

## What is not on the bench

Hardware that is not on the board is not tested by it: robots and their controllers, tool
heads, cameras, the Hailo accelerator, the display and the audio devices. List what was
missing in the last column of each row.
