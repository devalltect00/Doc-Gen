"""Documentation metadata contributed by supported frameworks and tools."""

FRAMEWORK_DIRECTORIES = {
    "google-apps-script": {
        "src": {
            "description": "Google Apps Script source and deployment manifest.",
            "details": [
                "Contains Apps Script modules and, commonly, appsscript.json.",
                "Source may be compiled into a generated dist directory before push.",
            ],
        },
    },
    "laravel": {
        "bootstrap": {
            "description": "Laravel bootstrap code and generated framework cache.",
            "details": ["Initializes the framework and application container."],
        },
        "config": {
            "description": "Laravel application and package configuration.",
            "details": ["Contains version-controlled framework settings."],
        },
        "database": {
            "description": "Database migrations, factories, and seeders.",
            "details": ["Defines repeatable database state and test data."],
        },
        "resources": {
            "description": "Views and uncompiled frontend resources.",
            "details": ["Contains templates, styles, and client-side source files."],
        },
        "routes": {
            "description": "Laravel HTTP, console, and channel route definitions.",
            "details": ["Maps incoming requests and commands to application logic."],
        },
        "storage": {
            "description": "Runtime files, logs, caches, and generated content.",
            "details": ["Runtime output is normally excluded from documentation."],
        },
    },
    "gin": {
        "api": {
            "description": "HTTP API contracts or transport-layer definitions.",
            "details": ["May contain handlers, schemas, or generated API assets."],
        },
    },
}

FRAMEWORK_ROOT_FILES = {
    "google-apps-script": {
        ".claspignore": "Files excluded from clasp deployments.",
        ".clasp.example.json": "Safe example clasp project configuration.",
        "appsscript.json": "Google Apps Script runtime and deployment manifest.",
        "src/appsscript.json": "Google Apps Script runtime and deployment manifest.",
    },
    "nextjs": {
        "next.config.js": "Next.js application configuration.",
        "next.config.mjs": "Next.js application configuration.",
        "next.config.ts": "Next.js application configuration.",
    },
    "laravel": {
        "artisan": "Laravel command-line application entry point.",
    },
}
