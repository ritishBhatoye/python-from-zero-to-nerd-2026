"""Tests for Exercise 80 — Integer to String Converter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("80_integer_to_string_converter")
    int_to_string = solution.int_to_string
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestIntegerToStringConverter:
    def test_single_digit(self):
        result = int_to_string(3)
        assert result == "3"
        assert isinstance(result, str)

    def test_two_digits(self):
        assert int_to_string(42) == "42"

    def test_negative(self):
        assert int_to_string(-10) == "-10"

    def test_zero(self):
        assert int_to_string(0) == "0"

    def test_large_number(self):
        assert int_to_string(123456) == "123456"

    def test_negative_single_digit(self):
        assert int_to_string(-5) == "-5"

    def test_hundred(self):
        assert int_to_string(100) == "100"
