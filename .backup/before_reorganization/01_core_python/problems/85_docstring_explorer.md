# Exercise 85 — Docstring Explorer

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q24  
**Status:** 🔴 Not started

## Concepts

- docstrings, __doc__ attribute, documentation, function documentation

## Prerequisites

- Basic function knowledge

---

## Objective

Create a function with proper docstring and demonstrate accessing built-in documentation.

---

## Requirements

```python
def square_with_doc(num: int) -> int:
    """
    Return the square value of the input number.
    
    The input number must be integer.
    
    Args:
        num: The number to square
    
    Returns:
        The square of num (num ** 2)
    
    Example:
        >>> square_with_doc(5)
        25
    """
```

Also implement:

```python
def get_builtin_docs() -> dict[str, str]:
    """
    Return documentation for abs, int, and input built-in functions.
    
    Returns:
        Dictionary with function names as keys and their __doc__ as values
    """
```

---

## Examples

```python
square_with_doc(5)
# 25

square_with_doc.__doc__
# Returns the docstring

get_builtin_docs()
# {'abs': 'Return the absolute value...', 'int': 'int([x]) -> integer...', ...}
```

---

## Constraints

- Use proper docstring format (triple quotes)
- Access __doc__ attribute to get documentation
- Include Args, Returns, and Example sections

---

## Test Command

```bash
pytest 01_core_python/tests/test_85_docstring_explorer.py -v
```

---

## Hints (use only if stuck)

1. Docstring goes right after function definition
2. Access built-in docs: `abs.__doc__`
3. Return a dictionary with function names and their docs

---

## Implementation

```
01_core_python/solutions/85_docstring_explorer.py
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
./scripts/commit_exercise.sh feat core 85_docstring_explorer
```
