"""Tests for Exercise 86 — Class vs Instance Attributes."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("86_class_vs_instance_attributes")
    Person = solution.Person
    demonstrate_attributes = solution.demonstrate_attributes
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestClassVsInstanceAttributes:
    def test_class_attribute_exists(self):
        assert hasattr(Person, 'species')
        assert Person.species == "Human"

    def test_instance_creation_with_name(self):
        person = Person("Alice")
        assert person.name == "Alice"
        assert person.species == "Human"

    def test_instance_creation_without_name(self):
        person = Person()
        assert person.name is None
        assert person.species == "Human"

    def test_multiple_instances_share_class_attribute(self):
        person1 = Person("Alice")
        person2 = Person("Bob")
        assert person1.species == person2.species == "Human"

    def test_instances_have_different_names(self):
        person1 = Person("Alice")
        person2 = Person("Bob")
        assert person1.name != person2.name
        assert person1.name == "Alice"
        assert person2.name == "Bob"

    def test_class_attribute_via_class(self):
        assert Person.species == "Human"

    def test_demonstrate_function(self):
        result = demonstrate_attributes()
        assert isinstance(result, dict)
