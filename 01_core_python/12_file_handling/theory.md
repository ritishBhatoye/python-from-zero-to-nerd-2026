# File Handling

## 🧠 What is it?

**File handling** means reading from and writing to files on your computer. Python can work with text files, CSV, JSON, and more.

## 🤔 Why do we need it?

- Save data permanently (survives after program ends)
- Read configuration files
- Process log files
- Import/export data
- Work with user uploads

## Reading Files

### Read Entire File
```python
# Open and read
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Better way (automatically closes)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Read Line by Line
```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes \n
```

### Read All Lines as List
```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    # lines = ["line 1\n", "line 2\n", ...]
```

## Writing Files

### Write (Overwrites File)
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line")
```

### Append (Adds to End)
```python
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

### Write Multiple Lines
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)
```

## File Modes

```python
"r"  # Read (default) - error if file doesn't exist
"w"  # Write - creates file or overwrites existing
"a"  # Append - adds to end of file
"r+" # Read and write
"w+" # Write and read (overwrites)
"a+" # Append and read
```

## Check if File Exists

```python
import os

if os.path.exists("data.txt"):
    print("File exists!")
else:
    print("File not found")
```

## Working with Paths

```python
from pathlib import Path

# Create path object
path = Path("data/files/info.txt")

# Check existence
if path.exists():
    print("Found!")

# Read file
content = path.read_text()

# Write file
path.write_text("New content")

# Get parent directory
print(path.parent)  # data/files

# Get filename
print(path.name)  # info.txt
```

## CSV Files

```python
import csv

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['col1', 'col2', 'col3']

# Write CSV
data = [
    ["Name", "Age"],
    ["Alice", "25"],
    ["Bob", "30"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

## JSON Files

```python
import json

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])

# Write JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=2)
```

## 🌍 Real-world use

### Save User Settings
```python
import json

settings = {
    "theme": "dark",
    "notifications": True
}

with open("settings.json", "w") as f:
    json.dump(settings, f)
```

### Process Log File
```python
errors = []

with open("app.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            errors.append(line.strip())

print(f"Found {len(errors)} errors")
```

### Read Configuration
```python
config = {}

with open("config.txt", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        config[key] = value

print(config["database_url"])
```

## ⚠️ Common Mistakes

### Mistake 1: Forgetting to close file
```python
# ❌ File might not close properly
file = open("data.txt")
data = file.read()
# Forgot file.close()!

# ✅ Use with (closes automatically)
with open("data.txt") as file:
    data = file.read()
```

### Mistake 2: Wrong mode
```python
# ❌ Opens in read mode, can't write
with open("data.txt", "r") as f:
    f.write("text")  # Error!

# ✅ Use write mode
with open("data.txt", "w") as f:
    f.write("text")
```

### Mistake 3: Not handling missing files
```python
# ❌ Crashes if file missing
with open("data.txt", "r") as f:
    data = f.read()

# ✅ Handle error
try:
    with open("data.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")
```

## 🧠 Remember

- Use `with open()` to automatically close files
- `"r"` = read, `"w"` = write, `"a"` = append
- Always handle FileNotFoundError
- Use pathlib.Path for modern path handling
- JSON is great for structured data
- CSV for spreadsheet-like data
