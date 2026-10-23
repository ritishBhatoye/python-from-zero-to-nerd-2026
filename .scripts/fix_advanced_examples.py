#!/usr/bin/env python3
"""Fix generic examples in advanced level problems."""

import re
from pathlib import Path


def generate_example_from_objective(title: str, objective: str) -> str:
    """Generate a specific example based on title and objective."""
    
    # Map of patterns to examples
    examples_map = {
        "password": ('**Input:** `"Abc123@pwd,weakpass,Valid1@"`\n'
                    '**Output:** `"Abc123@pwd,Valid1@"`\n\n'
                    'Only passwords meeting all criteria are returned.'),
        "sort tuples": ('**Input:** `[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]`\n'
                       '**Output:** `[(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]`\n\n'
                       'Sorted by first element, then by second element.'),
        "generator": ('**Output:** `0,7,14,21,28,...`\n\n'
                     'Generates numbers divisible by 7 using yield.'),
        "robot": ('**Input:** `"UP 5,DOWN 3,LEFT 3,RIGHT 2"`\n'
                 '**Output:** `2` (distance from origin)\n\n'
                 'Calculate Euclidean distance after all movements.'),
        "frequency": ('**Input:** `"New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."`\n'
                     '**Output:** `{"2": 2, "3.": 1, "3?": 1, "New": 1, "Python": 5, "Read": 1, "and": 1, ...}`\n\n'
                     'Count word frequency (case insensitive).'),
        "static method": ('**Example:**\n```python\nAmerican.print_nationality()  # Output: America\n```'),
        "inheritance": ('**Example:**\n```python\nsubclass = Person("John")\nsubclass.get_name()  # Returns: John\n```'),
        "circle": ('**Input:** `radius = 5`\n'
                  '**Output:** `78.54`\n\n'
                  'Calculate area using π * r².'),
        "rectangle": ('**Input:** `length = 5, width = 3`\n'
                     '**Output:** `15`\n\n'
                     'Calculate area using length × width.'),
        "shape": ('**Example:**\n```python\ns = Square(5)\nprint(s.area())  # Output: 25\n```'),
        "runtimeerror": ('**Output:** Raises `RuntimeError` with custom message.'),
        "division": ('**Input:** `10 / 2`\n'
                    '**Output:** `5.0`\n\n'
                    '**Input:** `10 / 0`\n'
                    '**Output:** Error message handled by except block.'),
        "exception": ('**Example:**\n```python\nraise CustomError("Error message")\n```'),
        "email username": ('**Input:** `"john.doe@example.com"`\n'
                          '**Output:** `"john.doe"`'),
        "email company": ('**Input:** `"john.doe@example.com"`\n'
                         '**Output:** `"example"`'),
        "digits": ('**Input:** `"abc123def456"`\n'
                  '**Output:** `"123456"`'),
        "unicode": ('**Example:**\n```python\nu = "Hello, 世界"\nprint(u)  # Output: Hello, 世界\n```'),
        "ascii": ('**Input:** ASCII string\n'
                 '**Output:** Unicode representation'),
        "comment": ('**Example:** File with Unicode comment character.'),
        "series sum": ('**Input:** `n = 3`\n'
                      '**Output:** `1.8333` (1/2 + 2/3 + 3/4)'),
        "recursive": ('**Input:** `n = 5`\n'
                     '**Output:** `500` (100 + 100 + 100 + 100 + 100)'),
        "fibonacci number": ('**Input:** `n = 7`\n'
                            '**Output:** `13`\n\n'
                            'The 7th Fibonacci number.'),
        "fibonacci sequence": ('**Input:** `n = 8`\n'
                              '**Output:** `[0, 1, 1, 2, 3, 5, 8, 13]`\n\n'
                              'First 8 Fibonacci numbers.'),
        "divisible 5 and 7": ('**Output:** Numbers divisible by both 5 and 7: `0, 35, 70, 105, ...`'),
        "eval": ('**Input:** `"2+3*4"`\n'
                '**Output:** `14`\n\n'
                'Evaluate mathematical expression.'),
        "binary search": ('**Input:** `[1, 3, 5, 7, 9], target=5`\n'
                         '**Output:** `2` (index of 5)'),
        "random float 10": ('**Output:** Random float between 10.0 and 100.0'),
        "random float 5": ('**Output:** Random float between 5.0 and 95.0'),
        "random list": ('**Output:** List of 5 random numbers: `[3, 17, 8, 22, 15]`'),
        "random integer 7": ('**Output:** Random integer between 7 and 15'),
        "compress": ('**Input:** `"hello world"`\n'
                    '**Output:** Compressed and decompressed string'),
        "execution time": ('**Output:** Prints execution time of function'),
        "shuffle": ('**Input:** `[1, 2, 3, 4, 5]`\n'
                   '**Output:** `[3, 1, 5, 2, 4]` (random order)'),
        "sentences": ('**Input:** Subject/verb/object lists\n'
                     '**Output:** Generated sentences like "I love Python"'),
        "remove divisible": ('**Input:** `[7, 14, 21, 35, 42]`\n'
                            '**Output:** `[]` (all removed)\n\n'
                            'Removes numbers divisible by both 5 and 7.'),
        "3d array": ('**Output:** `[[[0, 0], [0, 0]], [[0, 0], [0, 0]]]`\n\n'
                    'Creates 2x2x2 array of zeros.'),
        "remove indices": ('**Input:** `[1, 2, 3, 4, 5], indices=[0, 2, 4]`\n'
                          '**Output:** `[2, 4]`'),
        "remove value": ('**Input:** `[10, 24, 35, 24, 50]`\n'
                        '**Output:** `[10, 35, 50]`'),
        "intersection": ('**Input:** `list1=[1,2,3], list2=[2,3,4]`\n'
                        '**Output:** `[2, 3]`'),
        "person gender": ('**Example:**\n```python\nmale = Male("John")\nprint(male.get_gender())  # Output: Male\n```'),
        "character count": ('**Input:** `"hello"`\n'
                           '**Output:** `{\'h\': 1, \'e\': 1, \'l\': 2, \'o\': 1}`'),
        "reverse": ('**Input:** `"hello"`\n'
                   '**Output:** `"olleh"`'),
        "permutations": ('**Input:** `"abc"`\n'
                        '**Output:** `["abc", "acb", "bac", "bca", "cab", "cba"]`'),
        "chickens and rabbits": ('**Input:** `heads=35, legs=94`\n'
                                '**Output:** `chickens=23, rabbits=12`\n\n'
                                'Solve: c + r = 35, 2c + 4r = 94'),
    }
    
    # Find matching pattern
    key = title.lower()
    for pattern, example in examples_map.items():
        if pattern in key or pattern in objective.lower():
            return example
    
    # Fallback
    return f'**See test cases in test file for expected input/output examples.**'


def fix_file(file_path: Path) -> bool:
    """Fix a single file."""
    content = file_path.read_text()
    
    if "See objective and requirements for expected behavior" not in content:
        return False
    
    # Extract title and objective
    title_match = re.search(r"# Exercise \d+ — (.+)", content)
    title = title_match.group(1) if title_match else ""
    
    obj_match = re.search(r"## Objective\n\n(.+?)(?=\n---|$)", content, re.DOTALL)
    objective = obj_match.group(1).strip() if obj_match else ""
    
    # Generate example
    example = generate_example_from_objective(title, objective)
    
    # Replace
    new_content = content.replace(
        "**See objective and requirements for expected behavior.**",
        example
    )
    
    if new_content != content:
        file_path.write_text(new_content)
        print(f"✅ Fixed: {file_path.name} - {title}")
        return True
    
    return False


def main():
    base = Path("/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026/01_core_python")
    problems_dir = base / "level_3_advanced" / "problems"
    
    files = sorted(problems_dir.glob("*.md"))
    fixed = 0
    
    for f in files:
        if fix_file(f):
            fixed += 1
    
    print(f"\n📊 Fixed {fixed} files")


if __name__ == "__main__":
    main()
