# Exercise 80 — Integer to String Converter

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q27-28  
**Status:** 🔴 Not started

## Concepts

- type conversion, str() function, functions

## Prerequisites

- Basic function knowledge

---

## Objective

Convert an integer to a string representation.

---

## Requirements

```python
def int_to_string(n: int) -> str:
    """
    Convert an integer to its string representation.
    
    Args:
        n: Integer to convert
    
    Returns:
        String representation of the integer
    """
```

---

## Examples

```python
int_to_string(3)
# "3"

int_to_string(42)
# "42"

int_to_string(-10)
# "-10"
```

---

## Constraints

- Use `str()` built-in function
- Handle negative numbers
- Handle zero

---

## Edge Cases

- Zero: int_to_string(0) returns "0"
- Negative: int_to_string(-5) returns "-5"
- Large numbers work correctly

---

## Test Command

```bash
pytest 01_core_python/tests/test_80_integer_to_string_converter.py -v
```

---

## Hints (use only if stuck)

1. Use the `str()` function
2. Return `str(n)`
3. One-liner solution

---

## Implementation

```
01_core_python/solutions/80_integer_to_string_converter.py
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
./scripts/commit_exercise.sh feat core 80_integer_to_string_converter
```
