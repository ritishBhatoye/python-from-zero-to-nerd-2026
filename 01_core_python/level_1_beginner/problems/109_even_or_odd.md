# Exercise 09 — Even or Odd

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q32 (improved)  
**Status:** 🔴 Not started

## Concepts

- functions, modulo operator, booleans, conditionals

## Prerequisites

- Exercises 01–08

---

## Objective

Practice writing small, testable functions — the building block of all Python code.

---

## Requirements

```python
def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise. Zero is even."""

def describe_parity(n: int) -> str:
    """Return 'even' or 'odd'."""
```

---

## Examples

```python
is_even(4)           # True
is_even(7)           # False
describe_parity(0)   # "even"
describe_parity(3)   # "odd"
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_09_even_or_odd.py -v
```

---

## Implementation

```
01_core_python/solutions/09_even_or_odd.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 09_even_or_odd
```
