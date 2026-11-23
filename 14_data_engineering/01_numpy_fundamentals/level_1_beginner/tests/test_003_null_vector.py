"""
Tests for Exercise 003: Null Vector
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_null_vector():
    """Test null vector creation."""
    import numpy as np
    z = np.zeros(10)
    assert z.shape == (10,)
    assert np.all(z == 0)
    assert z.dtype == np.float64



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
