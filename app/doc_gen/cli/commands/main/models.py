# app/doc_gen/cli/commands/main/models.py

from __future__ import annotations

from dataclasses import dataclass

from doc_gen.cli.constants.enums import LogLevelChoices


@dataclass
class MainArgs:
    no_banner: bool
    help: bool
    version: bool | None
    debug: bool
    log_level: LogLevelChoices
