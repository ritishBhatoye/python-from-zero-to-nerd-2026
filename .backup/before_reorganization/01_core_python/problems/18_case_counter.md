<Exercise 18 — Case Counter>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q14 (improved)  
**Status:** 🔴 Not started

## Concepts

- Strings, Case checking, Dictionaries

## Prerequisites

- Previous exercises

---

## Objective

Count the number of uppercase and lowercase letters in a text.

---

## Requirements

```python
def count_case(text: str) -> dict[str, int]:
    """Return a dictionary with counts of 'upper' and 'lower' case letters."""
```

---

## Examples

```python
count_case("Hello world!")  # {'upper': 1, 'lower': 9}
```

---

## Constraints

- Python 3.12+ only
- Ignore spaces, punctuation, and digits

---

## Edge Cases

- Empty string
- String with no letters
- String with only uppercase or only lowercase letters

---

## Test Command

```bash
pytest 01_core_python/tests/test_18_case_counter.py -v
```

---

## Hints (use only if stuck)

1. String methods `isupper()` and `islower()` can be helpful.

---

## Implementation

```
01_core_python/solutions/18_case_counter.py
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
./scripts/commit_exercise.sh feat core 18_case_counter
```
