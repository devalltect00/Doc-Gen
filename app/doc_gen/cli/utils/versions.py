# app/doc_gen/cli/utils/versions.py

import typer
import typer.rich_utils
from rich import print as rprint

from doc_gen.services.banner_service import BannerService
from doc_gen.theme import theme

banner = BannerService(package_name="DOC-GEN", font="slant")


def get_version():
    __version__ = banner.get_version()
    return __version__


def version_callback(value: bool):
    if value:
        __version__ = banner.get_version()
        rprint(
            f"[{theme.primary}]Doc Gen[/{theme.primary}]: [{theme.secondary}]{__version__}[/{theme.secondary}]"
        )
        raise typer.Exit()
