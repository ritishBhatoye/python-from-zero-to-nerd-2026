<Exercise 15 — Digit Repetition Sum>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** zhiwehu Q15 (improved)
**Status:** 🔴 Not started

## Concepts

- arithmetic, string manipulation, type conversion

## Prerequisites

- None

---

## Objective

Compute the sum `a + aa + aaa + aaaa` where `a` is a given digit.

---

## Requirements

```python
def digit_repeat_sum(a: int) -> int:
    """Compute a + aa + aaa + aaaa."""
```

---

## Examples

```python
digit_repeat_sum(9)  # 11106 (9 + 99 + 999 + 9999)
```

---

## Constraints

- Python 3.12+ only
- Raise ValueError for `a` not in 1..9

---

## Edge Cases

- `a` outside the range 1-9 (e.g., 0, 10, -5)

---

## Test Command

```bash
pytest 01_core_python/tests/test_15_digit_repetition_sum.py -v
```

---

## Hints (use only if stuck)

1. Convert `a` to a string to easily create 'aa', 'aaa', etc.
2. Convert back to integer to sum them.

---

## Implementation

```
01_core_python/solutions/15_digit_repetition_sum.py
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
./scripts/commit_exercise.sh feat core 15_digit_repetition_sum
```
