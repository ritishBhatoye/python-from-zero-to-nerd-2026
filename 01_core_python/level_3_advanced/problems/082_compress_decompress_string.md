# Exercise 082 — String Compression and Decompression Using zlib

**Phase:** `01_core_python`  
**Level:** 3 — Advanced  
**Status:** 🔴 Not started

## Concepts
- String Encoding and Decoding
- Data Compression
- Data Decompression
- Python `zlib` Module
- Bytes and Strings
- Type Conversion
- Functions
- Memory Efficiency

## Prerequisites
- Python strings
- Bytes and byte sequences
- Basic functions
- Importing Python modules
- Understanding of encoding and decoding

---

## Objective

Implement string compression and decompression using Python's built-in `zlib` module.

Convert a string into compressed binary data and then decompress it back into its original form.

## Requirements

1. Import Python's built-in `zlib` module.
2. Implement a function named `compress_string(text)` that accepts a string.
3. Encode the input string into bytes before compression.
4. Compress the encoded data using `zlib`.
5. Implement another function named `decompress_string(data)` that accepts compressed binary data.
6. Decompress the binary data and decode it back into a string.
7. Ensure the decompressed string matches the original input exactly.
8. Handle empty strings correctly.
9. Do not use external compression libraries.
10. Do not hardcode the compressed output.

---

## Examples

**Example 1 — Basic string**

Input:
`"hello world"`

Expected result:
- Compressed data: Binary data (`bytes`)
- Decompressed data: `"hello world"`

**Example 2 — Repeated characters**

Input:
`"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"`

Expected result:
- Compressed data: Binary data (`bytes`)
- Decompressed data: `"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"`

**Example 3 — Empty string**

Input:
`""`

Expected result:
- Decompressed data: `""`

**Example 4 — Longer text**

Input:
`"Python is a powerful programming language. " * 100`

Expected result:
- Decompressed data must exactly match the original input.

---

## Hints (use only if stuck)

1. Explore Python's built-in `zlib` module.
2. Understand the difference between `str` and `bytes`.
3. Investigate string encoding before compression.
4. Look into the compression and decompression functions provided by `zlib`.
5. Remember that decompressed bytes must be decoded back into a string.
6. Consider comparing the original and decompressed strings.

---

## Test Command

```bash
pytest 01_core_python/level_3_advanced/tests/test_082_compress_decompress_string.py -v
```

## Implementation

`01_core_python/level_3_advanced/solutions/082_compress_decompress_string.py`

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
- **Difference between strings and bytes:**
- **How compression reduces data size:**
- **When compression is useful in real-world applications:**