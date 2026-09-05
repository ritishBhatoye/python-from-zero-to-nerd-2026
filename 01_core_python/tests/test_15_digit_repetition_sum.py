"""Tests for Exercise 15 — Digit Repetition Sum."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("15_digit_repetition_sum")
    digit_repeat_sum = solution.digit_repeat_sum
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestDigitRepeatSum:
    def test_basic(self):
        assert digit_repeat_sum(9) == 11106  # 9 + 99 + 999 + 9999

    def test_one(self):
        assert digit_repeat_sum(1) == 1234  # 1 + 11 + 111 + 1111

    def test_invalid_zero(self):
        with pytest.raises(ValueError):
            digit_repeat_sum(0)

    def test_invalid_ten(self):
        with pytest.raises(ValueError):
            digit_repeat_sum(10)

    def test_invalid_negative(self):
        with pytest.raises(ValueError):
            digit_repeat_sum(-1)
