<Exercise 14 — Comma Separated to Collection>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner
**Inspired by:** zhiwehu Q4 (improved)
**Status:** 🔴 Not started

## Concepts

- string splitting, lists, tuples, type conversion

## Prerequisites

- None

---

## Objective

Convert a comma-separated string of items into a list and a tuple.

---

## Requirements

```python
def parse_csv_numbers(text: str) -> tuple[list[str], tuple[str, ...]]:
    """Split comma-separated text into a list and a tuple, stripping whitespace."""
```

---

## Examples

```python
parse_csv_numbers("34,67,55,33,12,98")  # (['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98'))
```

---

## Constraints

- Python 3.12+ only
- Handle arbitrary whitespace around the items

---

## Edge Cases

- Empty string
- String with only commas
- Spaces around values

---

## Test Command

```bash
pytest 01_core_python/tests/test_14_comma_separated_to_collection.py -v
```

---

## Hints (use only if stuck)

1. Use the `split()` method on strings.
2. Strip whitespace using `.strip()` for each element.

---

## Implementation

```
01_core_python/solutions/14_comma_separated_to_collection.py
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
./scripts/commit_exercise.sh feat core 14_comma_separated_to_collection
```
