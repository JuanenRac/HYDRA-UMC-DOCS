# =============================================================================
# HYDRA-UMC-DOCS - tests/test_publication.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The publication check, on throw-away git repositories and on single lines.

Every forbidden word is built from pieces, so that this file never contains one
(the documentation-boundary check of CI reads the tracked files, this one too).
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from hydra_umc_docs import publication
from hydra_umc_docs.publication import scan_text

PRIVATE = "SON" + "NET"
AI = "Cla" + "ude"
AUTHOR = "JuanenRac (Electro Hobby 3D)"
EMAIL = "electrohobby3d@gmail.com"


def scan(line: str, document: bool = False):
    findings: list = []
    scan_text("R", "f", line, findings, document=document)
    return findings


def kinds(findings):
    return sorted({(kind, what) for kind, _repo, _where, what in findings})


def test_a_private_key_header_blocks():
    assert kinds(scan("-----BEGIN " + "RSA PRIVATE KEY-----")) == [("BLOCK", "private key")]


def test_the_projects_own_address_is_fine_a_personal_one_blocks():
    assert scan(f"contact {EMAIL}") == []
    found = scan("write to someone" + "@gmail.com please")
    assert [item[0] for item in found] == ["BLOCK"] and "personal e-mail" in found[0][3]
    assert "someone" not in found[0][3]   # the address itself is never printed


@pytest.mark.parametrize("address", ["8.8.8.8", "1.1.1.1", "192.168.0.10", "10.1.2.3", "127.0.0.1", "172.16.5.4", "224.0.0.1"])
def test_private_and_well_known_addresses_are_fine(address):
    assert scan(f"host {address}") == []


def test_a_public_address_blocks_and_is_cut_to_its_first_octet():
    found = scan("server at " + ".".join(["93", "184", "216", "34"]))
    assert len(found) == 1 and found[0][0] == "BLOCK" and found[0][3] == "public IP address 93.x.x.x"


def test_a_version_number_with_four_parts_is_not_an_address():
    assert scan("release version 93.184.216.34") == []
    assert scan("v93.184.216.34") == []


def test_names_of_private_documents_and_tracking_codes_block():
    assert ("BLOCK", "the name of a private document") in kinds(scan(f"see {PRIVATE}/notes"))
    assert ("BLOCK", "an internal tracking code") in kinds(scan("fixed as " + "REV" + "-123"))
    assert ("BLOCK", "an internal tracking code") in kinds(scan("see " + "[[" + "project_x" + "]]"))
    assert ("BLOCK", "a reference to private planning material") in kinds(scan("the " + "internal work" + " log says"))


def test_ai_and_review_round_mentions_and_dates_are_for_a_person_to_review():
    assert kinds(scan(f"written by {AI}")) == [("REVIEW", "mentions an AI tool")]
    assert kinds(scan("the " + "aud" + "it" + " round 3 found")) == [("REVIEW", "mentions an internal review round")]
    assert scan("the " + "aud" + "it" + " log of the server") == []
    assert kinds(scan("released on " + "2031" + "-01-02", document=True)) == [("REVIEW", "a calendar date in a document")]
    assert scan("released on " + "2031" + "-01-02", document=False) == []


def test_literal_secrets_are_reviewed_but_examples_are_not():
    assert [item[0] for item in scan('password = "Zx9' + 'qL2vB7nRt"')] == ["REVIEW"]
    assert scan('password = "changeme-please"') == []
    assert scan('token = "${TOKEN_FROM_ENV}"') == []


def test_tracked_secret_paths():
    for path in (".env", "config/prod.env", "keys/server.pem", "id_ed25519", "secrets/db"):
        assert publication.BAD_PATH.search(path), path
    for path in (".env.example", "secrets/example.json", "README.md"):
        assert not publication.BAD_PATH.search(path), path


def git(repo: Path, *args: str, env_author: str = AUTHOR, email: str = EMAIL) -> None:
    environment = {
        "GIT_AUTHOR_NAME": env_author, "GIT_AUTHOR_EMAIL": email,
        "GIT_COMMITTER_NAME": env_author, "GIT_COMMITTER_EMAIL": email,
        "PATH": __import__("os").environ["PATH"], "HOME": str(repo), "SYSTEMROOT": __import__("os").environ.get("SYSTEMROOT", ""),
    }
    subprocess.run(["git", "-C", str(repo), "-c", "commit.gpgsign=false", *args], check=True, capture_output=True, env=environment)


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    path = tmp_path / "HYDRA-UMC-FAKE"
    path.mkdir()
    git(path, "init", "-q")
    (path / "README.md").write_text("A clean repository.\n", encoding="utf-8")
    git(path, "add", ".")
    git(path, "commit", "-q", "-m", "Add the readme")
    return path


def test_a_clean_repository_has_no_findings(repo):
    assert publication.check_repo(repo) == []
    assert publication.summarize([]) == (0, 0)


def test_a_commit_by_someone_else_or_with_a_trailer_blocks(repo):
    (repo / "a.txt").write_text("a\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "Add a", env_author="Somebody Else", email="x@example.org")
    (repo / "b.txt").write_text("b\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "Add b\n\nCo-Authored-By: Someone <s@example.org>")
    (repo / "c.txt").write_text("c\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", f"Add c, written with {AI}")
    whats = [item[3] for item in publication.check_repo(repo) if item[0] == "BLOCK"]
    assert any("author or committer" in what for what in whats)
    assert sum("trailer" in what for what in whats) == 2


def test_a_tracked_env_file_and_a_leaked_line_block(repo):
    (repo / ".env").write_text("A=1\n", encoding="utf-8")
    (repo / "notes.md").write_text(f"see {PRIVATE}\n", encoding="utf-8")
    git(repo, "add", "-f", ".")
    git(repo, "commit", "-q", "-m", "Add files")
    whats = [item[3] for item in publication.check_repo(repo) if item[0] == "BLOCK"]
    assert "a secrets, key or environment file is tracked" in whats
    assert "the name of a private document" in whats


def test_history_scan_finds_a_removed_secret_file_and_removed_lines(repo):
    (repo / "server.pem").write_text("x\n", encoding="utf-8")
    (repo / "conf.txt").write_text("host " + ".".join(["93", "184", "216", "34"]) + "\n", encoding="utf-8")
    git(repo, "add", "-f", ".")
    git(repo, "commit", "-q", "-m", "Add")
    git(repo, "rm", "-q", "-f", "server.pem", "conf.txt")
    git(repo, "commit", "-q", "-m", "Remove")
    assert publication.check_repo(repo, history=False) == []
    whats = [item[3] for item in publication.check_repo(repo, history=True) if item[0] == "BLOCK"]
    assert "a secrets, key or environment file was tracked in the history" in whats
    assert "public IP address 93.x.x.x" in whats


def test_family_repos_lists_only_checkouts_of_the_family(tmp_path):
    for name in ("HYDRA-UMC", "HYDRA-UMC-A", "OTHER"):
        (tmp_path / name / ".git").mkdir(parents=True)
    (tmp_path / "HYDRA-UMC-B").mkdir()   # no .git
    assert [p.name for p in publication.family_repos(tmp_path)] == ["HYDRA-UMC", "HYDRA-UMC-A"]


def test_the_check_passes_on_this_repository():
    """The repository that carries the check must itself have nothing to publish."""
    here = Path(__file__).resolve().parents[1]
    if not (here / ".git").exists():
        pytest.skip("not a git checkout")
    blocked = [item for item in publication.check_repo(here) if item[0] == "BLOCK" and not item[2].startswith("commit ")]
    assert blocked == []
