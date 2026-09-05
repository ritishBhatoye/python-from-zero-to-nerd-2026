# Exercise 59 — Set Comprehension
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Set comprehensions
- Finding unique properties

## Prerequisites

- Previous exercises

---

## Objective

Find all the unique lengths of words in a given list using set comprehension.

---

## Requirements

```python
def unique_lengths(words: list[str]) -> set[int]:
    """Return a set of unique word lengths from the given list of words."""
```

---

## Examples

```python
unique_lengths(["cat", "dog", "elephant"])  # {3, 8}
unique_lengths(["one", "two", "six"])       # {3}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Must use set comprehension.

---

## Edge Cases

- Empty list input.
- List where all words have the same length.

---

## Test Command

```bash
pytest 01_core_python/tests/test_59_set_comprehension.py -v
```

---

## Hints (use only if stuck)

1. The syntax is `{expression for item in iterable}`. Note the curly braces!

---

## Implementation

```
01_core_python/solutions/59_set_comprehension.py
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
./scripts/commit_exercise.sh feat core 59_set_comprehension
```
