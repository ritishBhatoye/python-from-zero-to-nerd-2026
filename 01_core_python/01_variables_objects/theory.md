# Variables and Objects

## 🧠 What is it?

A **variable** is a name that points to a value stored in computer memory. In Python, everything you work with (numbers, text, lists) is an **object**.

Think of a variable like a label on a box. The label is the variable name, and the box contains the actual data (object).

## 🤔 Why do we need it?

Without variables, you can't save data to use later. You need variables to:
- Store user input
- Remember calculation results
- Keep data while your program runs

## 💻 Simple Example

```python
# Create variables
name = "Alice"
age = 25
is_student = True

# Use them
print(name)  # Alice
print(age)   # 25
```

## 🔍 How it works

1. `name = "Alice"` - Creates a text object `"Alice"` and makes `name` point to it
2. `age = 25` - Creates a number object `25` and makes `age` point to it
3. Python remembers these so you can use them later

**Important:** In Python, variables don't contain values - they point to objects.

```python
x = 10
y = x  # Both point to the same object
```

## 🌍 Real-world use

1. **Web forms** - Store username and password when user logs in
2. **Shopping cart** - Keep track of items and total price
3. **Game** - Save player score and level

## Variables Rules

### Valid names:
```python
user_name = "Bob"      # ✅ Good
age2 = 30              # ✅ Numbers allowed (not at start)
_private = "secret"    # ✅ Underscore allowed
```

### Invalid names:
```python
2age = 30              # ❌ Can't start with number
user-name = "Bob"      # ❌ No hyphens
class = "Math"         # ❌ Can't use Python keywords
```

## Python Objects - Key Concepts

### Everything is an Object

```python
x = 5
print(type(x))  # <class 'int'>

name = "Python"
print(type(name))  # <class 'str'>
```

Every object has:
- **Type** - What kind of object (int, str, list, etc.)
- **Value** - The actual data
- **Identity** - Unique ID in memory

### Mutable vs Immutable

**Mutable** means you can change the object after creating it.
**Immutable** means you cannot change it.

```python
# Mutable - can change
my_list = [1, 2, 3]
my_list[0] = 99      # ✅ Works
print(my_list)       # [99, 2, 3]

# Immutable - cannot change
my_text = "hello"
my_text[0] = "H"     # ❌ Error!
```

**Immutable types:** int, float, str, tuple, bool
**Mutable types:** list, dict, set

### Multiple Assignment

```python
# Same value to multiple variables
x = y = z = 0

# Multiple variables at once
name, age, city = "Bob", 25, "NYC"
```

### Reassignment

Variables can point to different objects:

```python
x = 10        # x points to 10
x = "hello"   # Now x points to "hello"
x = [1, 2]    # Now x points to a list
```

## ⚠️ Common Mistakes

### Mistake 1: Using before defining
```python
print(score)  # ❌ Error - score not defined yet
score = 100   # Define it first
```

### Mistake 2: Confusing variable with string
```python
name = "Alice"
print(name)    # ✅ Prints: Alice
print("name")  # ✅ Prints: name (the word itself)
```

### Mistake 3: Thinking variables copy values
```python
list1 = [1, 2, 3]
list2 = list1           # Both point to SAME list
list2.append(4)
print(list1)            # [1, 2, 3, 4] - Changed!
```

To actually copy:
```python
list2 = list1.copy()    # Now they're separate
```

## 🧠 Remember

- Variables are names that point to objects
- Everything in Python is an object
- Some objects can be changed (mutable), others cannot (immutable)
- Use clear, descriptive variable names
- Python figures out the type automatically - no need to declare it

---

## Deep Dive: Object Identity

Every object has a unique ID in memory:

```python
x = 1000
y = 1000
print(id(x))  # Memory address
print(id(y))  # Different address

print(x is y)  # False - different objects
print(x == y)  # True - same value
```

**Small integer optimization:** Python reuses objects for small integers (-5 to 256):

```python
a = 5
b = 5
print(a is b)  # True - same object in memory
```

This is for performance, but you rarely need to worry about it.
