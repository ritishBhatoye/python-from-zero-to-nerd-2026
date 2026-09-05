"""Tests for Exercise 10 — Max of Three Numbers."""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from conftest import import_solution

try:
    solution = import_solution("10_max_of_three")
    max_of_three = solution.max_of_three
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestMaxOfThree:
    def test_basic(self):
        assert max_of_three(1, 5, 3) == 5

    def test_negatives(self):
        assert max_of_three(-1, -5, -3) == -1

    def test_all_equal(self):
        assert max_of_three(4, 4, 4) == 4

    def test_does_not_use_builtin_max(self):
        source_path = (
            Path(__file__).resolve().parent.parent
            / "solutions"
            / "10_max_of_three.py"
        )
        tree = ast.parse(source_path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                assert node.func.id != "max", "Do not use built-in max()"
