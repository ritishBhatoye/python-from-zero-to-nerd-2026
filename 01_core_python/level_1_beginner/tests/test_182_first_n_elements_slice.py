"""Tests for Exercise 88 — First N Elements Slice."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("88_first_n_elements_slice")
    first_five_squares = solution.first_five_squares
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFirstNElementsSlice:
    def test_default_20(self):
        result = first_five_squares()
        assert result == [1, 4, 9, 16, 25]

    def test_ten_gives_first_five(self):
        result = first_five_squares(10)
        assert result == [1, 4, 9, 16, 25]

    def test_less_than_five(self):
        result = first_five_squares(3)
        assert result == [1, 4, 9]

    def test_exactly_five(self):
        result = first_five_squares(5)
        assert result == [1, 4, 9, 16, 25]

    def test_returns_list(self):
        result = first_five_squares()
        assert isinstance(result, list)

    def test_length_at_most_five(self):
        result = first_five_squares(100)
        assert len(result) == 5
