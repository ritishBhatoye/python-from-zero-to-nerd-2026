"""Tests for Exercise 48 — Even Digit Numbers."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("48_even_digits")
    all_even_digits = solution.all_even_digits
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestEvenDigits:
    def test_basic(self):
        assert all_even_digits(20, 25) == [20, 22, 24]
        assert all_even_digits(200, 210) == [200, 202, 204, 206, 208]

    def test_empty_result(self):
        assert all_even_digits(11, 19) == []

    def test_edge_case(self):
        assert all_even_digits(25, 20) == []

    def test_negative_range(self):
        assert all_even_digits(-25, -20) == [-24, -22, -20]
