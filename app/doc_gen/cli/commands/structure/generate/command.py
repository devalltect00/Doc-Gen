# app/doc_gen/cli/commands/structure/generate/command.py

"""
Command:

    doc-gen structure generate
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
from doc_gen.core.structure.generate.main import (
    StructureGenerateMain,
)

from .options import (
    OutputFileOption,
)
from .resolver import (
    resolve_structure_generate_args,
)

app = typer.Typer()


@app.callback(invoke_without_command=True)
@handle_cli_errors(
    "Documentation generation",
    solution=(
        "Verify the target directory and output path are accessible, then "
        "preview the result with --dry-run."
    ),
)
def generate(
    target_directory: TargetDirectoryArgument = None,
    profile: ProfileOption = None,
    smart_mode: SmartModeOption = None,
    max_depth: MaxDepthOption = None,
    show_files: ShowFilesOption = None,
    collapse_dirs: CollapseDirectoriesOption = None,
    project_type: ProjectTypeOption = None,
    output_file: OutputFileOption = None,
    verbose: VerboseOption = None,
    dry_run: DryRunOption = None,
):
    """
    Generate PROJECT_STRUCTURE.md.

    Examples
    --------

    Generate with defaults:

        doc-gen structure generate

    Generate specific project:

        doc-gen structure generate ./project

    Generate with profile:

        doc-gen structure generate --profile detailed

    Generate with custom output:

        doc-gen structure generate \
            --output docs/PROJECT_STRUCTURE.md

    Generate using smart mode:

        doc-gen structure generate --smart
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

    args = resolve_structure_generate_args(
        config=config,
        common_args=common_args,
        output_file=output_file,
    )

    #
    # TEMPORARY
    #
    # Backend integration will happen later.
    #
    # typer.echo(args)

    # Example future usage:
    #
    # StructureGenerateMain().execute(args)

    StructureGenerateMain().execute(args)
