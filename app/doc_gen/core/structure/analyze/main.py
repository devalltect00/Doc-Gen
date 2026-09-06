# app/doc_gen/core/structure/analyze/main.py

"""
Application service for:

    doc-gen structure analyze
"""

import logging
from time import perf_counter

from doc_gen.cli.commands.structure.analyze.models import (
    StructureAnalyzeArgs,
)
from doc_gen.core.structure.common.config_builder import (
    StructureConfigBuilder,
)
from doc_gen.core.structure.factory import (
    StructureFactory,
)
from doc_gen.core.structure.presenters.analysis_presenter import (
    AnalysisPresenter,
)
from doc_gen.ui.console import console
from doc_gen.ui.panels import success_summary_panel
from doc_gen.ui.progress import progress_spinner
from doc_gen.ui.tables import configuration_table

logger = logging.getLogger(__name__)


class StructureAnalyzeMain:
    """
    Analyze repository structure.
    """

    def execute(
        self,
        args: StructureAnalyzeArgs,
    ) -> None:
        """
        Execute analysis.
        """
        try:
            logger.info("Repository analysis started")

            start_time = perf_counter()

            with progress_spinner("Preparing configuration"):
                config = StructureConfigBuilder.from_args(args)

            # print("args",args)

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

            # print("config", config)

            with progress_spinner("Creating scanner"):
                scanner_service = StructureFactory.create_scanner(
                    config=config,
                )

            with progress_spinner("Analyzing repository"):
                result = scanner_service.analyze()

            # print("result",result)

            logger.debug(
                "Project type: %s",
                result.project_type,
            )

            logger.debug(
                "Score: %s",
                result.project_score,
            )

            logger.debug(
                "Category: %s",
                result.category,
            )

            output = AnalysisPresenter().render(result)
            console.print(output)

            # Success

            elapsed_time = perf_counter() - start_time

            console.print(
                success_summary_panel(
                    message="Repository analysis completed.",
                    elapsed_time=elapsed_time,
                )
            )

            logger.info("Repository analysis completed")

        except Exception:
            raise
