# Strings

## 🧠 What is it?

A **string** is text. It's a sequence of characters (letters, numbers, symbols) enclosed in quotes.

```python
"Hello"
'Python'
"123"
```

## 🤔 Why do we need it?

Almost every program works with text:
- User names
- Messages
- File paths
- URLs
- Email addresses
- Any text data

## 💻 Simple Example

```python
# Creating strings
name = "Alice"
message = 'Hello World'
quote = "She said, 'Hi!'"

# Combining strings
greeting = "Hello, " + name
print(greeting)  # Hello, Alice
```

## 🔍 How it works

Strings are **immutable** - you cannot change them after creation.

```python
text = "Hello"
text[0] = "h"  # ❌ Error - can't modify

# Instead, create a new string
text = "h" + text[1:]  # ✅ Works
print(text)  # hello
```

## Creating Strings

### Single vs Double Quotes
```python
name = 'Alice'      # Single quotes
city = "New York"   # Double quotes
# Both work the same!

# Use quotes inside quotes
text1 = "He said, 'Hi!'"
text2 = 'She said, "Hello!"'
```

### Multi-line Strings
```python
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""
```

### Escape Characters
```python
# Special characters
print("Line 1\nLine 2")      # \n = new line
print("Column1\tColumn2")    # \t = tab
print("He said, \"Hi!\"")    # \" = quote inside string
print("C:\\Users\\Files")    # \\ = backslash
```

## String Operations

### Concatenation (joining)
```python
first = "Hello"
last = "World"
result = first + " " + last  # "Hello World"
```

### Repetition
```python
laugh = "ha" * 3  # "hahaha"
line = "-" * 20   # "--------------------"
```

### Length
```python
text = "Python"
print(len(text))  # 6
```

### Accessing Characters
```python
word = "Python"
print(word[0])    # P (first character)
print(word[-1])   # n (last character)
print(word[1:4])  # yth (slice)
```

## String Methods

### Case Conversion
```python
text = "Hello World"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.capitalize()) # Hello world
```

### Finding & Checking
```python
text = "Python Programming"

# Find substring
print(text.find("Pro"))      # 7 (position)
print(text.find("Java"))     # -1 (not found)

# Check if contains
print("Python" in text)      # True
print("Java" in text)        # False

# Check start/end
print(text.startswith("Py")) # True
print(text.endswith("ing"))  # True
```

### Cleaning
```python
text = "  Hello World  "
print(text.strip())   # "Hello World" (removes spaces)
print(text.lstrip())  # "Hello World  " (left only)
print(text.rstrip())  # "  Hello World" (right only)
```

### Replacing
```python
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)  # I love Python
```

### Splitting & Joining
```python
# Split string into list
sentence = "Python is awesome"
words = sentence.split()  # ["Python", "is", "awesome"]

csv = "apple,banana,orange"
fruits = csv.split(",")   # ["apple", "banana", "orange"]

# Join list into string
result = " ".join(words)  # "Python is awesome"
```

## String Formatting

### f-strings (Modern, Preferred)
```python
name = "Alice"
age = 25

# Simple
message = f"My name is {name}"

# With expressions
info = f"{name} is {age} years old"
calc = f"Next year: {age + 1}"

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # Price: $19.99
```

### format() Method
```python
template = "Hello, {}!"
print(template.format("Alice"))  # Hello, Alice!

message = "{0} is {1} years old"
print(message.format("Bob", 30))  # Bob is 30 years old
```

### % Formatting (Old Style)
```python
name = "Alice"
print("Hello, %s!" % name)  # Hello, Alice!
```

## 🌍 Real-world use

1. **User Input** - Getting and displaying user names, emails
2. **File Paths** - Working with file names and directories
3. **API Responses** - Parsing JSON strings from web services
4. **Log Messages** - Creating readable log entries
5. **Data Cleaning** - Removing extra spaces, fixing capitalization

### Practical Example: Email Validation
```python
email = input("Enter email: ")

if "@" in email and "." in email:
    username = email.split("@")[0]
    print(f"Welcome, {username}!")
else:
    print("Invalid email")
```

## ⚠️ Common Mistakes

### Mistake 1: Trying to modify strings
```python
text = "hello"
text[0] = "H"  # ❌ Error - strings are immutable
```

### Mistake 2: Forgetting quotes are part of syntax
```python
name = Alice   # ❌ Error - Alice is a variable
name = "Alice" # ✅ Correct - "Alice" is a string
```

### Mistake 3: Using + with different types
```python
age = 25
message = "I am " + age  # ❌ Error - can't add string and int

# Fix 1: Convert to string
message = "I am " + str(age)  # ✅

# Fix 2: Use f-string
message = f"I am {age}"       # ✅
```

### Mistake 4: Comparing with wrong case
```python
password = "Python"
if password == "python":  # False - case matters!
    print("Correct")

# Fix: convert to same case
if password.lower() == "python":  # ✅
    print("Correct")
```

## 🧠 Remember

- Strings are text in quotes
- Strings are immutable (cannot be changed)
- Use f-strings for formatting: `f"Hello {name}"`
- Many useful methods: `.upper()`, `.lower()`, `.strip()`, `.split()`
- Always convert numbers to strings before concatenating: `str(age)`

---

## Advanced: String Encoding

Strings are sequences of Unicode characters:

```python
text = "Hello 你好 🎉"
print(text)  # Works with any language/emoji

# Encoding (string → bytes)
data = text.encode('utf-8')
print(data)  # b'Hello \xe4\xbd\xa0\xe5\xa5\xbd \xf0\x9f\x8e\x89'

# Decoding (bytes → string)
original = data.decode('utf-8')
print(original)  # Hello 你好 🎉
```

This is important for:
- Reading files with different encodings
- Working with web data
- Handling international text

## String Performance

```python
# ❌ Slow - creates new string each time
result = ""
for i in range(1000):
    result += str(i)

# ✅ Fast - joins at the end
numbers = [str(i) for i in range(1000)]
result = "".join(numbers)
```

For concatenating many strings, use `join()` instead of `+`.
