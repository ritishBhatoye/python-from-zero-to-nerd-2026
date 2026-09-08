#!/usr/bin/env python3
"""
Fix generic example placeholders with specific test cases.
"""

import re
from pathlib import Path


def generate_specific_example(title: str, objective: str) -> str:
    """Generate specific example based on title and objective."""
    title_lower = title.lower()
    obj_lower = objective.lower()

    # 2D Array / Matrix
    if (
        "2d array" in title_lower
        or "2d_array" in title_lower
        or ("array" in title_lower and "element[i][j]" in objective)
    ):
        return """**Input:** `3,5`  
**Output:** `[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]`

The array has 3 rows and 5 columns, where `array[i][j] = i * j`"""

    # Square root formula (Q6)
    elif "square root" in title_lower or (
        "formula" in title_lower and "C" in objective and "D" in objective
    ):
        return """**Input:** `100,150,180`  
**Output:** `18,22,24`

Formula: `Q = √[(2 * C * D) / H]` where C=50, H=30  
For D=100: Q = √[(2*50*100)/30] = √333.33 ≈ 18"""

    # Sort words
    elif "sort" in title_lower and "word" in title_lower:
        return """**Input:** `without,hello,bag,world`  
**Output:** `bag,hello,without,world`

Words sorted alphabetically"""

    # Capitalize
    elif "capitalize" in title_lower or (
        "line" in title_lower and "upper" in obj_lower
    ):
        return """**Input:**
```
Hello world
Practice makes perfect
```
**Output:**
```
HELLO WORLD
PRACTICE MAKES PERFECT
```"""

    # Remove duplicates
    elif "remove duplicates" in title_lower or (
        "duplicate" in title_lower and "sort" in title_lower
    ):
        return """**Input:** `hello world and practice makes perfect and hello world again`  
**Output:** `again and hello makes perfect practice world`

Unique words sorted alphabetically"""

    # Binary divisible
    elif "binary" in title_lower and "divisible" in title_lower:
        return """**Input:** `0100,0011,1010,1001`  
**Output:** `1010`

0100 = 4 (not divisible by 5)  
1010 = 10 (divisible by 5) ✓"""

    # All even digits
    elif "even digits" in title_lower or "each digit" in obj_lower:
        return """**Input:** Range 1000-3000  
**Output:** `2000,2002,2004,2006,2008,2020,2022,...,2888`

Numbers where every digit is even (0,2,4,6,8)"""

    # Count letters and digits
    elif "letter" in title_lower and "digit" in title_lower and "count" in title_lower:
        return """**Input:** `hello world! 123`  
**Output:**
```
LETTERS 10
DIGITS 3
```"""

    # Count upper/lower case
    elif "upper" in title_lower and "lower" in title_lower and "case" in title_lower:
        return """**Input:** `Hello world!`  
**Output:**
```
UPPER CASE 1
LOWER CASE 9
```"""

    # a+aa+aaa+aaaa pattern
    elif "a+aa" in title_lower or ("compute" in obj_lower and "a+aa" in obj_lower):
        return """**Input:** `9`  
**Output:** `11106`

Calculation: 9 + 99 + 999 + 9999 = 11106"""

    # Filter odd numbers
    elif "filter" in title_lower and "odd" in title_lower:
        return """**Input:** `1,2,3,4,5,6,7,8,9`  
**Output:** `1,3,5,7,9`

Only odd numbers"""

    # Bank transaction
    elif "bank" in title_lower or "transaction" in title_lower:
        return """**Input:**
```
D 300
D 300
W 200
D 100
```
**Output:** `500`

D = Deposit, W = Withdrawal  
Net: 300 + 300 - 200 + 100 = 500"""

    # String operations
    if "string integer sum" in title_lower or (
        "string" in title_lower and "sum" in title_lower and "integer" in obj_lower
    ):
        return """**Input:** `s1="3", s2="4"`  
**Output:** `7`

**Input:** `s1="10", s2="25"`  
**Output:** `35`"""

    elif "concatenat" in title_lower or (
        "string" in title_lower and "concatenat" in obj_lower
    ):
        return """**Input:** `s1="Hello", s2="World"`  
**Output:** `"HelloWorld"`

**Input:** `s1="Python", s2="3"`  
**Output:** `"Python3"`"""

    elif "longer" in title_lower or "maximum length" in title_lower:
        return """**Input:** `s1="hello", s2="world"`  
**Output:** `"hello"` (or `"world"` if equal, print both)

**Input:** `s1="Python", s2="AI"`  
**Output:** `"Python"`"""

    elif "input" in title_lower and "output" in title_lower and "class" in title_lower:
        return """**Input:** `"Hello Python"`  
**Output:** `"HELLO PYTHON"`

The class should:
- `getString()`: Accept input
- `printString()`: Print uppercase version"""

    elif "docstring" in title_lower or "documentation" in title_lower:
        return """**Example:**
```python
print(abs.__doc__)  # Prints documentation for abs()
print(my_function.__doc__)  # Prints your function's docstring
```"""

    elif "class" in title_lower and "instance" in title_lower:
        return """**Example:**
```python
class Person:
    name = "Person"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

p = Person("Alice")
print(Person.name)  # "Person"
print(p.name)       # "Alice"
```"""

    elif "list" in title_lower and "square" in title_lower:
        return """**Input:** `n=5`  
**Output:** `[1, 4, 9, 16, 25]`

**Input:** `n=3`  
**Output:** `[1, 4, 9]`"""

    elif "first" in title_lower and "element" in title_lower:
        return """**Input:** `lst=[1,2,3,4,5], n=3`  
**Output:** `[1, 2, 3]`

**Input:** `lst=[10,20,30], n=2`  
**Output:** `[10, 20]`"""

    elif "last" in title_lower and "element" in title_lower:
        return """**Input:** `lst=[1,2,3,4,5], n=3`  
**Output:** `[3, 4, 5]`

**Input:** `lst=[10,20,30], n=2`  
**Output:** `[20, 30]`"""

    elif "tuple" in title_lower and "converter" in title_lower:
        return """**Input:** `[1, 2, 3, 4, 5]`  
**Output:** `(1, 2, 3, 4, 5)`

**Input:** `["a", "b", "c"]`  
**Output:** `("a", "b", "c")`"""

    elif "dictionary" in title_lower and (
        "square" in title_lower or "generator" in title_lower
    ):
        if "range" in title_lower or "1-20" in title_lower:
            return """**Output:** `{1: 1, 2: 4, 3: 9, ..., 20: 400}`

Generates dictionary where key=i, value=i² for i in range(1, 21)"""
        else:
            return """**Input:** `n=5`  
**Output:** `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`"""

    elif "values only" in title_lower or (
        "dict" in title_lower and "value" in title_lower
    ):
        return """**Example:**
```python
d = {1: 1, 2: 4, 3: 9}
# Print: 1, 4, 9 (values only)
```"""

    elif "keys only" in title_lower or ("dict" in title_lower and "key" in title_lower):
        return """**Example:**
```python
d = {1: 1, 2: 4, 3: 9}
# Print: 1, 2, 3 (keys only)
```"""

    elif "even" in title_lower and "checker" in title_lower:
        return """**Input:** `4`  
**Output:** `"It is an even number"`

**Input:** `7`  
**Output:** `"It is an odd number"`"""

    # Default for remaining cases
    return """**See objective and requirements for expected behavior.**"""


