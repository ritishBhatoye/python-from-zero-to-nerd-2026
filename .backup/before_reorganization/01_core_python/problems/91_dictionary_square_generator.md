# Exercise 91 — Dictionary Square Generator (1-3)

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q33  
**Status:** 🔴 Not started

## Concepts

- dictionaries, loops, exponentiation, dict[key]=value pattern

## Prerequisites

- Basic dictionary knowledge

---

## Objective

Create a dictionary where keys are 1, 2, 3 and values are their squares.

---

## Requirements

```python
def create_square_dict_1_to_3() -> dict[int, int]:
    """
    Create dictionary with keys 1-3 and values as their squares.
    
    Returns:
        Dictionary {1: 1, 2: 4, 3: 9}
    """
```

---

## Examples

```python
create_square_dict_1_to_3()
# {1: 1, 2: 4, 3: 9}
```

---

## Constraints

- Use dict[key]=value pattern
- Keys: 1, 2, 3
- Values: 1, 4, 9

---

## Test Command

```bash
pytest 01_core_python/tests/test_91_dictionary_square_generator.py -v
```

---

## Hints (use only if stuck)

1. Create empty dict: `d = dict()`
2. Assign values: `d[1] = 1`, `d[2] = 2**2`, etc.
3. Use ** operator for squares

---

## Implementation

```
01_core_python/solutions/91_dictionary_square_generator.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 91_dictionary_square_generator
```
