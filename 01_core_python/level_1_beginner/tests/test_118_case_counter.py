"""Tests for Exercise 18 — Case Counter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("18_case_counter")
    count_case = solution.count_case
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCountCase:
    def test_basic(self):
        assert count_case("Hello world!") == {"upper": 1, "lower": 9}

    def test_empty(self):
        assert count_case("") == {"upper": 0, "lower": 0}

    def test_all_upper(self):
        assert count_case("HELLO") == {"upper": 5, "lower": 0}

    def test_all_lower(self):
        assert count_case("hello") == {"upper": 0, "lower": 5}

    def test_no_letters(self):
        assert count_case("12345 !@#") == {"upper": 0, "lower": 0}
