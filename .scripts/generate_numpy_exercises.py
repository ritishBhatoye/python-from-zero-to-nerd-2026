#!/usr/bin/env python3
"""Generate 100 NumPy exercises organized by difficulty level."""

from pathlib import Path


# Exercise data: (number, title, objective, difficulty_stars)
EXERCISES = [
    (1, "Import NumPy", "Import the numpy package under the name `np`", "★☆☆"),
    (2, "NumPy Version", "Print the numpy version and the configuration", "★☆☆"),
    (3, "Null Vector", "Create a null vector of size 10", "★☆☆"),
    (4, "Array Memory Size", "Find the memory size of any array", "★☆☆"),
    (5, "NumPy Documentation", "Get the documentation of the numpy add function from the command line", "★☆☆"),
    (6, "Vector with One Value", "Create a null vector of size 10 but the fifth value which is 1", "★☆☆"),
    (7, "Vector Range", "Create a vector with values ranging from 10 to 49", "★☆☆"),
    (8, "Reverse Vector", "Reverse a vector (first element becomes last)", "★☆☆"),
    (9, "3x3 Matrix", "Create a 3x3 matrix with values ranging from 0 to 8", "★☆☆"),
    (10, "Non-zero Indices", "Find indices of non-zero elements from [1,2,0,0,4,0]", "★☆☆"),
    (11, "Identity Matrix", "Create a 3x3 identity matrix", "★☆☆"),
    (12, "3D Random Array", "Create a 3x3x3 array with random values", "★☆☆"),
    (13, "Random Min Max", "Create a 10x10 array with random values and find the minimum and maximum values", "★☆☆"),
    (14, "Random Mean", "Create a random vector of size 30 and find the mean value", "★☆☆"),
    (15, "Border Array", "Create a 2d array with 1 on the border and 0 inside", "★☆☆"),
    (16, "Add Border", "Add a border (filled with 0's) around an existing array", "★☆☆"),
    (17, "NaN and Inf", "What is the result of expressions with np.nan and np.inf?", "★☆☆"),
    (18, "Diagonal Matrix", "Create a 5x5 matrix with values 1,2,3,4 just below the diagonal", "★☆☆"),
    (19, "Checkerboard", "Create a 8x8 matrix and fill it with a checkerboard pattern", "★☆☆"),
    (20, "3D Index", "Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?", "★☆☆"),
    (21, "Tile Checkerboard", "Create a checkerboard 8x8 matrix using the tile function", "★☆☆"),
    (22, "Normalize Matrix", "Normalize a 5x5 random matrix", "★☆☆"),
    (23, "Custom Dtype", "Create a custom dtype that describes a color as four unsigned bytes (RGBA)", "★☆☆"),
    (24, "Matrix Multiplication", "Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)", "★☆☆"),
    (25, "Negate Elements", "Given a 1D array, negate all elements which are between 3 and 8, in place", "★☆☆"),
    (26, "Sum Function", "What is the output of sum(range(5),-1) with and without numpy?", "★☆☆"),
    (27, "Legal Expressions", "Consider an integer vector Z, which expressions are legal?", "★☆☆"),
    (28, "Division Results", "What are the results of np.array(0) / np.array(0)?", "★☆☆"),
    (29, "Round Away", "How to round away from zero a float array?", "★☆☆"),
    (30, "Common Values", "How to find common values between two arrays?", "★☆☆"),
    (31, "Ignore Warnings", "How to ignore all numpy warnings (not recommended)?", "★☆☆"),
    (32, "Complex Sqrt", "Is np.sqrt(-1) == np.emath.sqrt(-1) true?", "★☆☆"),
    (33, "Date Operations", "How to get the dates of yesterday, today and tomorrow?", "★☆☆"),
    (34, "Month Dates", "How to get all the dates corresponding to the month of July 2016?", "★★☆"),
    (35, "In-place Operations", "How to compute ((A+B)*(-A/2)) in place (without copy)?", "★★☆"),
    (36, "Integer Part", "Extract the integer part of a random array of positive numbers using 4 different methods", "★★☆"),
    (37, "Matrix Row Values", "Create a 5x5 matrix with row values ranging from 0 to 4", "★★☆"),
    (38, "Generator Array", "Consider a generator function that generates 10 integers and use it to build an array", "★☆☆"),
    (39, "Linspace Exclude", "Create a vector of size 10 with values ranging from 0 to 1, both excluded", "★★☆"),
    (40, "Sort Vector", "Create a random vector of size 10 and sort it", "★★☆"),
    (41, "Fast Sum", "How to sum a small array faster than np.sum?", "★★☆"),
    (42, "Array Equality", "Consider two random arrays A and B, check if they are equal", "★★☆"),
    (43, "Immutable Array", "Make an array immutable (read-only)", "★★☆"),
    (44, "Cartesian to Polar", "Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates", "★★☆"),
    (45, "Replace Maximum", "Create random vector of size 10 and replace the maximum value by 0", "★★☆"),
    (46, "Structured Array XY", "Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area", "★★☆"),
    (47, "Cauchy Matrix", "Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))", "★★☆"),
    (48, "Scalar Types", "Print the minimum and maximum representable values for each numpy scalar type", "★★☆"),
    (49, "Print All Values", "How to print all the values of an array?", "★★☆"),
    (50, "Closest Value", "How to find the closest value (to a given scalar) in a vector?", "★★☆"),
    (51, "Position Color", "Create a structured array representing a position (x,y) and a color (r,g,b)", "★★☆"),
    (52, "Point Distances", "Consider a random vector with shape (100,2) representing coordinates, find point by point distances", "★★☆"),
    (53, "Float to Int", "How to convert a float (32 bits) array into an integer (32 bits) array in place?", "★★☆"),
    (54, "Read CSV", "How to read a CSV file with missing values?", "★★☆"),
    (55, "Enumerate Array", "What is the equivalent of enumerate for numpy arrays?", "★★☆"),
    (56, "Gaussian Array", "Generate a generic 2D Gaussian-like array", "★★☆"),
    (57, "Random Placement", "How to randomly place p elements in a 2D array?", "★★☆"),
    (58, "Subtract Mean Row", "Subtract the mean of each row of a matrix", "★★☆"),
    (59, "Sort by Column", "How to sort an array by the nth column?", "★★☆"),
    (60, "Null Columns", "How to tell if a given 2D array has null columns?", "★★☆"),
    (61, "Nearest Value", "Find the nearest value from a given value in an array", "★★☆"),
    (62, "Iterator Sum", "Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator?", "★★☆"),
    (63, "Array Class", "Create an array class that has a name attribute", "★★☆"),
    (64, "Add by Index", "Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)?", "★★★"),
    (65, "Accumulate Elements", "How to accumulate elements of a vector (X) to an array (F) based on an index list (I)?", "★★★"),
    (66, "Unique Colors", "Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors", "★★☆"),
    (67, "Sum Last Axes", "Considering a four dimensions array, how to get sum over the last two axis at once?", "★★★"),
    (68, "Subset Means", "Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices?", "★★★"),
    (69, "Dot Diagonal", "How to get the diagonal of a dot product?", "★★★"),
    (70, "Interleave Zeros", "Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value?", "★★★"),
    (71, "Multiply Arrays", "Consider an array of dimension (5,5,3), how to multiply it by an array with dimensions (5,5)?", "★★★"),
    (72, "Swap Rows", "How to swap two rows of an array?", "★★★"),
    (73, "Unique Segments", "Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the triangles", "★★★"),
    (74, "Bincount Inverse", "Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C?", "★★★"),
    (75, "Sliding Window", "How to compute averages using a sliding window over an array?", "★★★"),
    (76, "Shifted Rows", "Considering a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is shifted by 1", "★★★"),
    (77, "Negate Inplace", "How to negate a boolean, or to change the sign of a float inplace?", "★★★"),
    (78, "Point to Line", "Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i?", "★★★"),
    (79, "Points to Lines", "Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j to each line i?", "★★★"),
    (80, "Extract Subpart", "Consider an arbitrary array, write a function that extracts a subpart with a fixed shape and centered on a given element (pad with a fill value when necessary)", "★★★"),
    (81, "Rolling Windows", "Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]?", "★★★"),
    (82, "Matrix Rank", "Compute a matrix rank", "★★★"),
    (83, "Most Frequent", "How to find the most frequent value in an array?", "★★★"),
    (84, "Extract Blocks", "Extract all the contiguous 3x3 blocks from a random 10x10 matrix", "★★★"),
    (85, "Symmetric Array", "Create a 2D array subclass such that Z[i,j] == Z[j,i]", "★★★"),
    (86, "Matrix Products", "Consider a set of p matrices with shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of the p matrix products at once?", "★★★"),
    (87, "Block Sum", "Consider a 16x16 array, how to get the block-sum (block size is 4x4)?", "★★★"),
    (88, "Game of Life", "How to implement the Game of Life using numpy arrays?", "★★★"),
    (89, "N Largest Values", "How to get the n largest values of an array?", "★★★"),
    (90, "Cartesian Product", "Given an arbitrary number of vectors, build the cartesian product (every combination of every item)", "★★★"),
    (91, "Record Array", "How to create a record array from a regular array?", "★★★"),
    (92, "Power Methods", "Consider a large vector Z, compute Z to the power of 3 using 3 different methods", "★★★"),
    (93, "Row Containment", "Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain at least one element of each row of B regardless of order?", "★★★"),
    (94, "Unequal Rows", "Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3])", "★★★"),
    (95, "Binary Representation", "Convert a vector of ints into a matrix binary representation", "★★★"),
    (96, "Unique Rows", "Given a two dimensional array, how to extract unique rows?", "★★★"),
    (97, "Einsum Operations", "Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function", "★★★"),
    (98, "Sample Path", "Considering a path described by two vectors (X,Y), how to sample it using equidistant samples?", "★★★"),
    (99, "Multinomial Rows", "Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees", "★★★"),
    (100, "Bootstrap CI", "Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (resample elements with replacement N times, compute mean of each sample, then compute percentiles)", "★★★"),
]


