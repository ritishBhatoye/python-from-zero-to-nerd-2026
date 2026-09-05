<Exercise 16 — Formula Calculator>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** zhiwehu Q6 (improved)
**Status:** 🔴 Not started

## Concepts

- math module, lists, comprehensions

## Prerequisites

- None

---

## Objective

Calculate a specific mathematical formula for a sequence of values.

---

## Requirements

```python
def formula_q(d_values: list[int]) -> list[int]:
    """Compute Q = floor(sqrt(2*50*D/30)) for each D in d_values."""
```

---

## Examples

```python
formula_q([100, 150, 180])  # [18, 22, 24]
```

---

## Constraints

- Python 3.12+ only
- Use `math.sqrt`
- Truncate the result to an integer using `int()` (equivalent to floor for positive values)

---

## Edge Cases

- Empty list
- List with zero or negative values (handle appropriately or assume non-negative)

---

## Test Command

```bash
pytest 01_core_python/tests/test_16_formula_calculator.py -v
```

---

## Hints (use only if stuck)

1. Use a list comprehension to process each item.
2. The formula simplifies to `(100 * D) / 30`.

---

## Implementation

```
01_core_python/solutions/16_formula_calculator.py
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
./scripts/commit_exercise.sh feat core 16_formula_calculator
```
