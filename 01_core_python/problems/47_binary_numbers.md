# Exercise 47 — Binary Numbers in Range
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q11 (improved)  
**Status:** 🔴 Not started

## Concepts

- string-to-int conversion, base 2, modulo operator

## Prerequisites

- Lists, conditionals, built-in functions

---

## Objective

Filter a list of binary number strings to those divisible by a specific divisor.

---

## Requirements

```python
def filter_divisible_binary(binaries: list[str], divisor: int) -> list[str]:
    """Return binary strings from the list that are divisible by divisor."""
```

---

## Examples

```python
filter_divisible_binary(["0100", "0011", "1010", "1001"], 5)  # ["1010"]
```

---

## Constraints

- Python 3.12+ only
- Assume the strings are valid binary representations.
- Raise `ValueError` if `divisor == 0`.
- No external imports.

---

## Edge Cases

- Empty list.
- Divisor is negative.

---

## Test Command

```bash
pytest 01_core_python/tests/test_47_binary_numbers.py -v
```

---

## Hints (use only if stuck)

1. Use `int(string, 2)` to convert a binary string to an integer.

---

## Implementation

```
01_core_python/solutions/47_binary_numbers.py
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
./scripts/commit_exercise.sh feat core 47_binary_numbers
```
