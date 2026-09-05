"""Tests for Exercise 44 — Multiplication Table."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("44_multiplication_table")
    multiplication_table = solution.multiplication_table
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestMultiplicationTable:
    def test_basic(self):
        assert multiplication_table(5, 3) == [
            "5 x 1 = 5",
            "5 x 2 = 10",
            "5 x 3 = 15",
        ]
        assert multiplication_table(2, 2) == [
            "2 x 1 = 2",
            "2 x 2 = 4",
        ]

    def test_default_args(self):
        result = multiplication_table(5)
        assert len(result) == 10
        assert result[-1] == "5 x 10 = 50"

    def test_edge_case(self):
        assert multiplication_table(5, 0) == []
        assert multiplication_table(5, -2) == []
        assert multiplication_table(0, 2) == ["0 x 1 = 0", "0 x 2 = 0"]
        assert multiplication_table(-3, 2) == ["-3 x 1 = -3", "-3 x 2 = -6"]
