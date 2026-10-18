<!--
=============================================================================
HYDRA-UMC-DOCS - Threat model of the HYDRA-UMC ecosystem
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# Threat model

What HYDRA-UMC protects, from whom, where its pieces trust each other, what each piece does about each threat, and what is left. It is written from what the code and the documents of the repositories say, piece by piece; it is **not the result of an external review or a penetration test**, and the software has not been attacked on a real installation. Read it with the [security baseline](SECURITY_BASELINE.md), which lists what is enforced and what is not done.

The special feature of this ecosystem is that the consequences are physical: a robot arm, a CNC machine, a laser cell or a drone can hurt a person. The first asset is therefore not data.

## What there is to protect

| Asset | Why it matters |
|---|---|
| The ability to move, stop or release a machine (robot commands, the global stop, jobs sent to a bridge) | The consequences are physical. Whoever can send a command can move a machine; whoever can block the stop can keep it moving |
| The state of the safety gates (the cell state, the zone checks, the interlocks, `SafetyState`) | A gate that can be lied to is not a gate |
| The firmware on the boards, and the images that carry it | Whoever controls the firmware controls the motion hardware |
| The code that updates the machines (the updater, the repositories it installs from, the build scripts the candidates bring) | An update runs code with the rights of the user who runs it |
| Accounts, tokens, the JWT secret, MQTT credentials, bridge and gateway tokens | A stolen credential speaks as that person or service |
| Camera pictures and recordings, the layout of the cell, work files and models | Privacy and the intellectual property of a workshop |
| Telemetry and production data (OEE, availability, vibration baselines) | Business confidentiality; and the integrity of the baselines that raise alarms |
| The CM5 that runs the services | It holds all of the above |

## Who might attack

* **Someone passive or active on the same network**: a guest on the Wi-Fi, a compromised laptop or phone, a camera. Because the server listens on every interface, this person can reach the login, the discovery route and, by default, a few read-only information routes without a token.
* **A person who steals a signed-in phone, tablet, watch or the onboard display.**
* **A malicious or mistaken publisher on the MQTT broker**, or a compromised bridge host.
* **A malicious or damaged repository or release**: the account the machines update from, a dependency, or a build script that comes with a candidate version.
* **Someone with physical access to a board**: SWD pins, the CAN bus, the SPI link, the SD card of the CM5.
* **A hostile document or voice input** fed to an AI service.
* **The internet**, if the server is ever exposed to it. The documents say not to, without TLS, a short token life and a CORS allowlist.

Out of scope here: a determined attacker with long physical access (secrets in flash and in files are not protected against that), radio-level attacks on Wi-Fi and Bluetooth, and the security of the router and the switches.

## Where the pieces trust each other

```
 people ──(HTTP/WS, Bearer)──▶ SERVER ──(loopback HTTP)──▶ AI services, spi_bridge ──(SPI)──▶ H745 ──(CAN)──▶ G474 ──▶ tool head
                                  ▲
 bridges ──(MQTT, job + gate)─────┘ authorisation stays in the server; the MCU is the last physical authority (not built yet)
```

* **Clients to the server.** The server trusts a valid, unexpired, non-revoked Bearer token and the role inside it. Clients are not privileged: they cannot reach the firmware except through the server.
* **The server to its local services.** Loopback HTTP with a token the server keeps; the services do not trust the network.
* **Bridges to the server.** A bridge trusts nothing in the message: the machine state it uses is the one it observes. The server remains the authority for what a person may do; the SDK states that a bridge cannot bypass the server's authorisation.
* **The server to the firmware.** A flash goes through the SPI bridge, administrators only; the bootloader trusts an image only after the CRC32 and the HMAC verify.
* **The updater to a candidate repository.** It trusts git over HTTPS to the repositories of the owner. It runs the candidate's own build-test script, which is why the signature gate exists.

## Threats and what each piece does about them

