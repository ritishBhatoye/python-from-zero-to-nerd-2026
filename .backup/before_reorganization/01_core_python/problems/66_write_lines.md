# Exercise 66 — Write Lines
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- File writing, Iteration, String formatting

## Prerequisites

- Previous exercises

---

## Objective

Write a list of strings to a file, numbering each line.

---

## Requirements

```python
def write_numbered_lines(filepath: str, lines: list[str]) -> int:
    """
    Writes each line to the file, prefixed with its 1-based line number (e.g., '1: Hello').
    Returns the total number of lines written.
    """
```

---

## Examples

```python
lines = ['Apple', 'Banana']
write_numbered_lines('fruits.txt', lines)  # Returns 2

# fruits.txt content:
# 1: Apple
# 2: Banana
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Empty list of lines (should write an empty file and return 0)

---

## Test Command

```bash
pytest 01_core_python/tests/test_66_write_lines.py -v
```

---

## Hints (use only if stuck)

1. Open the file in write mode ('w').
2. `enumerate(lines, start=1)` is handy here.

---

## Implementation

```
01_core_python/solutions/66_write_lines.py
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
./scripts/commit_exercise.sh feat core 66_write_lines
```
