<!--
=============================================================================
HYDRA-UMC-DOCS - Security baseline of the HYDRA-UMC ecosystem
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# Security baseline

What the code of the family enforces today, what is only a setting that is off by default, and what is missing. It is a reading of the repositories, **not the result of a penetration test or of an external review**, and nothing in it has been tried against an attacker on a real installation. Read it with the [threat model](THREAT_MODEL.md).

The sources are named in each line: the code and READMEs of `HYDRA-UMC-SERVER`, `HYDRA-UMC-MQTT-BROKER`, `HYDRA-UMC-SDK`, `HYDRA-UMC`, `HYDRA-UMC-OS`, `HYDRA-UMC-UPDATER` and the services that have a security section of their own.

## Network position

The design is a trusted local network. The server listens on every interface (`0.0.0.0`, port 3000) because the clients on the LAN need to reach it; the other services are documented as loopback systemd units (the AI, voice and data services), or take a bearer token when they are bound to a network address. The server's own README says that exposing it beyond a trusted LAN (a router port-forward) changes the threat model, and asks for a short token lifetime, TLS and a CORS allowlist before that. A VPN note exists (`HYDRA-UMC-SERVER/docs/REMOTE_ACCESS_VPN.md`). No VLAN or firewall design was found in the repositories read for this page.

## What the software enforces

### Server

* **Authentication on every write.** A JWT signed with `JWT_SECRET`, sent as `Authorization: Bearer`; the WebSocket takes the token as the `hydra.bearer` subprotocol, and a token in the address is refused by default.
* **Refresh tokens** are opaque, rotated on every use, and revoked when the account is deleted or its password or role changes; a logout revokes one explicitly.
* **Passwords** are hashed with scrypt; accounts created after the first need at least 8 characters (`secretsPolicy.ts`). The page `REMOTE_API.md` still says 4 in one passage: the code is the stricter one.
* **Two roles.** `admin` (settings, accounts, flashing, PTZ, service control) and `operator` (read state, send robot commands, the global stop). The last administrator cannot be deleted or demoted.
* **Rate limits** per address: the login (5 failed attempts per 15 minutes by default), the refresh, and a separate budget for the global stop.
* **Production start policy.** With `NODE_ENV=production` the server refuses to start with an empty or example `JWT_SECRET`, one shorter than 32 characters or too repetitive, an example bootstrap password, one shorter than 12 characters or one that contains the user name; and it refuses to create the first administrator without both bootstrap values. CORS denies every cross-origin browser request until an allowlist is set.
* **Cameras.** Live streams, photos and recordings demand a short-lived ticket (`POST /api/camera/ticket`) or a Bearer token by default.
* **Who connects.** `GET /api/connections/clients` and `/events` list the clients the server has seen and their sign-ins, sign-outs and refused sign-ins in a closed contract with no password, token or secret; the address of a client is kept only behind its own switch. Flash progress messages go only to administrators.
* **Reboot and shutdown** accept only a plain request from the device itself: a proxied request, another origin or a cross-site fetch gets `403`.
* **Robot ownership.** A robot reserved by one account cannot be commanded by another, except for the stop commands, which are never blocked by a reservation.
* **Transport.** HTTPS and WSS when `TLS_CERT_PATH` and `TLS_KEY_PATH` are set; a path that is set but unreadable stops the start instead of falling back to plain HTTP.

### Broker and bridges

* **Broker.** In production the broker refuses to start without `MQTT_AUTH_JSON` and `MQTT_ACL_JSON`, with passwords shorter than 16 characters or example passwords, or with an ACL that does not cover the prefix of every credential; `MQTT_ALLOW_ANONYMOUS=1` is an explicit, announced opt-out. An ACL scopes a client by its client-id prefix, and a wildcard subscription cannot escalate beyond it. A payload size cap and a retained-message lifetime are optional. TLS (and optional mutual TLS) is available on 8883 and a secure WebSocket port.
* **Bridges.** A job crosses `evaluate_job()` of the SDK: productive phases need a `READY` cell and an `IDLE` machine; `ABORT` is always forwarded; the machine state that counts is the one the bridge observes, not the one claimed in the message; a retained message is never treated as a request; a key is handled once. A bridge cannot send raw CAN or SPI frames and cannot override the MCU limits, the watchdogs or the E-STOP.
* **Per bridge limits.** The laser bridge cannot arm or fire; the CNC bridge never streams a G-code program; the printer bridge references an already uploaded file by name; the OpenPnP results are tagged simulation-only.

