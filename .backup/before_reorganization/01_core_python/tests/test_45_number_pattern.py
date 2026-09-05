"""Tests for Exercise 45 — Number Pattern."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("45_number_pattern")
    number_triangle = solution.number_triangle
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestNumberPattern:
    def test_basic(self):
        assert number_triangle(3) == "1\n1 2\n1 2 3"
        assert number_triangle(5) == "1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5"

    def test_edge_case(self):
        assert number_triangle(1) == "1"
        assert number_triangle(0) == ""
        assert number_triangle(-5) == ""
