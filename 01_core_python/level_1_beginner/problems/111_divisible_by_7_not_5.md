<Exercise 11 — Divisible by 7 Not 5>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** zhiwehu Q1 (improved)
**Status:** 🔴 Not started

## Concepts

- range, loops, modulo operator, conditionals

## Prerequisites

- None

---

## Objective

Find numbers in a given range that are divisible by 7 but not a multiple of 5.

---

## Requirements

```python
def find_divisible(start: int, end: int) -> list[int]:
    """Return all numbers in [start, end] divisible by 7 but not multiples of 5."""
```

---

## Examples

```python
find_divisible(2000, 2020)  # [2002, 2009, 2016]
```

---

## Constraints

- Python 3.12+ only
- Both `start` and `end` are inclusive.
- `start` <= `end`

---

## Edge Cases

- Range contains no matching numbers
- `start` equals `end` and is/isn't matching

---

## Test Command

```bash
pytest 01_core_python/tests/test_11_divisible_by_7_not_5.py -v
```

---

## Hints (use only if stuck)

1. Use the `%` operator to check for divisibility.
2. A list comprehension might be elegant.

---

## Implementation

```
01_core_python/solutions/11_divisible_by_7_not_5.py
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
./scripts/commit_exercise.sh feat core 11_divisible_by_7_not_5
```
