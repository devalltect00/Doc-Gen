# app/doc_gen/core/structure/common/config_builder.py

"""
Configuration builders.

Convert CLI argument models into backend models.
"""

from doc_gen.core.structure.common.models import (
    StructureConfig,
)
from doc_gen.core.structure.common.profile_service import ProfileService


class StructureConfigBuilder:
    """
    Build backend configuration objects.

    Any structure command args model that contains
    StructureCommonArgs fields can be converted.
    """

    @staticmethod
    def from_args(
        args,
    ) -> StructureConfig:
        """
        Build StructureConfig from any
        structure command args model.

        Parameters
        ----------
        args:
            StructureGenerateArgs
            StructurePrintArgs
            StructureAnalyzeArgs

        Returns
        -------
        StructureConfig
        """

        config = StructureConfig(
            target_directory=args.target_directory,
            max_depth=args.max_depth,
            show_files=args.show_files,
            collapse_dirs=args.collapse_dirs,
            smart_mode=args.smart_mode,
            project_type=args.project_type,
        )

        config = ProfileService().apply(
            config=config,
            profile_name=args.profile,
        )

        return config
