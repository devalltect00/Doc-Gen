# app/doc_gen/cli/commands/structure/print/command.py

"""
Command:

    doc-gen structure print
"""

import typer

from doc_gen.cli.commands.structure.common.options import (
    CollapseDirectoriesOption,
    DryRunOption,
    MaxDepthOption,
    ProfileOption,
    ProjectTypeOption,
    ShowFilesOption,
    SmartModeOption,
    TargetDirectoryArgument,
    VerboseOption,
)
from doc_gen.cli.commands.structure.common.resolver import (
    resolve_structure_common_args,
)
from doc_gen.cli.errors import handle_cli_errors
from doc_gen.config.config_loader import get_config
from doc_gen.core.structure.print.main import (
    StructurePrintMain,
)

from .resolver import (
    resolve_structure_print_args,
)

app = typer.Typer()


@app.callback(invoke_without_command=True)
@handle_cli_errors(
    "Structure printing",
    solution="Verify the target directory and selected profile before retrying.",
)
def print_structure(
    target_directory: TargetDirectoryArgument = None,
    profile: ProfileOption = None,
    smart_mode: SmartModeOption = None,
    max_depth: MaxDepthOption = None,
    show_files: ShowFilesOption = None,
    collapse_dirs: CollapseDirectoriesOption = None,
    project_type: ProjectTypeOption = None,
    verbose: VerboseOption = None,
    dry_run: DryRunOption = None,
):
    """
    Print project structure to terminal.
    """

    config = get_config()

    common_args = resolve_structure_common_args(
        config=config,
        target_directory=target_directory,
        profile=profile,
        smart_mode=smart_mode,
        max_depth=max_depth,
        show_files=show_files,
        collapse_dirs=collapse_dirs,
        project_type=project_type,
        verbose=verbose,
        dry_run=dry_run,
    )

    args = resolve_structure_print_args(
        config=config,
        common_args=common_args,
    )

    #
    # TODO
    #
    # StructurePrintMain().execute(args)
    #
    # typer.echo(args)

    StructurePrintMain().execute(args)