| Threat | What is done | What is left |
|---|---|---|
| Someone on the LAN sends a command to the server | Every write needs a Bearer token; two roles; ownership of a robot; rate limit on the login | In development mode the first account is `admin`/`admin`. Tokens last 30 days unless shortened and cannot be revoked individually except by changing the password or role |
| Brute force of the login | 5 failed attempts per 15 minutes per address by default; scrypt | The limit is per address; a distributed attack is not addressed |
| Eavesdropping on the LAN | Optional TLS on the server and the broker | Plain HTTP, WS and MQTT by default: tokens and commands travel in clear text until TLS is set |
| A page open in the kiosk browser powers the cell off | `reboot` and `shutdown` refuse proxied, cross-origin and cross-site requests | |
| Reading status and metrics without an account | `HYDRA_UMC_INFO_AUTH=required` | Off by default: `/metrics`, system metrics, ecosystem status and the model list are public until it is set |
| A stolen phone or watch | Biometric login on the Android app; refresh tokens are revocable | The Keystore, biometric and Bluetooth code paths are stated as not verified on a device; the watch relay keeps the server JWT on the phone |
| A forged MQTT job claims the machine is idle | The gate uses the observed state, ignores retained messages, handles a key once | Anyone allowed to publish to a bridge's command topic can still ask for a job; the broker ACL is the control, and it is optional outside production |
| A compromised bridge process | It can only publish on its own `hydra/bridges/<name>/#` and read its own `cmd/#` | A compromised host is not contained by the broker |
| A bridge or an AI service is made to actuate | No bridge sends raw CAN or SPI; voice needs a signed single-use confirmation; the maintenance assistant has an allowlist and no tool call from a retrieved text | All of these are software rules: the MCU-level interlock that would enforce them does not exist yet |
| A malicious firmware image | CRC32 and HMAC-SHA256 into a backup slot; downgrade protection | The key is shared by all boards of a type, no read-out protection, a published development key unless a release key is given, a fixed downgrade-authorisation value in the CAN document |
| A malicious update of a repository | Clone, stage, verify, promote; an optional signed-commit gate; one install at a time; time limits | The gate is off by default; the candidate's build-test script runs before the commit is proven the maintainer's if the gate is off; the manifest has a hash and no signature |
| Secrets in Git | `.env` ignored in every repository; the documentation-boundary check in the CI of each | A new repository must carry the same files; the publication check of this repository looks for keys, public addresses and e-mails, and can scan the history |
| A hostile document poisons the assistant | Allowlisted document types, no symbolic links, control characters stripped; adversarial tests for the maintenance assistant | No language model runs today, so the exposure of a real model has not been tested |
| Denial of service on the server | Rate limits, bounded buffers and queues in the services | No measured load test is documented |
| A stuck or compromised dashboard stops the machine from stopping | The server keeps answering stop commands from other clients when a UI hangs; the stop is never blocked by a reservation | The stop acts on the server's state. Until the firmware has an E-STOP path, a physical stop has to be a physical device |

## External review of this ecosystem

A reader from outside the project read the READMEs of the family and concluded that the platform has capabilities that do not exist. The cause was documentation, not code: capabilities that are planned were written in the present tense, some badges promised more than the code does, and some sections contradicted the status box of their own page. The table puts each claim next to what the repositories actually contain.

| Claim that was read | Reality |
|---|---|
| A wired hardware E-STOP stops the machines | No E-STOP path exists in the firmware. `POST /api/stop-all` changes the state held by the server and the zone logic only *requests* a stop through a requester that sends nothing. A physical stop has to be a physical device |
| The firmware enforces kinematic limits and torque limits | It does not. Limits exist only as software checks (server, kinematics validation, hardware-in-the-loop interlock), and no part of the family senses or controls torque |
| Firmware updates are signed | Images are checked with a CRC32 and a symmetric HMAC-SHA256 whose key is shared by all boards of a type; the URTC release images are signed with the published development key. An asymmetric signature is planned, and the update manifest carries a hash, not a signature |
| Nodes authenticate each other with mutual TLS | TLS and mutual TLS are optional, off by default and only offered by the broker and the gateway. There is no node-to-node mutual TLS |
| The bus is FDCAN | The silicon has FDCAN peripherals, used in classic CAN mode: frames of at most eight bytes, no CAN FD |
| A real-time motion engine with S-curve profiles and PID loops runs on the motion controller | It is not written. The motion core runs a smoke test; the CM4 core polls the slave boards and relays frames |
| Object detection runs on the Hailo accelerators | No detector runs. The repositories hold a model registry and a safe-load check, and the zone logic takes object positions from a file |
| Predictive maintenance is AI-driven | The anomaly detector uses a Fourier transform and a statistical baseline. No machine-learning model is trained or used, and no failure is predicted |
| The digital twin is a physics replica of the factory | Today it checks whether its children are ready. No physics engine exists |
| Most repositories are `established` | The word means recorded real use. Where the README or changelog does not record a run on the real target, the manifest now says `functional` |

What changed: every README states what is planned and what has only been tested against fakes, emulators or fixtures, carries a short safety and security status note in the eight languages, and is scanned by `tools/check_claims.py`, which fails when a sentence with a risk word has no status marker next to it and has not been read and put in `data/claims_reviewed.json` by a person. The check runs in the nightly family run and in `tools/check_all.sh`.

## What to do first

1. Finish the physical safety path before anything else: an E-STOP that does not depend on the CM5, the server or a network, and software limits and interlocks in the firmware, tested on a board. No document in this repository should be read as saying the ecosystem is safe to run a machine that can hurt someone without one.
2. Turn on the settings in the baseline's table that are off by default, in that order: production mode, `HYDRA_UMC_INFO_AUTH`, TLS on the server and the broker, broker authentication and ACLs.
3. Give the update manifest a signature field and check it in the updater and the OS agent; switch the signed-commit gate on.
4. Enable read-out protection and per-board keys once a board exists to test the option bytes on.
5. Run the publication check of this repository over the whole family before every public release, with the history scan on.
