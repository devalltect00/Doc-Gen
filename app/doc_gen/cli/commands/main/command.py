# app/doc_gen/cli/commands/main/command.py

import logging
import sys

import typer

from doc_gen.cli.commands.main.models import MainArgs
from doc_gen.cli.commands.main.options import (
    DebugOption,
    HelpOption,
    LogLevelOption,
    NoBannerOption,
    VersionOption,
)
from doc_gen.cli.commands.main.resolver import resolve_main_args
from doc_gen.cli.errors import handle_cli_errors
from doc_gen.cli.utils import banner
from doc_gen.config.config_loader import get_config
from doc_gen.utils.logging import setup_logging


@handle_cli_errors(
    "Command startup",
    solution="Review .config/doc_gen/config.toml and the supplied CLI options.",
)
def main(
    ctx: typer.Context,
    no_banner: NoBannerOption = None,
    help: HelpOption = None,
    version: VersionOption = None,
    debug: DebugOption = None,
    log_level: LogLevelOption = None,
):
    config = get_config()

    # REQUIRED defaults
    cli_args = MainArgs(
        no_banner=no_banner,
        help=help,
        version=version,
        debug=debug,
        log_level=log_level,
    )

    args = resolve_main_args(config=config, cli_args=cli_args)

    setup_logging(level=args.log_level, debug=args.debug)

    if args.help:
        if not args.no_banner:
            banner.show()
        typer.echo(ctx.get_help())
        raise typer.Exit()

    if not args.no_banner:
        banner.show()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()

    full_command = " ".join(sys.argv[1:])
    logger = logging.getLogger("main")
    logger.debug("[cyan]CLI COMMAND[/cyan] | [dim]Doc Gen %s[/dim]", full_command)
