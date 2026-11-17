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
    assert [light for _, light, _ in status.rows("en", MANIFEST, entry)].count("green") == 2
    assert [light for area, light, _ in status.rows("en", manifest, entry) if area == "Real hardware"] == ["white"]


def test_not_applicable_is_never_green_and_shows_a_white_light_and_its_legend_only_then():
    entry = {"hardware": "not_applicable", "tests": {"count": 3, "command": "pytest"}}
    for code in sorted(glance.LANGUAGE_FILES):
        section = status.render_section(code, MANIFEST, entry)
        marked = [line for line in section.splitlines() if line.startswith("| ") and "⚪" in line]
        assert len(marked) == 1, code
        legend = [line for line in section.splitlines() if " · " in line and "⚪" in line]
        assert len(legend) == 1, code    # the legend names the white light
    bound = status.render_section("en", MANIFEST, {"hardware": "not_run", "tests": {"count": 3, "command": "pytest"}})
    assert "⚪" not in bound
    assert status.HARDWARE_LIGHT["not_applicable"] == "white"
    assert status.HARDWARE_LIGHT["in_use"] == "green"


def test_extra_lines_come_from_the_data_in_the_fixed_order_and_every_state_has_all_eight_languages():
    from hydra_umc_docs import status_rows

    entry = {"hardware": "not_run", "tests": {"count": 5, "command": "pytest"},
             "rows": {"deployment": "cm5_service", "security": "host_tested", "interface": "documented_tested"}}
    areas = [area for area, _, _ in status.rows("en", MANIFEST, entry)]
    assert areas == ["Software", "Tests", "Real hardware", "Interface and protocols", "Security", "Deployment", "Documentation"]
    for key, states in status_rows.STATES.items():
        assert set(status_rows.LABELS[key]) == set(status_rows.LANGS)
        for state, (level, notes) in states.items():
            assert level in status.LIGHTS, (key, state)
            assert set(notes) == set(status_rows.LANGS), (key, state)
            assert all(text.strip() for text in notes.values()), (key, state)
    for code in glance.LANGUAGE_FILES:
        assert len(status.rows(code, MANIFEST, entry)) == 7


def test_an_integration_line_never_goes_above_the_evidence_of_the_manifest():
    entry = {"hardware": "not_run", "rows": {"integration": "bench"}}

    def light(manifest):
        return [level for area, level, _ in status.rows("en", manifest, entry) if area == "Integration"][0]

    assert light(dict(MANIFEST, evidence="none")) == "orange"
    assert light(dict(MANIFEST, evidence="simulator")) == "orange"
    assert light(dict(MANIFEST, evidence="bench")) == "yellow"
    assert light(dict(MANIFEST, evidence="none", hardware_bound=False)) == "yellow"


def test_a_security_line_is_white_when_there_is_nothing_to_protect():
    from hydra_umc_docs import status_rows

    for state, (level, _) in status_rows.STATES["security"].items():
        assert (level == "white") == (state == "not_applicable"), state
    for key, states in status_rows.STATES.items():
        assert states.get("not_applicable", ("white",))[0] == "white", key


def test_the_data_file_rejects_an_unknown_line_or_state(tmp_path):
    import json

    path = tmp_path / "glance.json"
    path.write_text(json.dumps({"repos": {"X": {"hardware": "not_run", "rows": {"security": "perfect"}}}}), encoding="utf-8")
    with pytest.raises(glance.GlanceError):
        glance.load_data(path)
