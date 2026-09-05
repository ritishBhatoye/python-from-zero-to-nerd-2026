"""Tests for Exercise 68 — Log File Analyzer."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("68_log_file_analyzer")
    analyze_log = solution.analyze_log
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestAnalyzeLog:
    def test_basic(self, tmp_path):
        f = tmp_path / "app.log"
        f.write_text("INFO: Start\nWARNING: Low mem\nERROR: Crash\nINFO: End\n")
        assert analyze_log(str(f)) == {"INFO": 2, "WARNING": 1, "ERROR": 1}

    def test_with_malformed(self, tmp_path):
        f = tmp_path / "bad.log"
        f.write_text("INFO: Good\nJust text\nDEBUG: Unknown\nWARNING: Okay: Sure\n")
        assert analyze_log(str(f)) == {"INFO": 1, "WARNING": 1}

    def test_empty(self, tmp_path):
        f = tmp_path / "empty.log"
        f.write_text("")
        assert analyze_log(str(f)) == {}
