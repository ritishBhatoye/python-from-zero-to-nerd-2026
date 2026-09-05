"""Tests for Exercise 03 — Age Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("03_age_calculator")
    calculate_age = solution.calculate_age
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCalculateAge:
    def test_valid_age(self):
        result = calculate_age(2003, 2026)
        assert result["birth_year"] == 2003
        assert result["current_year"] == 2026
        assert result["age"] == 23
        assert result["message"] == "23 years old"

    def test_birth_year_after_current_raises(self):
        with pytest.raises(ValueError):
            calculate_age(2030, 2026)

    def test_unreasonable_age_raises(self):
        with pytest.raises(ValueError):
            calculate_age(1800, 2026)
