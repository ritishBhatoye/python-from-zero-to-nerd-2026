"""Tests for Exercise 59 — Set Comprehension."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("59_set_comprehension")
    unique_lengths = solution.unique_lengths
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestUniqueLengths:
    def test_different_lengths(self):
        assert unique_lengths(["cat", "dog", "elephant"]) == {3, 8}

    def test_same_lengths(self):
        assert unique_lengths(["one", "two", "six"]) == {3}

    def test_empty_list(self):
        assert unique_lengths([]) == set()

    def test_empty_strings(self):
        assert unique_lengths(["", "a", ""]) == {0, 1}
