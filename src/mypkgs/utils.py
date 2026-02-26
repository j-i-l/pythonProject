"""
Utility functions for configuration and environment management.
"""

import os
import json
from typing import Any, Dict

from dotenv import load_dotenv


def get_config(config_path: str) -> Dict[str, Any]:
    """
    Load a JSON configuration file into a dictionary.

    Parameters
    ----------
    config_path : str
        The absolute or relative path to the configuration JSON file.

    Returns
    -------
    Dict[str, Any]
        The parsed configuration data.

    Raises
    ------
    FileNotFoundError
        If the config_path does not exist.
    json.JSONDecodeError
        If the file is not valid JSON.

    Examples
    --------
    >>> config = get_config("config.json")
    >>> print(config["name"])
    'Jonas'
    """
    with open(config_path, 'r') as f:
        return json.load(f)


def set_output_dir() -> str:
    """
    Retrieve and prepare the output directory from environment variables.

    Returns
    -------
    str
        The path to the validated and created output directory.

    Raises
    ------
    ValueError
        If the 'OUTPUT_DIR' environment variable is not set.

    Notes
    -----
    This function checks for an environment variable named ``OUTPUT_DIR``.
    If found, it creates the directory (including parents) if it doesn't
    already exist.

    Examples
    --------
    >>> # Assuming export OUTPUT_DIR="/tmp/results"
    >>> path = set_output_dir()
    >>> print(path)
    '/tmp/results'
    """
    # Load the environment variables from the .env file
    load_dotenv()

    output_dir = os.environ.get("OUTPUT_DIR")
    if not output_dir:
        raise ValueError("OUTPUT_DIR environment variable is not set.")

    os.makedirs(output_dir, exist_ok=True)
    return output_dir
