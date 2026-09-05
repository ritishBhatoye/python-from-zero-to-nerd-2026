"""Tests for Exercise 22 — Capitalize Sentences."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("22_capitalize_sentences")
    capitalize_lines = solution.capitalize_lines
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCapitalizeLines:
    def test_basic(self):
        assert capitalize_lines(["hello world", "practice"]) == ["HELLO WORLD", "PRACTICE"]

    def test_empty_list(self):
        assert capitalize_lines([]) == []

    def test_empty_strings(self):
        assert capitalize_lines(["", "hello", ""]) == ["", "HELLO", ""]

    def test_already_upper(self):
        assert capitalize_lines(["HELLO", "WORLD"]) == ["HELLO", "WORLD"]

    def test_mixed_chars(self):
        assert capitalize_lines(["123 hello!", "abc 456"]) == ["123 HELLO!", "ABC 456"]
