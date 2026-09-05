"""Tests for Exercise 19 — String Reverser."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("19_string_reverser")
    reverse_string = solution.reverse_string
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestReverseString:
    def test_basic(self):
        assert reverse_string("hello") == "olleh"

    def test_empty(self):
        assert reverse_string("") == ""

    def test_single_char(self):
        assert reverse_string("a") == "a"

    def test_spaces(self):
        assert reverse_string("a b c") == "c b a"
