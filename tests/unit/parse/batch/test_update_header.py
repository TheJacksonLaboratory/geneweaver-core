"""Tests for the update_header function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.batch import update_header


@pytest.mark.parametrize(
    ("key", "value", "header", "expected"),
    [
        # Test case where key is "description" and header does not already contain
        # "description"
        ("description", "new description", {}, {"description": " new description"}),
        # Test case where key is "description" and header already contains "description"
        (
            "description",
            "new description",
            {"description": "old description"},
            {"description": "old description new description"},
        ),
        # Test case where key is not "description" and header does not already contain
        # the key
        ("name", "new name", {}, {"name": "new name"}),
        # Test case where key is not "description" and header already contains the key
        ("name", "new name", {"name": "old name"}, {"name": "new name"}),
        # Test case where header contains other keys
        (
            "name",
            "new name",
            {"description": "description", "abbreviation": "abbreviation"},
            {
                "description": "description",
                "abbreviation": "abbreviation",
                "name": "new name",
            },
        ),
        # Test case where key is "description", value is empty string and header does
        # not contain "description"
        ("description", "", {}, {"description": " "}),
        # Test case where key is "description", value is empty string and header
        # contains "description"
        (
            "description",
            "",
            {"description": "old description"},
            {"description": "old description "},
        ),
        # Test case where key is not "description", value is empty string and header
        # does not contain the key
        ("name", "", {}, {"name": ""}),
        # Test case where key is not "description", value is empty string and header
        # contains the key
        ("name", "", {"name": "old name"}, {"name": ""}),
        # Test case where key is not "description", value is None and header contains
        # the key
        ("name", None, {"name": "old name"}, {"name": None}),
        # Test case where key is not "description", value is None and header does not
        # contain the key
        ("name", None, {}, {"name": None}),
    ],
)
def test_update_header(key, value, header, expected):
    """Tests the update_header function."""
    result = update_header(key, value, header)
    assert result == expected, f"Expected {expected}, but got {result}"