def create_problem_file(num: int, title: str, objective: str, stars: str, level_dir: Path) -> None:
    """Create a problem markdown file."""
    level_name = level_dir.name.replace("level_", "").replace("_", " ").title()
    
    # Generate example based on exercise number
    example = generate_example(num, title, objective)
    
    content = f"""# Exercise {num:03d} — {title}

**Phase:** `14_data_engineering`  
**Topic:** NumPy Fundamentals  
**Level:** {level_name}  
**Difficulty:** {stars}  
**Status:** 🔴 Not started

## Concepts

- NumPy arrays
- Array operations
- See problem description

## Prerequisites

- NumPy installed (`pip install numpy`)
- Basic Python knowledge

---

## Objective

{objective}

---

## Requirements

Implement the solution as described above.

---

## Examples

{example}

---

## Hints (use only if stuck)

1. Review NumPy documentation for relevant functions
2. Consider array shape and dtype
3. Test with simple cases first

---

## Test Command

```bash
pytest 14_data_engineering/01_numpy_fundamentals/{level_dir.name}/tests/test_{num:03d}_{title.lower().replace(' ', '_').replace('-', '_')}.py -v
```

---

## Implementation

```
14_data_engineering/01_numpy_fundamentals/{level_dir.name}/solutions/{num:03d}_{title.lower().replace(' ', '_').replace('-', '_')}.py
```

---

## Reflection (fill after solving)

- **What I learned:**
- **Mistakes I made:**
- **Key NumPy concepts used:**
- **How I could improve this:**
"""
    
    filename = f"{num:03d}_{title.lower().replace(' ', '_').replace('-', '_')}.md"
    file_path = level_dir / "problems" / filename
    file_path.write_text(content)
    print(f"✅ Created: {file_path.name}")


