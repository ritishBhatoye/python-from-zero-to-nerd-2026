"""Pytest configuration for NumPy exercises."""
import pytest
import numpy as np


@pytest.fixture
def sample_array():
    """Provide a sample array for testing."""
    return np.array([1, 2, 3, 4, 5])
