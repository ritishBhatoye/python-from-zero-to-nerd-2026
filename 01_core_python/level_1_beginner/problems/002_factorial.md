# Exercise 002 — Factorial Calculator

**Phase:** `01_core_python`  
**Level:** 1 — Beginner  
**Status:** 🔴 Not started

## Concepts

- Functions
- Recursion OR loops
- Mathematical operations

## Prerequisites

- Basic function definition
- Understanding of factorial concept (n! = n × (n-1) × ... × 1)

---

## Objective

Write a program which can compute the factorial of a given number. The result should be printed in a comma-separated sequence on a single line.

For example, if the input is:
```
8
```

Then, the output should be:
```
40320
```

---

## Requirements

1. Create a function that calculates factorial
2. The function should accept an integer
3. Return the factorial result
4. Handle the case where n = 0 (0! = 1)

---

## Examples

**Input:** `5`  
**Output:** `120`

**Input:** `8`  
**Output:** `40320`

**Input:** `0`  
**Output:** `1`

---

## Hints (use only if stuck)

1. Factorial can be implemented recursively: `factorial(n) = n * factorial(n-1)`
2. Base case: `factorial(0) = 1` and `factorial(1) = 1`
3. OR use a loop: multiply numbers from 1 to n
4. Python has `math.factorial()` but implement your own for practice

---

## Test Command

```bash
pytest 01_core_python/level_1_beginner/tests/test_002_factorial.py -v
```

---

## Implementation

```
01_core_python/level_1_beginner/solutions/002_factorial.py
```

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
