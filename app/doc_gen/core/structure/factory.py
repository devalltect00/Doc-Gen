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

from __future__ import annotations

from doc_gen.core.structure.common.models import (
    StructureConfig,
)
from doc_gen.core.structure.scanner.models import ProjectFingerprint
from doc_gen.core.structure.scanner.project_detector import ProjectDetector
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
        fingerprint: ProjectFingerprint | None = None,
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

        resolved_fingerprint = fingerprint or ProjectDetector(
            config.target_directory
        ).detect_fingerprint(config.project_type)

        return IgnoreLoader(
            root_path=str(
                config.target_directory,
            ),
            project_type=resolved_fingerprint.primary_type,
            project_types=resolved_fingerprint.detected_technologies,
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

        fingerprint = ProjectDetector(config.target_directory).detect_fingerprint(
            config.project_type
        )
        ignore_loader = cls.create_ignore_loader(config, fingerprint)

        return ScannerService(
            config=config,
            ignore_loader=ignore_loader,
            fingerprint=fingerprint,
        )
