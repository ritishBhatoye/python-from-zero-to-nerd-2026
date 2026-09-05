# Exercise 07 — Discount Calculator

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- floats, percentages, arithmetic, functions

## Prerequisites

- Exercises 01–06

---

## Objective

Apply percentage discounts — standard e-commerce and billing logic.

---

## Requirements

```python
def apply_discount(price: float, discount_percent: float) -> dict:
```

Return:

```python
{
    "original_price": float,   # 2 decimals
    "discount_percent": float,
    "discount_amount": float,  # 2 decimals
    "final_price": float,      # 2 decimals
    "saved": bool,             # True if discount_percent > 0
}
```

Raise `ValueError` if `price < 0` or `discount_percent < 0` or `discount_percent > 100`.

---

## Examples

```python
apply_discount(1000.0, 15.0)
# discount_amount=150.0, final_price=850.0, saved=True
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_07_discount_calculator.py -v
```

---

## Implementation

```
01_core_python/solutions/07_discount_calculator.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 07_discount_calculator
```
