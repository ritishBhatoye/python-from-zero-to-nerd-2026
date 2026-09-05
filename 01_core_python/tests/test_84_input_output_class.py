"""Tests for Exercise 84 — Input Output Class."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("84_input_output_class")
    InputOutputString = solution.InputOutputString
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestInputOutputClass:
    def test_basic_usage(self):
        obj = InputOutputString()
        obj.get_string("Hello World")
        result = obj.print_string()
        assert result == "HELLO WORLD"

    def test_lowercase_input(self):
        obj = InputOutputString()
        obj.get_string("python")
        result = obj.print_string()
        assert result == "PYTHON"

    def test_empty_string(self):
        obj = InputOutputString()
        obj.get_string("")
        result = obj.print_string()
        assert result == ""

    def test_already_uppercase(self):
        obj = InputOutputString()
        obj.get_string("ALREADY UPPERCASE")
        result = obj.print_string()
        assert result == "ALREADY UPPERCASE"

    def test_mixed_case(self):
        obj = InputOutputString()
        obj.get_string("MiXeD CaSe")
        result = obj.print_string()
        assert result == "MIXED CASE"

    def test_multiple_instances(self):
        obj1 = InputOutputString()
        obj2 = InputOutputString()
        obj1.get_string("first")
        obj2.get_string("second")
        assert obj1.print_string() == "FIRST"
        assert obj2.print_string() == "SECOND"
