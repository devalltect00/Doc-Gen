# app/doc_gen/core/shared/__init__.py

"""
Shared core models and utilities.
"""

from .exceptions import (
    ConfigurationError,
    DocGenError,
    ValidationError,
)
from .result import CommandResult

__all__ = [
    "CommandResult",
    "DocGenError",
    "ConfigurationError",
    "ValidationError",
]
