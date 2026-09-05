# Exercise 03 — Code Style Basics

**Phase:** `00_setup`  
**Type:** concept  
**Difficulty:** Level 0 — Warm-up  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- readable code, naming, ruff-compatible style

## Objective

Practice writing clean, lint-friendly Python before tackling harder exercises.

## Requirements

```python
def format_full_name(first_name: str, last_name: str) -> str:
```

Return `"Last, First"` with both names stripped and title-cased.

Raise `ValueError` if either name is empty after stripping.

After implementing, run:

```bash
ruff check 00_setup/solutions/03_code_style_basics.py
```

## Test Command

```bash
pytest 00_setup/tests/test_03_code_style_basics.py -v
```

## Implementation

```
00_setup/solutions/03_code_style_basics.py
```

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat setup 03_code_style_basics
```
