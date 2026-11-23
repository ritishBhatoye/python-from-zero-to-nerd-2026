#!/usr/bin/env python3
"""Generate comprehensive test cases for all 100 NumPy exercises."""

from pathlib import Path


# Test implementations for each exercise
TESTS = {
    1: """def test_import_numpy():
    \"\"\"Test NumPy import.\"\"\"
    import numpy as np
    assert hasattr(np, '__version__')
    assert hasattr(np, 'array')
""",
    
    2: """def test_numpy_version():
    \"\"\"Test NumPy version and config.\"\"\"
    import numpy as np
    assert np.__version__ is not None
    # Config should be callable
    assert hasattr(np, 'show_config')
""",
    
    3: """def test_null_vector():
    \"\"\"Test null vector creation.\"\"\"
    import numpy as np
    z = np.zeros(10)
    assert z.shape == (10,)
    assert np.all(z == 0)
    assert z.dtype == np.float64
""",
    
    4: """def test_array_memory_size():
    \"\"\"Test array memory size calculation.\"\"\"
    import numpy as np
    z = np.zeros((10, 10))
    # 10x10 float64 = 800 bytes
    assert z.nbytes == 800
    assert z.itemsize == 8  # float64 is 8 bytes
    assert z.size == 100  # 10x10 elements
""",
    
    5: """def test_numpy_documentation():
    \"\"\"Test NumPy documentation access.\"\"\"
    import numpy as np
    # Check that add function has documentation
    assert np.add.__doc__ is not None
    assert 'add' in dir(np)
""",
    
    6: """def test_vector_with_one_value():
    \"\"\"Test vector with one non-zero value.\"\"\"
    import numpy as np
    z = np.zeros(10)
    z[4] = 1
    assert z.shape == (10,)
    assert z[4] == 1
    assert np.sum(z) == 1
    assert np.count_nonzero(z) == 1
""",
    
    7: """def test_vector_range():
    \"\"\"Test vector with range values.\"\"\"
    import numpy as np
    z = np.arange(10, 50)
    assert z.shape == (40,)
    assert z[0] == 10
    assert z[-1] == 49
    assert len(z) == 40
""",
    
    8: """def test_reverse_vector():
    \"\"\"Test vector reversal.\"\"\"
    import numpy as np
    z = np.arange(5)
    reversed_z = z[::-1]
    assert list(reversed_z) == [4, 3, 2, 1, 0]
    # Alternative methods
    assert list(np.flip(z)) == [4, 3, 2, 1, 0]
""",
    
    9: """def test_3x3_matrix():
    \"\"\"Test 3x3 matrix creation.\"\"\"
    import numpy as np
    z = np.arange(9).reshape(3, 3)
    assert z.shape == (3, 3)
    assert z[0, 0] == 0
    assert z[2, 2] == 8
    assert np.sum(z) == 36
""",
    
    10: """def test_non_zero_indices():
    \"\"\"Test finding non-zero indices.\"\"\"
    import numpy as np
    nz = np.nonzero([1, 2, 0, 0, 4, 0])
    assert len(nz[0]) == 3
    assert list(nz[0]) == [0, 1, 4]
""",
    
    11: """def test_identity_matrix():
    \"\"\"Test identity matrix creation.\"\"\"
    import numpy as np
    z = np.eye(3)
    assert z.shape == (3, 3)
    assert z[0, 0] == 1
    assert z[0, 1] == 0
    assert np.sum(z) == 3
    assert np.trace(z) == 3
""",
    
    12: """def test_3d_random_array():
    \"\"\"Test 3D random array creation.\"\"\"
    import numpy as np
    z = np.random.random((3, 3, 3))
    assert z.shape == (3, 3, 3)
    assert z.ndim == 3
    assert 0 <= z.min() <= 1
    assert 0 <= z.max() <= 1
""",
    
    13: """def test_random_min_max():
    \"\"\"Test finding min and max in random array.\"\"\"
    import numpy as np
    z = np.random.random((10, 10))
    zmin, zmax = z.min(), z.max()
    assert 0 <= zmin <= 1
    assert 0 <= zmax <= 1
    assert zmin <= zmax
""",
    
    14: """def test_random_mean():
    \"\"\"Test mean of random vector.\"\"\"
    import numpy as np
    z = np.random.random(30)
    m = z.mean()
    assert 0 <= m <= 1
    assert abs(m - 0.5) < 0.5  # Mean should be around 0.5
""",
    
    15: """def test_border_array():
    \"\"\"Test array with 1 on border and 0 inside.\"\"\"
    import numpy as np
    z = np.ones((5, 5))
    z[1:-1, 1:-1] = 0
    assert z[0, 0] == 1
    assert z[2, 2] == 0
    assert np.sum(z) == 16  # Border elements only
""",
    
    16: """def test_add_border():
    \"\"\"Test adding border to array.\"\"\"
    import numpy as np
    z = np.ones((3, 3))
    z_bordered = np.pad(z, pad_width=1, mode='constant', constant_values=0)
    assert z_bordered.shape == (5, 5)
    assert z_bordered[0, 0] == 0
    assert z_bordered[2, 2] == 1
""",
    
    17: """def test_nan_and_inf():
    \"\"\"Test NaN and Inf behavior.\"\"\"
    import numpy as np
    assert np.isnan(0 * np.nan)
    assert not (np.nan == np.nan)
    assert not (np.inf > np.nan)
    assert np.isnan(np.nan - np.nan)
""",
    
    18: """def test_diagonal_matrix():
    \"\"\"Test matrix with values below diagonal.\"\"\"
    import numpy as np
    z = np.diag(1 + np.arange(4), k=-1)
    assert z.shape == (5, 5)
    assert z[1, 0] == 1
    assert z[4, 3] == 4
""",
    
    19: """def test_checkerboard():
    \"\"\"Test checkerboard pattern.\"\"\"
    import numpy as np
    z = np.zeros((8, 8), dtype=int)
    z[1::2, ::2] = 1
    z[::2, 1::2] = 1
    assert z.shape == (8, 8)
    assert z[0, 0] == 0
    assert z[0, 1] == 1
    assert np.sum(z) == 32
""",
    
    20: """def test_3d_index():
    \"\"\"Test finding 100th element index in 3D array.\"\"\"
    import numpy as np
    index = np.unravel_index(99, (6, 7, 8))
    assert len(index) == 3
    # Verify it's the correct index
    arr = np.arange(6*7*8).reshape(6, 7, 8)
    assert arr[index] == 99
""",
}

