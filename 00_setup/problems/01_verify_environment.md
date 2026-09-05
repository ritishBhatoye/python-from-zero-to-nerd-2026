# Exercise 01 — Verify Environment

**Phase:** `00_setup`  
**Type:** micro  
**Difficulty:** Level 0 — Warm-up  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- Python version, sys module, environment setup

## Objective

Confirm your Python environment meets project requirements before writing curriculum code.

## Requirements

```python
def verify_environment() -> dict:
```

Return:

```python
{
    "python_version": str,       # e.g. "3.12.4"
    "version_ok": bool,          # True if >= 3.12
    "platform": str,             # sys.platform value
    "message": str,              # "Ready" or "Upgrade to Python 3.12+"
}
```

Use the `sys` module. Do not hardcode your version.

## Test Command

```bash
pytest 00_setup/tests/test_01_verify_environment.py -v
```

## Implementation

```
00_setup/solutions/01_verify_environment.py
```

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat setup 01_verify_environment
```
