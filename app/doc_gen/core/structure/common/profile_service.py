# app/doc_gen/core/structure/common/profile_service.py

"""
Profile application service.
"""

from copy import deepcopy

from doc_gen.core.structure.common.models import (
    StructureConfig,
)
from doc_gen.core.structure.profiles import (
    PROFILES,
)


class ProfileService:
    """
    Apply structure profiles.
    """

    def apply(
        self,
        *,
        config: StructureConfig,
        profile_name,
    ) -> StructureConfig:
        """
        Apply profile configuration.
        """

        profile = PROFILES.get(
            profile_name,
        )

        if profile is None:
            return config

        # print("profile",profile)

        if profile == "custom":
            return config

        updated = deepcopy(
            config,
        )

        updated.max_depth = profile.max_depth

        updated.show_files = profile.show_files

        updated.collapse_dirs = set(
            profile.collapse_dirs,
        )

        return updated
