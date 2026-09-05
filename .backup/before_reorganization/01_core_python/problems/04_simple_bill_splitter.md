# Exercise 04 — Simple Bill Splitter

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- floats, division, rounding, functions

## Prerequisites

- Exercises 01–03

---

## Objective

Split a restaurant bill among friends including optional tip — a common real-world calculation.

---

## Requirements

```python
def split_bill(total: float, num_people: int, tip_percent: float = 0.0) -> dict:
```

Return:

```python
{
    "total": float,           # original bill (2 decimals)
    "tip_amount": float,      # tip in currency (2 decimals)
    "grand_total": float,     # total + tip (2 decimals)
    "per_person": float,      # grand_total / num_people (2 decimals)
    "num_people": int,
}
```

Raise `ValueError` if `num_people < 1` or `total < 0` or `tip_percent < 0`.

---

## Examples

```python
split_bill(1000.0, 4, 10.0)
# tip_amount=100.0, grand_total=1100.0, per_person=275.0
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_04_simple_bill_splitter.py -v
```

---

## Implementation

```
01_core_python/solutions/04_simple_bill_splitter.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 04_simple_bill_splitter
```
