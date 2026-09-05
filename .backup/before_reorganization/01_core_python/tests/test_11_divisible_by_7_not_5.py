"""Tests for Exercise 11 — Divisible by 7 Not 5."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("11_divisible_by_7_not_5")
    find_divisible = solution.find_divisible
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFindDivisible:
    def test_basic(self):
        assert find_divisible(2000, 2020) == [2002, 2009, 2016]

    def test_no_matches(self):
        assert find_divisible(10, 13) == []

    def test_start_equals_end_match(self):
        assert find_divisible(7, 7) == [7]

    def test_start_equals_end_no_match_div_by_5(self):
        assert find_divisible(35, 35) == []

    def test_start_equals_end_no_match_not_div_by_7(self):
        assert find_divisible(8, 8) == []

    def test_negative_range(self):
        assert find_divisible(-20, -1) == [-14, -7]
