# Exercise 67 — CSV Reader
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- File I/O, String parsing, Dictionaries

## Prerequisites

- Previous exercises

---

## Objective

Manually parse a simple CSV file into a list of dictionaries.

---

## Requirements

```python
def read_csv_data(filepath: str) -> list[dict[str, str]]:
    """
    Reads a CSV file where the first row contains headers.
    Returns a list of dictionaries, one for each data row.
    Do NOT use the built-in csv module.
    """
```

---

## Examples

```python
# data.csv content:
# name,age
# Alice,30
# Bob,25

read_csv_data('data.csv') 
# [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified. DO NOT use the `csv` module.

---

## Edge Cases

- File with only headers (returns empty list)
- Empty values (e.g. `Alice,,30`)

---

## Test Command

```bash
pytest 01_core_python/tests/test_67_csv_reader.py -v
```

---

## Hints (use only if stuck)

1. Read all lines and `strip()` them.
2. The first line contains the headers (split by `,`).
3. Zip headers with each subsequent line's split values.

---

## Implementation

```
01_core_python/solutions/67_csv_reader.py
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
./scripts/commit_exercise.sh feat core 67_csv_reader
```
