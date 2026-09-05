# Exercise 43 — Leap Year Checker
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- conditionals, logical operators, modulo operator

## Prerequisites

- Conditionals, basic math operators

---

## Objective

Determine if a given year is a leap year.

---

## Requirements

```python
def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise."""
```

---

## Examples

```python
is_leap_year(2024)  # True
is_leap_year(2023)  # False
is_leap_year(1900)  # False
is_leap_year(2000)  # True
```

---

## Constraints

- Python 3.12+ only
- A year is leap if divisible by 4 but not 100, unless also by 400.
- Raise `ValueError` for `year <= 0`.
- No external imports.

---

## Edge Cases

- Centuries not divisible by 400 (e.g., 1900).
- Centuries divisible by 400 (e.g., 2000).

---

## Test Command

```bash
pytest 01_core_python/tests/test_43_leap_year_checker.py -v
```

---

## Hints (use only if stuck)

1. Use `and` and `or` logical operators to combine conditions.
2. The modulo operator `%` helps check divisibility.

---

## Implementation

```
01_core_python/solutions/43_leap_year_checker.py
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
./scripts/commit_exercise.sh feat core 43_leap_year_checker
```
