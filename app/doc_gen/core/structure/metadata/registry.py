"""Resolve composable metadata for detected project fingerprints."""

from copy import deepcopy

from doc_gen.core.structure.metadata.ecosystems import (
    ECOSYSTEM_DIRECTORIES,
    ECOSYSTEM_ROOT_FILES,
)
from doc_gen.core.structure.metadata.frameworks import (
    FRAMEWORK_DIRECTORIES,
    FRAMEWORK_ROOT_FILES,
)
from doc_gen.core.structure.metadata.models import MetadataCatalog
from doc_gen.core.structure.metadata.repository_docs import (
    COMMON_DIRECTORIES,
    COMMON_ROOT_FILES,
)
from doc_gen.core.structure.scanner.models import ProjectFingerprint


class MetadataRegistry:
    """Merge common, ecosystem, and framework documentation metadata."""

    def resolve(self, fingerprint: ProjectFingerprint) -> MetadataCatalog:
        """Return metadata in deterministic common-to-specific precedence."""

        directories = deepcopy(COMMON_DIRECTORIES)
        root_files = dict(COMMON_ROOT_FILES)

        for ecosystem in fingerprint.ecosystems:
            directories.update(deepcopy(ECOSYSTEM_DIRECTORIES.get(ecosystem, {})))
            root_files.update(ECOSYSTEM_ROOT_FILES.get(ecosystem, {}))

        for framework in fingerprint.frameworks:
            directories.update(deepcopy(FRAMEWORK_DIRECTORIES.get(framework, {})))
            root_files.update(FRAMEWORK_ROOT_FILES.get(framework, {}))

        return MetadataCatalog(
            directories=directories,
            root_files=root_files,
        )
