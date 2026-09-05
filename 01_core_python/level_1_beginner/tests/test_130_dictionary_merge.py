"""Tests for Exercise 34 — Dictionary Merge."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("34_dictionary_merge")
    merge_dicts = solution.merge_dicts
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestMergeDicts:
    def test_basic(self):
        assert merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 3, 'c': 4}
        assert merge_dicts({'x': 10}, {'y': 20}) == {'x': 10, 'y': 20}

    def test_edge_case(self):
        assert merge_dicts({}, {}) == {}
        assert merge_dicts({'a': 1}, {}) == {'a': 1}
        assert merge_dicts({}, {'a': 1}) == {'a': 1}
        
    def test_no_mutation(self):
        d1 = {'a': 1}
        d2 = {'b': 2}
        result = merge_dicts(d1, d2)
        assert d1 == {'a': 1}
        assert d2 == {'b': 2}
        assert result is not d1
        assert result is not d2
