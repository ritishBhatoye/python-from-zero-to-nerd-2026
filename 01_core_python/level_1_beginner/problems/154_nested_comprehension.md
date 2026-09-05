# Exercise 60 — Nested Comprehension
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q7 (improved)  
**Status:** 🔴 Not started

## Concepts

- Nested list comprehensions
- Matrix generation

## Prerequisites

- Previous exercises

---

## Objective

Generate a multiplication grid (a list of lists) where `grid[i][j] = i * j`. The outer list should correspond to `i` (ranging from `0` to `rows-1`) and inner list to `j` (ranging from `0` to `cols-1`).

---

## Requirements

```python
def multiplication_grid(rows: int, cols: int) -> list[list[int]]:
    """Return a multiplication grid of dimensions rows x cols."""
```

---

## Examples

```python
multiplication_grid(3, 4)
# [
#   [0, 0, 0, 0],
#   [0, 1, 2, 3],
#   [0, 2, 4, 6]
# ]
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Should be implemented using nested list comprehensions if possible.

---

## Edge Cases

- 0 rows or 0 cols.
- 1x1 grid.

---

## Test Command

```bash
pytest 01_core_python/tests/test_60_nested_comprehension.py -v
```

---

## Hints (use only if stuck)

1. A nested list comprehension looks like `[[expression for inner_item in inner_iterable] for outer_item in outer_iterable]`.

---

## Implementation

```
01_core_python/solutions/60_nested_comprehension.py
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
./scripts/commit_exercise.sh feat core 60_nested_comprehension
```
