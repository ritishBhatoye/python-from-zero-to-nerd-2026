# Exercise 70 — Phase 1 Capstone: Contact Book
**Phase:** `01_core_python`  
**Type:** capstone
**Difficulty:** Level 2 — Intermediate
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Dictionaries, Lists, CRUD operations, File I/O (CSV), Modules

## Prerequisites

- All Phase 1 exercises

---

## Objective

Build a simple contact book application to tie together all the basics of Python.

---

## Requirements

Implement the following functions in your module:

```python
def create_contact(name: str, phone: str, email: str = '') -> dict[str, str]:
    """Creates and returns a contact dictionary."""

def add_contact(contacts: list[dict[str, str]], contact: dict[str, str]) -> list[dict[str, str]]:
    """Adds a contact. Raises ValueError if a contact with the same name already exists."""

def find_contact(contacts: list[dict[str, str]], name: str) -> dict[str, str] | None:
    """Searches for a contact by name (case-insensitive). Returns None if not found."""

def delete_contact(contacts: list[dict[str, str]], name: str) -> list[dict[str, str]]:
    """Deletes a contact by name. Raises ValueError if not found."""

def export_contacts(contacts: list[dict[str, str]], filepath: str) -> int:
    """Writes contacts to a CSV file (name,phone,email). Returns the number of contacts exported."""

def import_contacts(filepath: str) -> list[dict[str, str]]:
    """Reads contacts from a CSV file and returns a list of contact dictionaries."""
```

---

## Examples

```python
contacts = []
c1 = create_contact("Alice", "123-456")
contacts = add_contact(contacts, c1)

find_contact(contacts, "alice") # {'name': 'Alice', 'phone': '123-456', 'email': ''}

export_contacts(contacts, 'contacts.csv') # Returns 1
```

---

## Constraints

- Python 3.12+ only
- For CSV import/export, do not use the `csv` module—parse and write manually.

---

## Edge Cases

- Duplicate names in `add_contact`
- Deleting non-existent names
- Case-insensitivity in search

---

## Test Command

```bash
pytest 01_core_python/tests/test_70_contact_book.py -v
```

---

## Hints (use only if stuck)

1. Use `.lower()` for case-insensitive comparisons.
2. A CSV line can be constructed by joining dictionary values with commas.

---

## Implementation

```
01_core_python/solutions/70_contact_book.py
```

Create this file yourself — it does not exist until you implement it.

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes:**
- **Python concepts:**
- **Possible improvements:**

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 70_contact_book
```
