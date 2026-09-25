"""Models for project-aware repository documentation metadata."""

from dataclasses import dataclass

DirectoryMetadata = dict[str, dict[str, object]]
RootFileMetadata = dict[str, str]


@dataclass(frozen=True)
class MetadataCatalog:
    """Resolved directory and root-file documentation for one repository."""

    directories: DirectoryMetadata
    root_files: RootFileMetadata
