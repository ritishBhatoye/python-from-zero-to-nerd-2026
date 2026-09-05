<Exercise 25 — Remove Duplicates>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q10 (improved)  
**Status:** 🔴 Not started

## Concepts

- Lists
- Sets
- Sorting

## Prerequisites

- Previous exercises

---

## Objective

Remove duplicate words from a list and return them in sorted order.

---

## Requirements

```python
def remove_duplicates(words: list[str]) -> list[str]:
    """Remove duplicates from a list of words and return them sorted."""
```

---

## Examples

```python
remove_duplicates(["hello", "world", "and", "practice", "makes", "perfect", "and", "hello", "world", "again"])  
# ["again", "and", "hello", "makes", "perfect", "practice", "world"]

remove_duplicates([])  
# []
```

---

## Constraints

- Python 3.12+ only
- No external imports

---

## Edge Cases

- Empty list
- List with all identical words
- List with already unique words

---

## Test Command

```bash
pytest 01_core_python/tests/test_25_remove_duplicates.py -v
```

---

## Hints (use only if stuck)

1. A `set` automatically removes duplicates.
2. The `sorted()` function returns a sorted list.

---

## Implementation

```
01_core_python/solutions/25_remove_duplicates.py
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
./scripts/commit_exercise.sh feat core 25_remove_duplicates
```
