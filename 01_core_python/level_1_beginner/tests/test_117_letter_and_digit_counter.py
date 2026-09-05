"""Tests for Exercise 17 — Letter and Digit Counter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("17_letter_and_digit_counter")
    count_letters_digits = solution.count_letters_digits
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCountLettersDigits:
    def test_basic(self):
        assert count_letters_digits("hello world! 123") == {"letters": 10, "digits": 3}

    def test_empty(self):
        assert count_letters_digits("") == {"letters": 0, "digits": 0}

    def test_only_letters(self):
        assert count_letters_digits("hello") == {"letters": 5, "digits": 0}

    def test_only_digits(self):
        assert count_letters_digits("12345") == {"letters": 0, "digits": 5}

    def test_only_punctuation(self):
        assert count_letters_digits("!@#$ %^&*") == {"letters": 0, "digits": 0}
