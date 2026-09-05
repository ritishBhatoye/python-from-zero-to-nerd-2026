"""Tests for Exercise 26 — Sort Words."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("26_sort_words")
    sort_words = solution.sort_words
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSortWords:
    def test_basic(self):
        assert sort_words(["without", "hello", "bag", "world"]) == ["bag", "hello", "without", "world"]

    def test_case_insensitive(self):
        assert sort_words(["Zebra", "apple", "Banana"]) == ["apple", "Banana", "Zebra"]

    def test_empty(self):
        assert sort_words([]) == []

    def test_mixed_case_same_word(self):
        words = ["a", "A", "b"]
        expected = ["a", "A", "b"] 
        assert sort_words(words) == expected
        
    def test_preserves_original(self):
        words = ["c", "b", "a"]
        sort_words(words)
        assert words == ["c", "b", "a"]
