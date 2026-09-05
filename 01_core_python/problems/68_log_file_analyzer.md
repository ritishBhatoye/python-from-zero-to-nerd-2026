# Exercise 68 — Log File Analyzer
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 2 — Intermediate
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- File processing, String splitting, Dictionaries

## Prerequisites

- Previous exercises

---

## Objective

Analyze a log file to count occurrences of different log levels.

---

## Requirements

```python
def analyze_log(filepath: str) -> dict[str, int]:
    """
    Reads a log file where each line is formatted as 'LEVEL: message'.
    Levels can be INFO, WARNING, or ERROR.
    Returns a dictionary with the count of each level.
    Skips malformed lines that do not match the format.
    """
```

---

## Examples

```python
# app.log content:
# INFO: System started
# WARNING: Low memory
# ERROR: Disk full
# INFO: Process running
# Malformed log line

analyze_log('app.log')
# {'INFO': 2, 'WARNING': 1, 'ERROR': 1}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Empty log file
- Logs with no recognized levels
- Missing spaces or extra colons in message

---

## Test Command

```bash
pytest 01_core_python/tests/test_68_log_file_analyzer.py -v
```

---

## Hints (use only if stuck)

1. Use `split(': ', 1)` to separate the level and the message.
2. Maintain a counter dictionary or use `collections.Counter`.

---

## Implementation

```
01_core_python/solutions/68_log_file_analyzer.py
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
./scripts/commit_exercise.sh feat core 68_log_file_analyzer
```
