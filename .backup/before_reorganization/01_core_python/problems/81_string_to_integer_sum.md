# Exercise 81 — String to Integer Sum

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q29  
**Status:** 🔴 Not started

## Concepts

- type conversion, int() function, string parsing

## Prerequisites

- Basic function knowledge

---

## Objective

Accept two numbers as strings, convert them to integers, and return their sum.

---

## Requirements

```python
def sum_string_numbers(s1: str, s2: str) -> int:
    """
    Convert two string numbers to integers and return their sum.
    
    Args:
        s1: First number as string
        s2: Second number as string
    
    Returns:
        Sum of the two numbers as integer
    """
```

---

## Examples

```python
sum_string_numbers("3", "4")
# 7

sum_string_numbers("10", "25")
# 35

sum_string_numbers("100", "200")
# 300
```

---

## Constraints

- Use `int()` to convert strings to integers
- Assume valid integer strings as input
- Return integer, not string

---

## Edge Cases

- Zero strings: sum_string_numbers("0", "5") returns 5
- Negative numbers: sum_string_numbers("-5", "3") returns -2

---

## Test Command

```bash
pytest 01_core_python/tests/test_81_string_to_integer_sum.py -v
```

---

## Hints (use only if stuck)

1. Convert each string: `int(s1)` and `int(s2)`
2. Add them together
3. Return the result

---

## Implementation

```
01_core_python/solutions/81_string_to_integer_sum.py
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
./scripts/commit_exercise.sh feat core 81_string_to_integer_sum
```
