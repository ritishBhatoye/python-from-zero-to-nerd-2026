"""Tests for Exercise 27 — Filter Odd Squares."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("27_odd_numbers")
    odd_numbers = solution.odd_numbers
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestOddNumbers:
    def test_basic(self):
        assert odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]

    def test_all_even(self):
        assert odd_numbers([2, 4, 6, 8]) == []

    def test_empty(self):
        assert odd_numbers([]) == []

    def test_negative_numbers(self):
        assert odd_numbers([-3, -2, -1, 0, 1, 2, 3]) == [-3, -1, 1, 3]

    def test_all_odd(self):
        assert odd_numbers([1, 3, 5]) == [1, 3, 5]
