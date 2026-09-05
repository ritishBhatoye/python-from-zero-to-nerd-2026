"""Tests for Exercise 67 — CSV Reader."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("67_csv_reader")
    read_csv_data = solution.read_csv_data
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestReadCsvData:
    def test_basic(self, tmp_path):
        f = tmp_path / "data.csv"
        f.write_text("name,age\nAlice,30\nBob,25\n")
        expected = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
        assert read_csv_data(str(f)) == expected

    def test_only_headers(self, tmp_path):
        f = tmp_path / "empty.csv"
        f.write_text("name,age,city\n")
        assert read_csv_data(str(f)) == []

    def test_empty_values(self, tmp_path):
        f = tmp_path / "empty_vals.csv"
        f.write_text("a,b,c\n1,,3\n")
        assert read_csv_data(str(f)) == [{'a': '1', 'b': '', 'c': '3'}]
