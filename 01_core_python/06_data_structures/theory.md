# Data Structures (Lists, Tuples, Sets, Dictionaries)

## 🧠 What is it?

**Data structures** are containers that hold multiple values. Python has four main types:

- **List** `[]` - Ordered, changeable, allows duplicates
- **Tuple** `()` - Ordered, unchangeable, allows duplicates
- **Set** `{}` - Unordered, changeable, NO duplicates
- **Dictionary** `{}` - Key-value pairs, unordered, changeable

## 🤔 Why do we need it?

Single variables can only hold one value. Data structures let you:
- Store multiple related values together
- Organize data efficiently
- Process collections of data

## Lists

### Creating Lists
```python
# Empty list
numbers = []

# List with values
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]  # Can mix types
```

### Accessing Elements
```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])   # apple (first)
print(fruits[-1])  # orange (last)
print(fruits[1:3]) # ["banana", "orange"] (slice)
```

### Modifying Lists
```python
fruits = ["apple", "banana", "orange"]

# Change value
fruits[0] = "grape"

# Add to end
fruits.append("mango")

# Insert at position
fruits.insert(1, "kiwi")

# Remove by value
fruits.remove("banana")

# Remove by index
del fruits[0]

# Remove and return last
last = fruits.pop()
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5]

numbers.sort()           # [1, 1, 3, 4, 5]
numbers.reverse()        # [5, 4, 3, 1, 1]
count = numbers.count(1) # 2
index = numbers.index(4) # 2
numbers.clear()          # []
```

### List Operations
```python
# Concatenation
list1 = [1, 2]
list2 = [3, 4]
result = list1 + list2  # [1, 2, 3, 4]

# Repetition
repeated = [0] * 5      # [0, 0, 0, 0, 0]

# Check membership
if "apple" in fruits:
    print("Found!")

# Length
print(len(fruits))
```

## Tuples

### Creating Tuples
```python
# Empty tuple
empty = ()

# Tuple with values
coordinates = (10, 20)
person = ("Alice", 25, "NYC")

# Single element (needs comma!)
single = (5,)  # ✅
not_tuple = (5)  # ❌ This is just 5
```

### Why Use Tuples?
- **Faster** than lists
- **Protect data** from accidental changes
- Can be used as dictionary keys (lists can't)

```python
# ✅ Tuple works as key
location = (40.7, -74.0)
cities = {location: "New York"}

# ❌ List doesn't work as key
location = [40.7, -74.0]
cities = {location: "New York"}  # Error!
```

### Tuple Operations
```python
coords = (10, 20, 30)

# Access (same as lists)
print(coords[0])   # 10
print(coords[-1])  # 30

# Cannot modify!
coords[0] = 99  # ❌ Error

# Unpacking
x, y, z = coords
print(x)  # 10
```

## Sets

### Creating Sets
```python
# Empty set
empty = set()  # Can't use {} (that's a dict)

# Set with values
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "orange"}
```

### No Duplicates!
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3} - duplicates removed
```

### Set Operations
```python
# Add
fruits.add("mango")

# Remove
fruits.remove("banana")  # Error if not found
fruits.discard("banana") # No error if not found

# Clear all
fruits.clear()
```

### Math Set Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (combine)
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}

# Intersection (common)
print(set1 & set2)  # {3, 4}

# Difference (in set1 but not set2)
print(set1 - set2)  # {1, 2}

# Symmetric difference (in one, not both)
print(set1 ^ set2)  # {1, 2, 5, 6}
```

## Dictionaries

### Creating Dictionaries
```python
# Empty dictionary
empty = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Different types as values
mixed = {
    "name": "Bob",
    "scores": [85, 90, 95],
    "is_active": True
}
```

### Accessing Values
```python
person = {"name": "Alice", "age": 25}

# Get value
print(person["name"])  # Alice

# Safe get (no error if missing)
print(person.get("age"))      # 25
print(person.get("country"))  # None
print(person.get("country", "USA"))  # USA (default)
```

### Modifying Dictionaries
```python
person = {"name": "Alice"}

# Add/update
person["age"] = 25
person["city"] = "NYC"

# Remove
del person["city"]

# Remove and return
age = person.pop("age")

# Clear all
person.clear()
```

### Dictionary Methods
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Get all keys
keys = person.keys()     # dict_keys(['name', 'age', 'city'])

# Get all values
values = person.values() # dict_values(['Alice', 25, 'NYC'])

# Get key-value pairs
items = person.items()   # dict_items([('name', 'Alice'), ...])
```

### Looping Through Dictionaries
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Loop keys
for key in person:
    print(key)

# Loop values
for value in person.values():
    print(value)

# Loop both
for key, value in person.items():
    print(f"{key}: {value}")
```

## 🌍 Real-world use

### 1. Shopping Cart (List)
```python
cart = []
cart.append({"name": "Laptop", "price": 999})
cart.append({"name": "Mouse", "price": 25})

total = sum(item["price"] for item in cart)
```

### 2. GPS Coordinates (Tuple)
```python
new_york = (40.7128, -74.0060)
london = (51.5074, -0.1278)
# Coordinates don't change, so tuple is perfect
```

### 3. Remove Duplicates (Set)
```python
emails = ["a@a.com", "b@b.com", "a@a.com", "c@c.com"]
unique_emails = set(emails)
# {"a@a.com", "b@b.com", "c@c.com"}
```

### 4. User Profile (Dictionary)
```python
user = {
    "id": 12345,
    "username": "alice",
    "email": "alice@example.com",
    "is_premium": True,
    "followers": 1250
}
```

## ⚠️ Common Mistakes

### Mistake 1: Modifying list while iterating
```python
# ❌ Causes bugs
numbers = [1, 2, 3, 4]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

# ✅ Create new list
numbers = [n for n in numbers if n % 2 != 0]
```

### Mistake 2: Using list as dictionary key
```python
# ❌ Error - list is mutable
key = [1, 2]
d = {key: "value"}

# ✅ Use tuple
key = (1, 2)
d = {key: "value"}
```

### Mistake 3: Forgetting get() can return None
```python
person = {"name": "Alice"}

# ❌ Might crash
city = person.get("city")
print(city.upper())  # Error if None!

# ✅ Check first or use default
city = person.get("city", "Unknown")
```

### Mistake 4: Expecting set to be ordered
```python
numbers = {3, 1, 4, 1, 5}
print(numbers)  # Order not guaranteed!
```

## 🧠 Remember

**Lists `[]`:**
- Use when order matters
- Use when you need to change values
- Can have duplicates

**Tuples `()`:**
- Use when data shouldn't change
- Faster than lists
- Can be dictionary keys

**Sets `{}`:**
- Automatically removes duplicates
- Fast membership testing
- Unordered

**Dictionaries `{}`:**
- Store key-value pairs
- Fast lookups by key
- Keys must be immutable (strings, numbers, tuples)

---

## Choosing the Right Structure

```python
# List - ordered collection
shopping_list = ["milk", "bread", "eggs"]

# Tuple - fixed data
rgb_color = (255, 128, 0)

# Set - unique values
unique_visitors = {"user1", "user2", "user1"}  # {"user1", "user2"}

# Dictionary - key-value mapping
settings = {"theme": "dark", "notifications": True}
```

## Nested Structures

```python
# List of dictionaries (common in APIs)
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# Dictionary of lists
courses = {
    "math": ["algebra", "calculus"],
    "science": ["physics", "chemistry"]
}

# Access nested data
print(users[0]["name"])      # Alice
print(courses["math"][0])    # algebra
```
