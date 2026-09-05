"""Tests for Exercise 14 — Comma Separated to Collection."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("14_comma_separated_to_collection")
    parse_csv_numbers = solution.parse_csv_numbers
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestParseCsvNumbers:
    def test_basic(self):
        expected_list = ['34', '67', '55', '33', '12', '98']
        expected_tuple = ('34', '67', '55', '33', '12', '98')
        assert parse_csv_numbers("34,67,55,33,12,98") == (expected_list, expected_tuple)

    def test_whitespace(self):
        expected_list = ['1', '2', '3']
        expected_tuple = ('1', '2', '3')
        assert parse_csv_numbers(" 1 , 2,3  ") == (expected_list, expected_tuple)

    def test_empty_string(self):
        assert parse_csv_numbers("") == ([], ())

    def test_only_commas(self):
        assert parse_csv_numbers(",,") == (['', '', ''], ('', '', ''))
