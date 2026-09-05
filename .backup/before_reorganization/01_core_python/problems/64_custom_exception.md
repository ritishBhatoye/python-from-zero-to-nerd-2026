# Exercise 64 — Custom Exception
**Phase:** `01_core_python`  
**Type:** concept/micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- Custom exceptions
- Classes
- Raising exceptions

## Prerequisites

- Previous exercises

---

## Objective

Create a custom exception class and a function that simulates withdrawing money from a bank account, raising the custom exception if funds are insufficient.

---

## Requirements

```python
class InsufficientFundsError(Exception):
    """
    Custom exception for insufficient funds.
    Must have 'balance' and 'amount' attributes.
    """
    def __init__(self, balance: float, amount: float):
        # Implementation here
        pass

def withdraw(balance: float, amount: float) -> float:
    """
    Withdraw amount from balance.
    Raise ValueError if amount <= 0.
    Raise InsufficientFundsError if amount > balance.
    Return the new balance.
    """
```

---

## Examples

```python
withdraw(100.0, 50.0)  # 50.0
withdraw(100.0, 200.0) # Raises InsufficientFundsError(balance=100.0, amount=200.0)
withdraw(100.0, -10.0) # Raises ValueError
```

---

## Constraints

- Python 3.12+ only
- No external imports unless specified

---

## Edge Cases

- Amount exactly equals balance (should succeed and return 0.0).
- Negative or zero amounts.

---

## Test Command

```bash
pytest 01_core_python/tests/test_64_custom_exception.py -v
```

---

## Hints (use only if stuck)

1. The custom exception should inherit from `Exception` and assign `self.balance = balance` and `self.amount = amount` in its `__init__`.
2. Don't forget to call `super().__init__(...)` with a message if you want a nice string representation.

---

## Implementation

```
01_core_python/solutions/64_custom_exception.py
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
./scripts/commit_exercise.sh feat core 64_custom_exception
```
