<Exercise 30 — Second Largest>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Lists
- Sets
- Sorting
- Exceptions

## Prerequisites

- Previous exercises

---

## Objective

Find the second largest unique value in a list of numbers.

---

## Requirements

```python
def second_largest(numbers: list[int]) -> int:
    """Return the second largest unique value in a list of numbers. Raises ValueError if there are less than 2 unique values."""
```

---

## Examples

```python
second_largest([10, 20, 4, 45, 99])  # 45
second_largest([10, 10, 10])  # Raises ValueError
```

---

## Constraints

- Python 3.12+ only
- No external imports

---

## Edge Cases

- List with less than 2 elements
- List with multiple identical largest values (e.g. `[5, 5, 4]`)

---

## Test Command

```bash
pytest 01_core_python/tests/test_30_second_largest.py -v
```

---

## Hints (use only if stuck)

1. Use a set to easily find unique values.
2. If the length of unique values is less than 2, raise a ValueError.
3. Sort the unique values and pick the second from the end.

---

## Implementation

```
01_core_python/solutions/30_second_largest.py
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
./scripts/commit_exercise.sh feat core 30_second_largest
```
