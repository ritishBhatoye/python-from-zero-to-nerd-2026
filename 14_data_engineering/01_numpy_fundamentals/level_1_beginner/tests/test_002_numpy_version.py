"""
Tests for Exercise 002: NumPy Version
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_numpy_version():
    """Test NumPy version and config."""
    import numpy as np
    assert np.__version__ is not None
    # Config should be callable
    assert hasattr(np, 'show_config')



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
