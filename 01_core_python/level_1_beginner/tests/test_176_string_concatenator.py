"""Tests for Exercise 82 — String Concatenator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("82_string_concatenator")
    concatenate_strings = solution.concatenate_strings
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestStringConcatenator:
    def test_numbers_as_strings(self):
        result = concatenate_strings("3", "4")
        assert result == "34"

    def test_words(self):
        result = concatenate_strings("hello", "world")
        assert result == "helloworld"

    def test_with_number(self):
        result = concatenate_strings("Python", "3")
        assert result == "Python3"

    def test_empty_first(self):
        result = concatenate_strings("", "hello")
        assert result == "hello"

    def test_empty_second(self):
        result = concatenate_strings("hello", "")
        assert result == "hello"

    def test_both_empty(self):
        result = concatenate_strings("", "")
        assert result == ""

    def test_spaces(self):
        result = concatenate_strings("Hello ", "World")
        assert result == "Hello World"

    def test_longer_strings(self):
        result = concatenate_strings("Python", "Programming")
        assert result == "PythonProgramming"
