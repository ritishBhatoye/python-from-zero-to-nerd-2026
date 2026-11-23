"""
Tests for Exercise 014: Random Mean
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_random_mean():
    """Test mean of random vector."""
    import numpy as np
    z = np.random.random(30)
    m = z.mean()
    assert 0 <= m <= 1
    assert abs(m - 0.5) < 0.5  # Mean should be around 0.5



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
