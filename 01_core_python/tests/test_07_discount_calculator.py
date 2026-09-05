"""Tests for Exercise 07 — Discount Calculator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("07_discount_calculator")
    apply_discount = solution.apply_discount
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestApplyDiscount:
    def test_with_discount(self):
        result = apply_discount(1000.0, 15.0)
        assert result["original_price"] == 1000.0
        assert result["discount_amount"] == 150.0
        assert result["final_price"] == 850.0
        assert result["saved"] is True

    def test_no_discount(self):
        result = apply_discount(500.0, 0.0)
        assert result["saved"] is False
        assert result["final_price"] == 500.0

    def test_invalid_discount_raises(self):
        with pytest.raises(ValueError):
            apply_discount(100.0, 101.0)
