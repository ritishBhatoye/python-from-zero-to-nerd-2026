"""Tests for Exercise 61 — Slice Operations."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("61_slice_operations")
    slice_operations = solution.slice_operations
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSliceOperations:
    def test_odd_length(self):
        items = [1, 2, 3, 4, 5]
        result = slice_operations(items)
        assert result['first_three'] == [1, 2, 3]
        assert result['last_three'] == [3, 4, 5]
        assert result['reversed'] == [5, 4, 3, 2, 1]
        assert result['every_other'] == [1, 3, 5]
        assert result['middle'] == [3]

    def test_even_length(self):
        items = [1, 2, 3, 4]
        result = slice_operations(items)
        assert result['first_three'] == [1, 2, 3]
        assert result['last_three'] == [2, 3, 4]
        assert result['reversed'] == [4, 3, 2, 1]
        assert result['every_other'] == [1, 3]
        assert result['middle'] == [2, 3]

    def test_empty_list(self):
        items = []
        result = slice_operations(items)
        assert result['first_three'] == []
        assert result['last_three'] == []
        assert result['reversed'] == []
        assert result['every_other'] == []
        assert result['middle'] == []

    def test_small_list(self):
        items = [1, 2]
        result = slice_operations(items)
        assert result['first_three'] == [1, 2]
        assert result['last_three'] == [1, 2]
        assert result['reversed'] == [2, 1]
        assert result['every_other'] == [1]
        assert result['middle'] == [1, 2]
