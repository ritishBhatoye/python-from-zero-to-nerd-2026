# Exercise 72 — Two-Dimensional Array Generator

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q7  
**Status:** 🔴 Not started

## Concepts

- nested lists, list comprehensions, 2D arrays, loops

## Prerequisites

- Exercises 01-10

---

## Objective

Generate a 2D array where each element at position [i][j] equals i * j.

---

## Requirements

```python
def generate_2d_array(rows: int, cols: int) -> list[list[int]]:
    """
    Generate a 2D array where element[i][j] = i * j.
    
    Args:
        rows: Number of rows (X)
        cols: Number of columns (Y)
    
    Returns:
        2D list where each element at [i][j] equals i * j
    
    Note: i ranges from 0 to rows-1, j ranges from 0 to cols-1
    """
```

---

## Examples

```python
generate_2d_array(3, 5)
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

generate_2d_array(2, 3)
# [[0, 0, 0], [0, 1, 2]]

generate_2d_array(1, 1)
# [[0]]
```

---

## Constraints

- Use list comprehension or nested loops
- 0-indexed (first row/col is index 0)

---

## Edge Cases

- When rows or cols is 1
- When rows or cols is 0 (return empty list)

---

## Test Command

```bash
pytest 01_core_python/tests/test_72_two_dimensional_array_generator.py -v
```

---

## Hints (use only if stuck)

1. Nested list comprehension: `[[expression for col in range(cols)] for row in range(rows)]`
2. The expression should be `row * col`
3. Alternative: use nested for loops

---

## Implementation

```
01_core_python/solutions/72_two_dimensional_array_generator.py
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
./scripts/commit_exercise.sh feat core 72_two_dimensional_array_generator
```
