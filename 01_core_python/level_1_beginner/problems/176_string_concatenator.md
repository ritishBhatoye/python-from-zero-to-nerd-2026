# Exercise 82 — String Concatenator

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q30  
**Status:** 🔴 Not started

## Concepts

- string concatenation, + operator, functions

## Prerequisites

- Basic string knowledge

---

## Objective

Concatenate two strings and return the result.

---

## Requirements

```python
def concatenate_strings(s1: str, s2: str) -> str:
    """
    Concatenate two strings.
    
    Args:
        s1: First string
        s2: Second string
    
    Returns:
        Concatenated string
    """
```

---

## Examples

```python
concatenate_strings("3", "4")
# "34"

concatenate_strings("hello", "world")
# "helloworld"

concatenate_strings("Python", "3")
# "Python3"
```

---

## Constraints

- Use the + operator for concatenation
- Return the concatenated result
- No spaces added between strings

---

## Edge Cases

- Empty strings: concatenate_strings("", "hello") returns "hello"
- Both empty: concatenate_strings("", "") returns ""

---

## Test Command

```bash
pytest 01_core_python/tests/test_82_string_concatenator.py -v
```

---

## Hints (use only if stuck)

1. Use + operator: `s1 + s2`
2. Return the result directly
3. One-liner function

---

## Implementation

```
01_core_python/solutions/82_string_concatenator.py
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
./scripts/commit_exercise.sh feat core 82_string_concatenator
```
