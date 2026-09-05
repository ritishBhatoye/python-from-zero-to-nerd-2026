# Functions

## 🧠 What is it?

A **function** is a reusable block of code that performs a specific task. You define it once and use it many times.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

## 🤔 Why do we need it?

- Avoid repeating code
- Organize code into logical pieces
- Make code easier to test and debug
- Share code between programs

## 💻 Simple Example

```python
# Define function
def add_numbers(a, b):
    result = a + b
    return result

# Use function
total = add_numbers(5, 3)
print(total)  # 8
```

## Creating Functions

### Basic Syntax
```python
def function_name(parameters):
    # Code here
    return value
```

### Function with No Parameters
```python
def say_hello():
    print("Hello!")

say_hello()  # Hello!
```

### Function with Parameters
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
```

### Function with Return Value
```python
def square(x):
    return x ** 2

result = square(5)  # 25
```

### Function with Multiple Parameters
```python
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)  # 15
```

### Function with Multiple Return Values
```python
def get_user():
    name = "Alice"
    age = 25
    return name, age  # Returns tuple

name, age = get_user()
```

## Default Parameters

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())         # Hello, Guest!
print(greet("Alice"))  # Hello, Alice!
```

## Keyword Arguments

```python
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}")

describe_pet("Buddy")                    # Buddy is a dog
describe_pet("Whiskers", animal="cat")   # Whiskers is a cat
describe_pet(animal="cat", name="Felix") # Felix is a cat
```

## Variable-Length Arguments

### *args - Variable positional arguments
```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

### **kwargs - Variable keyword arguments
```python
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC
```

## Docstrings

Document what your function does:

```python
def calculate_tax(amount, rate=0.1):
    """
    Calculate tax on an amount.
    
    Args:
        amount: The base amount
        rate: Tax rate (default 0.1 = 10%)
    
    Returns:
        The calculated tax
    """
    return amount * rate

# View documentation
help(calculate_tax)
```

## Lambda Functions

Small, anonymous functions:

```python
# Normal function
def square(x):
    return x ** 2

# Lambda (one-liner)
square = lambda x: x ** 2

print(square(5))  # 25

# Often used with map, filter
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16]
```

## 🌍 Real-world use

### 1. Validate Email
```python
def is_valid_email(email):
    return "@" in email and "." in email

if is_valid_email("user@example.com"):
    print("Valid")
```

### 2. Calculate Discount
```python
def apply_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

final_price = apply_discount(100, 20)  # $80
```

### 3. Format Currency
```python
def format_currency(amount):
    return f"${amount:,.2f}"

print(format_currency(1234.5))  # $1,234.50
```

## ⚠️ Common Mistakes

### Mistake 1: Forgetting return
```python
def add(a, b):
    a + b  # ❌ No return!

result = add(2, 3)
print(result)  # None

# ✅ Fix
def add(a, b):
    return a + b
```

### Mistake 2: Mutable default arguments
```python
# ❌ Bug! List shared across calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Unexpected!

# ✅ Fix
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Mistake 3: Not using functions enough
```python
# ❌ Repeating code
price1 = 100 * 0.9
price2 = 200 * 0.9
price3 = 150 * 0.9

# ✅ Use function
def apply_discount(price):
    return price * 0.9

price1 = apply_discount(100)
price2 = apply_discount(200)
price3 = apply_discount(150)
```

## 🧠 Remember

- Functions reduce code repetition
- Use descriptive names: `calculate_total()` not `calc()`
- Return values instead of printing when possible
- Add docstrings for complex functions
- Keep functions focused on one task

---

## Advanced: Scope

Variables inside functions are **local**:

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # 10
print(x)       # ❌ Error - x doesn't exist here

# Global variables
y = 20

def show():
    print(y)  # ✅ Can read global

show()  # 20
```

## First-Class Functions

Functions are objects - can be passed around:

```python
def greet():
    return "Hello!"

# Assign to variable
say_hi = greet
print(say_hi())  # Hello!

# Pass as argument
def call_function(func):
    return func()

print(call_function(greet))  # Hello!
```

This enables powerful patterns like decorators!
