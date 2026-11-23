"""
Tests for Exercise 017: NaN and Inf
"""
import pytest
import numpy as np
from pathlib import Path
import sys

# Add solutions directory to path
solutions_dir = Path(__file__).parent.parent / "solutions"
sys.path.insert(0, str(solutions_dir))


def test_nan_and_inf():
    """Test NaN and Inf behavior."""
    import numpy as np
    assert np.isnan(0 * np.nan)
    assert not (np.nan == np.nan)
    assert not (np.inf > np.nan)
    assert np.isnan(np.nan - np.nan)



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
