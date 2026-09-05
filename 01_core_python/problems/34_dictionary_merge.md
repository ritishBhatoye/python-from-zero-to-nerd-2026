# Exercise 34 — Dictionary Merge
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- dictionaries, dictionary updates

## Prerequisites

- Previous exercises

---

## Objective

Merge two dictionaries, resolving key collisions.

---

## Requirements

```python
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merge two dictionaries. If keys collide, values from dict2 win."""
```

---

## Examples

```python
merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})  # {'a': 1, 'b': 3, 'c': 4}
```

---

## Constraints

- Python 3.12+ only
- Do not mutate the original dictionaries, return a new one.

---

## Edge Cases

- Empty dictionaries
- Completely disjoint dictionaries
- Exactly same dictionaries

---

## Test Command

```bash
pytest 01_core_python/tests/test_34_dictionary_merge.py -v
```

---

## Hints (use only if stuck)

1. Python 3.9+ has a union operator `|` for dictionaries.
2. The `update()` method or dictionary unpacking `**` can also be used.

---

## Implementation

```
01_core_python/solutions/34_dictionary_merge.py
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
./scripts/commit_exercise.sh feat core 34_dictionary_merge
```
