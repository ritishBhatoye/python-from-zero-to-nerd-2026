# Exercise 76 — Filter Odd Numbers

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q16  
**Status:** 🔴 Not started

## Concepts

- list comprehensions, filtering, modulo operator

## Prerequisites

- Exercises 01-15, list comprehension basics

---

## Objective

Extract only odd numbers from a list using list comprehension.

---

## Requirements

```python
def filter_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Return a new list containing only the odd numbers from the input list.
    
    Args:
        numbers: List of integers
    
    Returns:
        List of odd integers only, preserving original order
    """
```

---

## Examples

```python
filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# [1, 3, 5, 7, 9]

filter_odd_numbers([10, 20, 30])
# []

filter_odd_numbers([11, 13, 15])
# [11, 13, 15]
```

---

## Constraints

- Use list comprehension with conditional
- Preserve original order
- Don't modify input list

---

## Edge Cases

- Empty list returns empty list
- All even numbers returns empty list
- All odd numbers returns copy of input

---

## Test Command

```bash
pytest 01_core_python/tests/test_76_filter_odd_numbers.py -v
```

---

## Hints (use only if stuck)

1. List comprehension with filter: `[x for x in numbers if condition]`
2. Odd check: `x % 2 != 0` or `x % 2 == 1`
3. One-liner solution is possible

---

## Implementation

```
01_core_python/solutions/76_filter_odd_numbers.py
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
./scripts/commit_exercise.sh feat core 76_filter_odd_numbers
```
