# Exercise 06 — Greeting Formatter

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- strings, f-strings, conditionals

## Prerequisites

- Exercises 01–05

---

## Objective

Format time-appropriate greetings for user interfaces and chatbots.

---

## Requirements

```python
def format_greeting(name: str, time_of_day: str) -> str:
```

`time_of_day` is one of: `"morning"`, `"afternoon"`, `"evening"` (case-insensitive).

Return:
- morning → `"Good morning, <name>!"`
- afternoon → `"Good afternoon, <name>!"`
- evening → `"Good evening, <name>!"`

Strip leading/trailing whitespace from `name`. Capitalize the first letter of each word in the name (title case).

Raise `ValueError` for invalid `time_of_day`.

---

## Examples

```python
format_greeting("  ritish  ", "morning")   # "Good morning, Ritish!"
format_greeting("alice", "EVENING")       # "Good evening, Alice!"
```

---

## Test Command

```bash
pytest 01_core_python/tests/test_06_greeting_formatter.py -v
```

---

## Implementation

```
01_core_python/solutions/06_greeting_formatter.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 06_greeting_formatter
```