### AI and voice

* **Voice** needs a token for a non-loopback bind; a confirmation is HMAC-signed, single-use, bound to the exact intent and entities it was issued for, and expires; the server keeps the gateway token and never lets voice become a direct robot command.
* **The maintenance assistant** has a fixed risk-level policy and tool allowlist; a retrieved document can never trigger a tool call.
* **Document search** never follows symbolic links, caps depth and file count, strips control characters, and keeps its cache as validated JSON (no pickle).

### Gateway, collector and others

* The industrial gateway refuses to start without `GATEWAY_JWT_SECRET` unless `GATEWAY_ALLOW_ANONYMOUS=1` says on purpose that it is an open lab gateway; `POST /command` is default-deny per protocol with a concurrency limit and a timeout.
* The telemetry collector listens on loopback by default and needs a bearer token (at least 16 characters) for a network address.
* The swarm synchronisation accepts an optional shared secret.

### Operating system and updates

* Every service runs as its own non-login account; secrets are created on the CM5 under `/etc/hydra-umc/` with restrictive permissions and are never copied from Git; the base agent has a read-only view of the system except its state directory and opens no MCU, CAN, motion or update path.
* **UPDATER:** clone, stage, verify, promote; one install at a time per workspace; time limits on git and build-test; no credential prompt. An optional gate verifies the signature of the candidate commit before anything runs (`HYDRA_UMC_UPDATER_REQUIRE_SIGNED=1`).
* **Firmware:** the bootloaders verify the CRC-32 of the image and an Ed25519 signature of its digest into a backup slot before the copy; the board holds only the public key, and an older image is accepted only with a downgrade token, itself an Ed25519 signature. A boot counter parks a board only after repeated watchdog resets. A release build (`HYDRA_UMC_RELEASE=1`) refuses to compile without a real `HYDRA_FW_UPDATE_PUBKEY_HEX` and a real `HYDRA_FW_HMAC_KEY_HEX` (the key of the local integrity check of the installed application); a build without them carries development keys that are published in the repository and warns loudly. The tool heads and expansion boards behind the relay run URTC bootloaders, which still take an HMAC-SHA256 with a shared key instead of a signature.

### The repositories themselves

* Every repository runs the same documentation-boundary check in CI (no private document names, no internal tracking codes), keeps `.env` out of Git and requires its README in eight languages. This repository adds the [publication check](../tools/publication_check.py) for keys, public addresses, personal e-mails and commit trailers.

## Settings that are off by default

These exist and work, but a default installation does not have them. They are the first things to turn on before a server is used beyond a trusted LAN.

