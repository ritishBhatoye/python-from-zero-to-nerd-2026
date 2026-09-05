"""Tests for Exercise 54 — Variable Arguments Sum."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("54_variable_arguments_sum")
    flexible_sum = solution.flexible_sum
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestVariableArgumentsSum:
    def test_basic_args_and_kwargs(self):
        result = flexible_sum(1, 2, 3, a=4, b=5)
        assert result == {
            "positional_sum": 6,
            "keyword_sum": 9,
            "total": 15,
            "count": 5
        }

    def test_mixed_types(self):
        result = flexible_sum(10.5, x=2.5)
        assert result == {
            "positional_sum": 10.5,
            "keyword_sum": 2.5,
            "total": 13.0,
            "count": 2
        }

    def test_only_args(self):
        result = flexible_sum(1, 1, 1)
        assert result == {
            "positional_sum": 3,
            "keyword_sum": 0,
            "total": 3,
            "count": 3
        }

    def test_only_kwargs(self):
        result = flexible_sum(y=10, z=20)
        assert result == {
            "positional_sum": 0,
            "keyword_sum": 30,
            "total": 30,
            "count": 2
        }

    def test_empty(self):
        result = flexible_sum()
        assert result == {
            "positional_sum": 0,
            "keyword_sum": 0,
            "total": 0,
            "count": 0
        }
