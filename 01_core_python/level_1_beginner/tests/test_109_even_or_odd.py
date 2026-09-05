"""Tests for Exercise 09 — Even or Odd."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("09_even_or_odd")
    is_even = solution.is_even
    describe_parity = solution.describe_parity
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestEvenOrOdd:
    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(7) is False
        assert is_even(0) is True

    def test_describe_parity(self):
        assert describe_parity(0) == "even"
        assert describe_parity(3) == "odd"
