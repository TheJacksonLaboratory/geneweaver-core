"""Tests for the parse_qvalue function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.batch import (
    InvalidBatchValueLineError,
    MultiLineStringError,
    process_value_line,
)


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        # normal case
        ("key value", ("key", "value")),
        # keys and values with multiple words
        ("key1_key2 value1_value2", ("key1_key2", "value1_value2")),
        # values with numeric characters
        ("key1 123", ("key1", "123")),
        # keys with numeric characters
        ("key_123 value", ("key_123", "value")),
    ],
)
def test_process_value_line_success(line, expected):
    """Test that process_value_line returns the expected tuple."""
    assert process_value_line(line) == expected


@pytest.mark.parametrize(
    ("line", "exception"),
    [
        # line with more than two words
        ("key value extra", InvalidBatchValueLineError),
        # line with only one word
        ("singleword", InvalidBatchValueLineError),
        # line with newline characters
        ("key value\nkey value", MultiLineStringError),
        # empty line
        ("", InvalidBatchValueLineError),
    ],
)
def test_process_value_line_failure(line, exception):
    """Test that process_value_line raises the expected exception."""
    with pytest.raises(exception):
        process_value_line(line)
