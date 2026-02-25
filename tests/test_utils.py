import os
import json
import pytest

# Import our package functions
from mypkgs.utils import get_config, set_output_dir


def test_get_config_success(tmp_path):
    """Test that valid JSON is loaded correctly."""
    # Create a temporary JSON file
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps({"name": "Jonas"}))

    # Run function and verify
    result = get_config(str(config_file))
    assert result == {"name": "Jonas"}
    assert result["name"] == "Jonas"


def test_get_config_file_not_found():
    """Test that a missing file raises the correct error."""
    with pytest.raises(FileNotFoundError):
        get_config("does_not_exist.json")


def test_set_output_dir_success(monkeypatch, tmp_path):
    """Test that the output directory is created when env var is set."""
    # Mock the environment variable to point to a temporary folder
    fake_out_dir = tmp_path / "my_results"
    monkeypatch.setenv("OUTPUT_DIR", str(fake_out_dir))

    # Run function
    result = set_output_dir()

    # Verify the path matches and the directory was actually created
    assert result == str(fake_out_dir)
    assert os.path.isdir(result)


def test_set_output_dir_missing_env(monkeypatch):
    """Test that a missing environment variable raises an error."""
    # Ensure the env var is completely removed
    monkeypatch.delenv("OUTPUT_DIR", raising=False)

    with pytest.raises(
        ValueError,
        match="OUTPUT_DIR environment variable is not set"
    ):
        set_output_dir()
