<Exercise 51 — Prime Checker>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, Mathematics, Loops, Conditionals

## Prerequisites

- Previous exercises

---

## Objective

Determine whether a given integer is a prime number.

---

## Requirements

```python
def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
```

---

## Examples

```python
is_prime(5)    # True
is_prime(10)   # False
is_prime(2)    # True
is_prime(1)    # False
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- `0` and `1` are not prime.
- Negative numbers are not prime.

---

## Test Command

```bash
pytest 01_core_python/tests/test_51_prime_checker.py -v
```

---

## Hints (use only if stuck)

1. A prime number is only divisible by 1 and itself.
2. You only need to check for divisors up to the square root of `n`.
3. Start by immediately returning `False` for `n <= 1`.

---

## Implementation

```
01_core_python/solutions/51_prime_checker.py
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
./scripts/commit_exercise.sh feat core 51_prime_checker
```
