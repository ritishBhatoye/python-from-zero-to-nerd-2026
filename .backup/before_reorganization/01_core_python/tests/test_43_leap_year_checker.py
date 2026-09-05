"""Tests for Exercise 43 — Leap Year Checker."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("43_leap_year_checker")
    is_leap_year = solution.is_leap_year
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestLeapYearChecker:
    def test_basic(self):
        assert is_leap_year(2024) is True
        assert is_leap_year(2023) is False

    def test_centuries(self):
        assert is_leap_year(1900) is False
        assert is_leap_year(2100) is False
        assert is_leap_year(2000) is True
        assert is_leap_year(2400) is True

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            is_leap_year(0)
        with pytest.raises(ValueError):
            is_leap_year(-2020)
