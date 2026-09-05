# Exercise 88 — First N Elements Slice

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q38  
**Status:** 🔴 Not started

## Concepts

- lists, slicing, list comprehension, indexing

## Prerequisites

- Basic list knowledge

---

## Objective

Generate a list of squares and return only the first 5 elements using slicing.

---

## Requirements

```python
def first_five_squares(n: int = 20) -> list[int]:
    """
    Generate squares from 1 to n, return first 5.
    
    Args:
        n: Upper limit for generating squares (default 20)
    
    Returns:
        List of first 5 squares: [1, 4, 9, 16, 25]
    """
```

---

## Examples

```python
first_five_squares(20)
# [1, 4, 9, 16, 25]

first_five_squares(10)
# [1, 4, 9, 16, 25]

first_five_squares(3)
# [1, 4, 9]  # Only 3 elements available
```

---

## Constraints

- Generate full list first
- Use slicing [:5] to get first 5 elements
- If list has fewer than 5 elements, return all

---

## Test Command

```bash
pytest 01_core_python/tests/test_88_first_n_elements_slice.py -v
```

---

## Hints (use only if stuck)

1. Generate list: `[i**2 for i in range(1, n+1)]`
2. Slice first 5: `li[:5]`
3. Slicing handles short lists automatically

---

## Implementation

```
01_core_python/solutions/88_first_n_elements_slice.py
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
./scripts/commit_exercise.sh feat core 88_first_n_elements_slice
```
