<Exercise 50 — GCD Calculator>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, Algorithms, Mathematics, While Loops, Exceptions

## Prerequisites

- Previous exercises

---

## Objective

Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.

---

## Requirements

```python
def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor (GCD) of a and b."""
```

---

## Examples

```python
gcd(48, 18)   # 6
gcd(-48, 18)  # 6
gcd(5, 0)     # 5
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Do NOT use `math.gcd`

---

## Edge Cases

- Negative numbers (use absolute values as GCD is always non-negative).
- Both numbers are zero (should raise a `ValueError`).

---

## Test Command

```bash
pytest 01_core_python/tests/test_50_gcd_calculator.py -v
```

---

## Hints (use only if stuck)

1. Use Euclid's algorithm: repeatedly replace `(a, b)` with `(b, a % b)` until `b` is 0.
2. The GCD is the absolute value of the remaining non-zero number.
3. Check if both are zero at the very beginning to raise `ValueError`.

---

## Implementation

```
01_core_python/solutions/50_gcd_calculator.py
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
./scripts/commit_exercise.sh feat core 50_gcd_calculator
```
