"""Tests for Exercise 78 — Square Value Function."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("78_square_value_function")
    square = solution.square
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSquareValueFunction:
    def test_square_2(self):
        assert square(2) == 4

    def test_square_3(self):
        assert square(3) == 9

    def test_square_5(self):
        assert square(5) == 25

    def test_square_0(self):
        assert square(0) == 0

    def test_square_negative(self):
        assert square(-3) == 9
        assert square(-5) == 25

    def test_square_float(self):
        result = square(5.5)
        assert result == pytest.approx(30.25)

    def test_square_1(self):
        assert square(1) == 1

    def test_square_10(self):
        assert square(10) == 100
