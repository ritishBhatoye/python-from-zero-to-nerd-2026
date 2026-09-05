"""Tests for Exercise 06 — Greeting Formatter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("06_greeting_formatter")
    format_greeting = solution.format_greeting
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFormatGreeting:
    def test_morning(self):
        assert format_greeting("  ritish  ", "morning") == "Good morning, Ritish!"

    def test_evening_case_insensitive(self):
        assert format_greeting("alice", "EVENING") == "Good evening, Alice!"

    def test_invalid_time_raises(self):
        with pytest.raises(ValueError):
            format_greeting("Bob", "midnight")
