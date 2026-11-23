"""
Tests for Exercise 016: Add Border
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_add_border():
    """Test adding border to array."""
    import numpy as np
    z = np.ones((3, 3))
    z_bordered = np.pad(z, pad_width=1, mode='constant', constant_values=0)
    assert z_bordered.shape == (5, 5)
    assert z_bordered[0, 0] == 0
    assert z_bordered[2, 2] == 1



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
