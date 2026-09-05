# Exercise 84 — Input Output Class

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q5  
**Status:** 🔴 Not started

## Concepts

- classes, __init__, methods, string methods, user input simulation

## Prerequisites

- Basic OOP knowledge

---

## Objective

Create a class that stores a string and provides methods to get and print it in uppercase.

---

## Requirements

```python
class InputOutputString:
    """A class that stores and manipulates a string."""
    
    def __init__(self):
        """Initialize with empty string."""
    
    def get_string(self, input_string: str) -> None:
        """Store the provided string."""
    
    def print_string(self) -> str:
        """Return the stored string in uppercase."""
```

---

## Examples

```python
obj = InputOutputString()
obj.get_string("Hello World")
result = obj.print_string()
# result: "HELLO WORLD"

obj2 = InputOutputString()
obj2.get_string("python")
result2 = obj2.print_string()
# result2: "PYTHON"
```

---

## Constraints

- Use `__init__` to initialize the string attribute
- Store the string in an instance variable
- Use `.upper()` method for uppercase conversion

---

## Edge Cases

- Empty string: returns ""
- Already uppercase: returns unchanged
- Mixed case: converts to uppercase

---

## Test Command

```bash
pytest 01_core_python/tests/test_84_input_output_class.py -v
```

---

## Hints (use only if stuck)

1. Initialize: `self.s = ""`
2. Store in get_string: `self.s = input_string`
3. Return uppercase: `return self.s.upper()`

---

## Implementation

```
01_core_python/solutions/84_input_output_class.py
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
./scripts/commit_exercise.sh feat core 84_input_output_class
```
