"""
Tests for Exercise 004: Array Memory Size
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_array_memory_size():
    """Test array memory size calculation."""
    import numpy as np
    z = np.zeros((10, 10))
    # 10x10 float64 = 800 bytes
    assert z.nbytes == 800
    assert z.itemsize == 8  # float64 is 8 bytes
    assert z.size == 100  # 10x10 elements



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
