# app/doc_gen/core/structure/generator/markdown_generator.py

"""
Markdown generation orchestration.
"""

from pathlib import Path

from doc_gen.core.structure.common.models import (
    StructureConfig,
)
from doc_gen.core.structure.generator.models import (
    GenerationResult,
    MarkdownDocument,
)
from doc_gen.core.structure.generator.renderers.directory_details_renderer import (
    DirectoryDetailsRenderer,
)
from doc_gen.core.structure.generator.renderers.notes_renderer import (
    NotesRenderer,
)
from doc_gen.core.structure.generator.renderers.repository_overview_renderer import (
    RepositoryOverviewRenderer,
)
from doc_gen.core.structure.generator.renderers.repository_structure_renderer import (
    RepositoryStructureRenderer,
)
from doc_gen.core.structure.generator.renderers.root_files_renderer import (
    RootFilesRenderer,
)
from doc_gen.core.structure.generator.writers.markdown_writer import (
    MarkdownWriter,
)
from doc_gen.core.structure.scanner.scanner_service import (
    ScannerService,
)


class MarkdownGenerator:
    """
    Generate repository markdown documentation.

    Responsibilities
    ----------------

    - Collect repository information from scanner services
    - Render markdown sections
    - Assemble final markdown document
    - Persist markdown document to disk
    - Return generation metadata for UI presentation
    """

    def __init__(
        self,
        *,
        config: StructureConfig,
        scanner_service: ScannerService,
    ) -> None:
        """
        Initialize markdown generator.

        Parameters
        ----------
        config:
            Resolved structure configuration.

        scanner_service:
            Scanner service used to collect repository data.
        """

        self.config = config

        self.scanner_service = scanner_service

        self.repository_overview_renderer = RepositoryOverviewRenderer()

        self.repository_structure_renderer = RepositoryStructureRenderer()

        self.root_files_renderer = RootFilesRenderer()

        self.directory_details_renderer = DirectoryDetailsRenderer()

        self.notes_renderer = NotesRenderer()

        self.writer = MarkdownWriter()

    def generate_document(
        self,
    ) -> MarkdownDocument:
        """
        Generate markdown document.

        Returns
        -------
        MarkdownDocument
            Fully assembled markdown content.
        """

        tree = self.scanner_service.generate_tree()

        directories = self.scanner_service.detect_top_directories()

        project_type = self.scanner_service.project_type

        sections = [
            "# Project Structure",
            "",
            self.repository_overview_renderer.render(),
            "",
            "---",
            "",
            self.repository_structure_renderer.render(
                project_type=project_type,
                tree=tree,
            ),
            "",
            "---",
            "",
            self.root_files_renderer.render(
                root_directory=self.config.target_directory,
            ),
            "",
            "---",
            "",
            self.directory_details_renderer.render(
                directories=directories,
            ),
            "",
            "---",
            "",
            self.notes_renderer.render(),
            "",
        ]

        return MarkdownDocument(
            content="\n".join(sections),
        )

    def save(
        self,
        *,
        output_file: Path,
        dry_run: bool = False,
    ) -> GenerationResult:
        """
        Generate and save markdown documentation.

        Parameters
        ----------
        output_file:
            Destination markdown file.

        dry_run:
            Generate result metadata without writing the output file.

        Returns
        -------
        GenerationResult
            Metadata describing the generated document.
        """

        tree = self.scanner_service.generate_tree()

        directories = self.scanner_service.detect_top_directories()

        document = self.generate_document()

        if not dry_run:
            self.writer.write(
                output_file=output_file,
                content=document.content,
            )

        return GenerationResult(
            output_file=output_file,
            project_type=self.scanner_service.project_type,
            directory_count=len(directories),
            tree_line_count=len(tree),
            dry_run=dry_run,
        )
