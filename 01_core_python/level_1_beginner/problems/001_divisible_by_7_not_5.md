# Exercise 001 — Divisible by 7 but not 5

**Phase:** `01_core_python`  
**Level:** 1 — Beginner  
**Source:** zhiwehu/Python-programming-exercises Q1  
**Status:** 🔴 Not started

## Concepts

- Loops (range)
- Conditionals
- Modulo operator (%)
- List operations

## Prerequisites

- Basic Python syntax
- Understanding of for loops
- Knowledge of modulo operator

---

## Objective

Write a program that finds all numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). Print the numbers as a comma-separated sequence on a single line.

---

## Requirements

1. Use a loop to iterate through numbers from 2000 to 3200 (inclusive)
2. Check if each number is divisible by 7 AND not divisible by 5
3. Store qualifying numbers in a list
4. Print the result as comma-separated values

---

## Examples

**Output:**
```
2002,2009,2016,2023,2037,...,3178,3185,3192,3199
```

---

## Hints (use only if stuck)

1. Use `range(2000, 3201)` to iterate through the numbers
2. Use the modulo operator `%` to check divisibility
3. A number is divisible by 7 if `n % 7 == 0`
4. A number is NOT a multiple of 5 if `n % 5 != 0`
5. Use a list to collect the numbers, then join them with commas

---

## Test Command

```bash
pytest 01_core_python/level_1_beginner/tests/test_001_divisible_by_7_not_5.py -v
```

---

## Implementation

```
01_core_python/level_1_beginner/solutions/001_divisible_by_7_not_5.py
```

Create this file yourself — it does not exist until you implement it.

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
