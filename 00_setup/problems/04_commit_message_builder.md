# Exercise 04 — Commit Message Builder

**Phase:** `00_setup`  
**Type:** concept  
**Difficulty:** Level 0 — Warm-up  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- Git workflow, conventional commits, strings

## Objective

Build conventional commit messages for the practice workflow — used with `scripts/commit_exercise.sh`.

## Requirements

```python
def build_commit_message(commit_type: str, scope: str, slug: str) -> str:
```

Return: `"<type>(<scope>): solve <slug with underscores replaced by spaces>"`

Valid types: `feat`, `test`, `fix`, `docs`, `refactor`

Raise `ValueError` for invalid type or empty scope/slug.

## Examples

```python
build_commit_message("feat", "core", "01_personal_expense_calculator")
# "feat(core): solve 01 personal expense calculator"
```

## Test Command

```bash
pytest 00_setup/tests/test_04_commit_message_builder.py -v
```

## Implementation

```
00_setup/solutions/04_commit_message_builder.py
```

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat setup 04_commit_message_builder
```
