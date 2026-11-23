"""
Tests for Exercise 013: Random Min Max
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_random_min_max():
    """Test finding min and max in random array."""
    import numpy as np
    z = np.random.random((10, 10))
    zmin, zmax = z.min(), z.max()
    assert 0 <= zmin <= 1
    assert 0 <= zmax <= 1
    assert zmin <= zmax



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
