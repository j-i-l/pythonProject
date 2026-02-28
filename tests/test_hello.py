"""
Tests for the processing utilities.
"""

import os
from mypkgs.hello import write_hello


def test_write_hello(tmp_path):
    """Test that the greeting is correctly written to a file."""
    # Run the function using the temporary directory
    output_filepath = write_hello("Simon", str(tmp_path))

    # Verify the file path returned is correct
    expected_path = os.path.join(str(tmp_path), "output_hello.txt")
    assert output_filepath == expected_path

    # Verify the file contents are correct
    with open(output_filepath, "r") as f:
        content = f.read()
    assert content == "Hello Simon"
