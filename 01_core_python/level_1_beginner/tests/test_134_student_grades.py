"""Tests for Exercise 38 — Student Grades."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("38_student_grades")
    average_grades = solution.average_grades
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestAverageGrades:
    def test_basic(self):
        assert average_grades({'Alice': [90.5, 80.0], 'Bob': [70.0, 75.0, 80.0]}) == {'Alice': 85.25, 'Bob': 75.0}
        assert average_grades({'Charlie': [100.0, 100.0, 100.0]}) == {'Charlie': 100.0}

    def test_edge_case(self):
        assert average_grades({}) == {}
        assert average_grades({'Dave': [85.123]}) == {'Dave': 85.12}
        assert average_grades({'Eve': [0.0, 0.0]}) == {'Eve': 0.0}
