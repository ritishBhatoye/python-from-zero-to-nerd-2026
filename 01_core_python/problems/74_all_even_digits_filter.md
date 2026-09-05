# Exercise 74 — All Even Digits Filter

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q12  
**Status:** 🔴 Not started

## Concepts

- numbers, strings, digit checking, filtering, loops

## Prerequisites

- Exercises 01-20

---

## Objective

Find all numbers in a range where every single digit is even.

---

## Requirements

```python
def filter_all_even_digits(start: int, end: int) -> list[int]:
    """
    Find all numbers in range [start, end] where all digits are even.
    
    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)
    
    Returns:
        List of numbers where every digit is even (0, 2, 4, 6, 8)
    """
```

---

## Examples

```python
filter_all_even_digits(1000, 3000)
# [2000, 2002, 2004, 2006, 2008, 2020, 2022, ...]  # All 4-digit nums with even digits

filter_all_even_digits(20, 30)
# [20, 22, 24, 26, 28]

filter_all_even_digits(100, 105)
# []  # No numbers have all even digits
```

---

## Constraints

- Convert number to string to check each digit
- All digits must be even (0, 2, 4, 6, 8)
- Both start and end are inclusive

---

## Edge Cases

- Single digit range
- No valid numbers in range (return empty list)
- Range with 0 (0 has one even digit)

---

## Test Command

```bash
pytest 01_core_python/tests/test_74_all_even_digits_filter.py -v
```

---

## Hints (use only if stuck)

1. Convert each number to string: `str(num)`
2. Check each character (digit): `for digit in str(num)`
3. Use `int(digit) % 2 == 0` to check if even
4. Use `all()` function: `all(int(d) % 2 == 0 for d in str(num))`

---

## Implementation

```
01_core_python/solutions/74_all_even_digits_filter.py
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
./scripts/commit_exercise.sh feat core 74_all_even_digits_filter
```
