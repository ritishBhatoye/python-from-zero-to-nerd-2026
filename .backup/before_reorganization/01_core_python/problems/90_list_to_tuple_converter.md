# Exercise 90 — List to Tuple Converter

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q41  
**Status:** 🔴 Not started

## Concepts

- lists, tuples, type conversion, list comprehension

## Prerequisites

- Basic list and tuple knowledge

---

## Objective

Generate a list of squares and convert it to a tuple.

---

## Requirements

```python
def squares_as_tuple(n: int = 20) -> tuple[int, ...]:
    """
    Generate squares from 1 to n and return as tuple.
    
    Args:
        n: Upper limit (default 20)
    
    Returns:
        Tuple of squares (1, 4, 9, 16, ..., n²)
    """
```

---

## Examples

```python
squares_as_tuple(5)
# (1, 4, 9, 16, 25)

squares_as_tuple(3)
# (1, 4, 9)

squares_as_tuple(1)
# (1,)
```

---

## Constraints

- Generate as list first
- Convert to tuple using tuple() constructor
- Return tuple type

---

## Test Command

```bash
pytest 01_core_python/tests/test_90_list_to_tuple_converter.py -v
```

---

## Hints (use only if stuck)

1. Generate list: `li = [i**2 for i in range(1, n+1)]`
2. Convert: `tuple(li)`
3. Or combine: `tuple(i**2 for i in range(1, n+1))`

---

## Implementation

```
01_core_python/solutions/90_list_to_tuple_converter.py
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
./scripts/commit_exercise.sh feat core 90_list_to_tuple_converter
```
