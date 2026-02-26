"""
Core package for the pythonProject Template 

This package provides utilities for environment management, 
configuration loading, mathematical operations, and core processing.
"""

try:
    # try to import version (provided by hatch (see pyproject.toml)
    from ._version import __version__
except ImportError:
    # Fallback if the package wasn't installed properly
    __version__ = "unknown"
