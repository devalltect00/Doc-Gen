# app/doc_gen/core/structure/factory.py

"""
Structure service factory.

Provides centralized creation of structure-related
services and dependencies.

This helps eliminate duplicated service creation
logic across:

    - StructureGenerateMain
    - StructurePrintMain
    - StructureAnalyzeMain
"""

from doc_gen.core.structure.common.models import (
    StructureConfig,
)
from doc_gen.core.structure.scanner.scanner_service import (
    ScannerService,
)
from doc_gen.utils.ignore_loader import (
    IgnoreLoader,
)


class StructureFactory:
    """
    Factory for structure services.

    This class centralizes creation of:

        - IgnoreLoader
        - ScannerService

    Future services can also be added here:

        - MarkdownGenerator
        - ExportService
        - ValidationService
        - CompareService
    """

    @staticmethod
    def create_ignore_loader(
        config: StructureConfig,
    ) -> IgnoreLoader:
        """
        Create IgnoreLoader.

        Parameters
        ----------
        config:
            Structure configuration.

        Returns
        -------
        IgnoreLoader
        """

        return IgnoreLoader(
            root_path=str(
                config.target_directory,
            ),
            project_type=config.project_type,
        )

    @classmethod
    def create_scanner(
        cls,
        *,
        config: StructureConfig,
    ) -> ScannerService:
        """
        Create ScannerService.

        Parameters
        ----------
        config:
            Structure configuration.

        Returns
        -------
        ScannerService
        """

        ignore_loader = cls.create_ignore_loader(
            config,
        )

        return ScannerService(
            config=config,
            ignore_loader=ignore_loader,
        )
