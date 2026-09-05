# Exercise 62 — Safe Division
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Exceptions
- Error handling
- `raise` statement

## Prerequisites

- Previous exercises

---

## Objective

Create a function that divides two numbers but raises specific exceptions for invalid inputs.

---

## Requirements

```python
def safe_divide(a: float, b: float) -> float:
    """
    Divide a by b.
    Raises TypeError if either argument is not a number.
    Raises ZeroDivisionError with message 'Cannot divide by zero' if b is 0.
    """
```

---

## Examples

```python
safe_divide(10.0, 2.0)  # 5.0
safe_divide(10.0, 0.0)  # Raises ZeroDivisionError('Cannot divide by zero')
safe_divide(10.0, "2")  # Raises TypeError
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Negative numbers.
- Zero as the numerator.
- Non-numeric inputs like strings, lists, or None.

---

## Test Command

```bash
pytest 01_core_python/tests/test_62_safe_division.py -v
```

---

## Hints (use only if stuck)

1. Check if `isinstance(a, (int, float))` and `isinstance(b, (int, float))`.
2. Raise exceptions using `raise ExceptionType("message")`.

---

## Implementation

```
01_core_python/solutions/62_safe_division.py
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
./scripts/commit_exercise.sh feat core 62_safe_division
```
