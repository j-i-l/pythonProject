"""
Example script demonstrating matrix multiplication from the mypkgs library.
"""

import numpy as np
from mypkgs.math import multiply_matrices


def main() -> None:
    """Execute a simple matrix multiplication demonstration."""
    print("Initializing matrices...")

    # Create two simple 2x2 matrices
    a = np.array([
        [1.0, 2.0],
        [3.0, 4.0]
    ])

    b = np.array([
        [2.0, 0.0],
        [1.0, 2.0]
    ])

    print(f"Matrix A:\n{a}\n")
    print(f"Matrix B:\n{b}\n")

    # Perform multiplication using our custom module
    try:
        result = multiply_matrices(a, b)
        print(f"Result of A @ B:\n{result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
