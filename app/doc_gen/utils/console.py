# app/doc_gen/utils/console.py

"""
Console utilities for styled CLI output.
"""

from doc_gen.ui.console import console


def print_header():
    console.print("\n[bold cyan]📦 Project Structure Generator[/bold cyan]\n")


def print_success(message: str):
    console.print(f"[green]✔ {message}[/green]")


def print_info(message: str):
    console.print(f"[blue]ℹ {message}[/blue]")


def print_warning(message: str):
    console.print(f"[yellow]⚠ {message}[/yellow]")


def print_error(message: str):
    console.print(f"[red]✖ {message}[/red]")


def print_section(title: str):
    console.print(f"\n[bold magenta]{title}[/bold magenta]\n")
