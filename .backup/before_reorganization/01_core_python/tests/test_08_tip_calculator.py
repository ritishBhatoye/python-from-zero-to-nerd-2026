"""Tests for Exercise 08 — Tip Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("08_tip_calculator")
    calculate_tip = solution.calculate_tip
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCalculateTip:
    def test_basic_tip(self):
        result = calculate_tip(500.0, 18.0, 2)
        assert result["tip_amount"] == 90.0
        assert result["total_with_tip"] == 590.0
        assert result["per_person"] == 295.0

    def test_single_person(self):
        result = calculate_tip(100.0, 10.0, 1)
        assert result["per_person"] == 110.0

    def test_invalid_people_raises(self):
        with pytest.raises(ValueError):
            calculate_tip(100.0, 10.0, 0)
