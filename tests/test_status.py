"""The "Project status" traffic-light table: made from the manifest and the data file, eight languages, only the light in the State column."""
import re

import pytest

from hydra_umc_docs import glance, status

MANIFEST = {"name": "HYDRA-UMC-DEMO", "version": "1.2.3", "maturity": "functional", "role": "service", "deployment_target": "cm5", "technologies": ["Python"]}
ENTRY = {"hardware": "simulated", "tests": {"count": 12, "command": "pytest"}}


def readme(code):
    return "# T\n\nintro\n\n" + glance.render_section(code, MANIFEST, ENTRY) + "\n## Other\n\ntext\n"


@pytest.mark.parametrize("code", sorted(glance.LANGUAGE_FILES))
def test_the_section_has_one_row_per_area_and_only_the_light_in_the_state_column(code):
    section = status.render_section(code, MANIFEST, ENTRY)
    rows = [line for line in section.splitlines() if line.startswith("| ")][1:]
    assert len(rows) == 4
    for row in rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        assert cells[1] in status.LIGHTS.values()
    assert "12" in rows[1]


def test_hardware_that_was_only_simulated_is_never_green():
    section = status.render_section("en", MANIFEST, ENTRY)
    hardware = [line for line in section.splitlines() if line.startswith("| Real hardware")][0]
    assert "🟠" in hardware and "🟢" not in hardware


def test_apply_inserts_after_the_glance_section_and_is_idempotent():
    section = status.render_section("en", MANIFEST, ENTRY)
    once = status.apply_to_text(readme("en"), section)
    assert status.apply_to_text(once, section) == once
    assert status.check_text(once, section) == []
    assert once.index("## 📋") < once.index("## 🚦") < once.index("## Other")
    assert len(re.findall(r"(?m)^## 🚦", once)) == 1


def test_check_reports_a_missing_and_a_stale_table():
    section = status.render_section("en", MANIFEST, ENTRY)
    assert status.check_text(readme("en"), section) == ["the status table is missing"]
    stale = status.apply_to_text(readme("en"), section).replace("🟠", "🟢")
    assert any("stale" in problem for problem in status.check_text(stale, section))


def test_a_scaffolding_repository_has_no_green_row():
    manifest = dict(MANIFEST, maturity="scaffolding")
    entry = {"hardware": "not_applicable", "tests": {"count": 3, "command": "pytest"}}
    lights = [light for _, light, _ in status.rows("en", manifest, entry)]
    assert "green" not in lights
    assert [light for _, light, _ in status.rows("en", MANIFEST, entry)].count("green") == 3
