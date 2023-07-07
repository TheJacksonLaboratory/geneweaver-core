"""Enum definitions for parsing."""
from enum import Enum


class GeneweaverFileType(str, Enum):
    """Enum for geneweaver specific file types."""

    BATCH = "batch"
    VALUES = "values"
