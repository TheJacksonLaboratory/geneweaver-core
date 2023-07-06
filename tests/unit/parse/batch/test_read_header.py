"""Tests for the read_header function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.batch import (
    IgnoreLineError,
    MissingRequiredHeaderError,
    NotAHeaderRowError,
    ReadMode,
    read_header,
)


@pytest.mark.parametrize("expected_exception", [NotAHeaderRowError, IgnoreLineError])
@pytest.mark.parametrize("read_mode", [ReadMode.HEADER, ReadMode.CONTENT])
@patch("geneweaver.core.parse.batch.process_header_line")
@patch("geneweaver.core.parse.batch.finalize_processed_geneset")
@patch("geneweaver.core.parse.batch.update_header")
def test_read_header_read_error(
    mock_update_header,
    mock_finalize_processed_geneset,
    mock_process_header_line,
    read_mode,
    expected_exception,
):
    """Test that read_header calls update_header."""
    mock_process_header_line.return_value = ("key", "value")
    mock_finalize_processed_geneset.return_value = ([], [], {})
    mock_process_header_line.side_effect = expected_exception()

    with pytest.raises(expected_exception):
        read_header("header_line_1", {}, [], read_mode, [])

    assert mock_update_header.call_count == 0
    assert mock_finalize_processed_geneset.call_count == 0
    assert mock_process_header_line.call_count == 1


@patch("geneweaver.core.parse.batch.process_header_line")
@patch("geneweaver.core.parse.batch.finalize_processed_geneset")
@patch("geneweaver.core.parse.batch.update_header")
def test_read_header_finalize_error(
    mock_update_header, mock_finalize_processed_geneset, mock_process_header_line
):
    """Test that read_header calls finalize_processed_geneset."""
    mock_process_header_line.return_value = ("key", "value")
    mock_finalize_processed_geneset.return_value = ([], [], {})
    mock_finalize_processed_geneset.side_effect = MissingRequiredHeaderError()

    with pytest.raises(MissingRequiredHeaderError):
        read_header("header_line_1", {}, [], ReadMode.CONTENT, [])

    assert mock_update_header.call_count == 0
    assert mock_finalize_processed_geneset.call_count == 1
    assert mock_process_header_line.call_count == 1


@pytest.mark.parametrize(
    "current_geneset_values",
    [
        [],
        ["geneset1"],
        ["geneset1", "geneset2"],
    ],
)
@pytest.mark.parametrize("process_return", [("key", "value")])
@pytest.mark.parametrize(
    "finalize_return",
    [
        ([], [], {}),
        ([], [], {"key": "value"}),
        ([], [], {"key": "value", "key2": "value2"}),
        (["geneset1"], [], {}),
        (["geneset1"], [], {"key": "value"}),
    ],
)
@pytest.mark.parametrize(
    "update_return",
    [
        {},
        {"key": "value"},
        {"key": "value", "key2": "value2"},
    ],
)
@pytest.mark.parametrize("read_mode", [ReadMode.HEADER, ReadMode.CONTENT])
@patch("geneweaver.core.parse.batch.process_header_line")
@patch("geneweaver.core.parse.batch.finalize_processed_geneset")
@patch("geneweaver.core.parse.batch.update_header")
def test_read_header(
    mock_update_header,
    mock_finalize_processed_geneset,
    mock_process_header_line,
    process_return,
    finalize_return,
    update_return,
    read_mode,
    current_geneset_values,
):
    """Test the read_header function for combinations of inputs and returns."""
    mock_process_header_line.return_value = process_return
    mock_finalize_processed_geneset.return_value = finalize_return
    mock_update_header.return_value = update_return

    starting_read_mode = str(read_mode.value)
    starting_genest_values_len = len(current_geneset_values)
    print(starting_read_mode)

    genesets, current_geneset_values, header, read_mode = read_header(
        "header_line_1", {}, current_geneset_values, read_mode, []
    )

    if starting_read_mode == "header":
        assert mock_finalize_processed_geneset.call_count == 0
        assert len(current_geneset_values) == starting_genest_values_len
    else:
        assert current_geneset_values == finalize_return[1]
        assert mock_update_header.call_count == 1
        assert mock_finalize_processed_geneset.call_count == 1
        assert mock_process_header_line.call_count == 1
