# Exercise 63 — Validate Age
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Input validation
- Exception handling
- Type conversion

## Prerequisites

- Previous exercises

---

## Objective

Write a function that validates an age value. It must convert the input to an integer and ensure it is within a valid human lifespan.

---

## Requirements

```python
def validate_age(value: object) -> int:
    """
    Convert the value to an integer.
    Raise TypeError if it cannot be converted (or if it's an inappropriate type).
    Raise ValueError if the age is not between 0 and 150 (inclusive).
    """
```

---

## Examples

```python
validate_age(25)      # 25
validate_age("30")    # 30
validate_age(-5)      # Raises ValueError
validate_age(200)     # Raises ValueError
validate_age("test")  # Raises ValueError or TypeError based on how conversion fails
validate_age([])      # Raises TypeError
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Age exactly 0.
- Age exactly 150.
- String representations of numbers.
- Types that cannot be converted to int (lists, dicts).

---

## Test Command

```bash
pytest 01_core_python/tests/test_63_validate_age.py -v
```

---

## Hints (use only if stuck)

1. Use a `try...except` block around `int(value)` to catch `ValueError` or `TypeError` during conversion. Re-raise a `TypeError` if conversion fails in a way that suggests invalid type. Actually, just letting `int()` raise its natural errors is okay, but make sure to raise `ValueError` specifically if the bounds check fails.

---

## Implementation

```
01_core_python/solutions/63_validate_age.py
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
./scripts/commit_exercise.sh feat core 63_validate_age
```