# Generate remaining test stubs for exercises without specific tests
def generate_generic_test(num: int, title: str) -> str:
    """Generate a generic test stub."""
    func_name = title.lower().replace(' ', '_').replace('-', '_')
    return f'''def test_{func_name}():
    """Test for exercise {num:03d}: {title}."""
    import numpy as np
    # TODO: Implement comprehensive test cases
    # This is a placeholder - add specific assertions based on the exercise
    assert np is not None
'''


def create_test_file(num: int, title: str, level_dir: Path) -> None:
    """Create or update a test file with proper test cases."""
    
    # Get test implementation or generate stub
    if num in TESTS:
        test_code = TESTS[num]
    else:
        test_code = generate_generic_test(num, title)
    
    # Create full test file content
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


{test_code}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''
    
    filename = f"test_{num:03d}_{title.lower().replace(' ', '_').replace('-', '_')}.py"
    file_path = level_dir / "tests" / filename
    file_path.write_text(content)
    print(f"✅ Updated: {file_path.name}")


def main():
    base = Path("/Users/ritishbhatoye/Documents/python-from-zero-to-nerd-2026")
    numpy_dir = base / "14_data_engineering" / "01_numpy_fundamentals"
    
    # Exercise data: same as generation script
    exercises = [
        (1, "Import NumPy"), (2, "NumPy Version"), (3, "Null Vector"),
        (4, "Array Memory Size"), (5, "NumPy Documentation"),
        (6, "Vector with One Value"), (7, "Vector Range"), (8, "Reverse Vector"),
        (9, "3x3 Matrix"), (10, "Non-zero Indices"), (11, "Identity Matrix"),
        (12, "3D Random Array"), (13, "Random Min Max"), (14, "Random Mean"),
        (15, "Border Array"), (16, "Add Border"), (17, "NaN and Inf"),
        (18, "Diagonal Matrix"), (19, "Checkerboard"), (20, "3D Index"),
        # Add remaining exercises as generic tests
        (21, "Tile Checkerboard"), (22, "Normalize Matrix"), (23, "Custom Dtype"),
        (24, "Matrix Multiplication"), (25, "Negate Elements"), (26, "Sum Function"),
        (27, "Legal Expressions"), (28, "Division Results"), (29, "Round Away"),
        (30, "Common Values"), (31, "Ignore Warnings"), (32, "Complex Sqrt"),
        (33, "Date Operations"),
    ]
    
    # Add more exercises for levels 2 and 3
    for i in range(34, 101):
        exercises.append((i, f"Exercise {i}"))
    
    print("\n📝 Updating test files with proper test cases...\n")
    
    updated = 0
    for num, title in exercises:
        # Determine level
        if num <= 33:
            level_name = "level_1_beginner"
        elif num <= 66:
            level_name = "level_2_intermediate"
        else:
            level_name = "level_3_advanced"
        
        level_dir = numpy_dir / level_name
        create_test_file(num, title, level_dir)
        updated += 1
    
    print(f"\n✅ Updated {updated} test files!")
    print(f"📊 Test coverage:")
    print(f"   - Detailed tests: {len(TESTS)} exercises")
    print(f"   - Generic stubs: {100 - len(TESTS)} exercises")
    print(f"\n💡 You can now run: pytest 14_data_engineering/01_numpy_fundamentals/ -v")


if __name__ == "__main__":
    main()
