"""Tests for Exercise 83 — Longer String Selector."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("83_longer_string_printer")
    select_longer_string = solution.select_longer_string
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestLongerStringSelector:
    def test_first_longer(self):
        result = select_longer_string("hello", "hi")
        assert result == "hello"

    def test_second_longer(self):
        result = select_longer_string("one", "three")
        assert result == "three"

    def test_equal_length(self):
        result = select_longer_string("cat", "dog")
        assert result == ["cat", "dog"]
        assert isinstance(result, list)

    def test_empty_first(self):
        result = select_longer_string("", "hello")
        assert result == "hello"

    def test_empty_second(self):
        result = select_longer_string("hello", "")
        assert result == "hello"

    def test_both_empty(self):
        result = select_longer_string("", "")
        assert result == ["", ""]

    def test_much_longer(self):
        result = select_longer_string("a", "verylongstring")
        assert result == "verylongstring"

    def test_equal_single_char(self):
        result = select_longer_string("a", "b")
        assert result == ["a", "b"]
