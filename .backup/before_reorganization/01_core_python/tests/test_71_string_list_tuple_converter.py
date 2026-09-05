"""Tests for Exercise 71 — String to List and Tuple Converter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("71_string_list_tuple_converter")
    parse_to_list_and_tuple = solution.parse_to_list_and_tuple
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestStringListTupleConverter:
    def test_basic_comma_separated_numbers(self):
        result = parse_to_list_and_tuple("34,67,55,33,12,98")
        assert result[0] == ['34', '67', '55', '33', '12', '98']
        assert result[1] == ('34', '67', '55', '33', '12', '98')
        assert isinstance(result[0], list)
        assert isinstance(result[1], tuple)

    def test_words(self):
        result = parse_to_list_and_tuple("apple,banana,cherry")
        assert result[0] == ['apple', 'banana', 'cherry']
        assert result[1] == ('apple', 'banana', 'cherry')

    def test_single_value(self):
        result = parse_to_list_and_tuple("10")
        assert result[0] == ['10']
        assert result[1] == ('10',)

    def test_empty_string(self):
        result = parse_to_list_and_tuple("")
        assert result[0] == ['']
        assert result[1] == ('',)

    def test_spaces_preserved(self):
        result = parse_to_list_and_tuple("hello world,foo bar")
        assert result[0] == ['hello world', 'foo bar']
        assert result[1] == ('hello world', 'foo bar')
