"""
Tests for Exercise 020: 3D Index
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_3d_index():
    """Test finding 100th element index in 3D array."""
    import numpy as np
    index = np.unravel_index(99, (6, 7, 8))
    assert len(index) == 3
    # Verify it's the correct index
    arr = np.arange(6*7*8).reshape(6, 7, 8)
    assert arr[index] == 99



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
