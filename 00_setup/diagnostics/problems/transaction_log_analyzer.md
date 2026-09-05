# Diagnostic Challenge #1 — Transaction Log Analyzer

**Phase:** 00_setup/diagnostics  
**Purpose:** Assess core Python proficiency before entering the curriculum  
**Difficulty:** Foundation → Practical  

---

## 🧠 CONCEPT BEING TESTED

This is not a teaching exercise — it is a **diagnostic**. It tests whether you
can comfortably combine these core Python skills in a single realistic problem:

- String parsing and sanitization
- Type conversion with error handling
- Dictionary and list aggregation
- Conditional logic and validation
- Sorting with custom keys
- Function design and return structure
- Defensive programming (never crash on bad input)

Your performance here determines where you start in the curriculum.

---

## WHY THIS PROBLEM

In real backend services, data engineering pipelines, and ML preprocessing,
raw data arrives messy. Engineers must parse, validate, aggregate, and report
without crashing on malformed input. This is a daily skill, not a textbook
exercise.

---

## 🎯 PRACTICAL CHALLENGE

Implement this function:

```python
def analyze_transaction_logs(raw_logs: list[str]) -> dict:
    ...
```

Each string in `raw_logs` is a pipe-delimited (`|`) transaction record:

```
"<timestamp> | <user_id> | <transaction_type> | <amount>"
```

Example:

```
"2026-09-01T08:00:00 | user_alice | DEPOSIT | 1200.50"
```

---

## 📋 REQUIREMENTS

### 1. Record Validation & Sanitization

- A valid record must contain exactly **4 non-empty fields** after splitting
  by `|`.
- Strip leading and trailing whitespace from every field.
- `transaction_type` must be strictly one of: `"DEPOSIT"`, `"WITHDRAWAL"`,
  `"TRANSFER"` (case-sensitive).
- `amount` must be a valid positive number (`amount > 0.0`).
- Any record that violates format, has invalid types, missing fields, or
  negative/zero amounts is **corrupted** and must be skipped (not crash).

### 2. Output Schema

Return a single dictionary with this exact structure:

```python
{
    "total_records": int,           # Total count of input strings
    "valid_records": int,           # Count of successfully parsed transactions
    "corrupted_records": int,       # Count of invalid/malformed entries skipped
    "total_volume": float,          # Sum of amounts of all valid records (round to 2 decimals)
    "breakdown_by_type": {
        "DEPOSIT":    {"count": int, "total": float},
        "WITHDRAWAL": {"count": int, "total": float},
        "TRANSFER":   {"count": int, "total": float},
    },
    "high_value_transactions": [    # Valid transactions with amount >= 500.0
        {                           # Sorted by amount DESCENDING
            "user_id": str,
            "type": str,
            "amount": float,
        },
        ...
    ],
    "unique_users": list[str],      # Unique user_ids from valid records, sorted alphabetically
}
```

### 3. Float Formatting

All aggregated float totals (`total_volume`, breakdown totals) and individual
amounts must be rounded to 2 decimal places using `round(val, 2)`.

---

## 🚧 CONSTRAINTS

- **No third-party libraries** (no Pandas, no external packages).
- **No `re` (regex) module** — use Python's built-in string methods only.
- Your function must **never raise an unhandled exception** regardless of
  input quality.

---

## 🧪 TEST CASES

See the test file at:

```
00_setup/diagnostics/tests/test_transaction_log_analyzer.py
```

Run them with:

```bash
cd /Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026
python -m pytest 00_setup/diagnostics/tests/test_transaction_log_analyzer.py -v
```

---

## 💡 HINTS (use only if stuck)

### Hint 1
Split each line by `"|"`, check you get exactly 4 parts, then `.strip()`
each one.

### Hint 2
Wrap `float()` conversion in `try/except ValueError`.

### Hint 3
Collect valid parsed entries in a temporary list of dicts first — filtering,
sorting, and aggregation become straightforward after.

---

## 🔥 BONUS CHALLENGE

Add a field `"top_spender"` to the return dictionary:

- The `user_id` with the highest cumulative `WITHDRAWAL` total.
- If no withdrawals exist or no valid records exist, return `None`.

---

## IMPLEMENTATION

Write your solution in:

```
00_setup/diagnostics/solutions/transaction_log_analyzer.py
```
