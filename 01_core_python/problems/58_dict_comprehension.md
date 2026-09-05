# Exercise 58 — Dict Comprehension
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Dict comprehensions
- Mapping keys to values

## Prerequisites

- Previous exercises

---

## Objective

Create a dictionary that maps words to their lengths using a dict comprehension.

---

## Requirements

```python
def word_lengths(words: list[str]) -> dict[str, int]:
    """Return a dict mapping each word to its length."""
```

---

## Examples

```python
word_lengths(["hello", "world"])  # {"hello": 5, "world": 5}
word_lengths(["a", "ab"])         # {"a": 1, "ab": 2}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Must use dict comprehension.

---

## Edge Cases

- Empty list input.
- List containing duplicate words.
- List containing empty strings.

---

## Test Command

```bash
pytest 01_core_python/tests/test_58_dict_comprehension.py -v
```

---

## Hints (use only if stuck)

1. The syntax is `{key: value for item in iterable}`.

---

## Implementation

```
01_core_python/solutions/58_dict_comprehension.py
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
./scripts/commit_exercise.sh feat core 58_dict_comprehension
```
