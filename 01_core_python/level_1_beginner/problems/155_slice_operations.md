# Exercise 61 — Slice Operations
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Slicing
- List access

## Prerequisites

- Previous exercises

---

## Objective

Perform various slicing operations on a list and return them in a dictionary.

---

## Requirements

```python
def slice_operations(items: list) -> dict:
    """
    Return a dict containing slices of the input list:
    - 'first_three': The first 3 items.
    - 'last_three': The last 3 items.
    - 'reversed': The reversed list.
    - 'every_other': Every other element starting from index 0.
    - 'middle': The middle element (as a list of 1 element if odd length, or 2 elements if even length).
    """
```

---

## Examples

```python
slice_operations([1, 2, 3, 4, 5])
# {
#   'first_three': [1, 2, 3],
#   'last_three': [3, 4, 5],
#   'reversed': [5, 4, 3, 2, 1],
#   'every_other': [1, 3, 5],
#   'middle': [3]
# }

slice_operations([1, 2, 3, 4])
# {
#   'first_three': [1, 2, 3],
#   'last_three': [2, 3, 4],
#   'reversed': [4, 3, 2, 1],
#   'every_other': [1, 3],
#   'middle': [2, 3]
# }
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Empty list should return empty lists for all keys.

---

## Edge Cases

- Empty list.
- List with less than 3 elements.
- Even vs odd length lists (middle logic).

---

## Test Command

```bash
pytest 01_core_python/tests/test_61_slice_operations.py -v
```

---

## Hints (use only if stuck)

1. Use negative indexing for `last_three`, e.g., `[-3:]`.
2. For reversed list, use `[::-1]`.
3. For middle, calculate `length = len(items)` and `mid = length // 2`. Use `mid-1:mid+1` if even, `mid:mid+1` if odd. Make sure to handle empty list correctly!

---

## Implementation

```
01_core_python/solutions/61_slice_operations.py
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
./scripts/commit_exercise.sh feat core 61_slice_operations
```
