# Changelog

All notable changes to this project are documented here.

## [Unreleased]

- **`tools/i18n_cross_check.py`:** reads the language files of STUDIO, SUITE, ANDROID-CONTROL and WATCH into one shape, fails when a client lacks a key in any of the eight languages and lists the texts that are the same in English in two clients but read differently in another language (`--lang`, `--list`, `--json`), so the wording can be aligned when a client is touched.

## [0.0.6] - The service and contract READMEs from their sources, the CM5 test bench document, own roadmaps and the manual steps to compile a HEF

- **README sources for the service and contract work:** a paragraph in the eight languages for the laser and CNC bridges (running as a service from one configuration file), the production reports (windows summed by the data lake and the cache of the aggregates), the twin (state schema and JSON Schema validation), the swarm sync (typed robot state), the physics replica (tests against two real arms), the semantic planner, the orchestrator and the job dispatcher (a plan as the common Operation) and the visual servoing API (the safety verdict by default in the unit); the count of contracts of the SDK is 13.
- **`docs/CM5_TEST_BENCH.md`:** the bench document of the CM5, with one row per service (port, health path, unit) and three columns left empty on purpose (what the installer guarantees, what was tested on a real CM5, what was not), and how a bench run fills them.
- **Own roadmaps in the READMEs of SYNTHETIC-DATA-GEN and VISUAL-SERVOING-API** (eight languages): the first one lists splits and fixed classes, masks, keypoints, PNG output and the TWIN integration; the second hand-eye calibration, image-based servoing, a rate limit and a watchdog. Both used the roadmap of other projects.
- **The roadmap of GATEWAY-INDUSTRIAL says that Profinet and ISO-27001 are only ideas** (eight languages), not implemented, and that they would live in a separate project still to be defined.
- **The DETECTION-HEF README points to the manual steps for compiling a HEF** (eight languages), and says the script that automates them waits for a Dataflow Compiler licence.
- **The SUITE README explains how to check the installer** (eight languages): it is not signed with Authenticode; a SHA-256 checksum and an Ed25519 signature are published next to it.
## [0.0.5] - The readme sources describe the functions of the night batches, the decisions of the week and a corrected count of tests

- **`docs/DESIGN_PROPOSALS.md`:** short designs, not implemented, for the larger features that would change a public contract or span several repositories (command lifecycle, signed and expiring commands, bridge health topic, server gateway to the bridges, orchestrated board updates, shadow mode, signed safety state, multi-stage missions, replicated mission registry, historical access for OPC-UA, shared session store, two-slot image, ecosystem map).
- **The VISION-STREAMER README source no longer promises the Pi 5 ISP for USB cameras** (introduction and diagram, eight languages).
- **A page of keys and secrets:** `docs/KEYS.md` lists every key, secret and token of the ecosystem (release signing, firmware, sessions, service tokens, MQTT, backup) with where it lives, who makes it, how it is replaced and what to do if it is lost or leaks. It holds no key material.
- **README in the universal layout:** the README and its seven translations follow the layout that the four families share (22 sections in a fixed order), with an architecture picture and a repository-structure picture drawn from `docs/architecture.json` and `docs/structure.json`; the CI validator checks both pictures and the file tree.

- **The READMEs of fourteen more repositories are written from one source each:** the development server, the touch screen app, the industrial gateway, the local technician, the MQTT broker, the MTConnect adapter, node healing, the OPC-UA server, the ops agent, the orchestrator, the OS image rebuilder, the OS layer, the path planner and the physics replica now have a source in `readme_src/repos`, with the prose of their earlier READMEs kept in `readme_src/verbatim` and the shared sentences of the services in `readme_src/service_kit.py`.

- **The layout of the README is checked in the CI:** the validator runs `tools/universal_readme_check.py` and lists, as a warning, what differs from the universal layout of the README.

## [0.0.4] - Added the "Project status" traffic-light table to the README generator

