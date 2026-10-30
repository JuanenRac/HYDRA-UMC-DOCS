# Design proposals

Short designs for larger features that change a public contract or span several repositories. None of them is implemented; each one says what it would change, so that a decision can be taken before any code is written. A proposal that is accepted moves into the contract documents of the SDK and the repository that owns it.

## 1. Command lifecycle on the robot command route

**Today.** `POST /api/robot/{id}/command` answers `success: true` as soon as the server has accepted the command; the client never learns whether the controller executed it.

**Proposal.** Answer with an `Operation` of the SDK (an `operation_id` and the status `queued` or `sent`) and publish its transitions (`running`, `completed`, `failed`, `cancelled`) on the WebSocket the clients already hold, as events keyed by `operation_id`. The lifecycle helpers and the rule for when a transition concludes success already exist in the Python, Go, TypeScript and Rust clients of the SDK.

**Contract impact.** The answer gains fields (additive); the WebSocket gains one event type. A client that ignores the new fields keeps working. Needs the server, STUDIO, SUITE and the mobile apps to show the state; the command route keeps `success` for the time being.

## 2. Expiring, signed commands on the job topic

**Today.** Anyone who may publish on a bridge command topic can make the bridge act, and an old message that is delivered late is executed as if it were new.

**Proposal.** Every publish to a `cmd/job` topic carries `issued_at`, `expires_in_ms` and a `signature` (HMAC over the topic, the payload and the two fields, with a key per bridge). The bridge refuses a message that is expired, unsigned or from a clock too far away. The shared job intake of the SDK is the single place to enforce it.

**Contract impact.** A new required envelope on command topics, so it ships behind a switch that is off by default and a version of the bridge contract that announces it. The key lives in the existing secrets file of each bridge.

## 3. Bridge health on a retained topic

**Proposal.** Each bridge publishes `hydra/bridges/<name>/health` (retained, QoS 1) with the shape of the SDK `HealthReport`, and sets a last-will that publishes `FAULT` when it disappears. The server and the dashboard read one topic family instead of probing every bridge. It reuses the contract that exists; only the topic name is new.

## 4. Gateway from the server to the bridges

**Proposal.** `GET /api/bridges/{name}/state` and `POST /api/bridges/{name}/cmd/{verb}` in the server, which publishes on the broker with the identity of the logged-in user and writes the audit entry. STUDIO and SUITE then control a CNC, a printer or a pick-and-place machine without knowing MQTT. The broker access list gives the server, and only the server, the right to publish on the command topics.

**Contract impact.** New routes in the OpenAPI document and in the route list of the server; roles reuse the existing ones.

## 5. Orchestrated update of the controller boards

**Proposal.** One service takes a list of boards and updates them in batches: put the board in its bootloader, send the signed image, check the reported version, and stop the batch at the first board that does not come back. Rolling back means sending the previous image, so the service keeps it. It needs the "enter bootloader" command to be reliable on every board and a host agent that can reach them.

## 6. Shadow mode in the hardware-in-the-loop bridge

**Proposal.** Run every real command on the twin a few milliseconds before the real one is sent, and block the command when the twin predicts a collision or a limit violation. The twin already checks trajectories; what is new is the place of the check (in the path of the real command) and the budget (the check must finish inside the time the command can wait, otherwise the command is refused, never sent unchecked).

## 7. Signed safety state

**Proposal.** The safety zones service signs the state it publishes (HMAC for a node that shares a secret, Ed25519 where the verifier must not be able to sign) and includes a counter, so the visual servoing service and the bridges can refuse a state that is old, replayed or unsigned. Fail-closed: an unsigned state is treated as `INHIBITED`.

## 8. Multi-stage missions

**Proposal.** A mission becomes a graph of jobs with dependencies; the orchestrator releases a job when the jobs it depends on are done, and a failed job holds back its dependents instead of failing the mission. The job dispatcher needs no change beyond the fields that already identify a job and its attempt. The graph must be acyclic and is checked when the mission is accepted.

## 9. Replicated mission registry

**Proposal.** The orchestrator keeps its missions in a map that the swarm-sync service replicates between two nodes, so a node that fails does not lose the registry. Before a mission that was in progress is queued again, the new node asks the old robot to confirm that it stopped (fencing), using the attempt number of the job as the token that decides which side wins.

## 10. Historical access for the OPC-UA server

**Proposal.** The OPC-UA server answers history reads for a variable by querying the data lake for the same series and time range, so a SCADA client can plot the past without a second database. The data lake already answers range queries; the work is the mapping between node ids and series, and a limit on how many points one read may return.

## 11. One session store for the mobile apps

**Proposal.** Android, iOS and the touch panel keep the login, the refresh token and the server fingerprint in one small, documented schema, so a fix to token handling lands in all three. The platforms keep their own secure storage; only the schema and the refresh rules are shared, and the shared test vectors live in the SDK.

## 12. Two-slot operating system image

**Proposal.** The image builder produces a root file system for two slots; the updater writes the idle one, switches the boot entry once, and goes back to the previous slot when the first boot does not report healthy within a time limit. It needs a boot loader that can try an entry once, so it can only be tested on a real board.

## 13. Ecosystem map in the studio

**Proposal.** A panel that draws the services of `GET /api/ecosystem/status` with the port registry of the SDK: state, version, the contract each one speaks and an alert when a version is outside the compatibility window. Read-only, so it needs no new route.
