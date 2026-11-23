"""
Tests for Exercise 001: Import NumPy
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_import_numpy():
    """Test NumPy import."""
    import numpy as np
    assert hasattr(np, '__version__')
    assert hasattr(np, 'array')



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
