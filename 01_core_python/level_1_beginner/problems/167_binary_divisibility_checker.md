# Exercise 73 — Binary Divisibility Checker

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q11  
**Status:** 🔴 Not started

## Concepts

- binary numbers, type conversion, int() with base, lists, filters

## Prerequisites

- Exercises 01-15

---

## Objective

Check which 4-digit binary numbers from a list are divisible by 5 when converted to decimal.

---

## Requirements

```python
def filter_binary_divisible_by_5(binary_strings: list[str]) -> list[str]:
    """
    Filter binary strings that are divisible by 5 when converted to decimal.
    
    Args:
        binary_strings: List of 4-digit binary number strings (e.g., ["0100", "1010"])
    
    Returns:
        List of binary strings (as strings) that are divisible by 5 in decimal
    """
```

---

## Examples

```python
filter_binary_divisible_by_5(["0100", "0011", "1010", "1001"])
# ["1010"]  # 1010 in binary = 10 in decimal, which is divisible by 5

filter_binary_divisible_by_5(["1111", "0101", "1100"])
# ["0101"]  # 0101 in binary = 5 in decimal

filter_binary_divisible_by_5(["0001", "0010", "0011"])
# []  # None are divisible by 5
```

---

## Constraints

- Use `int(binary_str, 2)` to convert binary to decimal
- Return result as list of binary strings (not decimal numbers)

---

## Edge Cases

- Empty list should return empty list
- All divisible by 5 should return all items
- None divisible should return empty list

---

## Test Command

```bash
pytest 01_core_python/tests/test_73_binary_divisibility_checker.py -v
```

---

## Hints (use only if stuck)

1. Convert each binary string to int: `int("1010", 2)` gives 10
2. Check divisibility with modulo: `decimal_value % 5 == 0`
3. Use list comprehension with condition

---

## Implementation

```
01_core_python/solutions/73_binary_divisibility_checker.py
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
./scripts/commit_exercise.sh feat core 73_binary_divisibility_checker
```
