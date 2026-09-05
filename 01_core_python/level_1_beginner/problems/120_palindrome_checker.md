<Exercise 20 — Palindrome Checker>
**Phase:** `01_core_python`
**Type:** concept/micro
**Difficulty:** Level 1 — Beginner
**Inspired by:** New (curriculum original)
**Status:** 🔴 Not started

## Concepts

- Strings, Conditionals, Pre-processing

## Prerequisites

- Previous exercises

---

## Objective

Check if a string reads the same forwards and backwards, ignoring case and spaces.

---

## Requirements

```python
def is_palindrome(s: str) -> bool:
    """Check if the string is a palindrome."""
```

---

## Examples

```python
is_palindrome("race car")  # True
is_palindrome("hello")     # False
```

---

## Constraints

- Python 3.12+ only
- Ignore case (treat 'A' and 'a' as same)
- Ignore spaces

---

## Edge Cases

- Empty string or only spaces
- Single character
- Palindrome with mixed case

---

## Test Command

```bash
pytest 01_core_python/tests/test_20_palindrome_checker.py -v
```

---

## Hints (use only if stuck)

1. Remove spaces and convert the string to lowercase first.

---

## Implementation

```
01_core_python/solutions/20_palindrome_checker.py
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
./scripts/commit_exercise.sh feat core 20_palindrome_checker
```
