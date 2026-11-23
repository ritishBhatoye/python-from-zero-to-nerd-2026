"""
Tests for Exercise 015: Border Array
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_border_array():
    """Test array with 1 on border and 0 inside."""
    import numpy as np
    z = np.ones((5, 5))
    z[1:-1, 1:-1] = 0
    assert z[0, 0] == 1
    assert z[2, 2] == 0
    assert np.sum(z) == 16  # Border elements only



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
