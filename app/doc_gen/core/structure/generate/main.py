# app/doc_gen/core/structure/generate/main.py

"""
Application service for:

    doc-gen structure generate
"""

import logging
from time import perf_counter

from doc_gen.cli.commands.structure.generate.models import (
    StructureGenerateArgs,
)
from doc_gen.core.structure.common.config_builder import (
    StructureConfigBuilder,
)
from doc_gen.core.structure.factory import (
    StructureFactory,
)
from doc_gen.core.structure.generator.markdown_generator import (
    MarkdownGenerator,
)
from doc_gen.core.structure.presenters.generation_presenter import (
    GenerationPresenter,
)
from doc_gen.ui.console import console
from doc_gen.ui.panels import success_summary_panel
from doc_gen.ui.progress import progress_spinner
from doc_gen.ui.tables import configuration_table

logger = logging.getLogger(__name__)


class StructureGenerateMain:
    """
    Structure generation application service.

    Responsibilities
    ----------------
    - Build backend configuration
    - Create scanner service
    - Generate markdown document
    - Save markdown file
    """

    def execute(
        self,
        args: StructureGenerateArgs,
    ) -> None:
        """
        Execute structure generation workflow.

        Parameters
        ----------
        args:
            Generate command arguments.

        Responsibilities
        ----------------
        - Build backend configuration
        - Create scanner service
        - Generate markdown
        - Save output file
        - Report progress to the user
        """
        try:
            logger.info("Documentation generation started")

            logger.debug(
                "Target directory: %s",
                args.target_directory,
            )
            logger.debug(
                "Output file: %s",
                args.output_file,
            )

            start_time = perf_counter()

            with progress_spinner("Preparing configuration"):
                #
                # Build backend config
                #
                config = StructureConfigBuilder.from_args(
                    args,
                )

            if args.verbose:
                console.print(
                    configuration_table(
                        target_directory=args.target_directory,
                        profile=args.profile,
                        smart_mode=args.smart_mode,
                        max_depth=args.max_depth,
                        show_files=args.show_files,
                        collapse_dirs=args.collapse_dirs,
                        project_type=args.project_type,
                    )
                )

            with progress_spinner("Creating scanner"):
                scanner_service = StructureFactory.create_scanner(
                    config=config,
                )

            with progress_spinner("Generating documentation"):
                #
                # Markdown generator
                #
                generator = MarkdownGenerator(
                    config=config,
                    scanner_service=scanner_service,
                )

                #
                # Generate and save
                #

                result = generator.save(
                    output_file=args.output_file,
                    dry_run=args.dry_run,
                )

            logger.info(
                "Documentation %s: %s",
                "previewed" if args.dry_run else "generated",
                args.output_file,
            )

            console.print(GenerationPresenter().render(result))

            # Success

            elapsed_time = perf_counter() - start_time

            message = (
                "Dry run completed; no files were modified.\n\n"
                f"Would write: {args.output_file}"
                if args.dry_run
                else "PROJECT_STRUCTURE.md generated successfully.\n\n"
                f"Output: {args.output_file}"
            )
            console.print(
                success_summary_panel(
                    message=message,
                    elapsed_time=elapsed_time,
                )
            )

            logger.info("Documentation generation completed")

        except Exception:
            raise
