"""Tests for Exercise 12 — Factorial Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("12_factorial_calculator")
    factorial = solution.factorial
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFactorial:
    def test_basic(self):
        assert factorial(8) == 40320

    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_larger(self):
        assert factorial(10) == 3628800
