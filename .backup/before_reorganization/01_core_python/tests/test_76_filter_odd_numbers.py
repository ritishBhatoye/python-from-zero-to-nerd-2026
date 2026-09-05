"""Tests for Exercise 76 — Filter Odd Numbers."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("76_filter_odd_numbers")
    filter_odd_numbers = solution.filter_odd_numbers
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFilterOddNumbers:
    def test_basic_mixed(self):
        result = filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert result == [1, 3, 5, 7, 9]

    def test_all_even(self):
        result = filter_odd_numbers([10, 20, 30])
        assert result == []

    def test_all_odd(self):
        result = filter_odd_numbers([11, 13, 15])
        assert result == [11, 13, 15]

    def test_empty_list(self):
        result = filter_odd_numbers([])
        assert result == []

    def test_single_odd(self):
        result = filter_odd_numbers([7])
        assert result == [7]

    def test_single_even(self):
        result = filter_odd_numbers([8])
        assert result == []

    def test_negative_numbers(self):
        result = filter_odd_numbers([-3, -2, -1, 0, 1, 2, 3])
        assert result == [-3, -1, 1, 3]

    def test_preserves_order(self):
        result = filter_odd_numbers([9, 7, 5, 3, 1])
        assert result == [9, 7, 5, 3, 1]
