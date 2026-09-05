<Exercise 27 — Filter Odd Squares>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q16 (improved)  
**Status:** 🔴 Not started

## Concepts

- Lists
- List comprehensions
- Modulo operator

## Prerequisites

- Previous exercises

---

## Objective

Return only the odd numbers from a given list of numbers using list comprehension.

---

## Requirements

```python
def odd_numbers(numbers: list[int]) -> list[int]:
    """Return a new list containing only the odd numbers from the input."""
```

---

## Examples

```python
odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])  # [1, 3, 5, 7, 9]
odd_numbers([2, 4, 6])  # []
```

---

## Constraints

- Python 3.12+ only
- No external imports
- Should ideally use a list comprehension

---

## Edge Cases

- Empty list
- List with negative odd and even numbers
- List with all even numbers

---

## Test Command

```bash
pytest 01_core_python/tests/test_27_odd_numbers.py -v
```

---

## Hints (use only if stuck)

1. Use modulo `% 2` to check for oddness (`num % 2 != 0`).
2. List comprehensions have the syntax: `[expression for item in iterable if condition]`.

---

## Implementation

```
01_core_python/solutions/27_odd_numbers.py
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
./scripts/commit_exercise.sh feat core 27_odd_numbers
```
