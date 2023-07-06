"""Tests for the parse_qvalue function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.batch import (
    BatchUploadGeneset,
    IgnoreLineError,
    NotAHeaderRowError,
    ReadMode,
    process_lines,
)


def test_process_lines_with_batch_file_contents(example_batch_file_contents):
    """Test that process_lines returns a list of BatchUploadGeneset objects."""
    result = process_lines(example_batch_file_contents)

    # Asserts that result is a list and is not empty
    assert isinstance(result, list)
    assert len(result) > 0

    # Asserts that all items in the result list are of the expected type
    for item in result:
        assert isinstance(item, BatchUploadGeneset)


@pytest.mark.parametrize(
    "contents",
    [
        "header_line\ncontent_line\n",
        "header_line\rcontent_line\r",
        "header_line\ncontent_line\r",
        "header_line\rcontent_line\n",
    ],
)
@pytest.mark.parametrize(
    "read_header_error",
    [
        IgnoreLineError,
        NotAHeaderRowError,
    ],
)
@pytest.mark.parametrize(
    "read_mode",
    [
        ReadMode.HEADER,
        ReadMode.CONTENT,
    ],
)
@pytest.mark.parametrize(
    "starting_genesets",
    [
        [],
        ["geneset1"],
        ["geneset1", "geneset2"],
    ],
)
@patch("geneweaver.core.parse.batch.read_header")
@patch("geneweaver.core.parse.batch.read_values")
@patch("geneweaver.core.parse.batch.create_geneset")
def test_process_lines_header_error(
    mock_create_geneset,
    mock_read_values,
    mock_read_header,
    contents,
    read_header_error,
    read_mode,
    starting_genesets,
):
    """Test that process_lines calls read_header and create_geneset."""
    mock_read_header.side_effect = [
        read_header_error(),
        ([] + starting_genesets, [], {}, read_mode),
    ]
    mock_create_geneset.return_value = "geneset"
    mock_read_values.return_value = (
        [("key1", "value1"), ("key2", "value2")],
        ReadMode.CONTENT,
    )

    result = process_lines(contents)

    assert mock_read_header.call_count == 2
    assert mock_create_geneset.call_count == 1
    if read_header_error is IgnoreLineError:
        assert mock_read_values.call_count == 0
    else:
        assert mock_read_values.call_count == 1
    assert result == starting_genesets + ["geneset"]
