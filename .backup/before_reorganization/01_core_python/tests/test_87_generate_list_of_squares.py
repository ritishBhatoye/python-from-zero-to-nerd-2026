"""Tests for Exercise 87 — Generate List of Squares."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("87_generate_list_of_squares")
    generate_squares_list = solution.generate_squares_list
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestGenerateListOfSquares:
    def test_default_20(self):
        result = generate_squares_list()
        assert len(result) == 20
        assert result[0] == 1
        assert result[-1] == 400

    def test_five_squares(self):
        result = generate_squares_list(5)
        assert result == [1, 4, 9, 16, 25]

    def test_three_squares(self):
        result = generate_squares_list(3)
        assert result == [1, 4, 9]

    def test_one_square(self):
        result = generate_squares_list(1)
        assert result == [1]

    def test_returns_list(self):
        result = generate_squares_list(5)
        assert isinstance(result, list)

    def test_all_values_correct(self):
        result = generate_squares_list(10)
        expected = [i**2 for i in range(1, 11)]
        assert result == expected
