"""Tests for Exercise 29 — Flatten Nested List."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("29_flatten_list")
    flatten = solution.flatten
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestFlatten:
    def test_basic(self):
        assert flatten([[1, 2], [3, [4]]]) == [1, 2, 3, [4]]

    def test_mixed(self):
        assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]

    def test_empty(self):
        assert flatten([]) == []
        assert flatten([[], []]) == []

    def test_no_nesting(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_deep_nesting(self):
        assert flatten([[[1]], [2]]) == [[1], 2]
