"""Tests for Exercise 21 — Word Counter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("21_word_counter")
    count_words = solution.count_words
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCountWords:
    def test_basic(self):
        assert count_words("hello world") == 2

    def test_multiple_spaces(self):
        assert count_words("  multiple   spaces  ") == 2

    def test_empty(self):
        assert count_words("") == 0

    def test_only_spaces(self):
        assert count_words("     ") == 0

    def test_single_word(self):
        assert count_words("hello") == 1
