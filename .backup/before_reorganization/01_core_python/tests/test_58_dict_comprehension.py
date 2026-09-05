"""Tests for Exercise 58 — Dict Comprehension."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("58_dict_comprehension")
    word_lengths = solution.word_lengths
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestWordLengths:
    def test_basic_words(self):
        assert word_lengths(["hello", "world", "python"]) == {"hello": 5, "world": 5, "python": 6}

    def test_empty_list(self):
        assert word_lengths([]) == {}

    def test_duplicate_words(self):
        assert word_lengths(["test", "test"]) == {"test": 4}

    def test_empty_string(self):
        assert word_lengths([""]) == {"": 0}
