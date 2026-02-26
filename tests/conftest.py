# conftest.py
import os
from unittest.mock import patch

import pytest

# Example for custom fixtures
# @pytest.fixture(autouse=True, scope="session")
# def disable_load_dotenv():
#     """
#     Replace `dotenv.load_dotenv` with a no‑op for the entire test run.
# 
#     This prevents accidental reading of a real .env file and guarantees
#     that only the values you set with `monkeypatch.setenv` (or
#     `os.environ` patches) are visible.
#     """
#     import dotenv
# 
#     with patch.object(dotenv, "load_dotenv", return_value=None):
#         yield

