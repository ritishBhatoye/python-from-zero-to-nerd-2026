<Exercise 17 — Letter and Digit Counter>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q13 (improved)  
**Status:** 🔴 Not started

## Concepts

- Strings, Counting, Dictionaries

## Prerequisites

- Previous exercises

---

## Objective

Count the number of letters and digits in a given text.

---

## Requirements

```python
def count_letters_digits(text: str) -> dict[str, int]:
    """Return a dictionary with counts of 'letters' and 'digits' in the string."""
```

---

## Examples

```python
count_letters_digits("hello world! 123")  # {'letters': 10, 'digits': 3}
```

---

## Constraints

- Python 3.12+ only
- Ignore spaces and punctuation, only count letters and digits

---

## Edge Cases

- Empty string
- String with no letters or no digits
- String with only punctuation

---

## Test Command

```bash
pytest 01_core_python/tests/test_17_letter_and_digit_counter.py -v
```

---

## Hints (use only if stuck)

1. You can use string methods like `isalpha()` and `isdigit()`.
2. Iterate through each character in the string.

---

## Implementation

```
01_core_python/solutions/17_letter_and_digit_counter.py
```

Create this file yourself — it does not exist until you implement it.

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes:**
- **Python concepts:**
- **Possible improvements:**

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 17_letter_and_digit_counter
```
