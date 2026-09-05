<Exercise 29 — Flatten Nested List>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Lists
- Type checking (`isinstance`)
- Iteration

## Prerequisites

- Previous exercises

---

## Objective

Flatten exactly one level of nesting in a list.

---

## Requirements

```python
def flatten(nested: list) -> list:
    """Flatten one level of nesting in a list."""
```

---

## Examples

```python
flatten([[1, 2], [3, [4]]])  # [1, 2, 3, [4]]
flatten([1, [2, 3], 4])      # [1, 2, 3, 4]
```

---

## Constraints

- Python 3.12+ only
- No external imports
- Should only flatten one level deep (e.g. nested lists within nested lists are kept as lists)

---

## Edge Cases

- Empty list
- List with no nested lists
- List with all nested lists

---

## Test Command

```bash
pytest 01_core_python/tests/test_29_flatten_list.py -v
```

---

## Hints (use only if stuck)

1. Iterate over the elements of the list.
2. Check if an element is a list using `isinstance(item, list)`.
3. If it's a list, extend the result list with its elements. If it's not a list, just append it.

---

## Implementation

```
01_core_python/solutions/29_flatten_list.py
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
./scripts/commit_exercise.sh feat core 29_flatten_list
```
