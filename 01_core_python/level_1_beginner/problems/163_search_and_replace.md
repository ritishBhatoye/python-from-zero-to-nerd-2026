# Exercise 69 — Search and Replace
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- In-place file modification, String replacement

## Prerequisites

- Previous exercises

---

## Objective

Replace all occurrences of a string in a file with another string.

---

## Requirements

```python
def search_replace_file(filepath: str, search: str, replace: str) -> int:
    """
    Replaces all occurrences of `search` with `replace` in the given file.
    Returns the total number of replacements made.
    """
```

---

## Examples

```python
# test.txt content:
# Hello foo
# foo foo bar

search_replace_file('test.txt', 'foo', 'world')  # Returns 3

# test.txt content:
# Hello world
# world world bar
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Search string not found
- Search string empty (should not loop infinitely, maybe raise ValueError)

---

## Test Command

```bash
pytest 01_core_python/tests/test_69_search_and_replace.py -v
```

---

## Hints (use only if stuck)

1. Read the entire file content, use `count()` and `replace()`, then overwrite the file.
2. Alternatively, read line by line if concerned about memory (not strictly required here).

---

## Implementation

```
01_core_python/solutions/69_search_and_replace.py
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
./scripts/commit_exercise.sh feat core 69_search_and_replace
```
