# Exercise 83 — Longer String Selector

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q31  
**Status:** 🔴 Not started

## Concepts

- string length, len() function, conditionals, comparison

## Prerequisites

- Basic conditionals

---

## Objective

Compare two strings and return the longer one, or both if equal length.

---

## Requirements

```python
def select_longer_string(s1: str, s2: str) -> str | list[str]:
    """
    Return the longer string. If equal length, return both as a list.
    
    Args:
        s1: First string
        s2: Second string
    
    Returns:
        The longer string, or list [s1, s2] if equal length
    """
```

---

## Examples

```python
select_longer_string("one", "three")
# "three"  # length 5 > length 3

select_longer_string("hello", "hi")
# "hello"  # length 5 > length 2

select_longer_string("cat", "dog")
# ["cat", "dog"]  # both length 3
```

---

## Constraints

- Use `len()` to get string length
- If equal length, return list with both strings
- Preserve original order in list [s1, s2]

---

## Edge Cases

- Empty strings: select_longer_string("", "hello") returns "hello"
- Both empty: select_longer_string("", "") returns ["", ""]

---

## Test Command

```bash
pytest 01_core_python/tests/test_83_longer_string_printer.py -v
```

---

## Hints (use only if stuck)

1. Get lengths: `len1 = len(s1)`, `len2 = len(s2)`
2. Use if/elif/else to compare
3. Equal case: `return [s1, s2]`

---

## Implementation

```
01_core_python/solutions/83_longer_string_printer.py
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
./scripts/commit_exercise.sh feat core 83_longer_string_printer
```
