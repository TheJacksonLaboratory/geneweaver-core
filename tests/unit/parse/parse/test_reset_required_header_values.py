"""Tests for the reset_required_header_values function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.parse import (
    HEADER_CHARACTERS,
    REQUIRED_HEADERS,
    SPACE_SEPARATED_HEADER_CHARACTERS,
    reset_required_header_values,
)


@pytest.mark.parametrize(
    ("header", "expected"),
    [
        # Only required keys are present
        (
            {
                HEADER_CHARACTERS[key]: f"value{index}"
                for index, key in enumerate(REQUIRED_HEADERS)
            },
            {},
        ),
        # Extra keys are present, but all required keys are still there
        (
            {
                **{
                    HEADER_CHARACTERS[key]: f"value{index}"
                    for index, key in enumerate(REQUIRED_HEADERS)
                },
                "extra_key": "extra_value",
            },
            {"extra_key": "extra_value"},
        ),
        # All possible non-spaced header keys are present
        (
            {
                **{
                    header_name: f"value{index}"
                    for index, header_name in enumerate(
                        list(HEADER_CHARACTERS.values())
                    )
                },
                "extra_key": "extra_value",
            },
            {
                **{
                    header_name: f"value{index}"
                    for index, header_name in enumerate(
                        list(HEADER_CHARACTERS.values())
                    )
                    if header_name
                    not in (HEADER_CHARACTERS[k] for k in REQUIRED_HEADERS)
                },
                "extra_key": "extra_value",
            },
        ),
        # All possible header keys are present
        (
            {
                **{
                    header_name: f"value{index}"
                    for index, header_name in enumerate(
                        list(HEADER_CHARACTERS.values())
                        + list(SPACE_SEPARATED_HEADER_CHARACTERS.values())
                    )
                },
                "extra_key": "extra_value",
            },
            {
                **{
                    header_name: f"value{index}"
                    for index, header_name in enumerate(
                        list(HEADER_CHARACTERS.values())
                        + list(SPACE_SEPARATED_HEADER_CHARACTERS.values())
                    )
                    if header_name
                    not in (HEADER_CHARACTERS[k] for k in REQUIRED_HEADERS)
                },
                "extra_key": "extra_value",
            },
        ),
        # No required keys are present
        ({"extra_key": "extra_value"}, {"extra_key": "extra_value"}),
        # Empty header
        ({}, {}),
    ],
)
def test_reset_required_header_values(header, expected):
    """Test that the reset_required_header_values function works as expected."""
    result = reset_required_header_values(header)
    assert result == expected, f"Expected {expected}, but got {result}"
