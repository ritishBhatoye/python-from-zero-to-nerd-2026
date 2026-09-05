# Exercise 38 — Student Grades
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- dictionaries, lists, math

## Prerequisites

- Previous exercises

---

## Objective

Calculate the average grade for each student.

---

## Requirements

```python
def average_grades(grades: dict[str, list[float]]) -> dict[str, float]:
    """Return each student's average grade rounded to 2 decimals."""
```

---

## Examples

```python
average_grades({'Alice': [90.5, 80.0], 'Bob': [70.0, 75.0, 80.0]})  # {'Alice': 85.25, 'Bob': 75.0}
```

---

## Constraints

- Python 3.12+ only
- Round the average to 2 decimal places using `round()`.

---

## Edge Cases

- Empty dictionary
- Student with no grades (should probably return 0.0 or be skipped/handled)
- Student with a single grade

---

## Test Command

```bash
pytest 01_core_python/tests/test_38_student_grades.py -v
```

---

## Hints (use only if stuck)

1. Use a dictionary comprehension or a loop.
2. Calculate the average by dividing the sum of the list by its length.
3. Use the `round(value, 2)` function.

---

## Implementation

```
01_core_python/solutions/38_student_grades.py
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
./scripts/commit_exercise.sh feat core 38_student_grades
```
