"""Tests for Exercise 60 — Nested Comprehension."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("60_nested_comprehension")
    multiplication_grid = solution.multiplication_grid
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestMultiplicationGrid:
    def test_3_by_4(self):
        expected = [
            [0, 0, 0, 0],
            [0, 1, 2, 3],
            [0, 2, 4, 6]
        ]
        assert multiplication_grid(3, 4) == expected

    def test_1_by_1(self):
        assert multiplication_grid(1, 1) == [[0]]

    def test_0_rows(self):
        assert multiplication_grid(0, 5) == []

    def test_0_cols(self):
        assert multiplication_grid(3, 0) == [[], [], []]
