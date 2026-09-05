"""Tests for Exercise 42 — Grade Classifier."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("42_grade_classifier")
    classify_grade = solution.classify_grade
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestGradeClassifier:
    def test_basic(self):
        assert classify_grade(95) == "A"
        assert classify_grade(85) == "B"
        assert classify_grade(75) == "C"
        assert classify_grade(65) == "D"
        assert classify_grade(55) == "F"

    def test_edge_case(self):
        assert classify_grade(100) == "A"
        assert classify_grade(90) == "A"
        assert classify_grade(89.9) == "B"
        assert classify_grade(0) == "F"

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            classify_grade(-1)
        with pytest.raises(ValueError):
            classify_grade(101)
