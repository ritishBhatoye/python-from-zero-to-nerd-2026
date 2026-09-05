<Exercise 19 — String Reverser>
**Phase:** `01_core_python`
**Type:** concept/micro
**Difficulty:** Level 1 — Beginner
**Inspired by:** New (curriculum original)
**Status:** 🔴 Not started

## Concepts

- Strings, Loops, Concatenation

## Prerequisites

- Previous exercises

---

## Objective

Reverse a string manually without using slicing `[::-1]` or `reversed()`.

---

## Requirements

```python
def reverse_string(s: str) -> str:
    """Reverse the given string using a loop."""
```

---

## Examples

```python
reverse_string("hello")  # "olleh"
```

---

## Constraints

- Python 3.12+ only
- Do not use `[::-1]` or `reversed()`

---

## Edge Cases

- Empty string
- Single character string

---

## Test Command

```bash
pytest 01_core_python/tests/test_19_string_reverser.py -v
```

---

## Hints (use only if stuck)

1. Initialize an empty string and prepend characters in a loop.

---

## Implementation

```
01_core_python/solutions/19_string_reverser.py
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
./scripts/commit_exercise.sh feat core 19_string_reverser
```
