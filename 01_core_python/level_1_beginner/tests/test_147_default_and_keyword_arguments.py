"""Tests for Exercise 53 — Default and Keyword Arguments."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("53_default_and_keyword_arguments")
    make_profile = solution.make_profile
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestDefaultAndKeywordArguments:
    def test_basic_profile(self):
        result = make_profile("Alice", 30)
        assert result == {"name": "Alice", "age": 30, "city": "Unknown", "hobbies": []}

    def test_keyword_arguments(self):
        result = make_profile("Bob", 25, city="New York", hobbies=["reading", "coding"])
        assert result == {"name": "Bob", "age": 25, "city": "New York", "hobbies": ["reading", "coding"]}

    def test_keyword_only_enforcement(self):
        with pytest.raises(TypeError):
            make_profile("Charlie", 40, "Chicago", ["swimming"])

    def test_mutable_default_trap(self):
        p1 = make_profile("Dave", 20)
        p1["hobbies"].append("gaming")
        
        p2 = make_profile("Eve", 22)
        assert p2["hobbies"] == []  # p2 should not inherit Dave's gaming hobby
