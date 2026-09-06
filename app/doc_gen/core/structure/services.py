# app/doc_gen/core/structure/services.py

"""
Structure service factory.
"""

from doc_gen.core.structure.scanner.scanner_service import (
    ScannerService,
)


class StructureServices:
    """
    Convenience factory.
    """

    @staticmethod
    def scanner(
        *,
        config,
        ignore_loader,
    ) -> ScannerService:
        return ScannerService(
            config=config,
            ignore_loader=ignore_loader,
        )
