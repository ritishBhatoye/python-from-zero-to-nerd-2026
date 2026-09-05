# Exercise 44 — Multiplication Table
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- loops, string formatting

## Prerequisites

- `for` loops, f-strings

---

## Objective

Generate a multiplication table for a specific number.

---

## Requirements

```python
def multiplication_table(n: int, up_to: int = 10) -> list[str]:
    """Return a list of strings representing the multiplication table for n."""
```

---

## Examples

```python
multiplication_table(5, 3)  # ['5 x 1 = 5', '5 x 2 = 10', '5 x 3 = 15']
```

---

## Constraints

- Python 3.12+ only
- No external imports.

---

## Edge Cases

- `up_to = 0` or negative values (should return an empty list).
- `n` can be zero or negative.

---

## Test Command

```bash
pytest 01_core_python/tests/test_44_multiplication_table.py -v
```

---

## Hints (use only if stuck)

1. Iterate from 1 to `up_to` using `range()`.
2. Use f-strings for formatting the output.

---

## Implementation

```
01_core_python/solutions/44_multiplication_table.py
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
./scripts/commit_exercise.sh feat core 44_multiplication_table
```
