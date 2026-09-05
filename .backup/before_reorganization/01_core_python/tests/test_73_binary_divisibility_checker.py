"""Tests for Exercise 73 — Binary Divisibility Checker."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("73_binary_divisibility_checker")
    filter_binary_divisible_by_5 = solution.filter_binary_divisible_by_5
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestBinaryDivisibilityChecker:
    def test_basic_example(self):
        result = filter_binary_divisible_by_5(["0100", "0011", "1010", "1001"])
        assert result == ["1010"]  # 1010 = 10 in decimal

    def test_multiple_matches(self):
        result = filter_binary_divisible_by_5(["1111", "0101", "1100", "1010"])
        assert set(result) == {"0101", "1010"}  # 5 and 10

    def test_no_matches(self):
        result = filter_binary_divisible_by_5(["0001", "0010", "0011"])
        assert result == []

    def test_empty_list(self):
        result = filter_binary_divisible_by_5([])
        assert result == []

    def test_all_divisible(self):
        result = filter_binary_divisible_by_5(["0000", "0101", "1010"])
        assert len(result) == 3  # 0, 5, 10 all divisible by 5

    def test_returns_strings(self):
        result = filter_binary_divisible_by_5(["1010"])
        assert result == ["1010"]
        assert isinstance(result[0], str)
