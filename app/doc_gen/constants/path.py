# app/doc_gen/constants/path.py

from pathlib import Path

# PROJECT SOURCE
THIS_PROJECT_SOURCE = ["doc_gen"]

### FILES PATH
DOC_GEN_SETTINGS = Path(".config/doc_gen/config.toml")

# LOG
LOG_DIRECTORY = "logs"
LOG_FILENAME = "doc_gen.log"

#####

THIS_PROJECT_SOURCE_WITH_DOTS = ".".join(THIS_PROJECT_SOURCE)
THIS_PROJECT_SOURCE_WITH_SLASH = "/".join(THIS_PROJECT_SOURCE)
