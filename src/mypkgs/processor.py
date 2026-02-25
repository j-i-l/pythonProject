"""
Core processing functions for the hello-world service.
"""

import os


def write_hello(name: str, output_dir: str) -> str:
    """
    Create a personalized greeting and write it to a text file.

    Parameters
    ----------
    name : str
        The name of the person to greet.
    output_dir : str
        The directory where the output file 'output_hello.txt' will be saved.

    Returns
    -------
    str
        The full path to the created output file.

    Examples
    --------
    >>> file_path = write_hello("Simon", "/tmp/results")
    >>> print(file_path)
    '/tmp/results/output_hello.txt'
    """
    output_file = os.path.join(output_dir, "output_hello.txt")
    output_content = f"Hello {name}"

    with open(output_file, 'w') as f:
        f.write(output_content)

    return output_file
