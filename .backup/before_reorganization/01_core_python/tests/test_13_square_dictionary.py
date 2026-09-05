"""Tests for Exercise 13 — Square Dictionary."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("13_square_dictionary")
    square_dict = solution.square_dict
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSquareDict:
    def test_basic(self):
        assert square_dict(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

    def test_one(self):
        assert square_dict(1) == {1: 1}

    def test_invalid_zero(self):
        with pytest.raises(ValueError):
            square_dict(0)

    def test_invalid_negative(self):
        with pytest.raises(ValueError):
            square_dict(-5)
