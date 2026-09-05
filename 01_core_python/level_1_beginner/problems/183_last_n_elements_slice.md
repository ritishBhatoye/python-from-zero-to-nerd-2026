# Exercise 89 — Last N Elements Slice

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q39  
**Status:** 🔴 Not started

## Concepts

- lists, negative slicing, indexing

## Prerequisites

- Basic list and slicing knowledge

---

## Objective

Generate a list of squares and return only the last 5 elements using negative slicing.

---

## Requirements

```python
def last_five_squares(n: int = 20) -> list[int]:
    """
    Generate squares from 1 to n, return last 5.
    
    Args:
        n: Upper limit for generating squares (default 20)
    
    Returns:
        List of last 5 squares from the sequence
    """
```

---

## Examples

```python
last_five_squares(20)
# [256, 289, 324, 361, 400]  # 16², 17², 18², 19², 20²

last_five_squares(10)
# [36, 49, 64, 81, 100]  # 6², 7², 8², 9², 10²

last_five_squares(3)
# [1, 4, 9]  # Only 3 elements available
```

---

## Constraints

- Generate full list first
- Use negative slicing [-5:] to get last 5 elements
- If list has fewer than 5 elements, return all

---

## Test Command

```bash
pytest 01_core_python/tests/test_89_last_n_elements_slice.py -v
```

---

## Hints (use only if stuck)

1. Generate list: `[i**2 for i in range(1, n+1)]`
2. Slice last 5: `li[-5:]`
3. Negative indices count from the end

---

## Implementation

```
01_core_python/solutions/89_last_n_elements_slice.py
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
./scripts/commit_exercise.sh feat core 89_last_n_elements_slice
```
