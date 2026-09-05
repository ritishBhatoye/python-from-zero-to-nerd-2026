# Arguments and Scope

## Arguments

### Positional Arguments
```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

greet("Alice", "Hello")  # Hello, Alice!
```

### Keyword Arguments
```python
greet(name="Bob", greeting="Hi")  # Hi, Bob!
greet(greeting="Hey", name="Charlie")  # Hey, Charlie!
```

### Default Arguments
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")  # Hello, Alice!
```

### *args (Variable Positional)
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4)  # 10
```

### **kwargs (Variable Keyword)
```python
def print_data(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

print_data(name="Alice", age=25)
```

## Scope

### Local Scope
```python
def my_func():
    x = 10  # Only exists inside function
    print(x)

my_func()  # 10
# print(x)  # Error - x doesn't exist here
```

### Global Scope
```python
x = 10  # Global

def show():
    print(x)  # Can read global

show()  # 10
```

### Modifying Global
```python
count = 0

def increment():
    global count  # Declare we're using global
    count += 1

increment()
print(count)  # 1
```

### Nonlocal (Nested Functions)
```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Modify outer function's variable
        x += 1
        print(x)
    
    inner()  # 11

outer()
```

## 🧠 Remember

- Arguments pass data into functions
- Scope determines where variables exist
- Local variables disappear after function ends
- Use `global` sparingly - better to return values
