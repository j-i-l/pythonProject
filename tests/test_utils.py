"""
Tests for the utility functions.
"""

import os
import json
from pathlib import Path

import pytest

# Import our refactored package functions
from mypkgs.utils import (
    load_json_config,
    prepare_output_dir
)


def test_load_json_config_success(tmp_path: Path):
    """Test that valid JSON is loaded correctly."""
    # Create a temporary JSON file
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps({"name": "Jonas"}))

    # Run function and verify
    result = load_json_config(config_file)
    assert result == {"name": "Jonas"}
    assert result["name"] == "Jonas"


def test_load_json_config_not_found():
    """Test that a missing file raises the correct error."""
    with pytest.raises(FileNotFoundError):
        load_json_config("does_not_exist.json")


def test_prepare_output_dir_success(tmp_path: Path):
    """Test that the output directory is created from a given path."""
    target_dir = tmp_path / "my_results"

    # Run function using the path directly (no environment variables needed)
    result = prepare_output_dir(target_dir)

    # Verify the path matches and the directory was actually created
    assert result == str(target_dir)
    assert os.path.isdir(result)
