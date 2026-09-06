# app/doc_gen/cli/commands/init/command.py

from types import SimpleNamespace

import typer

from doc_gen.cli.commands.init.models import InitArgs
from doc_gen.cli.commands.init.options import (
    AskOption,
    DryRunOption,
    ForceOption,
    ModeOption,
)
from doc_gen.cli.constants.enums import LogLevelChoices
from doc_gen.cli.errors import handle_cli_errors
from doc_gen.config.config_loader import get_config
from doc_gen.core.initialize.main import InitMain

from .resolver import resolve_init_args

app = typer.Typer()


@app.callback(
    rich_help_panel="Initialization",
)
@handle_cli_errors(
    "Initialization",
    solution="Verify the destination is writable, or preview with --dry-run.",
)
# @app.command("init")
def init(
    ctx: typer.Context,
    mode: ModeOption = None,
    force_init: ForceOption = None,
    ask: AskOption = None,
    dry_run: DryRunOption = None,
):
    """
    Initialize your project

    🚀 [bold cyan]Initialize your project[/bold cyan]

    Prepare everything needed to start using Doc Gen.

    [dim]Recommended to run once after installation or in a new project[/dim]

    ────────────────────────────────────────

    📦 [bold]What this command does:[/bold]

      • [green]Create configuration files[/green]

    ────────────────────────────────────────

    📌 [bold]Usage:[/bold]

      [yellow]path-header-scanner init[/yellow]

    ────────────────────────────────────────

    ⚙️ [bold]Options:[/bold]

      [cyan]--mode[/cyan] [dim](config | templates | examples | all)[/dim]
          Choose what to initialize
          [dim]Default: all[/dim]

      [cyan]--force[/cyan]
          Overwrite existing files without confirmation

      [cyan]--ask[/cyan]
          Prompt before creating or overwriting files

      [cyan]--dry-run[/cyan]
          Preview initialization without creating or overwriting files

    ────────────────────────────────────────

    🧪 [bold]Examples:[/bold]

      [yellow]path-header-scanner init[/yellow]
          [dim]Initialize everything[/dim]

      [yellow]path-header-scanner init --mode config[/yellow]
          [dim]Only create config files[/dim]

      [yellow]path-header-scanner init --force[/yellow]
          [dim]Overwrite existing setup[/dim]

      [yellow]doc-gen init --dry-run[/yellow]
          [dim]Preview initialization without making changes[/dim]

    ────────────────────────────────────────

    💡 [bold]Tips:[/bold]

      • Safe to run multiple times
      • Use [cyan]--mode[/cyan] to initialize specific parts only
    """
    config = get_config()

    # REQUIRED defaults
    cli_args = InitArgs(
        mode=mode,
        force_init=force_init,
        ask=ask,
        dry_run=dry_run,
    )

    args = resolve_init_args(config=config, cli_args=cli_args)

    combined_args = SimpleNamespace(
        **vars(args),
        debug=True,
        log_level=LogLevelChoices.INFO,
    )

    InitMain().execute(combined_args)
