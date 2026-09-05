# Exercise 45 — Number Pattern
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- nested loops, string joining

## Prerequisites

- Loops, strings

---

## Objective

Generate a triangular pattern of numbers.

---

## Requirements

```python
def number_triangle(rows: int) -> str:
    """Return a string representing a triangle of numbers."""
```

---

## Examples

```python
print(number_triangle(3))
# Output:
# 1
# 1 2
# 1 2 3
```

---

## Constraints

- Python 3.12+ only
- Return a single string with rows separated by newlines `\n`.
- If `rows <= 0`, return an empty string.
- No external imports.

---

## Edge Cases

- `rows = 0` or negative.
- `rows = 1`.

---

## Test Command

```bash
pytest 01_core_python/tests/test_45_number_pattern.py -v
```

---

## Hints (use only if stuck)

1. Use nested `for` loops or list comprehensions with `str.join()`.
2. Build each row individually, then join the rows.

---

## Implementation

```
01_core_python/solutions/45_number_pattern.py
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
./scripts/commit_exercise.sh feat core 45_number_pattern
```
