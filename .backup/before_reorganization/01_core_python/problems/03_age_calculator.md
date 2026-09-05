# Exercise 03 — Age Calculator

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 0 — Warm-up  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- integers, subtraction, f-strings, functions

## Prerequisites

- Exercise 01

---

## Objective

Compute age from birth year — used in forms, profiles, and eligibility checks.

---

## Requirements

```python
def calculate_age(birth_year: int, current_year: int) -> dict:
```

Return:

```python
{
    "birth_year": int,
    "current_year": int,
    "age": int,           # current_year - birth_year
    "message": str,       # "<age> years old"
}
```

Raise `ValueError` if:
- `birth_year > current_year`
- `age` would be negative or over 150

---

## Examples

```python
calculate_age(2003, 2026)
# {"birth_year": 2003, "current_year": 2026, "age": 23, "message": "23 years old"}
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_03_age_calculator.py -v
```

---

## Implementation

```
01_core_python/solutions/03_age_calculator.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 03_age_calculator
```
