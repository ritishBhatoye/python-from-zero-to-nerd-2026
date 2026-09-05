<Exercise 13 — Square Dictionary>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** zhiwehu Q3 (improved)
**Status:** 🔴 Not started

## Concepts

- dictionaries, loops, dictionary comprehensions

## Prerequisites

- None

---

## Objective

Generate a dictionary containing {i: i*i} for numbers from 1 to n.

---

## Requirements

```python
def square_dict(n: int) -> dict[int, int]:
    """Return {i: i*i} for i in 1..n."""
```

---

## Examples

```python
square_dict(8)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

---

## Constraints

- Python 3.12+ only
- Raise ValueError for n < 1

---

## Edge Cases

- `n = 1`
- `n < 1` (raise ValueError)

---

## Test Command

```bash
pytest 01_core_python/tests/test_13_square_dictionary.py -v
```

---

## Hints (use only if stuck)

1. Use a dictionary comprehension: `{i: i*i for i in range(1, n+1)}`.

---

## Implementation

```
01_core_python/solutions/13_square_dictionary.py
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
./scripts/commit_exercise.sh feat core 13_square_dictionary
```
