# Exercise 78 — Square Value Function

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q23  
**Status:** 🔴 Not started

## Concepts

- functions, exponentiation operator, return values

## Prerequisites

- Basic function knowledge

---

## Objective

Create a simple function to calculate the square of a number using the ** operator.

---

## Requirements

```python
def square(num: int | float) -> int | float:
    """
    Calculate the square of a number.
    
    Args:
        num: The number to square
    
    Returns:
        The square of num (num ** 2)
    """
```

---

## Examples

```python
square(2)
# 4

square(3)
# 9

square(5.5)
# 30.25
```

---

## Constraints

- Use the ** operator
- Handle both integers and floats
- One-line function body

---

## Edge Cases

- square(0) returns 0
- Negative numbers: square(-3) returns 9
- Floats work correctly

---

## Test Command

```bash
pytest 01_core_python/tests/test_78_square_value_function.py -v
```

---

## Hints (use only if stuck)

1. The ** operator: `num ** 2`
2. Just return the calculation directly
3. No need for conditionals

---

## Implementation

```
01_core_python/solutions/78_square_value_function.py
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
./scripts/commit_exercise.sh feat core 78_square_value_function
```
