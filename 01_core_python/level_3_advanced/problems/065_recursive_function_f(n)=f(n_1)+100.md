# Exercise 065 — Recursive Function: f(n) = f(n-1) + 100

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

---

## Concepts

- Recursive functions
- Base cases
- Recursive cases
- Function calls and return values
- Stack frames and recursion flow
- Integer arithmetic

## Prerequisites

- Python functions
- Function parameters and return values
- Conditional statements (`if` / `else`)
- Basic mathematical operations

---

## Objective

Write a recursive Python function that calculates the value of a mathematical sequence.

The sequence is defined as:

- f(0) = 0
- f(n) = f(n - 1) + 100, for n > 0

The function must calculate the result by repeatedly calling itself until it reaches the base case, `f(0) = 0`.

**Important:** You must use recursion. Do not use loops (`for` or `while`) to calculate the result.

---

## Requirements

1. Define a function named `f(n)`.
2. Accept a non-negative integer `n` as input.
3. Implement the base case:
   - If `n == 0`, return `0`.
4. Implement the recursive case:
   - If `n > 0`, return `f(n - 1) + 100`.
5. Return an integer as the final result.
6. Do not use loops to calculate the sequence.
7. Handle invalid negative inputs appropriately (raise a `ValueError`).

---

## Examples

**Example 1:**

Input: `n = 0`  
Output: `0`

**Example 2:**

Input: `n = 1`  
Output: `100`

**Example 3:**

Input: `n = 2`  
Output: `200`

**Example 4:**

Input: `n = 3`  
Output: `300`

**Example 5:**

Input: `n = 5`  
Output: `500`

**Example 6:**

Input: `n = 10`  
Output: `1000`

**Example 7:**

Input: `n = 25`  
Output: `2500`

---

## Understanding the Recursion

For `n = 3`, the function calls itself as follows:

f(3) = f(2) + 100

f(2) = f(1) + 100

f(1) = f(0) + 100

f(0) = 0

The function then returns the results:

f(1) = 100

f(2) = 200

f(3) = 300

---

## Edge Cases to Test

| Input | Expected Output |
|---|---:|
| `n = 0` | `0` |
| `n = 1` | `100` |
| `n = 2` | `200` |
| `n = 5` | `500` |
| `n = 10` | `1000` |
| `n = 25` | `2500` |
| `n = -1` | `ValueError` |

---

## Hints (Use Only If Stuck)

1. Every recursive function needs a stopping condition.
2. What should happen when `n == 0`?
3. How can you reduce the problem from `n` to `n - 1`?
4. Each recursive call should bring you closer to the base case.
5. Trace the function manually with `n = 3` before coding.

---

## Test Command

```bash
pytest 01_core_python/level_3_advanced/tests/test_065_recursive_function.py -v
```

## Implementation

```text
01_core_python/level_3_advanced/solutions/065_recursive_function.py
```

---

## Reflection (Fill After Solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How recursion works in this problem:**
- **What is the base case?**
- **What happens if the base case is missing?**
- **How I could improve this solution:**
