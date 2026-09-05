"""Tests for Exercise 66 — Write Lines."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("66_write_lines")
    write_numbered_lines = solution.write_numbered_lines
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestWriteNumberedLines:
    def test_basic(self, tmp_path):
        f = tmp_path / "test.txt"
        lines = ["Apple", "Banana", "Cherry"]
        assert write_numbered_lines(str(f), lines) == 3
        content = f.read_text()
        assert content == "1: Apple\n2: Banana\n3: Cherry\n"

    def test_empty(self, tmp_path):
        f = tmp_path / "empty.txt"
        assert write_numbered_lines(str(f), []) == 0
        content = f.read_text()
        assert content == ""
