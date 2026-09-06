# app/doc_gen/cli/commands/init/models.py

from dataclasses import dataclass

from doc_gen.cli.constants.enums import InitMode


@dataclass
class InitArgs:
    mode: InitMode
    force_init: bool
    ask: bool
    dry_run: bool
