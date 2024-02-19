"""Enum definitions for parsing."""

from enum import Enum


class FileType(str, Enum):
    """Enum for file types."""

    TEXT = "txt"
    EXCEL = "xlsx"
    CSV = "csv"
    BATCH = "gw"


class GeneweaverFileType(str, Enum):
    """Enum for geneweaver specific file types."""

    BATCH = "batch"
    VALUES = "values"
