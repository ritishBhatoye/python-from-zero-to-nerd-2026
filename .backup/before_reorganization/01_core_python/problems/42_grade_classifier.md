# Exercise 42 — Grade Classifier
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- conditionals, comparison operators

## Prerequisites

- Variables, conditionals

---

## Objective

Classify a numerical score into a letter grade.

---

## Requirements

```python
def classify_grade(score: float) -> str:
    """Return the letter grade for a given score."""
```

---

## Examples

```python
classify_grade(95)  # 'A'
classify_grade(72.5)  # 'C'
```

---

## Constraints

- Python 3.12+ only
- 'A' (90-100), 'B' (80-89), 'C' (70-79), 'D' (60-69), 'F' (below 60).
- Raise `ValueError` if `score < 0` or `score > 100`.
- No external imports.

---

## Edge Cases

- Exact boundary values (e.g., 90, 80).
- Zero or 100.

---

## Test Command

```bash
pytest 01_core_python/tests/test_42_grade_classifier.py -v
```

---

## Hints (use only if stuck)

1. Use `if`, `elif`, and `else` statements.
2. Ensure you check boundary conditions properly.

---

## Implementation

```
01_core_python/solutions/42_grade_classifier.py
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
./scripts/commit_exercise.sh feat core 42_grade_classifier
```
