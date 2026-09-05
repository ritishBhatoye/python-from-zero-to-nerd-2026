<Exercise 52 — Fibonacci Sequence>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, Lists, Loops, Exceptions

## Prerequisites

- Previous exercises

---

## Objective

Generate the first `n` numbers in the Fibonacci sequence and return them as a list.

---

## Requirements

```python
def fibonacci(n: int) -> list[int]:
    """Return a list containing the first n Fibonacci numbers."""
```

---

## Examples

```python
fibonacci(1)   # [0]
fibonacci(2)   # [0, 1]
fibonacci(5)   # [0, 1, 1, 2, 3]
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- `n < 1` should raise a `ValueError`.
- `n = 1` and `n = 2` should be handled correctly.

---

## Test Command

```bash
pytest 01_core_python/tests/test_52_fibonacci_sequence.py -v
```

---

## Hints (use only if stuck)

1. The first two Fibonacci numbers are 0 and 1.
2. Keep appending the sum of the last two elements in the sequence.

---

## Implementation

```
01_core_python/solutions/52_fibonacci_sequence.py
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
./scripts/commit_exercise.sh feat core 52_fibonacci_sequence
```
