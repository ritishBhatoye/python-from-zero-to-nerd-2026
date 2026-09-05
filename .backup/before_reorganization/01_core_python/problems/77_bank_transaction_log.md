# Exercise 77 — Bank Transaction Log

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** zhiwehu Q17  
**Status:** 🔴 Not started

## Concepts

- loops, conditionals, string parsing, accumulator pattern

## Prerequisites

- Exercises 01-20

---

## Objective

Process a bank transaction log and compute the final account balance.

---

## Requirements

```python
def calculate_balance(transactions: list[str]) -> int:
    """
    Calculate net balance from transaction log.
    
    Args:
        transactions: List of transaction strings in format:
                     "D amount" for deposit
                     "W amount" for withdrawal
    
    Returns:
        Final balance as integer
    
    Example:
        ["D 300", "D 300", "W 200", "D 100"] -> 500
    """
```

---

## Examples

```python
calculate_balance(["D 300", "D 300", "W 200", "D 100"])
# 500  # +300 +300 -200 +100

calculate_balance(["D 1000", "W 500", "W 300"])
# 200  # +1000 -500 -300

calculate_balance(["W 100", "D 100"])
# 0  # -100 +100
```

---

## Constraints

- Starting balance is 0
- "D" means deposit (add amount)
- "W" means withdrawal (subtract amount)
- Parse each transaction string to extract operation and amount

---

## Edge Cases

- Empty transaction list returns 0
- Negative balance is possible (no overdraft protection)
- Single transaction works correctly

---

## Test Command

```bash
pytest 01_core_python/tests/test_77_bank_transaction_log.py -v
```

---

## Hints (use only if stuck)

1. Split each transaction: `transaction.split()` gives `["D", "300"]`
2. First element is operation, second is amount
3. Use accumulator: start at 0, add or subtract based on operation
4. Convert amount string to int: `int(parts[1])`

---

## Implementation

```
01_core_python/solutions/77_bank_transaction_log.py
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
./scripts/commit_exercise.sh feat core 77_bank_transaction_log
```
