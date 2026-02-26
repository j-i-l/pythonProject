"""
Core processing functions for the hello-world service.

This module contains the business logic for generating greetings
and saving output files.
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
    """
    output_file = os.path.join(output_dir, "output_hello.txt")
    output_content = f"Hello {name}"

    with open(output_file, 'w') as f:
        f.write(output_content)

    return output_file
