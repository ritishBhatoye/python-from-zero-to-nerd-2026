# Exercise 02 — Hello Pytest

**Phase:** `00_setup`  
**Type:** micro  
**Difficulty:** Level 0 — Warm-up  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- functions, pytest basics, test-driven workflow

## Objective

Write your first tested function and learn the exercise workflow.

## Requirements

```python
def greet(name: str) -> str:
```

Return `"Hello, <name>!"` where `name` is stripped and title-cased.

Raise `ValueError` if name is empty after stripping.

## Examples

```python
greet("  ritish  ")  # "Hello, Ritish!"
```

## Test Command

```bash
pytest 00_setup/tests/test_02_hello_pytest.py -v
```

## Implementation

```
00_setup/solutions/02_hello_pytest.py
```

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat setup 02_hello_pytest
```
