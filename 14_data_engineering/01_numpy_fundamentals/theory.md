# NumPy Fundamentals — Theory

## 🧠 What is NumPy?

NumPy (Numerical Python) is the most important library for numerical computing in Python. It provides fast arrays and mathematical operations.

## 🤔 Why do we need it?

Python lists are slow for math operations on large amounts of data. NumPy arrays are:
- **50-100x faster** than Python lists
- Use **less memory**
- Have **built-in math functions**

## 💻 Simple Example

```python
import numpy as np

# Python list (slow)
python_list = [1, 2, 3, 4, 5]
squared = [x**2 for x in python_list]  # Slow loop

# NumPy array (fast)
numpy_array = np.array([1, 2, 3, 4, 5])
squared = numpy_array ** 2  # Fast vectorized operation
print(squared)  # [1 4 9 16 25]
```

## 🔍 How it works

1. **Import NumPy**: `import numpy as np`
2. **Create arrays**: `np.array([1, 2, 3])`
3. **Operations work on whole arrays at once** (vectorization)
4. No slow Python loops needed

## 🌍 Real-world use

1. **Data Science**: Pandas uses NumPy internally
2. **Machine Learning**: TensorFlow, PyTorch built on NumPy
3. **Scientific Computing**: Physics simulations, statistics
4. **Image Processing**: Images are NumPy arrays
5. **Financial Analysis**: Fast calculations on stock data

---

## 📚 Core Concepts

### 1. Arrays

NumPy's main object is the **ndarray** (n-dimensional array).

```python
import numpy as np

# 1D array
arr1d = np.array([1, 2, 3])

# 2D array (matrix)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

# 3D array
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])

print(arr1d.shape)  # (3,)
print(arr2d.shape)  # (2, 3)
print(arr3d.shape)  # (2, 2, 2)
```

### 2. Creating Arrays

```python
# Zeros
zeros = np.zeros((3, 4))  # 3x4 array of zeros

# Ones
ones = np.ones((2, 3))  # 2x3 array of ones

# Range
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Linspace (evenly spaced)
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# Random
random = np.random.rand(3, 3)  # 3x3 random values
```

### 3. Array Operations (Vectorization)

```python
arr = np.array([1, 2, 3, 4])

# Math operations (no loops needed!)
print(arr + 10)      # [11 12 13 14]
print(arr * 2)       # [2 4 6 8]
print(arr ** 2)      # [1 4 9 16]
print(np.sqrt(arr))  # [1. 1.41 1.73 2.]
```

### 4. Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[0])      # 10
print(arr[-1])     # 50

# Slicing
print(arr[1:4])    # [20 30 40]
print(arr[::2])    # [10 30 50]

# 2D indexing
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr2d[0, 1])  # 2 (row 0, column 1)
print(arr2d[:, 1])  # [2 5] (all rows, column 1)
```

### 5. Boolean Indexing

```python
arr = np.array([1, 2, 3, 4, 5])

# Boolean mask
mask = arr > 2
print(mask)        # [False False True True True]
print(arr[mask])   # [3 4 5]

# Direct filtering
print(arr[arr > 2])  # [3 4 5]
```

### 6. Array Shape Manipulation

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape
arr2d = arr.reshape(2, 3)
# [[1 2 3]
#  [4 5 6]]

# Flatten
flat = arr2d.flatten()  # [1 2 3 4 5 6]

# Transpose
transposed = arr2d.T
# [[1 4]
#  [2 5]
#  [3 6]]
```

### 7. Aggregation Functions

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))     # 15
print(np.mean(arr))    # 3.0
print(np.median(arr))  # 3.0
print(np.std(arr))     # 1.41 (standard deviation)
print(np.min(arr))     # 1
print(np.max(arr))     # 5
```

### 8. Matrix Operations

```python
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

# Element-wise multiplication
print(a * b)
# [[ 5 12]
#  [21 32]]

# Matrix multiplication (dot product)
print(np.dot(a, b))  # or a @ b
# [[19 22]
#  [43 50]]
```

---

## ⚠️ Common Mistakes

### 1. List vs Array

```python
# ❌ Wrong - using Python list
data = [1, 2, 3]
result = data * 2  # [1, 2, 3, 1, 2, 3] - duplicates list!

# ✅ Right - using NumPy array
data = np.array([1, 2, 3])
result = data * 2  # [2 4 6] - multiplies each element
```

### 2. Shape Mismatch

```python
a = np.array([1, 2, 3])      # shape (3,)
b = np.array([[1], [2], [3]])  # shape (3, 1)

# ❌ May cause errors or unexpected broadcasting
# ✅ Check shapes: print(a.shape, b.shape)
```

### 3. Copy vs View

```python
arr = np.array([1, 2, 3])

# View (changes original)
view = arr[:]
view[0] = 999
print(arr)  # [999, 2, 3] - original changed!

# Copy (independent)
copy = arr.copy()
copy[0] = 999
print(arr)  # [1, 2, 3] - original unchanged
```

### 4. Integer Division

```python
# ❌ Wrong - integer division loses precision
arr = np.array([1, 2, 3])
result = arr / 2  # Still gives floats in NumPy

# ✅ But be aware of data types
arr_int = np.array([1, 2, 3], dtype=int)
result = arr_int // 2  # [0 1 1] - integer division
```

---

## 🧠 Remember

- **NumPy is fast** because operations work on entire arrays
- **Always use NumPy arrays** for numerical data, not lists
- **Check array shapes** before operations
- **Use `.copy()`** when you don't want to modify the original
- **Broadcasting** allows operations on different shaped arrays

---

## 🎯 Key NumPy Functions to Know

### Array Creation
- `np.array()` - Create from list
- `np.zeros()`, `np.ones()` - Arrays of zeros/ones
- `np.arange()` - Range of values
- `np.linspace()` - Evenly spaced values
- `np.random.rand()` - Random values

### Array Information
- `.shape` - Dimensions
- `.dtype` - Data type
- `.size` - Total elements
- `.ndim` - Number of dimensions

### Operations
- `np.sum()`, `np.mean()`, `np.std()` - Statistics
- `np.min()`, `np.max()` - Min/max values
- `np.dot()` or `@` - Matrix multiplication
- `np.transpose()` or `.T` - Transpose

### Indexing
- `arr[i]` - Single element
- `arr[i:j]` - Slice
- `arr[arr > 5]` - Boolean indexing
- `np.where()` - Conditional selection

---

## 📖 Learning Path

1. **Beginner (1-33)**: Basic array operations, indexing, simple math
2. **Intermediate (34-66)**: Reshaping, broadcasting, structured arrays
3. **Advanced (67-100)**: Complex operations, optimization, algorithms

---

## 💡 Pro Tips

1. **Vectorize everything** - avoid Python loops with NumPy arrays
2. **Use built-in functions** - they're optimized C code
3. **Mind your dtypes** - `int64` vs `float64` matters
4. **Broadcasting is powerful** - learn how it works
5. **Profile your code** - use `%timeit` in Jupyter to compare speeds

---

## 🔗 Resources

- Official NumPy Documentation: https://numpy.org/doc/
- NumPy Quickstart: https://numpy.org/doc/stable/user/quickstart.html
- NumPy for MATLAB users: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
