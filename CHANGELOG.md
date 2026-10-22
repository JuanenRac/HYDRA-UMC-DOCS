# Changelog: HYDRA-UMC-DOCS 📚

All notable changes to this project are documented here.

## [Unreleased]

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
