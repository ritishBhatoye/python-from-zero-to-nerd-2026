"""Tests for Exercise 05 — Number Classifier."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("05_number_classifier")
    classify_number = solution.classify_number
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestClassifyNumber:
    def test_zero(self):
        result = classify_number(0)
        assert result["sign"] == "zero"
        assert result["parity"] == "even"
        assert result["digit_count"] == 1

    def test_negative_even(self):
        result = classify_number(-42)
        assert result["sign"] == "negative"
        assert result["parity"] == "even"
        assert result["digit_count"] == 2

    def test_positive_odd(self):
        result = classify_number(7)
        assert result["sign"] == "positive"
        assert result["parity"] == "odd"
        assert result["digit_count"] == 1
