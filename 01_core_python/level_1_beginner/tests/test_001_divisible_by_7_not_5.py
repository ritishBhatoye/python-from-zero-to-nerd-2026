"""Tests for Exercise 001 — Divisible by 7 but not 5."""

from __future__ import annotations

import pytest
import sys
from pathlib import Path

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))

try:
    from solution_001_divisible_by_7_not_5 import find_divisible
except ModuleNotFoundError:
    pytest.skip("Solution not implemented yet", allow_module_level=True)


class TestDivisibleBy7Not5:
    def test_function_exists(self):
        """Test that the function exists."""
        assert callable(find_divisible)
    
    def test_result_type(self):
        """Test that result is a string."""
        result = find_divisible()
        assert isinstance(result, str)
    
    def test_first_number(self):
        """Test that 2002 is the first number."""
        result = find_divisible()
        numbers = [int(n) for n in result.split(',')]
        assert numbers[0] == 2002
    
    def test_last_number(self):
        """Test that 3199 is the last number."""
        result = find_divisible()
        numbers = [int(n) for n in result.split(',')]
        assert numbers[-1] == 3199
    
    def test_all_divisible_by_7(self):
        """Test that all numbers are divisible by 7."""
        result = find_divisible()
        numbers = [int(n) for n in result.split(',')]
        for num in numbers:
            assert num % 7 == 0, f"{num} is not divisible by 7"
    
    def test_none_divisible_by_5(self):
        """Test that no numbers are divisible by 5."""
        result = find_divisible()
        numbers = [int(n) for n in result.split(',')]
        for num in numbers:
            assert num % 5 != 0, f"{num} is divisible by 5"
    
    def test_count(self):
        """Test that we have the correct count of numbers."""
        result = find_divisible()
        numbers = result.split(',')
        # There should be exactly 172 numbers
        assert len(numbers) == 172
