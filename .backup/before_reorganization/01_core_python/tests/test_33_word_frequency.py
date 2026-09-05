"""Tests for Exercise 33 — Word Frequency."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("33_word_frequency")
    word_frequency = solution.word_frequency
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestWordFrequency:
    def test_basic(self):
        assert word_frequency("Hello world! Hello python.") == {'hello': 2, 'world': 1, 'python': 1}
        assert word_frequency("Apple, banana, apple!") == {'apple': 2, 'banana': 1}

    def test_edge_case(self):
        assert word_frequency("") == {}
        assert word_frequency("!!!, ???") == {}
        assert word_frequency("  a  B   a  ") == {'a': 2, 'b': 1}
