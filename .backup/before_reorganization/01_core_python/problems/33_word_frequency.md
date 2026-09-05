# Exercise 33 — Word Frequency
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- dictionaries, string manipulation

## Prerequisites

- Previous exercises

---

## Objective

Calculate the frequency of each word in a string.

---

## Requirements

```python
def word_frequency(text: str) -> dict[str, int]:
    """Calculate the frequency of each word (case-insensitive, ignoring punctuation)."""
```

---

## Examples

```python
word_frequency("Hello world! Hello python.")  # {'hello': 2, 'world': 1, 'python': 1}
```

---

## Constraints

- Python 3.12+ only
- Strip common punctuation from words before counting.

---

## Edge Cases

- Empty string
- Text with only punctuation
- Case-insensitivity

---

## Test Command

```bash
pytest 01_core_python/tests/test_33_word_frequency.py -v
```

---

## Hints (use only if stuck)

1. Convert string to lowercase first.
2. Consider using string.punctuation to strip punctuation.

---

## Implementation

```
01_core_python/solutions/33_word_frequency.py
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
./scripts/commit_exercise.sh feat core 33_word_frequency
```
