"""Tests for Exercise 01 — Personal Expense Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

mod = pytest.importorskip("importlib")  # noqa: F401 — ensure pytest available

try:
    solution = import_solution("01_personal_expense_calculator")
    calculate_expenses = solution.calculate_expenses
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCalculateExpenses:
    def test_basic_expenses(self):
        result = calculate_expenses("Ritish", 15000, 8000, 2500)
        assert result["name"] == "Ritish"
        assert result["rent"] == 15000
        assert result["food"] == 8000
        assert result["transport"] == 2500
        assert result["total"] == 25500.0
        assert result["average"] == 8500.0
        assert result["highest_category"] == "rent"
        assert result["summary"] == "Ritish spent a total of 25500.0 across 3 categories."

    def test_food_is_highest(self):
        result = calculate_expenses("Alice", 100, 500, 200)
        assert result["highest_category"] == "food"
        assert result["total"] == 800.0

    def test_zero_values(self):
        result = calculate_expenses("Bob", 0, 0, 0)
        assert result["total"] == 0.0
        assert result["average"] == 0.0

    def test_rounding(self):
        result = calculate_expenses("Test", 10.555, 20.444, 30.001)
        assert result["total"] == round(10.555 + 20.444 + 30.001, 2)
        assert result["average"] == round(result["total"] / 3, 2)
