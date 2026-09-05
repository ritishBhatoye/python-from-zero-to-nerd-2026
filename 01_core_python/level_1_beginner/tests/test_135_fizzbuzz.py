"""Tests for Exercise 41 — FizzBuzz."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("41_fizzbuzz")
    fizzbuzz = solution.fizzbuzz
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFizzBuzz:
    def test_basic(self):
        assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_fizzbuzz(self):
        assert fizzbuzz(15)[14] == "FizzBuzz"

    def test_edge_case(self):
        assert fizzbuzz(1) == ["1"]

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            fizzbuzz(0)
        with pytest.raises(ValueError):
            fizzbuzz(-5)
