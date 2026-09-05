<Exercise 55 — Function Composition>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions as Objects, Higher-Order Functions, Lambdas, Composition

## Prerequisites

- Previous exercises

---

## Objective

Apply a sequence of functions to an initial value.

---

## Requirements

```python
from typing import Callable

def apply_operations(value: float, operations: list[Callable[[float], float]]) -> float:
    """Apply each function in operations to value sequentially."""
```

---

## Examples

```python
apply_operations(5.0, [lambda x: x * 2, lambda x: x + 3])
# 13.0  (5 * 2 = 10, then 10 + 3 = 13)

apply_operations(10.0, [lambda x: x - 2, lambda x: x ** 2])
# 64.0  (10 - 2 = 8, then 8^2 = 64)
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified (typing is allowed)

---

## Edge Cases

- Empty list of operations (should return the original value).
- Chaining multiple functions.

---

## Test Command

```bash
pytest 01_core_python/tests/test_55_function_composition.py -v
```

---

## Hints (use only if stuck)

1. Iterate over the functions in the list.
2. In each step, assign `value = func(value)`.

---

## Implementation

```
01_core_python/solutions/55_function_composition.py
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
./scripts/commit_exercise.sh feat core 55_function_composition
```
