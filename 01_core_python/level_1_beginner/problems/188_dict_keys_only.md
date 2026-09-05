# Exercise 94 — Dictionary Keys Only

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q36  
**Status:** 🔴 Not started

## Concepts

- dictionaries, dict.keys(), iteration

## Prerequisites

- Exercise 92

---

## Objective

Generate dictionary of squares (1-20) and return only the keys as a list.

---

## Requirements

```python
def get_square_keys_only(n: int = 20) -> list[int]:
    """
    Generate squares dict and return only keys.
    
    Args:
        n: Upper limit (default 20)
    
    Returns:
        List of keys [1, 2, 3, ..., n]
    """
```

---

## Examples

```python
get_square_keys_only(5)
# [1, 2, 3, 4, 5]
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_94_dict_keys_only.py -v
```

---

## Hints (use only if stuck)

1. Generate dict first
2. Use `.keys()` method
3. Convert to list

---

## Implementation

```
01_core_python/solutions/94_dict_keys_only.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 94_dict_keys_only
```
