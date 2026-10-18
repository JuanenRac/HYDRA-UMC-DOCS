<!--
=============================================================================
HYDRA-UMC-DOCS - The first vertical slice
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# First vertical slice

The smallest path from a client to a machine's state that exists today and that anybody can reproduce from clean checkouts, with no board and no network of devices. It proves that the **contracts agree between repositories**. It does not prove motion, and it says plainly where the path stops.

## The path

1. **HYDRA-UMC-SERVER** starts in an isolated temporary directory on a free port (the verification scripts of the server do this themselves, and `npm run dev` starts it by hand).
2. **HYDRA-UMC-SDK** is the judge of the first answer: the real `GET /api/hydra-info` response is validated against the `ServerDiscovery` contract with the reference client of the SDK (`tools/verify_discovery_contract.mjs` in the server, which expects the SDK next to it).
3. A client **signs in** (`POST /api/login`), receives a Bearer token and a refresh token, and **reads the state** (`GET /api/settings`), as STUDIO, SUITE, the phones and the command line all do. **HYDRA-UMC-TOOL-CLI** is the smallest real client: `hydra-cli status`, `robots` and `doctor` talk to a live server and check its answers against the contract.
4. The client sends an **atomic robot command** (`POST /api/robot/:id/command`); the server applies it to its state, saves it and broadcasts a `delta` on `/ws`. A second account cannot command a robot that the first one has claimed.
5. **`POST /api/stop-all`** stops every robot in the server's state and switches every valve and pump off, and answers one result per robot.
6. The same state is what the **gateway children** read to expose it as an OPC UA address space and MTConnect XML, the OPC UA one tested with a real OPC UA client over the binary protocol, the MTConnect one with HTTP tests of the document shape.

## How to run it

```bash
# 1. the server's own checks start a live instance of it on a temporary port
cd HYDRA-UMC-SERVER && npm ci && npm test   # with HYDRA-UMC-SDK checked out next to it

# 2. the command line against a server that is running (npm run dev in another terminal)
cd HYDRA-UMC-TOOL-CLI && ./run.sh status --server http://localhost:3000

# 3. the same server, seen from the whole family
cd HYDRA-UMC-DOCS && bash tools/check_all.sh
```

The scripts of the server that cover the steps are `verify_discovery_contract`, `verify_auth_negative`, `verify_refresh_token_contract`, `verify_robot_command_contract`, `verify_robot_ownership_contract`, `verify_global_stop_contract` and `verify_ws_sustained_reconnect_contract` (all under `tools/` and all run by `npm test`).

## What it proves

* The discovery answer of the server conforms to the contract that the SDK publishes.
* Authentication, refresh-token rotation and the negative cases (a wrong or missing token, a client that is not allowed) behave as `REMOTE_API.md` says.
* A command reaches the state, is persisted and is broadcast; ownership and the global stop behave as documented.

## What it does not prove

* **Motion.** There is no path from this state to a physical output: the H745 application that would act on it does not generate motion yet, and no populated board exists. The slice ends at the server's state.
* **The stop as a safety function.** `stop-all` changes the server's state. The firmware has no E-STOP path (see the [security baseline](SECURITY_BASELINE.md)).
* **The bridges, the broker, the cameras, the AI services and the data services.** Each has its own row in the [capability matrix](CAPABILITY_MATRIX.md); none is part of this path.
* **Several services on one machine.** The compose files and the full topology have not been exercised as one stack.

The next slice, in the order the dependencies allow: a bridge job through the SDK gate over a real broker to an emulated machine (the bridges are tested against emulators and fake brokers separately, never together with a real broker); then a firmware image through the SPI bridge to a board, once a board exists.
