"""Tests for Setup Exercise 02 — Hello Pytest."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("02_hello_pytest")
    greet = solution.greet
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestGreet:
    def test_basic_greet(self):
        assert greet("ritish") == "Hello, Ritish!"

    def test_strips_whitespace(self):
        assert greet("  alice  ") == "Hello, Alice!"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            greet("   ")
