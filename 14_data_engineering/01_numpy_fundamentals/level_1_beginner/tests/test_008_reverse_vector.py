"""
Tests for Exercise 008: Reverse Vector
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_reverse_vector():
    """Test vector reversal."""
    import numpy as np
    z = np.arange(5)
    reversed_z = z[::-1]
    assert list(reversed_z) == [4, 3, 2, 1, 0]
    # Alternative methods
    assert list(np.flip(z)) == [4, 3, 2, 1, 0]



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
