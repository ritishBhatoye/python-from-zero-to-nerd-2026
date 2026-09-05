# Exercise 08 — Tip Calculator

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- floats, division, rounding, functions

## Prerequisites

- Exercises 01–07

---

## Objective

Calculate tip and per-person totals for dining — extends bill splitting with tip logic.

---

## Requirements

```python
def calculate_tip(bill: float, tip_percent: float, num_people: int) -> dict:
```

Return:

```python
{
    "bill": float,
    "tip_percent": float,
    "tip_amount": float,
    "total_with_tip": float,
    "per_person": float,
    "num_people": int,
}
```

All currency values rounded to 2 decimals.

Raise `ValueError` if `bill < 0`, `tip_percent < 0`, or `num_people < 1`.

---

## Examples

```python
calculate_tip(500.0, 18.0, 2)
# tip_amount=90.0, total_with_tip=590.0, per_person=295.0
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_08_tip_calculator.py -v
```

---

## Implementation

```
01_core_python/solutions/08_tip_calculator.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 08_tip_calculator
```
