"""Tests for Exercise 37 — Group By Length."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("37_group_by_length")
    group_by_length = solution.group_by_length
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestGroupByLength:
    def test_basic(self):
        assert group_by_length(['hi', 'hey', 'oh']) == {2: ['hi', 'oh'], 3: ['hey']}
        assert group_by_length(["a", "bb", "ccc", "dd"]) == {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}

    def test_edge_case(self):
        assert group_by_length([]) == {}
        assert group_by_length(["abc", "def", "ghi"]) == {3: ["abc", "def", "ghi"]}
        assert group_by_length([""]) == {0: [""]}
