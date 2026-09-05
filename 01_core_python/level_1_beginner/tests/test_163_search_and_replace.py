"""Tests for Exercise 69 — Search and Replace."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("69_search_and_replace")
    search_replace_file = solution.search_replace_file
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSearchReplaceFile:
    def test_basic(self, tmp_path):
        f = tmp_path / "test.txt"
        f.write_text("Hello foo\nfoo foo bar\n")
        assert search_replace_file(str(f), "foo", "world") == 3
        assert f.read_text() == "Hello world\nworld world bar\n"

    def test_not_found(self, tmp_path):
        f = tmp_path / "test.txt"
        f.write_text("Hello\n")
        assert search_replace_file(str(f), "foo", "world") == 0
        assert f.read_text() == "Hello\n"

    def test_empty_search(self, tmp_path):
        f = tmp_path / "test.txt"
        f.write_text("Hello\n")
        with pytest.raises(ValueError):
            search_replace_file(str(f), "", "world")
