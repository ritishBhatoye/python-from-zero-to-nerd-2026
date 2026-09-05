"""Tests for Exercise 75 — Digit Pattern Sum."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("75_digit_pattern_sum")
    digit_pattern_sum = solution.digit_pattern_sum
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestDigitPatternSum:
    def test_digit_9(self):
        result = digit_pattern_sum(9)
        # 9 + 99 + 999 + 9999 = 11106
        assert result == 11106

    def test_digit_5(self):
        result = digit_pattern_sum(5)
        # 5 + 55 + 555 + 5555 = 6170
        assert result == 6170

    def test_digit_1(self):
        result = digit_pattern_sum(1)
        # 1 + 11 + 111 + 1111 = 1234
        assert result == 1234

    def test_digit_0(self):
        result = digit_pattern_sum(0)
        # 0 + 00 + 000 + 0000 = 0
        assert result == 0

    def test_digit_3(self):
        result = digit_pattern_sum(3)
        # 3 + 33 + 333 + 3333 = 3702
        assert result == 3702

    def test_digit_7(self):
        result = digit_pattern_sum(7)
        # 7 + 77 + 777 + 7777 = 8638
        assert result == 8638
