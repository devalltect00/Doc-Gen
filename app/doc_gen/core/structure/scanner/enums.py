# app/doc_gen/core/structure/scanner/enums.py

"""
Scanner enums.
"""

from enum import Enum


class ProjectType(str, Enum):
    GENERIC = "generic"

    PYTHON = "python"
    DJANGO = "django"
    FLASK = "flask"
    FASTAPI = "fastapi"

    NODEJS = "nodejs"
    REACTJS = "reactjs"
    NEXTJS = "nextjs"
    GOOGLE_APPS_SCRIPT = "google-apps-script"

    PHP = "php"
    LARAVEL = "laravel"

    GO = "go"
    GIN = "gin"
