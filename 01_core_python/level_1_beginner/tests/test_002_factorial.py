"""Tests for Exercise 002 — Factorial Calculator."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))

try:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "solution", solutions_dir / "002_factorial.py"
    )
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    factorial = solution.factorial
except (ModuleNotFoundError, FileNotFoundError, AttributeError):
    pytest.skip("Solution not implemented yet", allow_module_level=True)


class TestFactorial:
    def test_factorial_0(self):
        """Test factorial of 0."""
        assert factorial(0) == 1

    def test_factorial_1(self):
        """Test factorial of 1."""
        assert factorial(1) == 1

    def test_factorial_5(self):
        """Test factorial of 5."""
        assert factorial(5) == 120

    def test_factorial_8(self):
        """Test factorial of 8."""
        assert factorial(8) == 40320

    def test_factorial_10(self):
        """Test factorial of 10."""
        assert factorial(10) == 3628800
