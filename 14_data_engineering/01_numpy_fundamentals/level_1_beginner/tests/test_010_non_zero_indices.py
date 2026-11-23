"""
Tests for Exercise 010: Non-zero Indices
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_non_zero_indices():
    """Test finding non-zero indices."""
    import numpy as np
    nz = np.nonzero([1, 2, 0, 0, 4, 0])
    assert len(nz[0]) == 3
    assert list(nz[0]) == [0, 1, 4]



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
