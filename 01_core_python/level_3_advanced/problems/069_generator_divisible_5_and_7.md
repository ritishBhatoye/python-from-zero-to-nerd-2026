# Exercise 061 — Unicode String Handling

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

---

## Concepts

- Unicode strings
- Character representation
- Unicode code points
- Python string handling
- `ord()` and `chr()` functions

## Prerequisites

- Basic Python strings
- String indexing and iteration
- Basic functions

---

## Objective

Write a Python program that creates and displays a string containing characters from different languages using Python's built-in Unicode support.

The program should demonstrate that Python can store, process, and display Unicode characters without requiring special string prefixes.

---

## Requirements

1. Create a string containing English text and characters from another language.
2. Print the complete string.
3. Iterate through the string character by character.
4. Display each character and its corresponding Unicode code point using `ord()`.
5. Use `chr()` to convert a Unicode code point back into its corresponding character.
6. Ensure the program handles Unicode characters correctly.

---

## Examples

**Example 1: English and Chinese characters**

Input:
```python
text = "Hello, 世界"
```

Output:
```text
Hello, 世界
```

**Example 2: Unicode character inspection**

Input:
```python
text = "A世"
```

Output:
```text
Character: A | Code point: U+0041
Character: 世 | Code point: U+4E16
```

**Example 3: Unicode character conversion**

Input:
```python
code = 65
```

Output:
```text
Character: A
```

---

## Additional Test Cases

| Input string | Expected output |
|---|---|
| `"Hello"` | `Hello` |
| `"Hello, 世界"` | `Hello, 世界` |
| `"नमस्ते"` | `नमस्ते` |
| `"こんにちは"` | `こんにちは` |
| `"Café"` | `Café` |
| `"Hello 🌍"` | `Hello 🌍` |

---

## Hints (Use Only If Stuck)

1. Python 3 supports Unicode strings by default.
2. Use `ord()` to obtain a character's Unicode code point.
3. Use `chr()` to convert a Unicode code point into a character.
4. Use a `for` loop to process individual characters