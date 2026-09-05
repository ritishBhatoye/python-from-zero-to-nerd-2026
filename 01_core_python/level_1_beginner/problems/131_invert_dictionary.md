# Exercise 35 — Invert Dictionary
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- dictionaries, collections, data transformation

## Prerequisites

- Previous exercises

---

## Objective

Invert a dictionary's keys and values, grouping duplicate values into lists.

---

## Requirements

```python
def invert_dict(d: dict[str, int]) -> dict[int, list[str]]:
    """Invert dictionary keys and values. Values become lists of keys to handle duplicates."""
```

---

## Examples

```python
invert_dict({'a': 1, 'b': 2, 'c': 1})  # {1: ['a', 'c'], 2: ['b']}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Empty dictionary
- All keys map to the same value
- All keys map to distinct values

---

## Test Command

```bash
pytest 01_core_python/tests/test_35_invert_dictionary.py -v
```

---

## Hints (use only if stuck)

1. Create a new dictionary.
2. Iterate over the key-value pairs of the original dict using `.items()`.
3. If the value doesn't exist as a key in the new dict, create a new list for it.

---

## Implementation

```
01_core_python/solutions/35_invert_dictionary.py
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
./scripts/commit_exercise.sh feat core 35_invert_dictionary
```
