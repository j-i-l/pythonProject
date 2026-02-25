import pytest
import numpy as np

# Import our package functions
from mypkgs.math import multiply_matrices


def test_multiply_matrices_success():
    """Test standard 2x2 matrix multiplication."""
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[2.0, 0.0], [1.0, 2.0]])

    expected = np.array([[4.0, 4.0], [10.0, 8.0]])
    result = multiply_matrices(a, b)

    # np.testing.assert_array_equal is the safest way to compare NumPy arrays
    np.testing.assert_array_equal(result, expected)


def test_multiply_matrices_shape_mismatch():
    """Test that misaligned matrices raise a ValueError."""
    a = np.array([[1.0, 2.0], [3.0, 4.0]])  # 2x2
    b = np.array([[1.0, 2.0, 3.0]])         # 1x3

    # A 2x2 cannot be multiplied by a 1x3 matrix
    with pytest.raises(ValueError, match="Matrix dimensions do not align"):
        multiply_matrices(a, b)
