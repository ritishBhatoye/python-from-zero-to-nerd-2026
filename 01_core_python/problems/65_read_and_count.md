# Exercise 65 — Read and Count
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- File I/O, Error Handling, String methods

## Prerequisites

- Previous exercises

---

## Objective

Read a text file and return statistics about its contents.

---

## Requirements

```python
def count_file_stats(filepath: str) -> dict[str, int]:
    """
    Reads a text file and returns {'lines': N, 'words': N, 'characters': N}.
    Raises FileNotFoundError if the file doesn't exist.
    """
```

---

## Examples

```python
# Assuming 'file.txt' contains:
# Hello world
# Python is fun

count_file_stats('file.txt')  # {'lines': 2, 'words': 5, 'characters': 25}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Empty file (should return 0 for all)
- Non-existent file (should raise FileNotFoundError)

---

## Test Command

```bash
pytest 01_core_python/tests/test_65_read_and_count.py -v
```

---

## Hints (use only if stuck)

1. Use `open()` with a context manager (`with` statement).
2. Count lines by iterating over the file object, words by splitting lines.

---

## Implementation

```
01_core_python/solutions/65_read_and_count.py
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
./scripts/commit_exercise.sh feat core 65_read_and_count
```
