<Exercise 12 — Factorial Calculator>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** zhiwehu Q2 (improved)
**Status:** 🔴 Not started

## Concepts

- recursion, error handling

## Prerequisites

- None

---

## Objective

Calculate the factorial of a given number using recursion.

---

## Requirements

```python
def factorial(n: int) -> int:
    """Calculate the factorial of n recursively."""
```

---

## Examples

```python
factorial(8)  # 40320
factorial(0)  # 1
```

---

## Constraints

- Python 3.12+ only
- Must use recursion
- Raise ValueError for negative n

---

## Edge Cases

- `n = 0` (base case)
- `n < 0` (should raise ValueError)

---

## Test Command

```bash
pytest 01_core_python/tests/test_12_factorial_calculator.py -v
```

---

## Hints (use only if stuck)

1. The base case for recursion is `n == 0`.
2. Check for negative `n` before the recursive step and `raise ValueError("n must be non-negative")`.

---

## Implementation

```
01_core_python/solutions/12_factorial_calculator.py
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
./scripts/commit_exercise.sh feat core 12_factorial_calculator
```
