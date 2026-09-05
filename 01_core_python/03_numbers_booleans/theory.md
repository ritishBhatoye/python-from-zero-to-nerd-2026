# Numbers and Booleans

## 🧠 What is it?

**Numbers** are used for calculations and counting. Python has three main number types:
- **int** - Whole numbers (1, 42, -5)
- **float** - Decimal numbers (3.14, -0.5)
- **complex** - For advanced math (rarely used)

**Booleans** are True/False values used for logic and decisions.

## 🤔 Why do we need it?

Numbers:
- Calculate prices, scores, ages
- Count items
- Measure time, distance, temperature

Booleans:
- Make decisions (if user is logged in...)
- Check conditions (if age >= 18...)
- Control program flow

## 💻 Simple Example

```python
# Numbers
age = 25
price = 19.99
temperature = -5

# Math
total = price * 2
print(total)  # 39.98

# Booleans
is_adult = age >= 18
print(is_adult)  # True
```

## 🔍 How it works

### Integers (int)
Whole numbers with no decimal point.

```python
x = 10
y = -5
big = 1000000000  # Can be as large as memory allows
```

### Floats (float)
Numbers with decimal points.

```python
price = 9.99
pi = 3.14159
tiny = 0.0001
```

**Warning:** Floats are not always exact!
```python
print(0.1 + 0.2)  # 0.30000000000000004 (!)
```

### Booleans (bool)
Only two values: `True` or `False`

```python
is_sunny = True
is_raining = False
```

## Math Operations

### Basic Operations
```python
# Addition
print(10 + 5)   # 15

# Subtraction
print(10 - 5)   # 5

# Multiplication
print(10 * 5)   # 50

# Division (always gives float)
print(10 / 3)   # 3.3333...

# Floor division (removes decimal)
print(10 // 3)  # 3

# Remainder (modulo)
print(10 % 3)   # 1

# Power
print(2 ** 3)   # 8 (2×2×2)
```

### Order of Operations
Python follows PEMDAS (like math class):
```python
result = 2 + 3 * 4     # 14 (not 20)
result = (2 + 3) * 4   # 20 (parentheses first)
```

### Compound Assignment
```python
x = 10
x += 5   # Same as: x = x + 5
print(x) # 15

x *= 2   # Same as: x = x * 2
print(x) # 30
```

## Comparison Operators

Returns `True` or `False`:

```python
x = 10
y = 5

print(x == y)  # False (equal?)
print(x != y)  # True  (not equal?)
print(x > y)   # True  (greater than?)
print(x < y)   # False (less than?)
print(x >= 10) # True  (greater or equal?)
print(x <= 5)  # False (less or equal?)
```

## Logical Operators

Combine boolean values:

```python
age = 25
has_license = True

# AND - both must be True
can_drive = age >= 18 and has_license
print(can_drive)  # True

# OR - at least one must be True
is_allowed = age >= 18 or has_license
print(is_allowed)  # True

# NOT - flips the value
is_child = not (age >= 18)
print(is_child)  # False
```

### Truth Table
```python
True and True   # True
True and False  # False
False and False # False

True or True    # True
True or False   # True
False or False  # False

not True        # False
not False       # True
```

## Type Conversion

```python
# String to number
age = int("25")      # 25
price = float("9.99") # 9.99

# Number to string
text = str(42)       # "42"

# Number conversions
x = int(3.9)         # 3 (removes decimal)
y = float(10)        # 10.0
```

## Useful Functions

```python
# Absolute value
print(abs(-5))       # 5

# Rounding
print(round(3.7))    # 4
print(round(3.14159, 2))  # 3.14

# Min and Max
print(min(5, 2, 8))  # 2
print(max(5, 2, 8))  # 8

# Power
print(pow(2, 3))     # 8 (same as 2**3)
```

## 🌍 Real-world use

### 1. E-commerce
```python
price = 19.99
quantity = 3
discount = 0.1  # 10% off

subtotal = price * quantity
total = subtotal * (1 - discount)
print(f"Total: ${total:.2f}")  # Total: $53.97
```

### 2. Age Verification
```python
age = int(input("Enter age: "))
is_adult = age >= 18

if is_adult:
    print("Access granted")
else:
    print("You must be 18+")
```

### 3. Temperature Check
```python
temp = 32.5

is_hot = temp > 30
is_cold = temp < 10
is_comfortable = not (is_hot or is_cold)

print(f"Comfortable: {is_comfortable}")
```

### 4. Game Score
```python
score = 0
score += 10  # Enemy defeated
score += 50  # Level completed
score *= 2   # Bonus multiplier

print(f"Final score: {score}")  # 120
```

## ⚠️ Common Mistakes

### Mistake 1: Float precision
```python
print(0.1 + 0.2 == 0.3)  # False (!!)

# Fix: Use round or compare with tolerance
result = round(0.1 + 0.2, 10)
print(result == 0.3)  # True
```

### Mistake 2: Integer division confusion
```python
print(10 / 4)    # 2.5  (float division)
print(10 // 4)   # 2    (floor division)
```

### Mistake 3: Comparing with wrong type
```python
age = "25"
if age > 18:  # ❌ Error - can't compare string and int
    print("Adult")

# Fix: Convert first
age = int(age)
if age > 18:  # ✅
    print("Adult")
```

### Mistake 4: Using = instead of ==
```python
x = 5
if x = 5:  # ❌ Error - = is assignment, not comparison
    print("Five")

if x == 5:  # ✅ Correct - == is comparison
    print("Five")
```

### Mistake 5: Confusing and/or
```python
age = 20
# ❌ Wrong
if age > 18 and < 65:  # Syntax error

# ✅ Correct
if age > 18 and age < 65:  # Good
if 18 < age < 65:          # Even better!
```

## 🧠 Remember

**Numbers:**
- `int` for whole numbers, `float` for decimals
- Use `//` for integer division, `/` for regular division
- `%` gives the remainder
- Convert with `int()`, `float()`, `str()`

**Booleans:**
- Only `True` or `False`
- Use `==` to compare (not `=`)
- `and`, `or`, `not` for logic
- Comparisons return booleans

---

## Advanced: Number Systems

```python
# Binary (base 2)
binary = 0b1010
print(binary)  # 10

# Octal (base 8)
octal = 0o12
print(octal)   # 10

# Hexadecimal (base 16)
hex_num = 0xA
print(hex_num) # 10

# Convert to different bases
num = 42
print(bin(num))  # '0b101010'
print(oct(num))  # '0o52'
print(hex(num))  # '0x2a'
```

## Advanced: Truthy and Falsy

In Python, non-boolean values can be treated as True or False:

```python
# Falsy values (treated as False)
bool(0)      # False
bool(0.0)    # False
bool("")     # False (empty string)
bool([])     # False (empty list)
bool(None)   # False

# Truthy values (treated as True)
bool(42)     # True (any non-zero number)
bool("hi")   # True (any non-empty string)
bool([1])    # True (any non-empty list)
```

This is useful in conditions:
```python
name = input("Enter name: ")
if name:  # True if name is not empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name")
```

## Working with Large Numbers

Python handles big numbers automatically:

```python
big = 123456789012345678901234567890
bigger = big ** 2
print(bigger)  # Works fine, no overflow!
```

For very precise decimal math (like money):
```python
from decimal import Decimal

price = Decimal("19.99")
quantity = Decimal("3")
total = price * quantity
print(total)  # 59.97 (exactly!)
```
