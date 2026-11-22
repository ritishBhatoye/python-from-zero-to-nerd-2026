# Exercise 069 — Generator: Numbers Divisible by Both 5 and 7

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

---

## Concepts

- Generators
- `yield` keyword
- Generator functions
- Lazy evaluation
- Iteration
- Conditional statements
- Modulo operator (`%`)

## Prerequisites

- Python functions
- `for` loops
- Conditional statements (`if`)
- Modulo operator
- Basic understanding of iterables and iterators

---

## Objective

Write a Python generator function that generates all integers within a specified range that are divisible by both 5 and 7.

The generator must produce numbers one at a time using the `yield` keyword instead of returning all matching numbers in a list.

**Mathematical condition:**

A number `x` is valid if:

- `x % 5 == 0`
- `x % 7 == 0`

Both conditions must be satisfied.

---

## Requirements

1. Define a generator function named `generate_numbers(start, end)`.
2. Accept two integer parameters:
   - `start`: Beginning of the range (inclusive).
   - `end`: Ending of the range (inclusive).
3. Iterate through all integers between `start` and `end`.
4. Check whether each number is divisible by both 5 and 7.
5. Use the `yield` keyword to produce each matching number individually.
6. Do not use `return` to return a list of matching numbers.
7. Do not use list comprehensions or another generator expression to implement the solution.
8. Handle invalid ranges where `start > end` appropriately (raise a `ValueError`).

---

## Examples

**Example 1 — Basic range**

Input:
```python
start = 1
end = 100
```

Expected output:
```text
35, 70
```

**Example 2 — Range containing zero**

Input:
```python
start = 0
end = 100
```

Expected output:
```text
0, 35, 70
```

**Example 3 — Larger range**

Input:
```python
start = 1
end = 200
```

Expected output:
```text
35, 70, 105, 140, 175
```

**Example 4 — No matching numbers**

Input:
```python
start = 1
end = 30
```

Expected output:
```text
No matching numbers
```

**Example 5 — Negative range**

Input:
```python
start = -100
end = 0
```

Expected output:
```text
-70, -35, 0
```

---

## Additional Test Cases

| Start | End | Expected output |
|---:|---:|---|
| 1 | 10 | Empty generator |
| 1 | 35 | 35 |
| 35 | 105 | 35, 70, 105 |
| 50 | 150 | 70, 105, 140 |
| -50 | 50 | -35, 0, 35 |
| 100 | 100 | Empty generator |
| 105 | 35 | ValueError |

---

## Hints (Use Only If Stuck)

1. Think about how the modulo operator checks divisibility.
2. Remember that both divisibility conditions must be true.
3. A generator function uses `yield` instead of returning all results at once.
4. Explore how a `for` loop consumes values from a generator.
5. Consider what happens when no numbers satisfy the conditions.
6. Remember that generator objects are consumed during iteration.

---

## Test Command

```bash
pytest 01_core_python/level_3_advanced/tests/test_069_generator_divisible_5_and_7.py -v
```

## Implementation

```text
01_core_python/level_3_advanced/solutions/069_generator_divisible_5_and_7.py
```

---

## Reflection (Fill After Solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **What is the difference between `yield` and `return`?**
- **What is lazy evaluation?**
- **Why does a generator not store all values in memory at once?**
- **How could I improve this solution?**