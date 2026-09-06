# app/doc_gen/core/initialize/registry.py

from doc_gen.constants.path import (
    DOC_GEN_SETTINGS,
)
from doc_gen.core.initialize.loader import load_template
from doc_gen.core.initialize.models.template_file import TemplateFile


class DirRegistry:
    @staticmethod
    def get_config_directories() -> list[str]:
        return [".config/doc_gen"]

    def get_all_directories(self) -> list[str]:
        return [
            *self.get_config_directories(),
        ]


class FileRegistry:
    def __init__(self):
        # =========================
        # CONFIG
        # =========================
        self.config = TemplateFile(
            target_path=DOC_GEN_SETTINGS,
            content=lambda: load_template("config.toml"),
        )

    @staticmethod
    def get_config() -> list[TemplateFile]:
        # =========================
        # CONFIG
        # =========================
        return [
            TemplateFile(
                target_path=DOC_GEN_SETTINGS,
                content=lambda: load_template("config.toml"),
            )
        ]

    def get_all_files(self) -> list[TemplateFile]:
        return [
            *self.get_config(),
        ]
