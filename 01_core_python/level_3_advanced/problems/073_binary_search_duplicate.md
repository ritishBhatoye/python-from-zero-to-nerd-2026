# Exercise 073 — Binary Search

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

## Concepts
- Binary Search
- Divide and Conquer
- Functions
- List Indexing
- While Loops
- Time and Space Complexity
- Search Algorithms

## Prerequisites
- Python lists
- Functions
- Loops and conditional statements
- Basic understanding of sorted arrays

---

## Objective

Implement a binary search algorithm that searches for a target value in a sorted list and returns its index.

If the target does not exist in the list, return `-1`.

## Requirements

1. Implement a function named `binary_search(numbers, target)`.
2. The input list will contain integers sorted in ascending order.
3. Use the Binary Search algorithm (do not use Python's built-in `in`, `index()`, or `find()` methods to perform the search).
4. Return the index of the target if found.
5. Return `-1` if the target is not found.
6. Handle an empty list.
7. Aim for O(log n) time complexity.
8. Do not modify the original list.

---

## Examples

**Example 1**

Input: `numbers = [1, 3, 5, 7, 9], target = 5`

Output: `2`

**Example 2**

Input: `numbers = [2, 4, 6, 8, 10], target = 8`

Output: `3`

**Example 3**

Input: `numbers = [1, 3, 5, 7, 9], target = 4`

Output: `-1`

**Example 4**

Input: `numbers = [], target = 5`

Output: `-1`

**Example 5**

Input: `numbers = [10], target = 10`

Output: `0`

---

## Hints (use only if stuck)

1. Maintain two pointers representing the search boundaries.
2. Calculate the middle index of the current search range.
3. Compare the middle element with the target.
4. Eliminate half of the remaining search space after each comparison.
5. Continue until the target is found or the search range becomes empty.

---

## Test Command

```bash
pytest 01_core_python/level_3_advanced/tests/test_073_binary_search.py -v
```

## Implementation

`01_core_python/level_3_advanced/solutions/073_binary_search.py`

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
- **Time complexity:**
- **Space complexity:**