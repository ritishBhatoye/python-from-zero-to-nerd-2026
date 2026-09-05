"""Tests for Exercise 49 — Power Function."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("49_power_function")
    power = solution.power
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestPower:
    def test_basic_positive(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 1) == 10

    def test_zero_exponent(self):
        assert power(5, 0) == 1
        assert power(-10, 0) == 1
        assert power(0, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5
        assert power(2, -2) == 0.25
        assert power(10, -3) == 0.001

    def test_float_base(self):
        assert power(1.5, 2) == 2.25
        assert power(0.5, 3) == 0.125
        assert power(2.5, -2) == 0.16
