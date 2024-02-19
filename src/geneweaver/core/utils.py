"""Utility functions for use across the geneweaver core package."""

from typing import Any


def add_to_dict_if_not_none(d: dict, key: str, value: Any) -> None:  # noqa: ANN401
    """Add a value to a dictionary only if the value is not None.

    :param dict d: The dictionary to which the value should be added.
    :param str key: The key under which the value should be added.
    :param Any value: The value to be added. If this is None, the function does nothing.
    """
    if value is not None:
        d[key] = value
