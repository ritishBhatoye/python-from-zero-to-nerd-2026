<Exercise 26 — Sort Words>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q8 (improved)  
**Status:** 🔴 Not started

## Concepts

- Lists
- Sorting
- String methods

## Prerequisites

- Previous exercises

---

## Objective

Sort a list of words alphabetically, using case-insensitive sorting.

---

## Requirements

```python
def sort_words(words: list[str]) -> list[str]:
    """Sort a list of words alphabetically, ignoring case."""
```

---

## Examples

```python
sort_words(["Zebra", "apple", "Banana"])  # ["apple", "Banana", "Zebra"]
sort_words(["without", "hello", "bag", "world"])  # ["bag", "hello", "without", "world"]
```

---

## Constraints

- Python 3.12+ only
- No external imports
- Must not modify the original list (return a new sorted list)

---

## Edge Cases

- Empty list
- List with words of mixed cases but same letters (e.g., ["a", "A", "b"])
- Already sorted list

---

## Test Command

```bash
pytest 01_core_python/tests/test_26_sort_words.py -v
```

---

## Hints (use only if stuck)

1. Use the `sorted()` function.
2. Provide a `key` argument to `sorted()` to specify a function for sorting, like `str.lower`.

---

## Implementation

```
01_core_python/solutions/26_sort_words.py
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
./scripts/commit_exercise.sh feat core 26_sort_words
```
