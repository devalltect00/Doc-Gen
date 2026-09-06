# app/doc_gen/utils/progress.py

"""
Progress utilities using Rich.
"""

from contextlib import contextmanager

from rich.progress import Progress, SpinnerColumn, TextColumn


@contextmanager
def progress_spinner(message: str):
    """
    Display a spinner progress indicator.

    Args:
        message (str): Message to display during progress
    """
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,  # removes after done
    )

    with progress:
        task = progress.add_task(description=message, total=None)
        yield
        progress.update(task, description=f"{message} ✔")
