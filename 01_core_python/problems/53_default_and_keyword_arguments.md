<Exercise 53 — Default and Keyword Arguments>
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Functions, Default Arguments, Keyword-Only Arguments, Mutable Default Trap, Dictionaries

## Prerequisites

- Previous exercises

---

## Objective

Create a function with default and keyword-only arguments to generate a profile dictionary, correctly handling mutable default arguments (avoiding the mutable default trap).

---

## Requirements

```python
def make_profile(name: str, age: int, *, city: str = 'Unknown', hobbies: list[str] | None = None) -> dict:
    """Return a profile dictionary based on the provided arguments."""
```

---

## Examples

```python
make_profile("Alice", 30)
# {'name': 'Alice', 'age': 30, 'city': 'Unknown', 'hobbies': []}

make_profile("Bob", 25, city="New York", hobbies=["reading", "coding"])
# {'name': 'Bob', 'age': 25, 'city': 'New York', 'hobbies': ['reading', 'coding']}
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified
- `city` and `hobbies` MUST be keyword-only arguments (using `*`).
- If `hobbies` is `None`, it must default to an empty list `[]`.

---

## Edge Cases

- Supplying `None` for hobbies should result in an empty list.

---

## Test Command

```bash
pytest 01_core_python/tests/test_53_default_and_keyword_arguments.py -v
```

---

## Hints (use only if stuck)

1. Use `*` in the function signature to force the following arguments to be keyword-only.
2. Inside the function, use `if hobbies is None: hobbies = []` to avoid sharing a single mutable list across calls.

---

## Implementation

```
01_core_python/solutions/53_default_and_keyword_arguments.py
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
./scripts/commit_exercise.sh feat core 53_default_and_keyword_arguments
```
