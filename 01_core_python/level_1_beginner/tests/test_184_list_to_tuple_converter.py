"""Tests for Exercise 90 — List to Tuple Converter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("90_list_to_tuple_converter")
    squares_as_tuple = solution.squares_as_tuple
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestListToTupleConverter:
    def test_default_20(self):
        result = squares_as_tuple()
        assert isinstance(result, tuple)
        assert len(result) == 20
        assert result[0] == 1
        assert result[-1] == 400

    def test_five_squares(self):
        result = squares_as_tuple(5)
        assert result == (1, 4, 9, 16, 25)
        assert isinstance(result, tuple)

    def test_three_squares(self):
        result = squares_as_tuple(3)
        assert result == (1, 4, 9)

    def test_one_square(self):
        result = squares_as_tuple(1)
        assert result == (1,)
        assert isinstance(result, tuple)

    def test_returns_tuple_not_list(self):
        result = squares_as_tuple(5)
        assert isinstance(result, tuple)
        assert not isinstance(result, list)

    def test_immutable(self):
        result = squares_as_tuple(3)
        with pytest.raises(TypeError):
            result[0] = 100  # Tuples are immutable
