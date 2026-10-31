# =============================================================================
# HYDRA-UMC-DOCS - tests/test_check_test_counts.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
from __future__ import annotations

import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_tool():
    spec = importlib.util.spec_from_file_location("check_test_counts", REPO / "tools" / "check_test_counts.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_static_counters_count_the_tests_of_each_language(tmp_path):
    tool = load_tool()
    (tmp_path / "a_test.go").write_text("package a\nfunc TestOne(t *testing.T) {}\nfunc TestTwo(t *testing.T) {}\nfunc helper() {}\n", encoding="utf-8")
    (tmp_path / "lib.rs").write_text("#[test]\nfn one() {}\n#[tokio::test]\nasync fn two() {}\n", encoding="utf-8")
    (tmp_path / "x.test.ts").write_text("it('a', () => {});\ntest('b', () => {});\n", encoding="utf-8")
    assert tool.count_static(tmp_path, "go") == 2
    assert tool.count_static(tmp_path, "cargo") == 2
    assert tool.count_static(tmp_path, "js") == 2
    assert tool.count_static(tmp_path / "missing_dir_is_empty", "go") is None


def test_unittest_count_is_exact_and_a_broken_import_is_unknown(tmp_path):
    tool = load_tool()
    tests = tmp_path / "tests"
    tests.mkdir()
    (tests / "test_ok.py").write_text("import unittest\nclass T(unittest.TestCase):\n    def test_a(self): pass\n    def test_b(self): pass\n", encoding="utf-8")
    assert tool.count_unittest(tmp_path, "tests", "test_*.py") == 2
    (tests / "test_broken.py").write_text("import module_that_does_not_exist\n", encoding="utf-8")
    assert tool.count_unittest(tmp_path, "tests", "test_*.py") is None


def test_the_hub_data_lists_a_command_for_every_counted_repository():
    import json

    data = json.loads((REPO / "data" / "glance.json").read_text(encoding="utf-8"))
    for name, entry in data["repos"].items():
        tests = entry.get("tests")
        assert tests is None or (isinstance(tests["count"], int) and tests["count"] > 0), name
