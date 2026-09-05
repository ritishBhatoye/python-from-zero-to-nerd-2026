"""Tests for Exercise 20 — Palindrome Checker."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("20_palindrome_checker")
    is_palindrome = solution.is_palindrome
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestIsPalindrome:
    def test_basic_true(self):
        assert is_palindrome("race car") is True

    def test_basic_false(self):
        assert is_palindrome("hello") is False

    def test_mixed_case(self):
        assert is_palindrome("RaceCar") is True

    def test_empty(self):
        assert is_palindrome("") is True

    def test_only_spaces(self):
        assert is_palindrome("   ") is True

    def test_single_char(self):
        assert is_palindrome("a") is True
