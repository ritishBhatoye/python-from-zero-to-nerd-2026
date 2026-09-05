"""Tests for Exercise 81 — String to Integer Sum."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("81_string_to_integer_sum")
    sum_string_numbers = solution.sum_string_numbers
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestStringToIntegerSum:
    def test_basic_sum(self):
        result = sum_string_numbers("3", "4")
        assert result == 7
        assert isinstance(result, int)

    def test_larger_numbers(self):
        assert sum_string_numbers("10", "25") == 35

    def test_hundreds(self):
        assert sum_string_numbers("100", "200") == 300

    def test_with_zero(self):
        assert sum_string_numbers("0", "5") == 5
        assert sum_string_numbers("10", "0") == 10

    def test_negative_numbers(self):
        assert sum_string_numbers("-5", "3") == -2
        assert sum_string_numbers("-10", "-5") == -15

    def test_large_numbers(self):
        assert sum_string_numbers("1000", "2000") == 3000
