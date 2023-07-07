"""Test the is_batch_file function in geneweaver.core.parse.batch."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.batch import (
    GeneweaverFileType,
    IgnoreLineError,
    NotAHeaderRowError,
    UnsupportedFileTypeError,
    is_batch_file,
)

# First we'll mock out the process_header_line and process_value_line functions
# so that we can test the is_batch_file function in isolation.


# Tests to handle NotAHeaderRowError
@patch("geneweaver.core.parse.batch.process_header_line")
@patch("geneweaver.core.parse.batch.process_value_line")
def test_is_batch_file_header_error(mock_process_value_line, mock_process_header_line):
    """Test the case where we error reading the header line, but can read as a value."""
    mock_process_header_line.side_effect = NotAHeaderRowError()
    mock_process_value_line.return_value = "value"

    file_type = is_batch_file("header_line_1")

    assert file_type == GeneweaverFileType.VALUES
    assert mock_process_header_line.call_count == 1
    assert mock_process_value_line.call_count == 1


# Tests to handle IgnoreLineError
@patch("geneweaver.core.parse.batch.process_header_line")
def test_is_batch_file_ignore_line_error(mock_process_header_line):
    """If all lines are ignore lines, we consider it an unsupported file type."""
    mock_process_header_line.side_effect = IgnoreLineError()

    with pytest.raises(UnsupportedFileTypeError):
        is_batch_file("header_line_1")

    assert mock_process_header_line.call_count == 1


# Tests to process valid header and value lines
@patch("geneweaver.core.parse.batch.process_header_line")
@patch("geneweaver.core.parse.batch.process_value_line")
@pytest.mark.parametrize(
    ("process_return", "expected_file_type"),
    [
        ("header", GeneweaverFileType.BATCH),
        ("value", GeneweaverFileType.VALUES),
    ],
)
def test_is_batch_file(
    mock_process_value_line,
    mock_process_header_line,
    process_return,
    expected_file_type,
):
    """Let's mix them together and test both header and value lines.

    Here we test that if process_header_line returns a value, we return BATCH,
    and if it errors but process_value_line returns a value, we return VALUES.
    """
    if expected_file_type == GeneweaverFileType.BATCH:
        mock_process_header_line.return_value = process_return
    else:
        mock_process_header_line.side_effect = NotAHeaderRowError()
        mock_process_value_line.return_value = process_return

    file_type = is_batch_file("line_1")

    assert file_type == expected_file_type
    assert mock_process_header_line.call_count == 1
    if expected_file_type == GeneweaverFileType.BATCH:
        assert mock_process_value_line.call_count == 0
    else:
        assert mock_process_value_line.call_count == 1


# Now we'll test the is_batch_file function with real data. Without mocking
# the process_header_line and process_value_line functions, we'll be able to
# test the entire process of determining the file type.


@pytest.mark.parametrize(
    ("contents", "expected"),
    [
        ("!\theader\nsymbol\tvalue", GeneweaverFileType.BATCH),
        ("!header\nsymbol\tvalue", GeneweaverFileType.BATCH),
        ("! header\nsymbol value", GeneweaverFileType.BATCH),
        ("symbol\tvalue", GeneweaverFileType.VALUES),
        ("symbol value", GeneweaverFileType.VALUES),
        ("symbol  value\n! header", GeneweaverFileType.VALUES),
    ],
)
def test_is_batch_with_example_content(contents, expected):
    """Test the is_batch_file function with example content."""
    file_type = is_batch_file(contents)
    assert file_type == expected


@pytest.mark.parametrize(
    ("contents", "expected"),
    [
        ("value1\tvalue2\tvalue3\n", UnsupportedFileTypeError),
        ("value1\nvalue2\nvalue3\n", UnsupportedFileTypeError),
        ("#ignore_line_1\n#ignore_line_2\n", UnsupportedFileTypeError),
    ],
)
def test_is_batch_with_example_content_errors(contents, expected):
    """Test the is_batch_file function raises the right error with example content."""
    with pytest.raises(expected):
        _ = is_batch_file(contents)
