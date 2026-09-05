"""Tests for Exercise 47 — Binary Numbers in Range."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("47_binary_numbers")
    filter_divisible_binary = solution.filter_divisible_binary
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestBinaryNumbers:
    def test_basic(self):
        binaries = ["0100", "0011", "1010", "1001"]
        assert filter_divisible_binary(binaries, 5) == ["1010"]
        assert filter_divisible_binary(binaries, 2) == ["0100", "1010"]

    def test_edge_case(self):
        assert filter_divisible_binary([], 5) == []
        assert filter_divisible_binary(["1111"], 2) == []

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            filter_divisible_binary(["1010"], 0)
