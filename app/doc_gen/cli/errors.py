# app/doc_gen/cli/errors.py

"""Reusable exception boundaries for user-facing Doc Gen commands."""

from __future__ import annotations

import logging
from functools import wraps
from typing import Callable, Optional, TypeVar

import typer
from click.exceptions import Abort, ClickException, Exit

from doc_gen.core.shared import DocGenError
from doc_gen.ui.exceptions import show_error

logger = logging.getLogger(__name__)

R = TypeVar("R")


def handle_cli_errors(
    operation: str,
    *,
    solution: Optional[str] = None,
) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """Convert application failures into concise CLI error panels."""

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except (Exit, Abort, ClickException, typer.Exit, typer.Abort):
                raise
            except (DocGenError, OSError) as exc:
                logger.debug("%s failed: %s", operation, exc, exc_info=True)
                message = f"{operation} failed\n\n{exc}"
                if solution:
                    message += f"\n\nSolution\n\n{solution}"
                show_error(message)
                raise typer.Exit(code=1) from None
            except Exception as exc:
                logger.debug(
                    "%s failed unexpectedly: %s", operation, exc, exc_info=True
                )
                show_error(
                    f"{operation} failed unexpectedly.\n\n"
                    "Re-run with --debug and inspect the configured log file "
                    "for technical details."
                )
                raise typer.Exit(code=1) from None

        return wrapper

    return decorator
