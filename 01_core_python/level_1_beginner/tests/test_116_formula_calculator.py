"""Tests for Exercise 16 — Formula Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("16_formula_calculator")
    formula_q = solution.formula_q
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFormulaQ:
    def test_basic(self):
        assert formula_q([100, 150, 180]) == [18, 22, 24]

    def test_empty(self):
        assert formula_q([]) == []

    def test_zero(self):
        assert formula_q([0]) == [0]

    def test_negative(self):
        with pytest.raises(ValueError):
            # math.sqrt will naturally raise ValueError for negative numbers
            formula_q([-10])
