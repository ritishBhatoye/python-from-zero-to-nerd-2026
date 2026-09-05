# Exercise 41 — FizzBuzz
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** classic, improved  
**Status:** 🔴 Not started

## Concepts

- loops, conditionals, modulo operator

## Prerequisites

- Variables, loops, conditionals

---

## Objective

Return the classic FizzBuzz sequence up to a given number.

---

## Requirements

```python
def fizzbuzz(n: int) -> list[str]:
    """Return a list of strings representing the FizzBuzz sequence up to n."""
```

---

## Examples

```python
fizzbuzz(5)  # ["1", "2", "Fizz", "4", "Buzz"]
fizzbuzz(15)  # ..., "13", "14", "FizzBuzz"]
```

---

## Constraints

- Python 3.12+ only
- Raise `ValueError` if `n < 1`.
- No external imports.

---

## Edge Cases

- `n = 1`
- Multiples of both 3 and 5.

---

## Test Command

```bash
pytest 01_core_python/tests/test_41_fizzbuzz.py -v
```

---

## Hints (use only if stuck)

1. Check for `n % 15 == 0` first, before `n % 3` and `n % 5`.
2. Use a `for` loop from 1 to `n` inclusive.

---

## Implementation

```
01_core_python/solutions/41_fizzbuzz.py
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
./scripts/commit_exercise.sh feat core 41_fizzbuzz
```
