# Exercise 86 — Class vs Instance Attributes

**Phase:** `01_core_python`  
**Type:** concept  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q25  
**Status:** 🔴 Not started

## Concepts

- classes, class attributes, instance attributes, __init__, self

## Prerequisites

- Basic OOP knowledge

---

## Objective

Understand the difference between class-level and instance-level attributes.

---

## Requirements

```python
class Person:
    """Demonstrate class vs instance attributes."""
    
    # Class attribute (shared by all instances)
    species = "Human"
    
    def __init__(self, name: str | None = None):
        """
        Initialize with optional name.
        
        Args:
            name: Person's name (instance attribute)
        """
        self.name = name  # Instance attribute (unique per instance)
```

Also implement:

```python
def demonstrate_attributes() -> dict[str, str]:
    """
    Create two Person instances and return their attributes.
    
    Returns:
        Dictionary showing class attribute vs instance attributes
    """
```

---

## Examples

```python
person1 = Person("Alice")
person1.species  # "Human" (class attribute)
person1.name     # "Alice" (instance attribute)

person2 = Person("Bob")
person2.species  # "Human" (same class attribute)
person2.name     # "Bob" (different instance attribute)

Person.species   # "Human" (accessing via class)
```

---

## Constraints

- Define `species` as a class attribute (outside __init__)
- Define `name` as an instance attribute (inside __init__)
- Support None as default name

---

## Test Command

```bash
pytest 01_core_python/tests/test_86_class_vs_instance_attributes.py -v
```

---

## Hints (use only if stuck)

1. Class attribute: defined directly in class body
2. Instance attribute: defined with `self.` in __init__
3. Access class attribute via instance or class name

---

## Implementation

```
01_core_python/solutions/86_class_vs_instance_attributes.py
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
./scripts/commit_exercise.sh feat core 86_class_vs_instance_attributes
```
