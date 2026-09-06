# app/doc_gen/cli/commands/main/resolver.py

from doc_gen.cli.commands.main.models import MainArgs
from doc_gen.cli.constants.enums import LogLevelChoices


def resolve_main_args(config, cli_args) -> MainArgs:
    return MainArgs(
        no_banner=cli_args.no_banner or False,
        help=cli_args.help or False,
        version=cli_args.version or None,
        debug=config.resolve(
            cli_args.debug,
            ["cli", "execution", "debug"],
            False,
        ),
        log_level=config.resolve(
            cli_args.log_level,
            ["logging", "level"],
            LogLevelChoices.INFO,
        ),
    )
