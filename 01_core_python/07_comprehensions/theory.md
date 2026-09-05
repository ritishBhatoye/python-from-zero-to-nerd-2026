# Comprehensions

## 🧠 What is it?

**Comprehensions** are a short way to create lists, sets, and dictionaries. Instead of writing loops, you write one line.

```python
# Normal way
squares = []
for i in range(5):
    squares.append(i ** 2)

# Comprehension way
squares = [i ** 2 for i in range(5)]
```

Both give: `[0, 1, 4, 9, 16]`

## 🤔 Why do we need it?

- Write less code
- Faster to write
- Often faster to run
- More readable (once you learn it)

## List Comprehensions

### Basic Syntax
```python
[expression for item in iterable]
```

### Examples
```python
# Square numbers
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Convert to uppercase
words = ["hello", "world"]
upper = [word.upper() for word in words]
# ["HELLO", "WORLD"]

# Get lengths
names = ["Alice", "Bob", "Charlie"]
lengths = [len(name) for name in names]
# [5, 3, 7]
```

### With Conditions (if)
```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Only positive numbers
numbers = [-2, -1, 0, 1, 2]
positive = [x for x in numbers if x > 0]
# [1, 2]

# Filter and transform
numbers = [1, 2, 3, 4, 5]
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]
# [4, 8]
```

### With if-else
```python
# Label numbers as even/odd
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ["even", "odd", "even", "odd", "even"]

# Replace negative with zero
numbers = [-2, 3, -1, 5]
fixed = [x if x >= 0 else 0 for x in numbers]
# [0, 3, 0, 5]
```

### Nested Comprehensions
```python
# Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]

# Create pairs
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

## Dictionary Comprehensions

### Basic Syntax
```python
{key: value for item in iterable}
```

### Examples
```python
# Square numbers
squares = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Swap keys and values
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}
# {1: "a", 2: "b"}

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = {k: v for k, v in zip(keys, values)}
# {"name": "Alice", "age": 25, "city": "NYC"}
```

### With Conditions
```python
# Only items with even values
data = {"a": 1, "b": 2, "c": 3, "d": 4}
evens = {k: v for k, v in data.items() if v % 2 == 0}
# {"b": 2, "d": 4}
```

## Set Comprehensions

### Basic Syntax
```python
{expression for item in iterable}
```

### Examples
```python
# Unique squares
squares = {x ** 2 for x in [1, -1, 2, -2]}
# {1, 4}  (duplicates removed)

# Unique first letters
words = ["apple", "apricot", "banana", "blueberry"]
first_letters = {word[0] for word in words}
# {'a', 'b'}
```

## 🌍 Real-world use

### 1. Process API Data
```python
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]

# Get adults only
adults = [u["name"] for u in users if u["age"] >= 18]
# ["Alice", "Charlie"]
```

### 2. Clean User Input
```python
inputs = ["  Hello  ", "WORLD  ", " python"]
cleaned = [s.strip().lower() for s in inputs]
# ["hello", "world", "python"]
```

### 3. Create Lookup Dictionary
```python
products = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mouse"}
]

lookup = {p["id"]: p["name"] for p in products}
# {1: "Laptop", 2: "Mouse"}
```

### 4. Filter Files
```python
files = ["doc.txt", "image.png", "data.csv", "photo.jpg"]
images = [f for f in files if f.endswith(('.png', '.jpg'))]
# ["image.png", "photo.jpg"]
```

## ⚠️ Common Mistakes

### Mistake 1: Too complex comprehensions
```python
# ❌ Hard to read
result = [x * 2 if x > 0 else x * 3 if x < 0 else 0 for x in nums if x != 5]

# ✅ Use normal loop for complex logic
result = []
for x in nums:
    if x != 5:
        if x > 0:
            result.append(x * 2)
        elif x < 0:
            result.append(x * 3)
        else:
            result.append(0)
```

### Mistake 2: Modifying list being iterated
```python
# ❌ Don't do this
numbers = [1, 2, 3]
numbers = [numbers.append(x * 2) for x in numbers]  # Confusing!

# ✅ Create new list
numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]
```

### Mistake 3: Forgetting parentheses in tuples
```python
# ❌ Syntax error
pairs = [x, y for x in [1, 2] for y in ['a', 'b']]

# ✅ Use parentheses
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
```

## 🧠 Remember

- List comprehension: `[expr for item in items]`
- Add condition: `[expr for item in items if condition]`
- Dict comprehension: `{key: value for item in items}`
- Set comprehension: `{expr for item in items}`
- Keep it simple - if too complex, use normal loops

---

## When to Use vs Not Use

### ✅ Use Comprehensions:
- Simple transformations
- Filtering
- Creating new collections from existing ones

### ❌ Don't Use Comprehensions:
- Complex logic with multiple conditions
- Need to modify items during iteration
- Side effects (printing, file writing, etc.)

```python
# ❌ Don't use for side effects
[print(x) for x in items]  # Works but wrong

# ✅ Use normal loop
for x in items:
    print(x)
```

## Generator Expressions

Similar to comprehensions but use `()` instead of `[]`. They generate values one at a time (lazy evaluation), saving memory:

```python
# List comprehension - creates full list
squares_list = [x ** 2 for x in range(1000000)]  # Uses lots of memory

# Generator expression - creates values on demand
squares_gen = (x ** 2 for x in range(1000000))   # Uses little memory

# Use in loop
for square in squares_gen:
    print(square)
```

Perfect for large datasets!
