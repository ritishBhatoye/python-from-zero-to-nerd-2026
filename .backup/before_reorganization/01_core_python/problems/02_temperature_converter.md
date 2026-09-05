# Exercise 02 — Temperature Converter

**Phase:** `01_core_python`  
**Type:** micro  
**Difficulty:** Level 0 — Warm-up  
**Inspired by:** New  
**Status:** 🔴 Not started

## Concepts

- variables, arithmetic, functions, conditionals

## Prerequisites

- Exercise 01

---

## Objective

Convert temperatures between Celsius, Fahrenheit, and Kelvin — a everyday utility function.

---

## Requirements

```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
```

Supported units (case-insensitive): `"C"`, `"F"`, `"K"`.

Formulas:
- C → F: `(value * 9/5) + 32`
- C → K: `value + 273.15`
- F → C: `(value - 32) * 5/9`
- F → K: convert F → C → K
- K → C: `value - 273.15`
- K → F: convert K → C → F
- Same unit → return `value` unchanged

Round the result to **2 decimal places**.

Raise `ValueError` if `from_unit` or `to_unit` is not C, F, or K.

---

## Examples

```python
convert_temperature(0, "C", "F")    # 32.0
convert_temperature(100, "C", "K")  # 373.15
convert_temperature(32, "F", "C")   # 0.0
convert_temperature(25, "c", "f")   # 77.0  (case-insensitive)
```

---

## Edge Cases

- Negative temperatures
- Same-unit conversion returns input (rounded)

---

## Test Command

```bash
pytest 01_core_python/tests/test_02_temperature_converter.py -v
```

---

## Implementation

```
01_core_python/solutions/02_temperature_converter.py
```

---

## Suggested Commit

```bash
./scripts/commit_exercise.sh feat core 02_temperature_converter
```
