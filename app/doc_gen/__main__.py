# app/doc_gen/__main__.py

"""
Application entrypoint.
Entrypoint for doc-gen CLI.

This module allows the project to be executed using:

    python -m doc_gen

It delegates execution to the CLI application.
"""

from doc_gen.cli.main import app

if __name__ == "__main__":
    app()
