# app/doc_gen/cli/commands/structure/profiles.py

"""
Predefined configuration profiles for project structure output.
"""

PROFILES = {
    "minimal": {
        "max_depth": 2,
        "show_files": False,
        "collapse_dirs": {
            "node_modules",
            "venv",
            ".venv",
            "dist",
            "build",
            ".next",
        },
    },
    "default": {
        "max_depth": 3,
        "show_files": True,
        "collapse_dirs": {"node_modules", "venv", ".venv"},
    },
    "detailed": {
        "max_depth": 5,
        "show_files": True,
        "collapse_dirs": set(),
    },
    "custom": {},
}


def apply_profile(config, profile_name):
    profile = PROFILES.get(profile_name)

    if not profile:
        return config

    config.max_depth = profile["max_depth"]
    config.show_files = profile["show_files"]
    config.collapse_dirs = set(profile["collapse_dirs"])

    return config
