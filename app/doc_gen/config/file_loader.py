# app/doc_gen/config/file_loader.py

"""Load namespaced project configuration with a legacy-file fallback."""

from pathlib import Path
from typing import Any, Dict

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.9/3.10 only
    import tomli as tomllib


def load_project_config(root_path: str = ".") -> Dict[str, Any]:
    """
    Load `.config/doc_gen/config.toml` when present.

    The retired `.projectstructure.toml` location remains a read-only fallback
    for callers that still import this compatibility helper.

    Args:
        root_path (str): Root directory of the project

    Returns:
        dict: Configuration dictionary
    """
    root = Path(root_path)
    canonical_path = root / ".config" / "doc_gen" / "config.toml"
    legacy_path = root / ".projectstructure.toml"
    config_path = canonical_path if canonical_path.is_file() else legacy_path

    if not config_path.is_file():
        return {}

    try:
        with config_path.open("rb") as f:
            data = tomllib.load(f)

        return data.get("tool", {}).get("doc-gen", {})

    except (OSError, tomllib.TOMLDecodeError, TypeError):
        return {}
