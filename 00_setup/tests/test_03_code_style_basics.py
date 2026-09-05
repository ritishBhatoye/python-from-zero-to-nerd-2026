"""Tests for Setup Exercise 03 — Code Style Basics."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("03_code_style_basics")
    format_full_name = solution.format_full_name
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFormatFullName:
    def test_basic(self):
        assert format_full_name("ritish", "bhatoye") == "Bhatoye, Ritish"

    def test_strips_and_title_cases(self):
        assert format_full_name("  JOHN  ", "  doe  ") == "Doe, John"

    def test_empty_first_raises(self):
        with pytest.raises(ValueError):
            format_full_name("", "Doe")
