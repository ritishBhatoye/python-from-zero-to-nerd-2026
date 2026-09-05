"""Tests for Exercise 28 — List Statistics."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("28_list_statistics")
    list_stats = solution.list_stats
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestListStats:
    def test_basic(self):
        result = list_stats([1, 2, 3, 4, 5])
        assert result == {
            'min': 1,
            'max': 5,
            'sum': 15,
            'average': 3.0,
            'count': 5
        }

    def test_empty(self):
        with pytest.raises(ValueError):
            list_stats([])

    def test_single_element(self):
        result = list_stats([42])
        assert result == {
            'min': 42,
            'max': 42,
            'sum': 42,
            'average': 42.0,
            'count': 1
        }

    def test_floats_and_negatives(self):
        result = list_stats([-2.5, 0.0, 2.5])
        assert result == {
            'min': -2.5,
            'max': 2.5,
            'sum': 0.0,
            'average': 0.0,
            'count': 3
        }
