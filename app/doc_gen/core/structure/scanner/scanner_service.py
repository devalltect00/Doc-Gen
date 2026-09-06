# app/doc_gen/core/structure/scanner/scanner_service.py

"""
Structure scanner orchestration service.
"""

from doc_gen.core.structure.common.models import (
    StructureConfig,
)
from doc_gen.core.structure.scanner.models import (
    AnalysisResult,
)
from doc_gen.core.structure.scanner.project_analyzer import (
    ProjectAnalyzer,
)
from doc_gen.core.structure.scanner.project_detector import (
    ProjectDetector,
)
from doc_gen.core.structure.scanner.smart_mode import (
    SmartModeService,
)
from doc_gen.core.structure.scanner.tree_generator import (
    TreeGenerator,
)


class ScannerService:
    """
    Central structure scanner service.

    Responsibilities
    ----------------
    - Detect project type
    - Analyze repository
    - Apply smart mode adjustments
    - Generate repository tree

    Notes
    -----
    This class acts as the orchestration layer between
    detector, analyzer, smart-mode, and tree-generation services.
    """

    def __init__(
        self,
        *,
        config: StructureConfig,
        ignore_loader,
    ) -> None:
        """
        Initialize scanner service.

        Parameters
        ----------
        config:
            Structure configuration.

        ignore_loader:
            Ignore loader instance.
        """

        # print("config", config)

        self.ignore_loader = ignore_loader

        #
        # Detect project type
        #
        self.project_type = (
            config.project_type
            or ProjectDetector(
                config.target_directory,
            ).detect()
        )

        #
        # Repository analyzer
        #
        self.project_analyzer = ProjectAnalyzer(
            root_directory=config.target_directory,
            ignore_loader=ignore_loader,
        )

        #
        # Apply smart mode adjustments
        #
        score = self.project_analyzer.calculate_project_score()

        self.config = SmartModeService().apply(
            config=config,
            score=score,
        )

        #
        # Tree generator
        #
        self.tree_generator = TreeGenerator(
            root_directory=self.config.target_directory,
            ignore_loader=ignore_loader,
            max_depth=self.config.max_depth,
            show_files=self.config.show_files,
            collapse_dirs=self.config.collapse_dirs,
        )

    def generate_tree(self) -> list[str]:
        """
        Generate repository tree.

        Returns
        -------
        list[str]
        """
        return self.tree_generator.generate_tree()

    def detect_top_directories(self) -> list[str]:
        """
        Detect top-level directories.

        Returns
        -------
        list[str]
        """
        return self.tree_generator.detect_top_directories()

    def analyze(self) -> AnalysisResult:
        """
        Analyze repository.

        Returns
        -------
        AnalysisResult
        """

        score = self.project_analyzer.calculate_project_score()

        return AnalysisResult(
            project_type=self.project_type,
            project_size=self.project_analyzer.get_project_size(
                include_folders=False,
            ),
            project_score=score,
            category=self.project_analyzer.get_project_category(),
            top_directories=self.detect_top_directories(),
            smart_mode_enabled=self.config.smart_mode,
            max_depth_used=self.config.max_depth,
        )
