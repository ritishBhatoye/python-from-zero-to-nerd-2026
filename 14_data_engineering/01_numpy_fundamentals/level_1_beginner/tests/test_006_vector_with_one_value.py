"""
Tests for Exercise 006: Vector with One Value
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_vector_with_one_value():
    """Test vector with one non-zero value."""
    import numpy as np
    z = np.zeros(10)
    z[4] = 1
    assert z.shape == (10,)
    assert z[4] == 1
    assert np.sum(z) == 1
    assert np.count_nonzero(z) == 1



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
