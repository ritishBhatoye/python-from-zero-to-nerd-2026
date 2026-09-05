<Exercise 21 — Word Counter>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Strings, Splitting

## Prerequisites

- Previous exercises

---

## Objective

Count the number of words in a string, correctly handling multiple spaces and empty strings.

---

## Requirements

```python
def count_words(text: str) -> int:
    """Return the number of words in the string."""
```

---

## Examples

```python
count_words("hello world")       # 2
count_words("  multiple   spaces  ") # 2
```

---

## Constraints

- Python 3.12+ only
- Words are separated by whitespace

---

## Edge Cases

- Empty string
- String with only spaces
- String with multiple consecutive spaces

---

## Test Command

```bash
pytest 01_core_python/tests/test_21_word_counter.py -v
```

---

## Hints (use only if stuck)

1. `str.split()` without arguments splits by any whitespace and removes empty strings from the result.

---

## Implementation

```
01_core_python/solutions/21_word_counter.py
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
./scripts/commit_exercise.sh feat core 21_word_counter
```
