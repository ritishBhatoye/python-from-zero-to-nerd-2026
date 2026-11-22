# Exercise 051 — Class Inheritance

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

## Concepts
- Object-Oriented Programming (OOP)
- Class Inheritance
- Parent and Child Classes
- Constructors (`__init__`)
- Method Inheritance
- Method Overriding

## Prerequisites
- Python classes and objects
- Instance methods
- Constructors
- Basic OOP concepts

---

## Objective

Create a parent class named `American` and a child class named `NewYorker` that inherits from `American`.

The exercise is designed to help you understand how inheritance allows a child class to reuse the properties and methods of its parent class.

## Requirements

1. Define a parent class named `American`.
2. Define a child class named `NewYorker` that inherits from `American`.
3. The `American` class must have a constructor that accepts a person's name.
4. Store the name as an instance attribute.
5. Implement a `get_name()` method in the parent class that returns the person's name.
6. The `NewYorker` class must inherit the constructor and `get_name()` method without duplicating their implementation.
7. Create an instance of `NewYorker` and verify that it can access the inherited method.

**Important:** Do not implement the same functionality twice. The purpose is to demonstrate inheritance.

---

## Examples

**Example 1:**

```python
person = American("John")
print(person.get_name())

# Output:
John
```

**Example 2:**

```python
person = NewYorker("David")
print(person.get_name())

# Output:
David
```

**Example 3:**

```python
person1 = NewYorker("Alice")
person2 = NewYorker("Robert")

print(person1.get_name())
print(person2.get_name())

# Output:
Alice
Robert
```

---

## Hints (use only if stuck)

1. Python supports inheritance through parentheses after a class name.
2. A child class can inherit methods from its parent class.
3. You don't need to redefine an inherited constructor if the child class doesn't require additional initialization.
4. Test both parent and child classes independently.

---

## Test Command

```bash
pytest 01_core_python/level_3_advanced/tests/test_051_class_inheritance.py -v
```

---

## Implementation

`01_core_python/level_3_advanced/solutions/051_class_inheritance.py`

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
