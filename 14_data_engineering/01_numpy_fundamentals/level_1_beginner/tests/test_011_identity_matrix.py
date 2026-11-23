"""
Tests for Exercise 011: Identity Matrix
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_identity_matrix():
    """Test identity matrix creation."""
    import numpy as np
    z = np.eye(3)
    assert z.shape == (3, 3)
    assert z[0, 0] == 1
    assert z[0, 1] == 0
    assert np.sum(z) == 3
    assert np.trace(z) == 3



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
