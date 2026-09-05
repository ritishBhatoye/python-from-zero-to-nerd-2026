<Exercise 28 — List Statistics>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Lists
- Dictionaries
- Built-in math functions (`min`, `max`, `sum`)
- Exceptions

## Prerequisites

- Previous exercises

---

## Objective

Calculate basic statistics (min, max, sum, average, count) for a list of numbers.

---

## Requirements

```python
def list_stats(numbers: list[int | float]) -> dict[str, float]:
    """
    Return statistics for a list of numbers.
    Raises ValueError if the list is empty.
    Returns a dictionary with keys: 'min', 'max', 'sum', 'average', 'count'.
    """
```

---

## Examples

```python
list_stats([1, 2, 3, 4, 5])  
# {'min': 1, 'max': 5, 'sum': 15, 'average': 3.0, 'count': 5}
```

---

## Constraints

- Python 3.12+ only
- No external imports (e.g., no `statistics` module)

---

## Edge Cases

- Empty list (must raise `ValueError`)
- List with one element
- List with negative numbers and floats

---

## Test Command

```bash
pytest 01_core_python/tests/test_28_list_statistics.py -v
```

---

## Hints (use only if stuck)

1. Use Python's built-in functions: `min()`, `max()`, `sum()`, `len()`.
2. Average is `sum()` divided by `len()`.
3. Check `if not numbers:` to raise a `ValueError("List is empty")`.

---

## Implementation

```
01_core_python/solutions/28_list_statistics.py
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
./scripts/commit_exercise.sh feat core 28_list_statistics
```
