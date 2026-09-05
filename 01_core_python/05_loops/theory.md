# Loops (for & while)

## 🧠 What is it?

**Loops** repeat code multiple times without writing it again and again.

Two types:
- **for loop** - Repeat a specific number of times
- **while loop** - Repeat while a condition is True

## 🤔 Why do we need it?

- Process items in a list
- Repeat actions (like counting, searching)
- Keep programs running (like games, servers)
- Avoid copying code 100 times

## 💻 Simple Example

```python
# for loop
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Prints: 0, 1, 2, 3, 4
```

## for Loop

### Loop through range
```python
# 0 to 4
for i in range(5):
    print(i)

# 1 to 5
for i in range(1, 6):
    print(i)

# Count by 2s
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Loop through list
```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

### Loop through string
```python
for letter in "Python":
    print(letter)  # P, y, t, h, o, n
```

### Loop with index
```python
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange
```

## while Loop

Repeats while condition is True:

```python
count = 0
while count < 5:
    print(count)
    count += 1  # IMPORTANT: Update the variable!
```

### User input loop
```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Correct!")
```

### Menu loop
```python
choice = ""
while choice != "quit":
    print("1. Play")
    print("2. Settings")
    print("Type 'quit' to exit")
    choice = input("Choice: ")
```

## Loop Control

### break - Exit loop immediately
```python
for i in range(10):
    if i == 5:
        break  # Stop here
    print(i)  # Prints: 0, 1, 2, 3, 4
```

### continue - Skip to next iteration
```python
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)  # Prints: 0, 1, 3, 4
```

### else with loops
Runs if loop completes without break:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed!")  # Runs because no break
```

## Nested Loops

Loop inside a loop:

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

### Multiplication table
```python
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
```

## Infinite Loops

```python
# ⚠️ Runs forever (use Ctrl+C to stop)
while True:
    print("Forever...")
    
# Use break to exit
while True:
    choice = input("Continue? (y/n): ")
    if choice == "n":
        break
```

## 🌍 Real-world use

### 1. Process Files
```python
files = ["doc1.txt", "doc2.txt", "doc3.txt"]

for filename in files:
    print(f"Processing {filename}...")
    # Read and process file
```

### 2. Count Down
```python
for i in range(10, 0, -1):
    print(i)
print("Blast off! 🚀")
```

### 3. Search List
```python
numbers = [4, 7, 2, 9, 1]
target = 9

for i, num in enumerate(numbers):
    if num == target:
        print(f"Found {target} at index {i}")
        break
else:
    print(f"{target} not found")
```

### 4. Validation Loop
```python
while True:
    age = input("Enter age (1-120): ")
    if age.isdigit():
        age = int(age)
        if 1 <= age <= 120:
            break
    print("Invalid age, try again")
```

### 5. Sum Numbers
```python
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1-100: {total}")  # 5050
```

## ⚠️ Common Mistakes

### Mistake 1: Infinite loop (forgetting to update)
```python
# ❌ Never ends!
count = 0
while count < 5:
    print(count)  # Forgot: count += 1

# ✅ Fixed
count = 0
while count < 5:
    print(count)
    count += 1
```

### Mistake 2: Modifying list while iterating
```python
numbers = [1, 2, 3, 4]

# ❌ Can cause bugs
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Changes list during loop!

# ✅ Create new list instead
numbers = [1, 2, 3, 4]
numbers = [num for num in numbers if num % 2 != 0]
```

### Mistake 3: Using wrong range
```python
# ❌ Goes 0-4, not 1-5
for i in range(5):
    print(i)

# ✅ If you want 1-5
for i in range(1, 6):
    print(i)
```

### Mistake 4: Forgetting indentation
```python
# ❌ Only last print is in loop
for i in range(3):
print(i)

# ✅ Correct
for i in range(3):
    print(i)
```

### Mistake 5: Using while when for is better
```python
# ❌ More complex
i = 0
while i < 5:
    print(i)
    i += 1

# ✅ Simpler
for i in range(5):
    print(i)
```

## 🧠 Remember

- Use **for** when you know how many times to loop
- Use **while** when you loop until a condition changes
- Use **break** to exit early
- Use **continue** to skip one iteration
- Always update variables in while loops to avoid infinite loops
- `range(5)` gives 0-4, not 1-5

---

## Advanced Techniques

### Loop with dictionary
```python
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

for name, score in scores.items():
    print(f"{name}: {score}")
```

### Multiple sequences with zip
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Loop backwards
```python
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0
```

### Loop with step
```python
# Every 3rd number
for i in range(0, 20, 3):
    print(i)  # 0, 3, 6, 9, 12, 15, 18
```

## Performance Tips

```python
# ❌ Slow - checks length every time
i = 0
while i < len(items):
    process(items[i])
    i += 1

# ✅ Faster - direct iteration
for item in items:
    process(item)

# ✅ When you need index
for i, item in enumerate(items):
    process(i, item)
```
