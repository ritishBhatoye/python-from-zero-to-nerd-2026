"""Tests for Exercise 50 — GCD Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("50_gcd_calculator")
    gcd = solution.gcd
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestGcdCalculator:
    def test_basic_gcd(self):
        assert gcd(48, 18) == 6
        assert gcd(54, 24) == 6
        assert gcd(101, 103) == 1

    def test_negative_numbers(self):
        assert gcd(-48, 18) == 6
        assert gcd(48, -18) == 6
        assert gcd(-48, -18) == 6

    def test_zero_values(self):
        assert gcd(5, 0) == 5
        assert gcd(0, -5) == 5

    def test_both_zero(self):
        with pytest.raises(ValueError):
            gcd(0, 0)
