"""
Utility functions for configuration and environment management.

These functions are strictly decoupled from the project's folder structure
to ensure maximum reusability and testability.
"""

import os
import json
from typing import Any, Dict
from pathlib import Path


def load_json_config(config_path: Path | str) -> Dict[str, Any]:
    """
    Read and parse a JSON configuration file.
    
    # ... (Docstrings remain unchanged)
    """
    with open(config_path, 'r') as f:
        return json.load(f)


def prepare_output_dir(output_path: Path | str) -> str:
    """
    Ensure the provided output directory exists, creating it if necessary.
    
    # ... (Docstrings remain unchanged)
    """
    os.makedirs(output_path, exist_ok=True)
    return str(output_path)