def generate_example(num: int, title: str, objective: str) -> str:
    """Generate example based on exercise number."""
    examples = {
        1: "```python\nimport numpy as np\n```",
        2: "```python\nprint(np.__version__)\nnp.show_config()\n```",
        3: "**Output:** `array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])`",
        4: "**Input:** `arr = np.zeros((10,10))`\n**Output:** `800` (bytes for 10x10 float64 array)",
        5: "Run: `python -c \"import numpy; numpy.info(numpy.add)\"`",
        6: "**Output:** `array([0., 0., 0., 0., 1., 0., 0., 0., 0., 0.])`",
        7: "**Output:** `array([10, 11, 12, ..., 47, 48, 49])`",
        8: "**Input:** `[1, 2, 3, 4, 5]`\n**Output:** `[5, 4, 3, 2, 1]`",
        9: "**Output:**\n```\n[[0 1 2]\n [3 4 5]\n [6 7 8]]\n```",
        10: "**Output:** `(array([0, 1, 4]),)` - indices where elements are non-zero",
        11: "**Output:**\n```\n[[1. 0. 0.]\n [0. 1. 0.]\n [0. 0. 1.]]\n```",
        12: "**Output:** 3x3x3 array with random float values",
        13: "**Output:** `min: 0.0234, max: 0.9876` (example values)",
        14: "**Output:** `mean: 0.5123` (example value)",
        15: "**Example:** 5x5 array with 1s on border, 0s inside",
        16: "**Input:** `[[1,1],[1,1]]`\n**Output:**\n```\n[[0,0,0,0]\n [0,1,1,0]\n [0,1,1,0]\n [0,0,0,0]]\n```",
        17: "Test expressions: `0 * np.nan`, `np.nan == np.nan`, `np.inf > np.nan`",
        18: "**Output:** Matrix with 1,2,3,4 below main diagonal",
        19: "**Output:** 8x8 checkerboard pattern (alternating 0 and 1)",
        20: "**Output:** Index tuple (x, y, z) for 100th element",
    }
    
    return examples.get(num, "**See test cases in test file for expected input/output examples.**")


