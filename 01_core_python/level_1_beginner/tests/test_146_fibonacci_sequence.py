"""Tests for Exercise 52 — Fibonacci Sequence."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("52_fibonacci_sequence")
    fibonacci = solution.fibonacci
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFibonacciSequence:
    def test_basic_sequence(self):
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_small_n(self):
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]

    def test_invalid_n(self):
        with pytest.raises(ValueError):
            fibonacci(0)
        with pytest.raises(ValueError):
            fibonacci(-1)
        with pytest.raises(ValueError):
            fibonacci(-5)
