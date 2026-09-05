"""Tests for Exercise 02 — Temperature Converter."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("02_temperature_converter")
    convert_temperature = solution.convert_temperature
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestConvertTemperature:
    def test_celsius_to_fahrenheit(self):
        assert convert_temperature(0, "C", "F") == 32.0

    def test_celsius_to_kelvin(self):
        assert convert_temperature(100, "C", "K") == 373.15

    def test_fahrenheit_to_celsius(self):
        assert convert_temperature(32, "F", "C") == 0.0

    def test_same_unit(self):
        assert convert_temperature(25.5, "C", "C") == 25.5

    def test_case_insensitive(self):
        assert convert_temperature(25, "c", "f") == 77.0

    def test_invalid_unit_raises(self):
        with pytest.raises(ValueError):
            convert_temperature(10, "X", "C")
