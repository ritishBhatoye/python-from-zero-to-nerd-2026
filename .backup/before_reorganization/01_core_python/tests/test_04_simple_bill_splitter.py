"""Tests for Exercise 04 — Simple Bill Splitter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("04_simple_bill_splitter")
    split_bill = solution.split_bill
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSplitBill:
    def test_with_tip(self):
        result = split_bill(1000.0, 4, 10.0)
        assert result["total"] == 1000.0
        assert result["tip_amount"] == 100.0
        assert result["grand_total"] == 1100.0
        assert result["per_person"] == 275.0
        assert result["num_people"] == 4

    def test_no_tip(self):
        result = split_bill(200.0, 2, 0.0)
        assert result["tip_amount"] == 0.0
        assert result["grand_total"] == 200.0
        assert result["per_person"] == 100.0

    def test_invalid_people_raises(self):
        with pytest.raises(ValueError):
            split_bill(100.0, 0, 10.0)
