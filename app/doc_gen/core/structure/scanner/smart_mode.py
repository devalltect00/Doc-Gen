# app/doc_gen/core/structure/scanner/smart_mode.py

"""
Smart mode configuration adjustments.

Smart mode automatically adjusts structure
generation settings based on repository size.

This service is intentionally separated from
ScannerService to keep responsibilities isolated.
"""

from copy import deepcopy

from doc_gen.core.structure.common.models import (
    StructureConfig,
)


class SmartModeService:
    """
    Apply smart mode adjustments.

    Smart mode attempts to optimize the generated
    structure output based on repository size.
    """

    LARGE_PROJECT_SCORE = 5
    MEDIUM_PROJECT_SCORE = 3

    def apply(
        self,
        *,
        config: StructureConfig,
        score: int,
    ) -> StructureConfig:
        """
        Apply smart mode configuration.

        Parameters
        ----------
        config:
            Original structure configuration.

        score:
            Repository complexity score.

        Returns
        -------
        StructureConfig
            Adjusted configuration.

        Notes
        -----
        The original configuration is not modified.
        """

        #
        # Smart mode disabled
        #
        if not config.smart_mode:
            return config

        #
        # Create copy
        #
        adjusted = deepcopy(config)

        #
        # Large project
        #
        if score >= self.LARGE_PROJECT_SCORE:
            adjusted.max_depth = 2

            adjusted.show_files = False

            adjusted.collapse_dirs |= {
                "node_modules",
                ".venv",
                "venv",
                "dist",
                "build",
                ".next",
            }

            return adjusted

        #
        # Medium project
        #
        if score >= self.MEDIUM_PROJECT_SCORE:
            adjusted.max_depth = 3

            adjusted.show_files = True

            adjusted.collapse_dirs |= {
                "node_modules",
                ".venv",
                "venv",
            }

            return adjusted

        #
        # Small project
        #
        adjusted.max_depth = 5

        adjusted.show_files = True

        return adjusted
