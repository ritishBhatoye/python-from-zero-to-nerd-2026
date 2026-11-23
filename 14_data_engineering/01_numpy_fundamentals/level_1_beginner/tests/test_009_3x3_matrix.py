"""
Tests for Exercise 009: 3x3 Matrix
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_3x3_matrix():
    """Test 3x3 matrix creation."""
    import numpy as np
    z = np.arange(9).reshape(3, 3)
    assert z.shape == (3, 3)
    assert z[0, 0] == 0
    assert z[2, 2] == 8
    assert np.sum(z) == 36



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
