# app/doc_gen/core/initialize/loader.py

from importlib.resources import files
from pathlib import Path

from doc_gen.constants.path import (
    THIS_PROJECT_SOURCE_WITH_DOTS,
)


def load_template(name: str) -> str:
    # user override
    user_path = Path("templates") / name
    if user_path.exists():
        return user_path.read_text(encoding="utf-8")

    # fallback to package
    return (
        files(f"{THIS_PROJECT_SOURCE_WITH_DOTS}.templates")
        .joinpath(name)
        .read_text(encoding="utf-8")
    )
