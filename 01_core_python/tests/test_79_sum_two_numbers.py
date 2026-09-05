"""Tests for Exercise 79 — Sum Two Numbers."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("79_sum_two_numbers")
    sum_two_numbers = solution.sum_two_numbers
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSumTwoNumbers:
    def test_basic_sum(self):
        assert sum_two_numbers(1, 2) == 3

    def test_larger_numbers(self):
        assert sum_two_numbers(10, 25) == 35

    def test_with_zero(self):
        assert sum_two_numbers(0, 5) == 5
        assert sum_two_numbers(5, 0) == 5

    def test_negative_numbers(self):
        assert sum_two_numbers(-5, 3) == -2
        assert sum_two_numbers(-10, -5) == -15

    def test_floats(self):
        result = sum_two_numbers(3.5, 2.1)
        assert result == pytest.approx(5.6)

    def test_mixed_types(self):
        result = sum_two_numbers(5, 2.5)
        assert result == pytest.approx(7.5)

    def test_large_numbers(self):
        assert sum_two_numbers(1000000, 2000000) == 3000000
