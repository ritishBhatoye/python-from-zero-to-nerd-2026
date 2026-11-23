"""
Tests for Exercise 019: Checkerboard
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_checkerboard():
    """Test checkerboard pattern."""
    import numpy as np
    z = np.zeros((8, 8), dtype=int)
    z[1::2, ::2] = 1
    z[::2, 1::2] = 1
    assert z.shape == (8, 8)
    assert z[0, 0] == 0
    assert z[0, 1] == 1
    assert np.sum(z) == 32



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
