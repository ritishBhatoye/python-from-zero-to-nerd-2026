# Exercise 36 — Common Elements
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- sets, lists, type conversions

## Prerequisites

- Previous exercises

---

## Objective

Find common elements between two lists efficiently using sets.

---

## Requirements

```python
def common_elements(list1: list, list2: list) -> list:
    """Return a sorted list of elements present in both lists (no duplicates)."""
```

---

## Examples

```python
common_elements([1, 2, 3, 2], [2, 3, 4])  # [2, 3]
```

---

## Constraints

- Python 3.12+ only
- Elements must be sortable and hashable

---

## Edge Cases

- Empty lists
- Lists with no common elements
- Lists with duplicate common elements

---

## Test Command

```bash
pytest 01_core_python/tests/test_36_common_elements.py -v
```

---

## Hints (use only if stuck)

1. Convert lists to sets.
2. Use the set intersection operation.
3. Convert the result back to a sorted list.

---

## Implementation

```
01_core_python/solutions/36_common_elements.py
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
./scripts/commit_exercise.sh feat core 36_common_elements
```
