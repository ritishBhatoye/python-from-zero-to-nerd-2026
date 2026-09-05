"""Tests for Exercise 46 — Collatz Sequence."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("46_collatz_sequence")
    collatz = solution.collatz
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestCollatzSequence:
    def test_basic(self):
        assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
        assert collatz(3) == [3, 10, 5, 16, 8, 4, 2, 1]

    def test_edge_case(self):
        assert collatz(1) == [1]

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            collatz(0)
        with pytest.raises(ValueError):
            collatz(-5)
