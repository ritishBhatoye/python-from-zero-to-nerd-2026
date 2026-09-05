"""Tests for Exercise 55 — Function Composition."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("55_function_composition")
    apply_operations = solution.apply_operations
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFunctionComposition:
    def test_basic_composition(self):
        assert apply_operations(5.0, [lambda x: x * 2, lambda x: x + 3]) == 13.0
        assert apply_operations(10.0, [lambda x: x - 2, lambda x: x ** 2]) == 64.0

    def test_single_function(self):
        assert apply_operations(3.0, [lambda x: x * 10]) == 30.0

    def test_empty_operations(self):
        assert apply_operations(42.0, []) == 42.0
        assert apply_operations(-5.5, []) == -5.5

    def test_multiple_functions(self):
        ops = [
            lambda x: x + 1,
            lambda x: x * 2,
            lambda x: x - 3,
            lambda x: x / 2
        ]
        # (5 + 1) = 6
        # 6 * 2 = 12
        # 12 - 3 = 9
        # 9 / 2 = 4.5
        assert apply_operations(5.0, ops) == 4.5
