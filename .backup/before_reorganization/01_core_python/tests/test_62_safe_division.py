"""Tests for Exercise 62 — Safe Division."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("62_safe_division")
    safe_divide = solution.safe_divide
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestSafeDivide:
    def test_valid_division(self):
        assert safe_divide(10.0, 2.0) == 5.0
        assert safe_divide(10, 5) == 2.0
        assert safe_divide(-10, 2) == -5.0

    def test_zero_numerator(self):
        assert safe_divide(0, 5.0) == 0.0

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError) as exc_info:
            safe_divide(10.0, 0.0)
        assert str(exc_info.value) == "Cannot divide by zero"

    def test_type_error(self):
        with pytest.raises(TypeError):
            safe_divide(10.0, "2")
        with pytest.raises(TypeError):
            safe_divide("10", 2.0)
        with pytest.raises(TypeError):
            safe_divide(None, 5)
