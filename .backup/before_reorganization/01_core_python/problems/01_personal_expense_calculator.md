# Exercise 01 — Personal Expense Calculator

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 1 — Beginner  
**Inspired by:** New (curriculum original)  
**Status:** 🔴 Not started

## Concepts

- variables
- strings
- numbers
- basic arithmetic
- f-strings

## Prerequisites

- Basic Python syntax (variables, numbers, strings)

---

## Objective

Calculate a simple monthly expense summary — something you'd do in a personal budget spreadsheet or finance app.

---

## Requirements

Implement:

```python
def calculate_expenses(name: str, rent: float, food: float, transport: float) -> dict:
```

Return a dictionary with these exact keys:

| Key | Type | Description |
|-----|------|-------------|
| `name` | str | The person's name |
| `rent` | float | Rent amount |
| `food` | float | Food amount |
| `transport` | float | Transport amount |
| `total` | float | Sum of all three (rounded to 2 decimals) |
| `average` | float | Average of the three (rounded to 2 decimals) |
| `highest_category` | str | `"rent"`, `"food"`, or `"transport"` — whichever is highest |
| `summary` | str | See format below |

### Summary format

```
"<name> spent a total of <total> across 3 categories."
```

Example: `"Ritish spent a total of 25500.0 across 3 categories."`

---

## Examples

```python
calculate_expenses("Ritish", 15000, 8000, 2500)
# total = 25500.0, average = 8500.0, highest_category = "rent"
```

---

## Constraints

- Basic Python only — no imports required
- Loops/conditionals optional (a simple `if` or `max()` for highest category is fine)

---

## Edge Cases

- All three amounts equal → pick any of the three category names consistently (document your choice)
- Zero values are valid

---

## Test Command

```bash
pytest 01_core_python/tests/test_01_personal_expense_calculator.py -v
```

---

## Hints (use only if stuck)

1. Start with `total = rent + food + transport`
2. Average: `total / 3`
3. Compare the three values with `if/elif/else` or `max()` with a dict

---

## Implementation

```
01_core_python/solutions/01_personal_expense_calculator.py
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
./scripts/commit_exercise.sh feat core 01_personal_expense_calculator
```
