"""
Utility functions for configuration and environment management.

These functions are strictly decoupled from the project's folder structure
to ensure maximum reusability and testability.
"""

import json
from pathlib import Path
from typing import Any


def load_json_config(config_path: Path | str) -> dict[str, Any]:
    """
    Reads and parses a JSON configuration file.

    The specified file is accessed in read mode, and its contents are
    decoded from JSON format into a Python dictionary. It is required
    that the root element of the targeted JSON file constitutes a valid
    JSON object (key-value pairs).

    Parameters
    ----------
    config_path : pathlib.Path or str
        The file path to the targeted JSON configuration file.

    Returns
    -------
    dict[str, Any]
        A dictionary containing the parsed configuration parameters.

    Raises
    ------
    FileNotFoundError
        If the specified configuration file is not found at the given path.
    json.JSONDecodeError
        If the file contains invalid JSON syntax and cannot be parsed.
    IsADirectoryError
        If the provided path resolves to a directory.

    Examples
    --------
    >>> config = load_json_config("./configs/model_params.json")
    >>> type(config)
    <class 'dict'>
    """
    path = Path(config_path).resolve()
    with path.open("r", encoding="utf-8") as file:
        config_data = json.load(file)
    return config_data


def prepare_output_dir(output_path: Path | str) -> str:
    """
    Validates and prepares the designated output directory.

    This function ensures that the specified output path exists. If the
    directory does not exist, it safely creates it along with any necessar
    parent directories.

    Parameters
    ----------
    output_path : pathlib.Path or str
        The target directory path where output files will be saved.

    Returns
    -------
    str
        The absolute path of the prepared output directory as a string.

    Raises
    ------
    PermissionError
        If the program lacks the necessary permissions to create the directory.
    OSError
        If the path is invalid or creation fails for system-level reasons.

    Examples
    --------
    >>> prepared_path = prepare_output_dir("./results/experiment_1")
    >>> print(prepared_path)
    '/absolute/path/to/results/experiment_1'
    """
    path = Path(output_path).resolve()
    path.mkdir(parents=True, exist_ok=True)
    return str(path)
