# Exercise 10 — Max of Three Numbers

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q31 (improved)  
**Status:** 🔴 Not started

## Concepts

- functions, conditionals, comparison operators

## Prerequisites

- Exercises 01–09

---

## Objective

Find the maximum of three values without using built-in `max()` — builds comparison logic skills.

---

## Requirements

```python
def max_of_three(a: float, b: float, c: float) -> float:
```

Return the largest of the three values.

**Do not use** the built-in `max()` function.

---

## Examples

```python
max_of_three(1, 5, 3)    # 5
max_of_three(-1, -5, -3) # -1
max_of_three(4, 4, 2)    # 4
```

---

## Edge Cases

- All three equal
- Negative numbers
- Floats

---

## Test Command

```bash
pytest 01_core_python/tests/test_10_max_of_three.py -v
```

---

## Implementation

```
01_core_python/solutions/10_max_of_three.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 10_max_of_three
```
