# Keys and secrets of the ecosystem

One page that lists every key, secret and token the HYDRA-UMC software uses, where each one lives, who makes it, how it is replaced and what happens when it is lost. It holds no secret and no key material: only names, places and rules. The baseline of the protections is in [SECURITY_BASELINE.md](SECURITY_BASELINE.md) and the threats in [THREAT_MODEL.md](THREAT_MODEL.md).

## Rules that hold for all of them

* A secret is **made on the device that uses it** (random, from the operating system) and is never copied from Git, an image or another device. `HYDRA-UMC-OS/provisioning/generate_secrets.py` fills every placeholder of an env file with a random value of its own (64 hexadecimal characters for a key or token, 24 URL-safe characters for a password) and its `--check` refuses an example value or a short secret.
* Secrets are files under `/etc/hydra-umc/` readable only by their service, or environment variables of that service. No secret store exists yet (see the open gaps below).
* A key file that already exists is **never replaced by an installer**: replacing it would stop every signature or session made with it. Rotation is always a deliberate act.
* Development defaults (the example JWT secret, `admin`/`admin`, the published development firmware key) exist only outside production and are refused by the production start policy.
* Nothing in a log, a README or a commit may carry a key. The publication check of this repository scans for them.

## The keys

| Key | What it protects | Where it lives | Made by | Replaced by | If it is lost or leaks |
|---|---|---|---|---|---|
| **Release signing key** (Ed25519, private half) | The authenticity of every packaged component and every firmware image that is published | A file on the maintainer's machine, outside every repository; never on the CM5 | The maintainer, once | A new key pair; the public half is pinned in `HYDRA-UMC-OS/config/release_key.pub` and in the SDK trust folder, so both change in step and a new release of each carries it | Leak: publish a new public key and re-sign the current release; installed devices refuse anything signed only with the old one once they hold the new public key. Loss: same, since nothing can be signed until a new pair exists |
| **Release signing key** (public half) | Lets a device verify a package or an image | `HYDRA-UMC-OS/config/release_key.pub`; `contracts/trust/release_key.pub` of the SDK | Derived from the private half | With the private half | Not secret; a wrong value makes every verification fail loudly |
| **Firmware image signature** (Ed25519 of the image header and bytes) | The bootloaders of the boards accept an image only with it | Made where the private key is (`tools/image_header.py sign` in HYDRA-UMC); the server only relays the signature and holds no key | The maintainer | With the release key policy above | A board never accepts an unsigned image; a leak means signed images could be forged until the boards carry a new public key (a bootloader update) |
| **Firmware HMAC key** (`HYDRA_FW_HMAC_KEY_HEX`) | The HMAC-SHA256 check of an image into the backup slot, shared by every board of a type | Passed to the firmware build; a build without it uses a development key that is published and warns loudly | The maintainer, per release build | A new build with a new key, flashed to every board | The chips have no read-out protection, so one board exposes the key of its whole type: treat it as integrity against accidents, not as secrecy |
| **Server JWT secret** (`JWT_SECRET`) | Every session token of the control server | `/etc/hydra-umc/server.env` | `generate_secrets.py` on install | Change the value and restart the server: every token stops working and everybody signs in again | Replace at once (production refuses an empty, example, short or repetitive value) |
| **Refresh tokens** | Long sessions of the apps | The server state on the device; opaque to the client | The server on sign-in | Rotated on every use; revoked on logout, account deletion, password or role change | Revoke the account's sessions by changing its password |
| **Bootstrap administrator password** | The first administrator | `server.env` at the first start only | `generate_secrets.py` (printed once) | Change it in the app after the first sign-in | Another administrator resets it from the app; with none left, the account store of the device has to be repaired by hand |
| **Gateway JWT secret** (`GATEWAY_JWT_SECRET`) | The industrial gateway; it refuses to start without it unless anonymous use is switched on deliberately | The gateway env file | `generate_secrets.py` | Change the value and restart the gateway | Replace |
| **Voice relay token** (`HYDRA_UMC_VOICE_UI_TOKEN`) | The link between the server and the voice service | `server.env` and `voice-ui.env`, the same value in both | `generate_secrets.py` (one value, mirrored) | Change both files, restart both services | Replace in both places |
| **Voice result key** (`HYDRA_UMC_VOICE_UI_RESULT_KEY`) | The HMAC signature on the result of a confirmed voice request | Same two files, same value | `generate_secrets.py` | Change both files, restart both services | Replace; an unsigned or wrongly signed result is refused |
| **Voice confirmation secret** | Signs the single-use confirmation of a voice request | The voice service env | Its installer | Change and restart; pending confirmations simply expire | Replace |
| **Tool result key** (`HYDRA_UMC_LOCAL_TECHNICIAN_RESULT_KEY` or the `_FILE` form) | The signature of each result of the local technician | A key file made by `provisioning/make_result_key.py` (mode 0600, never printed, never shared between devices) | `make_result_key.py` on install | Delete the file by hand and run the script again; earlier signatures then no longer verify | Replace |
| **Service tokens** (job dispatcher, orchestrator, anomaly detector, data lake read, vision, vision streamer, AI services) | Each service that is reached over the network | The env file of the service; the server holds the ones it must present and never shows them to a client | `generate_secrets.py` | Change the value on both sides, restart both | Replace; a service on loopback may run without one, a service on a network address may not |
| **MQTT credentials and TLS** (`MQTT_USERNAME`, `MQTT_PASSWORD`, `MQTT_TLS_CERT`, `MQTT_TLS_KEY`, `MQTT_TLS_CA`) | The broker and every bridge | The broker and bridge env files; the certificates under the broker's folder | `generate_secrets.py` for the password; `provisioning/hydra_mqtt_tls.sh` for the certificates | New password in the broker and every client, or new certificates | Replace; the broker's access list stays the same |
| **Swarm synchronisation secret** (`SWARM_SYNC_SHARED_SECRET`) | Optional shared-secret authentication between controllers | The env file of each controller | The operator | Change on every controller | Replace |
| **TLS certificate and key of the server** (`TLS_CERT_PATH`, `TLS_KEY_PATH`) | HTTPS and WSS | Paths set in the server env | The operator or the Server Admin screen of the apps | Upload a new pair there; a pair that cannot be read or does not match is refused before it is saved | Replace; the apps show the SHA-256 fingerprint in use |
| **Android app signing key** | That an update of the control app is accepted by phones that already have it | A key store on the maintainer's machine, never in a repository | The maintainer, once | It cannot be replaced for installed phones: a new key means a new app identity | Loss means an update can no longer be installed over the old app; keep an off-line copy |
| **Backup passphrase** | The encrypted settings backup | Kept by the operator, never on the device | The operator | A new backup with a new passphrase | Without it the backup cannot be opened: there is no recovery |

## Who rotates what

* **The maintainer** rotates the release key, the firmware keys and the app signing key. There is no schedule; a leak or a change of maintainer is the trigger.
* **The operator of a device** rotates the env-file secrets of that device. Nothing else on the network depends on them except the two ends of a shared one (the voice pair, the MQTT credentials, a service token and the server that presents it): change both ends before restarting either.
* A new device never inherits a secret: it makes its own at install time.

## Recovery in short

1. Stop the service whose secret is lost.
2. Make a new value (`generate_secrets.py` for an env file, `make_result_key.py` for a key file) and write it to every place in the table above.
3. Start the services again and sign in again; check with `generate_secrets.py --check`.
4. For a release or firmware key, follow the rows above: the public half must reach the devices before they trust anything new.

## Gaps that remain

* There is no secret store, rotation tool or reminder: rotation is manual.
* The shared HMAC key of the firmware cannot be kept secret while the chips have no read-out protection.
* The backup passphrase has no escrow.
* The Android signing key has one copy that the maintainer must keep off-line.
