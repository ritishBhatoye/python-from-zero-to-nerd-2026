# Exercise 93 — Dictionary Values Only

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q35  
**Status:** 🔴 Not started

## Concepts

- dictionaries, dict.items(), iteration

## Prerequisites

- Exercise 92

---

## Objective

Generate dictionary of squares (1-20) and return only the values as a list.

---

## Requirements

```python
def get_square_values_only(n: int = 20) -> list[int]:
    """
    Generate squares dict and return only values.
    
    Args:
        n: Upper limit (default 20)
    
    Returns:
        List of square values [1, 4, 9, ..., n²]
    """
```

---

## Examples

```python
get_square_values_only(5)
# [1, 4, 9, 16, 25]

get_square_values_only(3)
# [1, 4, 9]
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_93_dict_values_only.py -v
```

---

## Hints (use only if stuck)

1. Generate dict first
2. Use `.values()` or iterate with `.items()`
3. Return list of values

---

## Implementation

```
01_core_python/solutions/93_dict_values_only.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 93_dict_values_only
```
