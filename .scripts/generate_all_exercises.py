#!/usr/bin/env python3
"""
Generate all 100+ Python exercises from the zhiwehu collection.
Organized by difficulty: Level 1 (Beginner) → Level 2 (Intermediate) → Level 3 (Advanced)
"""

import json
from pathlib import Path

# Load exercise data
script_dir = Path(__file__).parent
with open(script_dir / "exercises_data.json") as f:
    EXERCISES = json.load(f)


def slugify(title: str) -> str:
    """Convert title to filename slug."""
    return title.lower().replace(" ", "_").replace("-", "_").replace("/", "_")


def create_problem_md(ex: dict) -> str:
    """Generate problem markdown file content."""
    level_name = {1: "Beginner", 2: "Intermediate", 3: "Advanced"}[ex["level"]]
    slug = slugify(ex["title"])

    return f"""# Exercise {ex["q"]:03d} — {ex["title"]}

**Phase:** `01_core_python`  
**Level:** {ex["level"]} — {level_name}  
**Source:** zhiwehu/Python-programming-exercises Q{ex["q"]}  
**Status:** 🔴 Not started

## Concepts

- See problem description

## Prerequisites

- Basic Python knowledge

---

## Objective

{ex["desc"]}

---

## Requirements

Implement the solution as described above.

---

## Hints (use only if stuck)

1. Refer to the problem description
2. Consider using appropriate data structures
3. Test with multiple inputs

---

## Test Command

```bash
pytest 01_core_python/level_{ex["level"]}_{"beginner" if ex["level"] == 1 else "intermediate" if ex["level"] == 2 else "advanced"}/tests/test_{ex["q"]:03d}_{slug}.py -v
```

---

## Implementation

```
01_core_python/level_{ex["level"]}_{"beginner" if ex["level"] == 1 else "intermediate" if ex["level"] == 2 else "advanced"}/solutions/{ex["q"]:03d}_{slug}.py
```

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key Python concepts used:**
- **How I could improve this:**
"""


def create_solution_py(ex: dict) -> str:
    """Generate solution starter file."""
    slug = slugify(ex["title"])

    return f'''"""Exercise {ex["q"]:03d} — {ex["title"]}.

{ex["desc"]}
"""


# Your implementation here
pass


if __name__ == "__main__":
    # Test your solution
    print("Implement me!")
'''


def create_test_py(ex: dict) -> str:
    """Generate test file."""
    slug = slugify(ex["title"])
    class_name = "".join(word.capitalize() for word in ex["title"].split())

    return f'''"""Tests for Exercise {ex["q"]:03d} — {ex["title"]}."""

from __future__ import annotations

import pytest
import sys
import importlib.util
from pathlib import Path

solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))

try:
    spec = importlib.util.spec_from_file_location(
        "solution",
        solutions_dir / "{ex["q"]:03d}_{slug}.py"
    )
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
except (FileNotFoundError, AttributeError):
    pytest.skip("Solution not implemented yet", allow_module_level=True)


class Test{class_name.replace(" ", "").replace("-", "")}:
    def test_placeholder(self):
        """Placeholder test - implement based on requirements."""
        assert True  # Replace with actual tests
'''


def main():
    """Generate all exercise files."""
    base = Path(
        "/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026/01_core_python"
    )

    # Sort by question number
    sorted_exercises = sorted(EXERCISES, key=lambda x: x["q"])

    for ex in sorted_exercises:
        level_dir = {
            1: "level_1_beginner",
            2: "level_2_intermediate",
            3: "level_3_advanced",
        }[ex["level"]]

        slug = slugify(ex["title"])

        # Create files
        problem_path = base / level_dir / "problems" / f"{ex['q']:03d}_{slug}.md"
        solution_path = base / level_dir / "solutions" / f"{ex['q']:03d}_{slug}.py"
        test_path = base / level_dir / "tests" / f"test_{ex['q']:03d}_{slug}.py"

        problem_path.write_text(create_problem_md(ex))
        solution_path.write_text(create_solution_py(ex))
        test_path.write_text(create_test_py(ex))

        print(f"✅ Created Exercise {ex['q']:03d}: {ex['title']}")

    print(f"\n🎉 Generated {len(sorted_exercises)} exercises!")

    # Summary by level
    level_1 = len([e for e in sorted_exercises if e["level"] == 1])
    level_2 = len([e for e in sorted_exercises if e["level"] == 2])
    level_3 = len([e for e in sorted_exercises if e["level"] == 3])

    print("\n📊 Summary:")
    print(f"   Level 1 (Beginner): {level_1} exercises")
    print(f"   Level 2 (Intermediate): {level_2} exercises")
    print(f"   Level 3 (Advanced): {level_3} exercises")
    print(f"   Total: {level_1 + level_2 + level_3} exercises")


if __name__ == "__main__":
    main()
