# app/doc_gen/core/structure/scanner/models.py

"""
Scanner result models.
"""

from dataclasses import dataclass

from doc_gen.core.structure.scanner.enums import (
    ProjectType,
)


@dataclass
class AnalysisResult:
    """
    Repository analysis result.
    """

    project_type: ProjectType

    project_size: int

    project_score: int

    category: str

    top_directories: list[str]

    smart_mode_enabled: bool

    max_depth_used: int


@dataclass(frozen=True)
class ProjectFingerprint:
    """Describe the primary project type and its composable technology signals.

    The primary type preserves Doc Gen's existing single-value contract. The
    remaining fields let scanners and renderers combine ecosystem, framework,
    and tool-specific behavior for repositories that use more than one stack.
    """

    primary_type: ProjectType
    ecosystems: tuple[str, ...] = ()
    frameworks: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()

    @property
    def detected_technologies(self) -> tuple[str, ...]:
        """Return a stable, de-duplicated list of detected technology labels."""

        return tuple(
            dict.fromkeys(
                (
                    self.primary_type.value,
                    *self.ecosystems,
                    *self.frameworks,
                    *self.tools,
                )
            )
        )
