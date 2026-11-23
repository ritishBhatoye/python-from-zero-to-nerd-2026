"""
Tests for Exercise 005: NumPy Documentation
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_numpy_documentation():
    """Test NumPy documentation access."""
    import numpy as np
    # Check that add function has documentation
    assert np.add.__doc__ is not None
    assert 'add' in dir(np)



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
