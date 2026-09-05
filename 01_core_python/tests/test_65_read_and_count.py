"""Tests for Exercise 65 — Read and Count."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("65_read_and_count")
    count_file_stats = solution.count_file_stats
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCountFileStats:
    def test_basic(self, tmp_path):
        f = tmp_path / "test.txt"
        f.write_text("Hello world\nPython is fun\n")
        assert count_file_stats(str(f)) == {"lines": 2, "words": 5, "characters": 26}

    def test_empty(self, tmp_path):
        f = tmp_path / "empty.txt"
        f.write_text("")
        assert count_file_stats(str(f)) == {"lines": 0, "words": 0, "characters": 0}

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            count_file_stats("nonexistent_file.txt")
