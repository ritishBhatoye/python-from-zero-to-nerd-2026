#!/usr/bin/env python3
"""
Add example test cases to all exercise problem files.
"""

import re
from pathlib import Path

# Define examples for each exercise based on title/number
EXAMPLES = {
    "001_divisible": """**Output:**
```
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,...,3192,3199
```
The output should be a comma-separated string of all numbers between 2000-3200 that are divisible by 7 but NOT divisible by 5.""",
    "002_factorial": """**Input:** `5`  
**Output:** `120`

**Input:** `8`  
**Output:** `40320`

**Input:** `0`  
**Output:** `1`""",
    "003_dictionary": """**Input:** `n = 8`  
**Output:** `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}`""",
    "004_comma_separated": """**Input:** `34,67,55,33,12,98`  
**Output:**
```python
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```""",
    "005_string_class": """**Input:** `Hello World`  
**Output:** `HELLO WORLD`""",
    "006_square_root": """**Input:** `100,150,180`  
**Output:** `18,22,24`

Formula: Q = √[(2 * C * D) / H] where C=50, H=30""",
    "007_2d_array": """**Input:** `3,5`  
**Output:** `[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]`""",
    "008_sort": """**Input:** `without,hello,bag,world`  
**Output:** `bag,hello,without,world`""",
    "009_capitalize": """**Input:**
```
Hello world
Practice makes perfect
```
**Output:**
```
HELLO WORLD
PRACTICE MAKES PERFECT
```""",
    "010_remove_duplicates": """**Input:** `hello world and practice makes perfect and hello world again`  
**Output:** `again and hello makes perfect practice world`""",
}


# Generic examples for common patterns
def generate_example(title: str, objective: str) -> str:
    """Generate example based on title and objective."""
    title_lower = title.lower()

    # Pattern matching for common exercise types
    if "sum" in title_lower and "two" in title_lower:
        return """**Input:** `a=5, b=3`  
**Output:** `8`"""

    elif "factorial" in title_lower:
        return """**Input:** `5`  
**Output:** `120`"""

    elif "even" in title_lower and "odd" in title_lower:
        return """**Input:** `4`  
**Output:** `It is an even number`

**Input:** `7`  
**Output:** `It is an odd number`"""

    elif "square" in title_lower:
        return """**Input:** `5`  
**Output:** `25`"""

    elif "string" in title_lower and "upper" in title_lower:
        return """**Input:** `hello`  
**Output:** `HELLO`"""

    elif "string" in title_lower and "lower" in title_lower:
        return """**Input:** `HELLO`  
**Output:** `hello`"""

    elif "list" in title_lower and "square" in title_lower:
        return """**Output:** `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...]`"""

    elif "dictionary" in title_lower and "square" in title_lower:
        return """**Output:** `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, ...}`"""

    elif "filter" in title_lower or "even" in title_lower:
        return """**Input:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
**Output:** `[2, 4, 6, 8, 10]`"""

    elif "map" in title_lower:
        return """**Input:** `[1, 2, 3, 4, 5]`  
**Output:** `[1, 4, 9, 16, 25]`"""

    else:
        # Generic example
        return """**Example usage:**
```python
# See objective above for expected behavior
```"""


def add_examples_to_file(file_path: Path):
    """Add examples section to a problem file if missing."""
    content = file_path.read_text()

    # Check if Examples section already exists
    if "## Examples" in content or "## Example" in content:
        print(f"⏭️  Skipping {file_path.name} - already has examples")
        return False

    # Extract title
    title_match = re.search(r"# Exercise \d+ — (.+)", content)
    title = title_match.group(1) if title_match else ""

    # Extract objective
    obj_match = re.search(r"## Objective\n\n(.+?)(?=\n---|\n##|$)", content, re.DOTALL)
    objective = obj_match.group(1).strip() if obj_match else ""

    # Generate example
    example = generate_example(title, objective)

    # Try pattern 1: After Requirements, before Hints (collection exercises)
    pattern1 = r"(## Requirements\n\n.+?\n\n---\n\n)(## Hints)"

    # Try pattern 2: After Requirements table/section (original exercises)
    pattern2 = r"(### Summary format.+?\n\n)(---\n\n## Test)"
    pattern3 = r"(Return a dictionary.+?\n\n)(---\n\n## Test)"
    pattern4 = r"(## Requirements\n\n.+?\n)(---\n\n## Test)"

    if re.search(pattern1, content, re.DOTALL):
        new_content = re.sub(
            pattern1,
            rf"\1## Examples\n\n{example}\n\n---\n\n\2",
            content,
            flags=re.DOTALL,
        )
        file_path.write_text(new_content)
        print(f"✅ Added example to {file_path.name}")
        return True
    elif re.search(pattern2, content, re.DOTALL):
        new_content = re.sub(
            pattern2,
            rf"\1\n---\n\n## Examples\n\n{example}\n\n---\n\n## Test",
            content,
            flags=re.DOTALL,
        )
        file_path.write_text(new_content)
        print(f"✅ Added example to {file_path.name}")
        return True
    elif re.search(pattern3, content, re.DOTALL):
        new_content = re.sub(
            pattern3,
            rf"\1\n---\n\n## Examples\n\n{example}\n\n---\n\n## Test",
            content,
            flags=re.DOTALL,
        )
        file_path.write_text(new_content)
        print(f"✅ Added example to {file_path.name}")
        return True
    elif re.search(pattern4, content, re.DOTALL):
        new_content = re.sub(
            pattern4,
            rf"\1\n---\n\n## Examples\n\n{example}\n\n---\n\n## Test",
            content,
            flags=re.DOTALL,
        )
        file_path.write_text(new_content)
        print(f"✅ Added example to {file_path.name}")
        return True
    else:
        print(f"⚠️  Could not find insertion point in {file_path.name}")
        return False


def main():
    """Add examples to all problem files."""
    base = Path(
        "/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026/01_core_python"
    )

    # Find all problem files
    problem_files = []
    for level_dir in ["level_1_beginner", "level_2_intermediate", "level_3_advanced"]:
        problem_dir = base / level_dir / "problems"
        if problem_dir.exists():
            problem_files.extend(sorted(problem_dir.glob("*.md")))

    print(f"Found {len(problem_files)} problem files\n")

    added = 0
    skipped = 0
    failed = 0

    for file_path in problem_files:
        result = add_examples_to_file(file_path)
        if result is True:
            added += 1
        elif result is False and "already has examples" in str(result):
            skipped += 1
        else:
            failed += 1

    print("\n📊 Summary:")
    print(f"   ✅ Added examples: {added}")
    print(f"   ⏭️  Already had examples: {skipped}")
    print(f"   ⚠️  Failed: {failed}")
    print(f"   📝 Total: {len(problem_files)}")


if __name__ == "__main__":
    main()