def fix_generic_example(file_path: Path):
    """Replace generic example with specific one."""
    content = file_path.read_text()

    # Check if has any generic example variant
    has_generic = (
        "Example usage:" in content
        or "See objective above for expected behavior and test cases" in content
        or "See objective and requirements for expected behavior" in content
    )

    if not has_generic:
        return False

    # Extract title and objective
    title_match = re.search(r"# Exercise \d+ — (.+)", content)
    title = title_match.group(1) if title_match else ""

    obj_match = re.search(r"## Objective\n\n(.+?)(?=\n---|\n##|$)", content, re.DOTALL)
    objective = obj_match.group(1).strip() if obj_match else ""

    # Generate specific example
    new_example = generate_specific_example(title, objective)

    # Try different patterns
    patterns = [
        r"\*\*Example usage:\*\*\n```python\n# See objective above for expected behavior\n```",
        r"\*\*See objective above for expected behavior and test cases\.\*\*",
        r"\*\*See objective and requirements for expected behavior\.\*\*",
    ]

    for pattern in patterns:
        if re.search(pattern, content):
            new_content = re.sub(pattern, new_example, content)
            file_path.write_text(new_content)
            print(f"✅ Fixed {file_path.name}: {title}")
            return True

    print(f"⚠️  Pattern not found in {file_path.name}")
    return False


def main():
    """Fix all generic examples."""
    base = Path(
        "/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026/01_core_python"
    )

    # Find all problem files with any generic example variant
    files_to_fix = []
    for level_dir in ["level_1_beginner", "level_2_intermediate", "level_3_advanced"]:
        problem_dir = base / level_dir / "problems"
        if problem_dir.exists():
            for file_path in problem_dir.glob("*.md"):
                content = file_path.read_text()
                if (
                    "Example usage:" in content
                    or "See objective above for expected behavior and test cases"
                    in content
                    or "See objective and requirements for expected behavior" in content
                ):
                    files_to_fix.append(file_path)

    print(f"Found {len(files_to_fix)} files with generic examples\n")

    fixed = 0
    for file_path in sorted(files_to_fix):
        if fix_generic_example(file_path):
            fixed += 1

    print("\n📊 Summary:")
    print(f"   ✅ Fixed: {fixed}")
    print(f"   📝 Total: {len(files_to_fix)}")


if __name__ == "__main__":
    main()