- Added the "Project status" traffic-light table to the README generator: one row each for software, tests, real hardware and documentation, with the light taken only from the maturity, the test count and the hardware statement of the data file, in the eight languages and with only the light in the State column. `make_glance.py` writes and checks it together with the "At a glance" table.
- The reviewed line of the claims check for the Electro Hobby 3D updater follows its README again (the sentence about the two ecosystems grew), so the nightly check passes.
- The test counts of the "At a glance" data for the SERVER and the Android control app follow their READMEs again, so the nightly check of that section passes for them.
- The validator is the shared copy of the repositories again (it also checks the documentation links and the README section parity).
- Building no longer changes the version; raising it is the explicit `bump` command (`python tools/hydra_project_tool.py bump`). The build scripts only report the version they built, and CI fails if a build script runs a bump.
- The build and run scripts use the Python of the `.venv` directly instead of an activate script, and create the venv with the `py` launcher when there is one; CI fails if a script activates a venv.
- The brand generator no longer writes the banner of this repository: it is made, like every project banner, by the profile's `tools/project_banner.py`, and the generator keeps the icon and the map of the families.
- The banner follows the animated style of the ecosystem banners, with the name, the kind and the technologies of the project.
- Added `tools/hydra_project_tool.py`: the same `validate`, `test`, `version`, `status` and `bump` commands in every repository. The checks run with `HYDRA_UMC_CI=1` and fail if the version changes; only `bump` changes it.
- The nightly family check compares the shared tooling of every repository with its canonical copy (`sync_repo_tools.py --check`) and reports, as advisory, the consumers of the SDK that are not on its newest release tag; `check_all.sh --sync` runs the same two checks.
- The test counts of the orchestrator (126) and of the server (178) in the at-a-glance data are the ones their READMEs state.

## [0.0.3]

- New check `tools/check_claims.py` (module `claims`, 12 tests): it reads the English README of every repository of the family and fails when a sentence has a risk word (E-STOP, interlock, real-time, signed, mTLS, FDCAN, YOLO, AI-driven, autonomous, certified, ...) and no status marker next to it, unless the line is in `data/claims_reviewed.json`.
- The nightly family run and `tools/check_all.sh` run the claim check; the README documents the rule in the eight languages and carries the short safety and security status note.
- `docs/THREAT_MODEL.md` has a section that sets the capabilities a reader from outside concluded from the READMEs against what the repositories contain.
- The glance data, the catalogue and the README text follow the maturity that the manifests now declare.

## [0.0.2] - The At a glance tables

- **At a glance:** `tools/make_glance.py` inserts, or rewrites in place, the At a glance table in the README and its seven translations of every repository of the family, written from the manifest of each repository (version, maturity, stack, target) and from `data/glance.json` (test count when it is known, target, and one hardware statement chosen from a closed vocabulary that is translated once in the eight languages). It keeps the line endings of each file, never duplicates the section, and `--check` fails when a section is missing, misplaced or stale; `--repo NAME` limits it to one repository.
- **After a version bump:** run `python tools/make_glance.py --apply --repo NAME` to refresh the Version cell of that repository.
- **Nightly check:** the nightly workflow and `tools/check_all.sh` now compare the At a glance tables of all the sibling repositories with their manifests, so a table that was not refreshed after a version bump is reported.
- **This README:** the table of this repository is written by the same tool, so the labels are the ones used in the other repositories.

## [0.0.1] - The documentation and tooling hub of the ecosystem

- **Documents:** the architecture (layers, data flows, ports, trust boundaries), the interfaces and who owns each contract, the capability matrix (what is absent, builds, local, emulated, in use or verified, project by project), the security baseline, the threat model, the first vertical slice and the generated project catalogue. They are written from the READMEs, manifests, changelogs and documents of the other repositories, and mark what could not be traced.
- **Project catalogue:** `tools/make_catalog.py` writes the table from the manifests found next to this repository (`--check` for the whole table, `--check-structure` for which repositories exist and of what kind), with one curated sentence per repository.
- **Brand:** `tools/make_brand.py` writes the banner, the icon and the map of the families in the look of HYDRA-UMC.
- **READMEs:** `tools/make_readmes.py` writes the README of this repository in the eight languages (English, Spanish, French, Italian, German, Chinese, Japanese and European Portuguese) from one source, with the same sections and links in each.
- **Publication check:** `tools/publication_check.py` looks, in every repository of the family, for private keys, public IP addresses, personal e-mail addresses, tracked secret files, names of private documents, internal tracking codes, commits by someone else or with a co-author trailer, and (with `--history`) for lines that were committed and later removed. A key header or an address inside a test or conformance fixture, four small numbers that look like a version, and the name of an AI provider in a commit message are findings to review, not blocks; naming the assistant itself in a commit is a block.
- **Family check:** `tools/check_all.sh` runs the own `tools/ci_validate.py` of every repository next to this one and prints one PASS, FAIL or SKIP line each (a skipped check is never reported as a pass), then the checks of this repository; `--sync` adds the three sync scripts of HYDRA-UMC-SDK.
- **CI:** the baseline workflow runs the shared validation, the generator checks and the unit tests; a nightly workflow fetches the other repositories and compares them.
- **Shared checks:** `tools/ci_validate.py`, `tools/_doc_policy.py`, `tools/_readme_parity.py` and `bump_manifest_version.py` are the copies kept in sync by HYDRA-UMC-SDK, not re-implemented here.
