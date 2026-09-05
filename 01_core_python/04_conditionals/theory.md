# Conditionals (if/elif/else)

## 🧠 What is it?

**Conditionals** let your program make decisions. The code runs different instructions based on whether conditions are True or False.

```python
if condition:
    # Do this if True
else:
    # Do this if False
```

## 🤔 Why do we need it?

Programs need to make decisions:
- Check if password is correct
- Show different content to different users
- Validate user input
- Control game logic

## 💻 Simple Example

```python
age = 18

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")
```

## 🔍 How it works

Python checks the condition. If True, it runs the indented code below. If False, it skips to the `else` block.

**Indentation matters!** Python uses spaces/tabs to know what code belongs to the if block.

```python
temperature = 25

if temperature > 30:
    print("It's hot!")
    print("Drink water")  # Also part of if
print("Have a nice day")  # Always runs
```

## if Statement

```python
score = 85

if score >= 60:
    print("You passed!")
```

## if-else Statement

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## if-elif-else Statement

For multiple conditions:

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**How it works:**
1. Checks first condition
2. If False, checks next `elif`
3. Continues until one is True
4. Runs that block and stops
5. If all False, runs `else`

## Nested Conditionals

if inside if:

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")
```

## Comparison Operators

```python
x == y   # Equal
x != y   # Not equal
x > y    # Greater than
x < y    # Less than
x >= y   # Greater or equal
x <= y   # Less or equal
```

## Logical Operators

### and - Both must be True
```python
age = 25
income = 50000

if age >= 18 and income > 30000:
    print("Loan approved")
```

### or - At least one must be True
```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
```

### not - Flips True/False
```python
is_raining = False

if not is_raining:
    print("Go outside!")
```

## Combining Conditions

```python
age = 25
is_student = True
income = 20000

if (age >= 18 and age < 65) or is_student:
    if income < 30000:
        print("Eligible for discount")
```

## Ternary Operator (One-line if)

```python
age = 20

# Normal way
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Short way (ternary)
status = "Adult" if age >= 18 else "Minor"
```

## Membership Operators

### in - Check if value exists
```python
fruits = ["apple", "banana", "orange"]

if "apple" in fruits:
    print("We have apples!")

# Works with strings too
email = "user@example.com"
if "@" in email:
    print("Valid email format")
```

### not in - Check if value doesn't exist
```python
username = "admin"

if username not in ["banned1", "banned2"]:
    print("Welcome!")
```

## Identity Operators

### is - Check if same object
```python
x = None

if x is None:
    print("x is not set")

# Checking boolean
is_logged_in = True
if is_logged_in is True:  # Or just: if is_logged_in:
    print("Welcome back!")
```

### is not
```python
password = ""

if password is not None and password != "":
    print("Password accepted")
```

## 🌍 Real-world use

### 1. Login System
```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "secret123":
    print("Login successful")
else:
    print("Invalid credentials")
```

### 2. Temperature Warning
```python
temp = 35

if temp > 30:
    print("⚠️ Heat warning!")
elif temp < 0:
    print("🥶 Freezing warning!")
else:
    print("🌤️ Pleasant weather")
```

### 3. Shopping Discount
```python
total = 150
is_member = True

if total >= 100:
    if is_member:
        discount = 0.20  # 20% off
    else:
        discount = 0.10  # 10% off
else:
    discount = 0

final_price = total * (1 - discount)
print(f"You pay: ${final_price}")
```

### 4. Input Validation
```python
age = int(input("Enter age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age < 13:
    print("Child account")
elif age < 18:
    print("Teen account")
else:
    print("Adult account")
```

## ⚠️ Common Mistakes

### Mistake 1: Forgetting colon
```python
if age >= 18  # ❌ Missing :
    print("Adult")

if age >= 18:  # ✅
    print("Adult")
```

### Mistake 2: Wrong indentation
```python
if score > 50:
print("Pass")  # ❌ Must be indented

if score > 50:
    print("Pass")  # ✅
```

### Mistake 3: Using = instead of ==
```python
if x = 5:  # ❌ Assignment, not comparison
    print("Five")

if x == 5:  # ✅
    print("Five")
```

### Mistake 4: Comparing with wrong type
```python
age = "18"
if age >= 18:  # ❌ Can't compare string and int
    print("Adult")

age = int(age)  # ✅ Convert first
if age >= 18:
    print("Adult")
```

### Mistake 5: Unnecessary elif after return/break
```python
# ❌ Unnecessary
if score >= 90:
    return "A"
elif score >= 80:
    return "B"

# ✅ Simpler (return exits anyway)
if score >= 90:
    return "A"
if score >= 80:
    return "B"
```

### Mistake 6: Testing float equality
```python
x = 0.1 + 0.2
if x == 0.3:  # ❌ Might be False!
    print("Equal")

# ✅ Use tolerance
if abs(x - 0.3) < 0.0001:
    print("Equal")
```

## 🧠 Remember

- Use `if` to make decisions
- Indentation defines code blocks (4 spaces standard)
- `elif` for additional conditions
- `else` for everything else
- Use `==` for comparison (not `=`)
- Combine conditions with `and`, `or`, `not`
- Keep conditions simple and readable

---

## Advanced: Short-circuit Evaluation

Python stops checking conditions as soon as it knows the answer:

```python
def expensive_check():
    print("Checking...")
    return True

# With 'and', if first is False, second never runs
if False and expensive_check():
    pass  # "Checking..." never prints

# With 'or', if first is True, second never runs
if True or expensive_check():
    pass  # "Checking..." never prints
```

Use this for safe checking:
```python
if user is not None and user.is_active:  # ✅ Safe
    print("Active user")

if user.is_active and user is not None:  # ❌ Error if user is None
    print("Active user")
```

## Match-Case (Python 3.10+)

Modern alternative to multiple elif:

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:  # Default
        print("Unknown status")
```

More powerful than if/elif for pattern matching!
