"""
Tests for Exercise 018: Diagonal Matrix
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_diagonal_matrix():
    """Test matrix with values below diagonal."""
    import numpy as np
    z = np.diag(1 + np.arange(4), k=-1)
    assert z.shape == (5, 5)
    assert z[1, 0] == 1
    assert z[4, 3] == 4



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