def create_solution_stub(num: int, title: str, level_dir: Path) -> None:
    """Create a solution Python file stub."""
    content = f'''"""
Exercise {num:03d}: {title}
"""
import numpy as np


def solution():
    """
    Implement your solution here.
    """
    # TODO: Implement solution
    pass


if __name__ == "__main__":
    result = solution()
    print(result)
'''
    
    filename = f"{num:03d}_{title.lower().replace(' ', '_').replace('-', '_')}.py"
    file_path = level_dir / "solutions" / filename
    file_path.write_text(content)


def create_test_stub(num: int, title: str, level_dir: Path) -> None:
    """Create a test file stub."""
    content = f'''"""
Tests for Exercise {num:03d}: {title}
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_{title.lower().replace(' ', '_').replace('-', '_')}():
    """Test the solution."""
    # TODO: Implement test cases
    pass
'''
    
    filename = f"test_{num:03d}_{title.lower().replace(' ', '_').replace('-', '_')}.py"
    file_path = level_dir / "tests" / filename
    file_path.write_text(content)


def main():
    base = Path("/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026")
    numpy_dir = base / "14_data_engineering" / "01_numpy_fundamentals"
    
    # Create directory structure
    levels = {
        "level_1_beginner": (1, 33),
        "level_2_intermediate": (34, 66),
        "level_3_advanced": (67, 100),
    }
    
    for level_name, (start, end) in levels.items():
        level_dir = numpy_dir / level_name
        (level_dir / "problems").mkdir(parents=True, exist_ok=True)
        (level_dir / "solutions").mkdir(parents=True, exist_ok=True)
        (level_dir / "tests").mkdir(parents=True, exist_ok=True)
        print(f"\n📁 Created: {level_name}/")
    
    # Create conftest.py for each level
    conftest_content = '''"""Pytest configuration for NumPy exercises."""
import pytest
import numpy as np


@pytest.fixture
def sample_array():
    """Provide a sample array for testing."""
    return np.array([1, 2, 3, 4, 5])
'''
    
    for level_name in levels.keys():
        conftest_path = numpy_dir / level_name / "tests" / "conftest.py"
        conftest_path.write_text(conftest_content)
    
    print("\n📝 Generating exercises...\n")
    
    # Create exercise files
    for num, title, objective, stars in EXERCISES:
        # Determine level
        if num <= 33:
            level_name = "level_1_beginner"
        elif num <= 66:
            level_name = "level_2_intermediate"
        else:
            level_name = "level_3_advanced"
        
        level_dir = numpy_dir / level_name
        
        # Create files
        create_problem_file(num, title, objective, stars, level_dir)
        create_solution_stub(num, title, level_dir)
        create_test_stub(num, title, level_dir)
    
    print(f"\n✅ Successfully created 100 NumPy exercises!")
    print(f"📊 Distribution:")
    print(f"   - Level 1 (Beginner): 33 exercises")
    print(f"   - Level 2 (Intermediate): 33 exercises")
    print(f"   - Level 3 (Advanced): 34 exercises")
    print(f"\n📂 Location: 14_data_engineering/01_numpy_fundamentals/")


if __name__ == "__main__":
    main()
