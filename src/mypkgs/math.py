"""
Mathematical operations and linear algebra utilities.
"""

import numpy as np
import numpy.typing as npt


def multiply_matrices(
    matrix_a: npt.NDArray[np.float64],
    matrix_b: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """
    Multiply two matrices using matrix multiplication (dot product).

    This function utilizes the ``@`` operator for standard 2D matrix
    multiplication, which is equivalent to calling :obj:`numpy.matmul`.

    Parameters
    ----------
    matrix_a : numpy.ndarray
        The first input matrix (2D array).
    matrix_b : numpy.ndarray
        The second input matrix (2D array). The number of rows in `matrix_b`
        must strictly match the number of columns in `matrix_a`.

    Returns
    -------
    numpy.ndarray
        The resulting matrix from the multiplication.

    Raises
    ------
    ValueError
        If the inner dimensions of the matrices do not align for multiplication.
    """
    try:
        return matrix_a @ matrix_b
    except ValueError as e:
        raise ValueError(
            f"Matrix dimensions do not align for multiplication: {e}"
        )
