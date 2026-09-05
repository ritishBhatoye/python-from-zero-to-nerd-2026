# Exercise 05 — Number Classifier

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q12, Q32 (merged)  
**Status:** 🔴 Not started

## Concepts

- conditionals, integers, strings, functions

## Prerequisites

- Exercises 01–04

---

## Objective

Classify integers the way validation logic does in business rules and data pipelines.

---

## Requirements

```python
def classify_number(n: int) -> dict:
```

Return:

```python
{
    "value": int,
    "sign": str,        # "positive", "negative", or "zero"
    "parity": str,      # "even" or "odd" (zero is even)
    "digit_count": int, # number of digits (0 → 1 digit)
}
```

---

## Examples

```python
classify_number(0)
# {"value": 0, "sign": "zero", "parity": "even", "digit_count": 1}

classify_number(-42)
# {"value": -42, "sign": "negative", "parity": "even", "digit_count": 2}
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_05_number_classifier.py -v
```

---

## Implementation

```
01_core_python/solutions/05_number_classifier.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 05_number_classifier
```
