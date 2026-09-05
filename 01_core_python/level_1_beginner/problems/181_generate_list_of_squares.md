# Exercise 87 — Generate List of Squares

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q37  
**Status:** 🔴 Not started

## Concepts

- lists, loops, append, exponentiation, range

## Prerequisites

- Basic list and loop knowledge

---

## Objective

Generate a list containing squares of numbers from 1 to 20.

---

## Requirements

```python
def generate_squares_list(n: int = 20) -> list[int]:
    """
    Generate list of squares from 1 to n.
    
    Args:
        n: Upper limit (default 20)
    
    Returns:
        List of squares [1, 4, 9, 16, ..., n²]
    """
```

---

## Examples

```python
generate_squares_list(20)
# [1, 4, 9, 16, 25, ..., 400]

generate_squares_list(5)
# [1, 4, 9, 16, 25]

generate_squares_list(3)
# [1, 4, 9]
```

---

## Constraints

- Use a loop and list.append() OR list comprehension
- Include both 1 and n in the range
- Return a list of integers

---

## Test Command

```bash
pytest 01_core_python/tests/test_87_generate_list_of_squares.py -v
```

---

## Hints (use only if stuck)

1. Loop approach: `for i in range(1, n+1): li.append(i**2)`
2. List comprehension: `[i**2 for i in range(1, n+1)]`
3. Use ** operator for squaring

---

## Implementation

```
01_core_python/solutions/87_generate_list_of_squares.py
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
./scripts/commit_exercise.sh feat core 87_generate_list_of_squares
```
