<Exercise 49 — Power Function>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, Loops, Mathematics, Edge Cases

## Prerequisites

- Previous exercises

---

## Objective

Calculate the power of a base raised to an exponent without using built-in exponentiation functions.

---

## Requirements

```python
def power(base: int | float, exponent: int) -> int | float:
    """Calculate base^exponent without using ** or pow()."""
```

---

## Examples

```python
power(2, 3)   # 8
power(5, 0)   # 1
power(2, -2)  # 0.25
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Do NOT use the `**` operator or `pow()` function.

---

## Edge Cases

- `exponent = 0` (should return 1)
- Negative exponents (should return fractional result)

---

## Test Command

```bash
pytest 01_core_python/tests/test_49_power_function.py -v
```

---

## Hints (use only if stuck)

1. You can use a loop that repeats `abs(exponent)` times.
2. For negative exponents, remember that `base^-x = 1 / (base^x)`.

---

## Implementation

```
01_core_python/solutions/49_power_function.py
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
./scripts/commit_exercise.sh feat core 49_power_function
```
