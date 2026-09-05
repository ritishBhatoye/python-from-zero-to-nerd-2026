# Exercise 57 — List Comprehension Basics
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- List comprehensions
- Filtering and mapping

## Prerequisites

- Previous exercises

---

## Objective

Create a new list containing the squares of only the even numbers from an original list.

---

## Requirements

```python
def squares_of_evens(numbers: list[int]) -> list[int]:
    """Return a list containing the squares of all even numbers in the input list."""
```

---

## Examples

```python
squares_of_evens([1, 2, 3, 4, 5, 6])  # [4, 16, 36]
squares_of_evens([1, 3, 5])           # []
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Must use list comprehension.

---

## Edge Cases

- Empty list input.
- List with only odd numbers.
- List with negative even numbers.

---

## Test Command

```bash
pytest 01_core_python/tests/test_57_list_comprehension_basics.py -v
```

---

## Hints (use only if stuck)

1. Use `if x % 2 == 0` to check for even numbers.
2. The basic syntax is `[expression for item in iterable if condition]`.

---

## Implementation

```
01_core_python/solutions/57_list_comprehension_basics.py
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
./scripts/commit_exercise.sh feat core 57_list_comprehension_basics
```
