"""Tests for Exercise 35 — Invert Dictionary."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("35_invert_dictionary")
    invert_dict = solution.invert_dict
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestInvertDict:
    def test_basic(self):
        assert invert_dict({'a': 1, 'b': 2, 'c': 1}) == {1: ['a', 'c'], 2: ['b']}
        assert invert_dict({'x': 10, 'y': 20, 'z': 30}) == {10: ['x'], 20: ['y'], 30: ['z']}

    def test_edge_case(self):
        assert invert_dict({}) == {}
        assert invert_dict({'a': 1, 'b': 1, 'c': 1}) == {1: ['a', 'b', 'c']}
