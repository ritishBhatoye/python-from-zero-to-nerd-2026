# Exercise 073 — Binary Search: First and Last Occurrence

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

## Concepts
- Binary Search
- Divide and Conquer
- Duplicate Elements
- List Indexing
- While Loops
- Algorithm Optimization
- Time and Space Complexity

## Prerequisites
- Python lists
- Functions
- Conditional statements
- Basic Binary Search implementation
- Sorted arrays

---

## Objective

Implement a function that finds the first and last occurrence of a target value in a sorted list containing duplicate elements.

Return both indices as a tuple.

If the target does not exist, return `(-1, -1)`.

## Requirements

1. Implement a function named `find_first_last(numbers, target)`.
2. The input list contains integers sorted in ascending order.
3. The list may contain duplicate values.
4. Use Binary Search rather than a linear search.
5. Return the first and last indices of the target.
6. Return `(-1, -1)` if the target is absent.
7. Aim for O(log n) time complexity.
8. Do not modify the original list.

## Examples

**Example 1**

Input: `numbers = [1, 2, 2, 2, 3, 4], target = 2`

Output: `(1, 3)`

**Example 2**

Input: `numbers = [1, 2, 3, 4, 5], target = 3`

Output: `(2, 2)`

**Example 3**

Input: `numbers = [1, 2, 3, 4, 5], target = 6`

Output: `(-1, -1)`

**Example 4**

Input: `numbers = [], target = 5`

Output: `(-1, -1)`

## Hints (use only if stuck)

1. A normal Binary Search finds one occurrence.
2. Think about how to continue searching after finding the target.
3. Consider searching separately for the first and last occurrence.

## Test Command

`pytest 01_core_python/level_3_advanced/tests/test_073_binary_search_duplicate.py -v`

## Implementation

`01_core_python/level_3_advanced/solutions/073_binary_search_duplicate.py`

## Reflection

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
- **Time complexity:**
- **Space complexity:**