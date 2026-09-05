# Exceptions and Error Handling

## 🧠 What is it?

**Exceptions** are errors that happen when your program runs. **Error handling** lets your program deal with errors gracefully instead of crashing.

## 🤔 Why do we need it?

- Prevent program crashes
- Give users helpful error messages
- Handle unexpected situations
- Clean up resources (close files, etc.)

## 💻 Simple Example

```python
# Without error handling - CRASH!
number = int(input("Enter number: "))  # User types "abc" → Error!

# With error handling - No crash
try:
    number = int(input("Enter number: "))
except ValueError:
    print("That's not a number!")
    number = 0
```

## try-except

### Basic Syntax
```python
try:
    # Code that might cause error
    result = 10 / 0
except:
    # Handle any error
    print("An error occurred!")
```

### Catch Specific Errors
```python
try:
    number = int("abc")
except ValueError:
    print("Can't convert to integer!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

### Multiple Exceptions
```python
try:
    # Code
    x = int(input())
    result = 10 / x
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print(f"Other error: {e}")
```

## try-except-else

Runs if NO error occurred:

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid!")
else:
    print(f"You entered: {number}")
```

## try-except-finally

Always runs, even after errors:

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always closes file
```

## Common Exceptions

```python
# ValueError - wrong value type
int("abc")  # ValueError

# ZeroDivisionError - divide by zero
10 / 0  # ZeroDivisionError

# FileNotFoundError - file doesn't exist
open("missing.txt")  # FileNotFoundError

# KeyError - dictionary key doesn't exist
data = {"name": "Alice"}
data["age"]  # KeyError

# IndexError - list index out of range
items = [1, 2, 3]
items[10]  # IndexError

# TypeError - wrong type
"hello" + 5  # TypeError
```

## Raising Exceptions

Create your own errors:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)  # Cannot divide by zero!
```

## 🌍 Real-world use

### Validate User Input
```python
while True:
    try:
        age = int(input("Enter age: "))
        if age < 0 or age > 120:
            raise ValueError("Age must be 0-120")
        break
    except ValueError as e:
        print(f"Invalid: {e}")
```

### File Operations
```python
try:
    with open("data.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File doesn't exist. Creating new one...")
    with open("data.txt", "w") as f:
        f.write("")
```

### API Calls
```python
import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API error: {e}")
```

## ⚠️ Common Mistakes

### Mistake 1: Catching all exceptions
```python
# ❌ Hides all errors, hard to debug
try:
    # code
except:
    pass

# ✅ Be specific
try:
    # code
except ValueError:
    # handle ValueError
```

### Mistake 2: Not providing helpful messages
```python
# ❌ User doesn't know what went wrong
except ValueError:
    print("Error!")

# ✅ Helpful message
except ValueError:
    print("Please enter a valid number (digits only)")
```

### Mistake 3: Using exceptions for control flow
```python
# ❌ Don't use exceptions for normal logic
try:
    user = users[user_id]
except KeyError:
    user = None

# ✅ Use normal checks
user = users.get(user_id, None)
```

## 🧠 Remember

- Use try-except to handle errors
- Catch specific exceptions when possible
- finally always runs (good for cleanup)
- Raise exceptions when data is invalid
- Give users helpful error messages

---

## Custom Exceptions

```python
class InvalidAgeError(Exception):
    """Raised when age is invalid"""
    pass

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be 0-120")
    return age

try:
    set_age(150)
except InvalidAgeError as e:
    print(e)  # Age must be 0-120
```
