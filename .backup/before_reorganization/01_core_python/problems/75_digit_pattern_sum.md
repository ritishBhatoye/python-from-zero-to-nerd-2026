# Exercise 75 — Digit Pattern Sum

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q15  
**Status:** 🔴 Not started

## Concepts

- strings, numbers, mathematical patterns, string formatting

## Prerequisites

- Exercises 01-15

---

## Objective

Compute the value of a+aa+aaa+aaaa with a given digit a.

---

## Requirements

```python
def digit_pattern_sum(digit: int) -> int:
    """
    Calculate a + aa + aaa + aaaa where a is the input digit.
    
    Args:
        digit: Single digit (0-9)
    
    Returns:
        Sum of a, aa, aaa, aaaa as integers
    
    Example:
        If digit=9, calculate 9 + 99 + 999 + 9999 = 11106
    """
```

---

## Examples

```python
digit_pattern_sum(9)
# 11106  # 9 + 99 + 999 + 9999

digit_pattern_sum(5)
# 6170  # 5 + 55 + 555 + 5555

digit_pattern_sum(1)
# 1234  # 1 + 11 + 111 + 1111
```

---

## Constraints

- Input is a single digit (0-9)
- Build numbers by repeating the digit: "9", "99", "999", "9999"
- Convert to int before adding

---

## Edge Cases

- digit=0 should return 0
- digit=1 gives minimum positive sum

---

## Test Command

```bash
pytest 01_core_python/tests/test_75_digit_pattern_sum.py -v
```

---

## Hints (use only if stuck)

1. Build strings: `str(digit)`, `str(digit) * 2`, `str(digit) * 3`, `str(digit) * 4`
2. Convert each to int: `int(str(digit) * 2)`
3. Sum them all together
4. Alternative: Use f-strings or string multiplication

---

## Implementation

```
01_core_python/solutions/75_digit_pattern_sum.py
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
./scripts/commit_exercise.sh feat core 75_digit_pattern_sum
```
