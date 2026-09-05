# Exercise 79 — Sum Two Numbers

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q26  
**Status:** 🔴 Not started

## Concepts

- functions, parameters, arithmetic, return values

## Prerequisites

- Basic function knowledge

---

## Objective

Create a function that takes two numbers and returns their sum.

---

## Requirements

```python
def sum_two_numbers(a: int | float, b: int | float) -> int | float:
    """
    Return the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
```

---

## Examples

```python
sum_two_numbers(1, 2)
# 3

sum_two_numbers(10, 25)
# 35

sum_two_numbers(3.5, 2.1)
# 5.6
```

---

## Constraints

- Handle both integers and floats
- Return the sum directly
- No external libraries needed

---

## Edge Cases

- Negative numbers: sum_two_numbers(-5, 3) returns -2
- Zero: sum_two_numbers(0, 5) returns 5
- Large numbers work correctly

---

## Test Command

```bash
pytest 01_core_python/tests/test_79_sum_two_numbers.py -v
```

---

## Hints (use only if stuck)

1. Use the + operator
2. Return statement: `return a + b`
3. This is a one-line function

---

## Implementation

```
01_core_python/solutions/79_sum_two_numbers.py
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
./scripts/commit_exercise.sh feat core 79_sum_two_numbers
```
