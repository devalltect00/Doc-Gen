# app/doc_gen/config/file_loader.py

"""
Load project configuration from .projectstructure.toml
"""

import os
from typing import Any, Dict

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.9/3.10 only
    import tomli as tomllib


def load_project_config(root_path: str = ".") -> Dict[str, Any]:
    """
    Load configuration from .projectstructure.toml if exists.

    Args:
        root_path (str): Root directory of the project

    Returns:
        dict: Configuration dictionary
    """
    config_path = os.path.join(root_path, ".projectstructure.toml")

    if not os.path.exists(config_path):
        return {}

    try:
        with open(config_path, "rb") as f:
            data = tomllib.load(f)

        return data.get("tool", {}).get("doc-gen", {})

    except Exception:
        return {}
