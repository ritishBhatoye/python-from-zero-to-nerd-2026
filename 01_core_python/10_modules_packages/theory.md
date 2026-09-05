# Modules and Packages

## 🧠 What is it?

A **module** is a Python file containing code you can reuse.
A **package** is a folder containing multiple modules.

## 🤔 Why do we need it?

- Organize large programs into smaller files
- Reuse code across projects
- Use code written by others (libraries)

## Importing Modules

### Built-in Modules
```python
import math
print(math.sqrt(16))  # 4.0

import random
print(random.randint(1, 10))  # Random number 1-10

from datetime import datetime
now = datetime.now()
```

### Import Specific Items
```python
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.14159...
```

### Import with Alias
```python
import math as m
print(m.sqrt(16))

from datetime import datetime as dt
now = dt.now()
```

## Creating Your Own Module

### File: mymodule.py
```python
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

### File: main.py
```python
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.add(5, 3))
print(mymodule.PI)
```

## Packages

Folder structure:
```
mypackage/
    __init__.py
    math_tools.py
    string_tools.py
```

Usage:
```python
from mypackage import math_tools
result = math_tools.add(5, 3)
```

## Common Standard Library Modules

```python
# Math operations
import math

# Random numbers
import random

# Date and time
from datetime import datetime, timedelta

# Regular expressions
import re

# File and directory operations
import os
import pathlib

# JSON data
import json

# HTTP requests
import urllib.request
```

## 🌍 Real-world use

### Read JSON File
```python
import json

with open("data.json") as f:
    data = json.load(f)
```

### Work with Dates
```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)
print(tomorrow.strftime("%Y-%m-%d"))
```

### Generate Random Data
```python
import random

# Random choice
colors = ["red", "blue", "green"]
print(random.choice(colors))

# Shuffle list
random.shuffle(colors)
```

## 🧠 Remember

- Modules = reusable Python files
- Import with `import modulename`
- Create your own by saving `.py` files
- Python has many useful built-in modules
