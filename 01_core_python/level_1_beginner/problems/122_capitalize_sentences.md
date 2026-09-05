<Exercise 22 — Capitalize Sentences>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q9 (improved)  
**Status:** 🔴 Not started

## Concepts

- Lists, Strings, Uppercase

## Prerequisites

- Previous exercises

---

## Objective

Given a list of strings, return a new list where each string is fully uppercased.

---

## Requirements

```python
def capitalize_lines(lines: list[str]) -> list[str]:
    """Return a new list with all strings uppercased."""
```

---

## Examples

```python
capitalize_lines(["hello world", "practice makes perfect"])  
# ["HELLO WORLD", "PRACTICE MAKES PERFECT"]
```

---

## Constraints

- Python 3.12+ only
- Do not modify the original list (return a new one)

---

## Edge Cases

- Empty list
- List with empty strings
- List with strings already uppercased
- List with strings containing numbers or punctuation

---

## Test Command

```bash
pytest 01_core_python/tests/test_22_capitalize_sentences.py -v
```

---

## Hints (use only if stuck)

1. Use a list comprehension or a for loop with `.upper()`.

---

## Implementation

```
01_core_python/solutions/22_capitalize_sentences.py
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
./scripts/commit_exercise.sh feat core 22_capitalize_sentences
```
