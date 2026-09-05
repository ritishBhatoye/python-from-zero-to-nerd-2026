"""Tests for Exercise 89 — Last N Elements Slice."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("89_last_n_elements_slice")
    last_five_squares = solution.last_five_squares
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestLastNElementsSlice:
    def test_default_20(self):
        result = last_five_squares()
        assert result == [256, 289, 324, 361, 400]  # 16², 17², 18², 19², 20²

    def test_ten_gives_last_five(self):
        result = last_five_squares(10)
        assert result == [36, 49, 64, 81, 100]  # 6², 7², 8², 9², 10²

    def test_less_than_five(self):
        result = last_five_squares(3)
        assert result == [1, 4, 9]

    def test_exactly_five(self):
        result = last_five_squares(5)
        assert result == [1, 4, 9, 16, 25]

    def test_returns_list(self):
        result = last_five_squares()
        assert isinstance(result, list)

    def test_length_at_most_five(self):
        result = last_five_squares(100)
        assert len(result) == 5
        assert result[-1] == 10000  # 100²
