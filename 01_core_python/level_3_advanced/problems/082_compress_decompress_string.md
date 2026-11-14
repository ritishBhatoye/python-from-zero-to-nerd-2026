# Exercise 082 — Compress and Decompress a String

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

## Concepts

- String encoding and decoding
- Data compression and decompression
- Python's `zlib` module
- Bytes and strings
- Exception handling
- Working with binary data

## Prerequisites

- Basic Python string operations
- Understanding of bytes and string encoding
- Basic exception handling
- Familiarity with Python modules

---

## Objective

Build a program that compresses a string into binary data using Python's built-in `zlib` module and then decompresses it back into its original string.

The program should demonstrate how compression reduces data size and how compressed binary data can be restored to its original readable form.

---

## Requirements

1. Implement a function named `compress_string(text)` that:
   - Accepts a string as input.
   - Converts the string into bytes using an appropriate encoding.
   - Compresses the bytes using `zlib`.
   - Returns the compressed binary data.

2. Implement a function named `decompress_string(compressed_data)` that:
   - Accepts compressed binary data.
   - Decompresses it using `zlib`.
   - Converts the resulting bytes back into a readable string.
   - Returns the original string.

3. Handle invalid input appropriately.
4. Ensure that the decompressed result exactly matches the original input.
5. Test your implementation with different types of strings, including:
   - Short strings.
   - Long strings.
   - Strings containing numbers and special characters.
   - Unicode characters.
   - Empty strings.

---

## Examples

**Example 1:**

Input:
`"hello world"`

Expected behaviour:
- Compress the string.
- Decompress the compressed data.
- Return `"hello world"`.

**Example 2:**

Input:
`"Python is awesome! Python is awesome! Python is awesome!"`

Expected behaviour:
- Compress the repeated text.
- Decompress the result.
- Return the exact original string.

**Example 3:**

Input:
`"こんにちは Python 🚀"`

Expected behaviour:
- Successfully compress and decompress Unicode characters.
- Return the exact original string.

---

## Expected Output

Your program should demonstrate:

- Original string.
- Original data size in bytes.
- Compressed data size in bytes.
- Decompressed string.
- Whether the original and decompressed strings match.

**Note:** Compression does not guarantee a smaller output for short strings because of compression overhead.

---

## Hints (use only if stuck)

1. Explore Python's built-in `zlib` module.
2. Understand the difference between `str` and `bytes`.
3. Investigate string encoding and decoding.
4. Look into how compression and decompression functions work.
5. Consider what happens when invalid compressed data is provided.

---

## Test Command

```bash
pytest 01_core_python/level_3_advanced/tests/test_082_compress_decompress_string.py -v
```

---

## Implementation

```text
01_core_python/level_3_advanced/solutions/082_compress_decompress_string.py
```

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
- **What happens when compressed data is corrupted?**
- **When is compression actually beneficial?**