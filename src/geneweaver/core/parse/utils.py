"""Utility functions for the parser module."""

from pathlib import Path
from typing import Dict, List

from geneweaver.core.parse.enum import FileType
from geneweaver.core.types import StringOrPath


def get_file_type(file_path: StringOrPath) -> FileType:
    """Determine if a file at a given path is a csv or xlsx file.

    :param file_path: Path to the file.

    :returns: The file type.
                - 'csv' if the file is a CSV file,
                - 'xlsx' if the file is an Excel file.

    :raises ValueError: If the file type is not supported.
    """
    file_path = Path(file_path)  # convert to Path object if not already
    extension = file_path.suffix.lower()

    if extension == ".csv":
        return FileType.CSV
    elif extension == ".xlsx":
        return FileType.EXCEL
    elif extension == ".txt":
        return FileType.TEXT
    else:
        raise ValueError(f"Unsupported file type {extension}.")


def read_file_content(file_path: StringOrPath) -> str:
    """Read the content of the file at a given path.

    :param file_path: Path to the file.

    :returns: The content of the file as a string.

    :raises FileNotFoundError: If the file does not exist.
    :raises IsADirectoryError: If the path points to a directory.
    :raises PermissionError: If the file is not readable.
    """
    with open(file_path, "r") as f:
        content = f.read()

    return content


def replace_keys(
    data: List[Dict[str, str]], new_keys: List[str]
) -> List[Dict[str, str]]:
    """Replace keys in a list of dictionaries.

    :param data: Original list of dictionaries.
    :param new_keys: List of new keys. The order should correspond to the order of
    original keys.

    :returns: A new list of dictionaries with replaced keys.
    """
    new_data = []
    for row in data:
        new_row = dict(zip(new_keys, row.values()))  # noqa: B905
        new_data.append(new_row)
    return new_data
