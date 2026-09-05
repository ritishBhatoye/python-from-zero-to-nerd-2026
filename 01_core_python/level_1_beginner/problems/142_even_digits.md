# Exercise 48 — Even Digit Numbers
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q12 (improved)  
**Status:** 🔴 Not started

## Concepts

- integers to strings, `all()`, list comprehensions

## Prerequisites

- Strings, loops, conditionals

---

## Objective

Find all numbers in a given range where every digit is an even number.

---

## Requirements

```python
def all_even_digits(start: int, end: int) -> list[int]:
    """Return a list of integers in [start, end] where all digits are even."""
```

---

## Examples

```python
all_even_digits(20, 25)  # [20, 22, 24]
```

---

## Constraints

- Python 3.12+ only
- The range is inclusive.
- If `start > end`, return an empty list.
- Consider negative numbers by checking their absolute value digits.
- No external imports.

---

## Edge Cases

- Range with no such numbers.
- Negative ranges (e.g., -25 to -20).

---

## Test Command

```bash
pytest 01_core_python/tests/test_48_even_digits.py -v
```

---

## Hints (use only if stuck)

1. Convert the number to a string to easily iterate over its digits.
2. Use `.replace('-', '')` or `abs()` to handle negative signs.

---

## Implementation

```
01_core_python/solutions/48_even_digits.py
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
./scripts/commit_exercise.sh feat core 48_even_digits
```
