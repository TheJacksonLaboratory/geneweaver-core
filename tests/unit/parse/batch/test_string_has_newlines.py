"""Tests for the string_has_newlines function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.batch import string_has_newlines


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        # test string without newlines
        ("Hello, world!", False),
        # test string with newline character
        ("Hello,\nworld!", True),
        # test string with carriage return
        ("Hello,\rworld!", True),
        # test string with newline and carriage return
        ("Hello,\r\nworld!", True),
        # test multiline string
        (
            """
        Hello,
        world!
        """,
            True,
        ),
        # test string with spaces and no newlines
        ("     ", False),
        # test empty string
        ("", False),
        # test string with tabs and no newlines
        ("Hello\t\tworld!", False),
        ("Hello \t world!", False),
        # test string with tabs and newlines
        ("Hello\t\t\nworld!", True),
        ("Hello \t \n world!", True),
        # test string with tabs and carriage returns
        ("Hello\t\t\rworld!", True),
        ("Hello \t \r world!", True),
        # test string with tabs and carriage returns and newlines
        ("Hello\t\t\r\nworld!", True),
        ("Hello\t\r\n world!", True),
        # test string with tabs and carriage returns and newlines and spaces
        ("Hello\t\t \r\n world!", True),
        ("Hello\t\r\n world!", True),
    ],
)
def test_string_has_newlines(input_str, expected):
    """Test that string_has_newlines returns the expected value."""
    assert string_has_newlines(input_str) == expected
