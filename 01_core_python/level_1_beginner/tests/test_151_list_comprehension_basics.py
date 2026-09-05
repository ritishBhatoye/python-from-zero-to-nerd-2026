"""Tests for Exercise 57 — List Comprehension Basics."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("57_list_comprehension_basics")
    squares_of_evens = solution.squares_of_evens
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSquaresOfEvens:
    def test_mixed_numbers(self):
        assert squares_of_evens([1, 2, 3, 4, 5, 6]) == [4, 16, 36]

    def test_only_odds(self):
        assert squares_of_evens([1, 3, 5, 7]) == []

    def test_only_evens(self):
        assert squares_of_evens([2, 4, 6]) == [4, 16, 36]

    def test_empty_list(self):
        assert squares_of_evens([]) == []

    def test_negative_evens(self):
        assert squares_of_evens([-2, -4, -5]) == [4, 16]
