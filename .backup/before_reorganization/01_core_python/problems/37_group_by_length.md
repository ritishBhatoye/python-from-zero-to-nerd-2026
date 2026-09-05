# Exercise 37 — Group By Length
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- dictionaries, collections

## Prerequisites

- Previous exercises

---

## Objective

Group words by their length.

---

## Requirements

```python
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words by their length into a dictionary."""
```

---

## Examples

```python
group_by_length(['hi', 'hey', 'oh'])  # {2: ['hi', 'oh'], 3: ['hey']}
```

---

## Constraints

- Python 3.12+ only
- Elements in the resulting lists should be in the same order as in the original list.

---

## Edge Cases

- Empty list
- List with words of the same length
- List with words of all different lengths

---

## Test Command

```bash
pytest 01_core_python/tests/test_37_group_by_length.py -v
```

---

## Hints (use only if stuck)

1. Iterate over the words, check their length.
2. If the length is not a key in the dictionary, add it with an empty list.
3. Append the word to the list for that length.

---

## Implementation

```
01_core_python/solutions/37_group_by_length.py
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
./scripts/commit_exercise.sh feat core 37_group_by_length
```
