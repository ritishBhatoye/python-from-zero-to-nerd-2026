# Exercise 46 — Collatz Sequence
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- `while` loops, conditionals

## Prerequisites

- Variables, loops, conditionals

---

## Objective

Generate the Collatz sequence for a given positive integer.

---

## Requirements

```python
def collatz(n: int) -> list[int]:
    """Return the Collatz sequence starting from n."""
```

---

## Examples

```python
collatz(6)  # [6, 3, 10, 5, 16, 8, 4, 2, 1]
```

---

## Constraints

- Python 3.12+ only
- If even, divide by 2 (use integer division `//`).
- If odd, multiply by 3 and add 1.
- Stop when reaching 1 (include 1 in the list).
- Raise `ValueError` for `n < 1`.
- No external imports.

---

## Edge Cases

- `n = 1` (should just return `[1]`).

---

## Test Command

```bash
pytest 01_core_python/tests/test_46_collatz_sequence.py -v
```

---

## Hints (use only if stuck)

1. Use a `while` loop that continues as long as `n > 1`.
2. Don't forget to append `1` at the end, or append `n` at the start of each iteration.

---

## Implementation

```
01_core_python/solutions/46_collatz_sequence.py
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
./scripts/commit_exercise.sh feat core 46_collatz_sequence
```
