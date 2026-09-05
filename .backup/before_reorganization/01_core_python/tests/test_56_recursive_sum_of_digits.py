"""Tests for Exercise 56 — Recursive Sum of Digits."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("56_recursive_sum_of_digits")
    digit_sum = solution.digit_sum
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestRecursiveSumOfDigits:
    def test_basic_sum(self):
        assert digit_sum(12345) == 15
        assert digit_sum(99) == 18
        assert digit_sum(101) == 2

    def test_single_digit(self):
        assert digit_sum(0) == 0
        assert digit_sum(5) == 5
        assert digit_sum(9) == 9

    def test_negative_numbers(self):
        assert digit_sum(-123) == 6
        assert digit_sum(-99) == 18
        assert digit_sum(-5) == 5