| Setting | Default | Effect when set |
|---|---|---|
| `TLS_CERT_PATH` and `TLS_KEY_PATH` | plain HTTP and WS | HTTPS and WSS |
| `NODE_ENV=production` | development | The start policy above; example secrets are refused |
| `HYDRA_UMC_INFO_AUTH=required` | off | `/metrics`, `/api/system/metrics`, `/api/system/supervisor`, `/api/ecosystem/status` and `/api/models` need a signed-in client. **Until then they answer anyone who can reach the port** |
| `CORS_ALLOWED_ORIGINS` | any origin outside production | The allowlist |
| `JWT_EXPIRES_IN` | 30 days | A shorter life for a leaked token |
| `MQTT_AUTH_JSON`, `MQTT_ACL_JSON` | open broker outside production | Authentication and per-client topics |
| `MQTT_TLS_CERT`, `MQTT_TLS_KEY`, `MQTT_TLS_CA` | plain TCP | TLS and mutual TLS |
| `HYDRA_UMC_UPDATER_REQUIRE_SIGNED=1` | off | Signed commits only |
| `SWARM_SYNC_SHARED_SECRET` | off | Shared-secret authentication |
| `HYDRA_UMC_HEALTH_OPEN=1` (`health.open`) | off | `GET /health` answers without a sign-in with a bare report; until then `404` |
| `HYDRA_UMC_SAFETY_PUBLISH_STOP=1` (`safety.publishGlobalStop`) | off | A global stop is also announced on the MQTT bridge as a retained `SAFE_STOP` |
| `HYDRA_UMC_<BRIDGE>_GLOBAL_STOP=1` | off | The AMR, CNC, LASER, OPENPNP, PRINTER3D and ROS2 bridges refuse what moves while that announcement says `SAFE_STOP` (or cannot be read) |
| `HYDRA_UMC_CONNECTION_RECORD_ADDRESS=1` (`connections.recordAddress`) | off | The history of connections also keeps the address and user agent of each client (personal data), shown to administrators only |
| `HYDRA_UMC_CAMERA_AUTH=open` (`camera.open`) | tickets required | Camera pictures without a ticket: lowers protection, off on purpose |
| `HYDRA_UMC_WS_QUERY_TOKEN=allow` (`websocket.allowQueryToken`) | refused | A token in the WebSocket address (it stays in proxy logs): lowers protection |
| `HYDRA_UMC_LOG_REDACTION=off` (`logging.redactSecrets`) | secrets blanked | Stops blanking secrets in the log: lowers protection |
| `HYDRA_UMC_VOICE_CONFIRM_REQUIRE_SIGNATURE=1` (`voice.requireSignature`) | off | A confirmed spoken request needs a verified signature |
| `HYDRA_UMC_OPCUA_LIVENESS=1` | off | OPC UA `Online` follows `GET /api/robots/liveness` instead of the `online` flag of the settings |
| `journal.read`, `server.metrics` of the local technician | closed | Two optional tools: a bounded window of the journal of an allow-listed unit and one GET of an allow-listed metrics endpoint |
| `HYDRA_UMC_UPDATER_ROLLBACK_ON_UNHEALTHY=1` | off | A promotion whose health check still fails puts the previous installation back |
| `HYDRA_LOCAL_SCREEN` | `hdmi` | One local screen on the CM5: `hdmi`, `dsi` or `none` (the two kiosks never claim `tty1` together) |

## Not done yet

* **No E-STOP in the firmware.** The firmware repository states that it contains no E-STOP path, software limits, safety interlocks or power-loss dump. The server's global stop changes the server's state; the MCU is documented as the final physical authority but cannot yet play that role. Nothing may rely on any of it for the safety of a person.
* **No read-out protection** on the three chips: one board exposes the key of the local integrity check, which is shared by every board of that type; the update signing key is not exposed, because the board holds only its public half.
* **Update manifests carry a hash, not a signature** (`UpdateManifest` has `sha256` and an HTTPS URL; the update model of the OS asks for a signature and the schema has no field for it).
* **TLS is optional everywhere**, the broker's included. No link-level encryption or authentication of the SPI and CAN buses is documented: the bootloaders authenticate firmware images, not the traffic.
* **No reviewed access list**, no secret store (secrets are files and environment variables), no backup policy, no penetration test.
* **Development defaults** are permissive on purpose: outside production the server seeds `admin`/`admin` and uses a fixed development JWT secret when none is set, and CORS is open. A server started without `NODE_ENV=production` on a reachable address is open to anyone on that network.
* **A token in an address** is still used by one page: the embedded 3D view that the phone apps load in a web view. The server never reads it, but it can be recorded by whatever carries the page address.
* **The AI services are not hardened against hostile input beyond what their READMEs list**, and none runs a language model today.

## Where to start

1. Start the server with `NODE_ENV=production`, real bootstrap values, a short `JWT_EXPIRES_IN`, `HYDRA_UMC_INFO_AUTH=required` and TLS.
2. Run the broker with authentication, ACLs and TLS.
3. Keep every other service on loopback; give a service a network address only together with its token.
4. Treat the firmware as unsafe for any real machine until the E-STOP path exists and has been tested on a board.
