"""Tests for Exercise 63 — Validate Age."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("63_validate_age")
    validate_age = solution.validate_age
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestValidateAge:
    def test_valid_integer(self):
        assert validate_age(25) == 25
        assert validate_age(0) == 0
        assert validate_age(150) == 150

    def test_valid_string(self):
        assert validate_age("30") == 30

    def test_out_of_bounds_negative(self):
        with pytest.raises(ValueError):
            validate_age(-1)

    def test_out_of_bounds_large(self):
        with pytest.raises(ValueError):
            validate_age(151)

    def test_invalid_string(self):
        with pytest.raises(ValueError):
            validate_age("not a number")

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            validate_age([25])
        with pytest.raises(TypeError):
            validate_age({"age": 25})
