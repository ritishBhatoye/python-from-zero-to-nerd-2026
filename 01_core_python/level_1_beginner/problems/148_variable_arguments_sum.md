<Exercise 54 — Variable Arguments Sum>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, `*args`, `**kwargs`, Dictionaries, Aggregation

## Prerequisites

- Previous exercises

---

## Objective

Create a function that can accept any number of positional and keyword arguments, summing up their numeric values and counting them.

---

## Requirements

```python
def flexible_sum(*args: int | float, **kwargs: int | float) -> dict:
    """Return a dictionary summarizing the sums of args and kwargs."""
```

---

## Examples

```python
flexible_sum(1, 2, 3, a=4, b=5)
# {'positional_sum': 6, 'keyword_sum': 9, 'total': 15, 'count': 5}

flexible_sum(10.5, x=2.5)
# {'positional_sum': 10.5, 'keyword_sum': 2.5, 'total': 13.0, 'count': 2}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- Output dictionary keys must match exactly: `positional_sum`, `keyword_sum`, `total`, `count`.

---

## Edge Cases

- No arguments provided (sums should be 0, count 0).
- Mixed integer and float values.

---

## Test Command

```bash
pytest 01_core_python/tests/test_54_variable_arguments_sum.py -v
```

---

## Hints (use only if stuck)

1. Use `sum(args)` for positional arguments.
2. Use `sum(kwargs.values())` for keyword arguments.

---

## Implementation

```
01_core_python/solutions/54_variable_arguments_sum.py
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
./scripts/commit_exercise.sh feat core 54_variable_arguments_sum
```
