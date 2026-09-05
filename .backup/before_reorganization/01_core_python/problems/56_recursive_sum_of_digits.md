<Exercise 56 — Recursive Sum of Digits>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, Recursion, Mathematics

## Prerequisites

- Previous exercises

---

## Objective

Calculate the sum of the digits of an integer using recursion.

---

## Requirements

```python
def digit_sum(n: int) -> int:
    """Return the sum of the digits of n recursively."""
```

---

## Examples

```python
digit_sum(12345)  # 15
digit_sum(99)     # 18
digit_sum(-123)   # 6
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- MUST use recursion (a loop will fail the intent, though tests only check output).

---

## Edge Cases

- Negative numbers (use absolute value).
- Single digit numbers (return the number itself).

---

## Test Command

```bash
pytest 01_core_python/tests/test_56_recursive_sum_of_digits.py -v
```

---

## Hints (use only if stuck)

1. Convert negative numbers to positive using `abs(n)` at the start or in a wrapper.
2. Base case: if `n < 10`, return `n`.
3. Recursive step: return `(n % 10) + digit_sum(n // 10)`.

---

## Implementation

```
01_core_python/solutions/56_recursive_sum_of_digits.py
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
./scripts/commit_exercise.sh feat core 56_recursive_sum_of_digits
```
