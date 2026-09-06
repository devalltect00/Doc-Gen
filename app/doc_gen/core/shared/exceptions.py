# app/doc_gen/core/shared/exceptions.py

"""
Shared exceptions used by Doc-Gen.

This module contains application-specific exceptions used
throughout the project.

Using dedicated exception types makes error handling,
testing, and debugging easier.
"""


class DocGenError(Exception):
    """
    Base exception for Doc-Gen.

    All custom Doc-Gen exceptions should inherit from this
    exception.
    """


# =====================================================
# Configuration
# =====================================================


class ConfigurationError(DocGenError):
    """
    Raised when configuration is invalid.
    """


# =====================================================
# Validation
# =====================================================


class ValidationError(DocGenError):
    """
    Raised when validation fails.
    """
