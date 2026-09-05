"""Tests for Exercise 30 — Second Largest."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("30_second_largest")
    second_largest = solution.second_largest
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSecondLargest:
    def test_basic(self):
        assert second_largest([10, 20, 4, 45, 99]) == 45

    def test_duplicate_largest(self):
        assert second_largest([5, 5, 4]) == 4
        assert second_largest([10, 20, 20, 4, 5]) == 10

    def test_less_than_two_unique(self):
        with pytest.raises(ValueError):
            second_largest([10])
        
        with pytest.raises(ValueError):
            second_largest([10, 10, 10])
        
        with pytest.raises(ValueError):
            second_largest([])

    def test_negative_numbers(self):
        assert second_largest([-10, -20, -4, -45, -99]) == -10
