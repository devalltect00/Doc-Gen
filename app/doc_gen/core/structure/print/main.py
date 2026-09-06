# app/doc_gen/core/structure/print/main.py

"""
Application service for:

    doc-gen structure print
"""

import logging
from time import perf_counter

from doc_gen.cli.commands.structure.print.models import (
    StructurePrintArgs,
)
from doc_gen.core.structure.common.config_builder import (
    StructureConfigBuilder,
)
from doc_gen.core.structure.factory import (
    StructureFactory,
)
from doc_gen.core.structure.presenters.tree_presenter import (
    TreePresenter,
)
from doc_gen.ui.console import console
from doc_gen.ui.panels import success_summary_panel
from doc_gen.ui.progress import progress_spinner
from doc_gen.ui.tables import configuration_table

logger = logging.getLogger(__name__)


class StructurePrintMain:
    """
    Print repository structure.
    """

    def execute(
        self,
        args: StructurePrintArgs,
    ) -> None:
        """
        Execute print operation.
        """
        try:
            logger.info("Structure print started")

            logger.debug(
                "Target directory: %s",
                args.target_directory,
            )
            logger.debug(
                "Profile: %s",
                args.profile,
            )
            logger.debug(
                "Max depth: %s",
                args.max_depth,
            )
            logger.debug(
                "Show files: %s",
                args.show_files,
            )

            start_time = perf_counter()

            with progress_spinner("Preparing configuration"):
                config = StructureConfigBuilder.from_args(args)

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

            logger.debug("Scanner created")

            with progress_spinner("Generating structure tree"):
                tree = scanner_service.generate_tree()

            logger.debug(
                "Generated tree with %s lines",
                len(tree),
            )

            output = TreePresenter().render(tree)

            console.print(output)

            # Success

            elapsed_time = perf_counter() - start_time

            console.print(
                success_summary_panel(
                    message="Structure tree printed successfully.",
                    elapsed_time=elapsed_time,
                )
            )

            logger.info("Structure print completed")

        except Exception:
            raise
