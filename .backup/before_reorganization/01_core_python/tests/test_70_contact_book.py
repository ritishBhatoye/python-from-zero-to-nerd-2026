"""Tests for Exercise 70 — Phase 1 Capstone: Contact Book."""

from __future__ import annotations

import pytest

from conftest import import_solution

try:
    solution = import_solution("70_contact_book")
    create_contact = solution.create_contact
    add_contact = solution.add_contact
    find_contact = solution.find_contact
    delete_contact = solution.delete_contact
    export_contacts = solution.export_contacts
    import_contacts = solution.import_contacts
except ModuleNotFoundError as exc:
    pytest.skip(str(exc), allow_module_level=True)


class TestContactBook:
    def test_create_and_add(self):
        c1 = create_contact("Alice", "123", "a@a.com")
        assert c1 == {"name": "Alice", "phone": "123", "email": "a@a.com"}
        
        contacts = []
        contacts = add_contact(contacts, c1)
        assert len(contacts) == 1

        with pytest.raises(ValueError):
            add_contact(contacts, create_contact("Alice", "999"))

    def test_find_contact(self):
        contacts = [create_contact("Bob", "456")]
        assert find_contact(contacts, "bob") == {"name": "Bob", "phone": "456", "email": ""}
        assert find_contact(contacts, "Charlie") is None

    def test_delete_contact(self):
        contacts = [create_contact("Alice", "123")]
        contacts = delete_contact(contacts, "Alice")
        assert len(contacts) == 0

        with pytest.raises(ValueError):
            delete_contact(contacts, "Nonexistent")

    def test_import_export(self, tmp_path):
        f = tmp_path / "contacts.csv"
        contacts = [
            create_contact("Alice", "123", "a@a.com"),
            create_contact("Bob", "456", "")
        ]
        
        assert export_contacts(contacts, str(f)) == 2
        
        content = f.read_text()
        assert "name,phone,email" in content.lower()
        
        imported = import_contacts(str(f))
        assert imported == contacts
