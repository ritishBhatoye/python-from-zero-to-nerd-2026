"""Tests for Exercise 25 — Remove Duplicates."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("25_remove_duplicates")
    remove_duplicates = solution.remove_duplicates
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestRemoveDuplicates:
    def test_basic(self):
        words = ["hello", "world", "and", "practice", "makes", "perfect", "and", "hello", "world", "again"]
        expected = ["again", "and", "hello", "makes", "perfect", "practice", "world"]
        assert remove_duplicates(words) == expected

    def test_empty(self):
        assert remove_duplicates([]) == []

    def test_all_identical(self):
        assert remove_duplicates(["test", "test", "test"]) == ["test"]

    def test_already_unique_and_sorted(self):
        assert remove_duplicates(["a", "b", "c"]) == ["a", "b", "c"]
        
    def test_already_unique_unsorted(self):
        assert remove_duplicates(["c", "a", "b"]) == ["a", "b", "c"]
