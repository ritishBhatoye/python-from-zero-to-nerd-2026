"""Tests for Exercise 72 — Two-Dimensional Array Generator."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("72_two_dimensional_array_generator")
    generate_2d_array = solution.generate_2d_array
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestTwoDimensionalArrayGenerator:
    def test_3x5_array(self):
        result = generate_2d_array(3, 5)
        expected = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
        assert result == expected

    def test_2x3_array(self):
        result = generate_2d_array(2, 3)
        expected = [[0, 0, 0], [0, 1, 2]]
        assert result == expected

    def test_1x1_array(self):
        result = generate_2d_array(1, 1)
        assert result == [[0]]

    def test_zero_rows(self):
        result = generate_2d_array(0, 5)
        assert result == []

    def test_zero_cols(self):
        result = generate_2d_array(5, 0)
        assert result == [[], [], [], [], []]

    def test_4x4_square(self):
        result = generate_2d_array(4, 4)
        assert result[0] == [0, 0, 0, 0]
        assert result[1] == [0, 1, 2, 3]
        assert result[2] == [0, 2, 4, 6]
        assert result[3] == [0, 3, 6, 9]
