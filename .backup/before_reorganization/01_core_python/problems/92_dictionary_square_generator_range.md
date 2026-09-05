# Exercise 92 — Dictionary Square Generator (1-20)

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q34  
**Status:** 🔴 Not started

## Concepts

- dictionaries, loops, range, exponentiation

## Prerequisites

- Exercise 91

---

## Objective

Create a dictionary where keys are 1-20 and values are their squares.

---

## Requirements

```python
def create_square_dict_1_to_20() -> dict[int, int]:
    """
    Create dictionary with keys 1-20 and values as squares.
    
    Returns:
        Dictionary {1: 1, 2: 4, ..., 20: 400}
    """
```

---

## Examples

```python
result = create_square_dict_1_to_20()
# {1: 1, 2: 4, 3: 9, ..., 20: 400}
result[5]  # 25
result[20]  # 400
```

---

## Constraints

- Use range() for loop
- Keys from 1 to 20 (inclusive)

---

## Test Command

```bash
pytest 01_core_python/tests/test_92_dictionary_square_generator_range.py -v
```

---

## Hints (use only if stuck)

1. Loop: `for i in range(1, 21)`
2. Assign in loop: `d[i] = i**2`

---

## Implementation

```
01_core_python/solutions/92_dictionary_square_generator_range.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 92_dictionary_square_generator_range
```
