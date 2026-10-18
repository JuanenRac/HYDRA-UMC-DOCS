# Changelog: HYDRA-UMC-DOCS 📚

All notable changes to this project will be documented in this file. The
version number follows this ecosystem's "odometer" scheme: PATCH +1 on
every real build, rolling into MINOR past 9 (`0.0.9` -> `0.1.0`); MAJOR is
bumped manually only. See `bump_version.py`.

## [0.0.1] - The documentation and tooling hub of the ecosystem

- **Documents:** the architecture (layers, data flows, ports, trust boundaries), the interfaces and who owns each contract, the capability matrix (what is absent, builds, local, emulated, in use or verified, project by project), the security baseline, the threat model, the first vertical slice and the generated project catalogue. They are written from the READMEs, manifests, changelogs and documents of the other repositories, and mark what could not be traced.
- **Project catalogue:** `tools/make_catalog.py` writes the table from the manifests found next to this repository (`--check` for the whole table, `--check-structure` for which repositories exist and of what kind), with one curated sentence per repository.
- **Brand:** `tools/make_brand.py` writes the banner, the icon and the map of the families in the look of HYDRA-UMC.
- **READMEs:** `tools/make_readmes.py` writes the README of this repository in the eight languages (English, Spanish, French, Italian, German, Chinese, Japanese and European Portuguese) from one source, with the same sections and links in each.
- **Publication check:** `tools/publication_check.py` looks, in every repository of the family, for private keys, public IP addresses, personal e-mail addresses, tracked secret files, names of private documents, internal tracking codes, commits by someone else or with a co-author trailer, and (with `--history`) for lines that were committed and later removed. A key header or an address inside a test or conformance fixture, four small numbers that look like a version, and the name of an AI provider in a commit message are findings to review, not blocks; naming the assistant itself in a commit is a block.
- **Family check:** `tools/check_all.sh` runs the own `tools/ci_validate.py` of every repository next to this one and prints one PASS, FAIL or SKIP line each (a skipped check is never reported as a pass), then the checks of this repository; `--sync` adds the three sync scripts of HYDRA-UMC-SDK.
- **CI:** the baseline workflow runs the shared validation, the generator checks and the unit tests; a nightly workflow fetches the other repositories and compares them.
- **Shared checks:** `tools/ci_validate.py`, `tools/_doc_policy.py`, `tools/_readme_parity.py` and `bump_manifest_version.py` are the copies kept in sync by HYDRA-UMC-SDK, not re-implemented here.
