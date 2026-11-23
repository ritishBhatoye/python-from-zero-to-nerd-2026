"""
Tests for Exercise 012: 3D Random Array
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_3d_random_array():
    """Test 3D random array creation."""
    import numpy as np
    z = np.random.random((3, 3, 3))
    assert z.shape == (3, 3, 3)
    assert z.ndim == 3
    assert 0 <= z.min() <= 1
    assert 0 <= z.max() <= 1



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
