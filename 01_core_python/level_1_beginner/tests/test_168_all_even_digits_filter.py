"""Tests for Exercise 74 — All Even Digits Filter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("74_all_even_digits_filter")
    filter_all_even_digits = solution.filter_all_even_digits
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestAllEvenDigitsFilter:
    def test_20_to_30(self):
        result = filter_all_even_digits(20, 30)
        assert result == [20, 22, 24, 26, 28]

    def test_100_to_105(self):
        result = filter_all_even_digits(100, 105)
        assert result == []  # No numbers have all even digits

    def test_200_to_210(self):
        result = filter_all_even_digits(200, 210)
        expected = [200, 202, 204, 206, 208]
        assert result == expected

    def test_single_digit_range(self):
        result = filter_all_even_digits(0, 9)
        assert result == [0, 2, 4, 6, 8]

    def test_no_matches(self):
        result = filter_all_even_digits(11, 19)
        assert result == []

    def test_sample_from_1000_3000(self):
        result = filter_all_even_digits(1000, 3000)
        assert 2000 in result
        assert 2002 in result
        assert 2222 in result
        assert 2468 in result
        assert 1000 not in result  # Has 1
        assert 2001 not in result  # Has 1
