# Exercise 71 — String to List and Tuple Converter

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q4  
**Status:** 🔴 Not started

## Concepts

- strings, lists, tuples, type conversion, split method

## Prerequisites

- Basic Python syntax

---

## Objective

Learn how to convert comma-separated string input into both list and tuple data structures.

---

## Requirements

```python
def parse_to_list_and_tuple(input_string: str) -> tuple[list[str], tuple[str, ...]]:
    """
    Accept a comma-separated string and return both a list and tuple of the values.
    
    Args:
        input_string: Comma-separated values (e.g., "34,67,55,33,12,98")
    
    Returns:
        A tuple containing (list_of_values, tuple_of_values)
    """
```

---

## Examples

```python
parse_to_list_and_tuple("34,67,55,33,12,98")
# (['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98'))

parse_to_list_and_tuple("apple,banana,cherry")
# (['apple', 'banana', 'cherry'], ('apple', 'banana', 'cherry'))

parse_to_list_and_tuple("10")
# (['10'], ('10',))
```

---

## Constraints

- Use `str.split()` method
- Use `tuple()` constructor for conversion
- Return values as strings (don't convert to int)

---

## Edge Cases

- Single value (no commas) should return list and tuple with one element
- Empty string should return empty list and tuple

---

## Test Command

```bash
pytest 01_core_python/tests/test_71_string_list_tuple_converter.py -v
```

---

## Hints (use only if stuck)

1. Use `.split(',')` to break the string into parts
2. Convert the list to tuple using `tuple(your_list)`
3. Return both as a tuple: `(list_result, tuple_result)`

---

## Implementation

```
01_core_python/solutions/71_string_list_tuple_converter.py
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
./scripts/commit_exercise.sh feat core 71_string_list_tuple_converter
```
