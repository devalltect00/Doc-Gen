# app/doc_gen/core/structure/scanner/enums.py

"""
Scanner enums.
"""

from enum import Enum


class ProjectType(str, Enum):
    GENERIC = "generic"

    PYTHON = "python"
    DJANGO = "django"

    NODEJS = "nodejs"
    REACTJS = "reactjs"
    NEXTJS = "nextjs"
