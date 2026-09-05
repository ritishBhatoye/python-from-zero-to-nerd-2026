"""Tests for Exercise 36 — Common Elements."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("36_common_elements")
    common_elements = solution.common_elements
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCommonElements:
    def test_basic(self):
        assert common_elements([1, 2, 3, 2], [2, 3, 4]) == [2, 3]
        assert common_elements(["a", "b", "c"], ["c", "d", "e"]) == ["c"]

    def test_edge_case(self):
        assert common_elements([], [1, 2]) == []
        assert common_elements([1, 2], []) == []
        assert common_elements([1, 2], [3, 4]) == []
        assert common_elements([1, 1, 1], [1, 1]) == [1]
