"""Tests for the process_header_line function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import MagicMock, patch

import pytest
from geneweaver.core.parse.batch import (
    HEADER_CHARACTERS,
    SPACE_SEPARATED_HEADER_CHARACTERS,
    IgnoreLineError,
    NotAHeaderRowError,
    process_header_line,
)


@pytest.fixture()
def mock_read_single_prefix():
    """Patch the read_single_prefix_header function."""
    with patch("geneweaver.core.parse.batch.read_single_prefix_header") as mock:
        yield mock


@pytest.fixture()
def mock_read_space_separated():
    """Patch the read_space_separated_header function."""
    with patch("geneweaver.core.parse.batch.read_space_separated_header") as mock:
        yield mock


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        (f"{key}sample line", ("single_prefix_key", "single_prefix_value"))
        for key in HEADER_CHARACTERS.keys()
    ]
    + [
        (f"{key} sample line", ("space_separated_key", "space_separated_value"))
        for key in HEADER_CHARACTERS.keys()
    ],
)
def test_process_header_line_single_prefix(
    line,
    expected,
    mock_read_single_prefix: MagicMock,
    mock_read_space_separated: MagicMock,
):
    """Test that process_header_line calls read_single_prefix_header."""
    mock_read_single_prefix.return_value = expected

    assert process_header_line(line) == expected
    mock_read_single_prefix.assert_called_once()
    mock_read_space_separated.assert_not_called()


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        (f"{key} sample line", ("space_separated_key", "space_separated_value"))
        for key in SPACE_SEPARATED_HEADER_CHARACTERS.keys()
    ],
)
def test_process_header_line_space_separated(
    line,
    expected,
    mock_read_single_prefix: MagicMock,
    mock_read_space_separated: MagicMock,
):
    """Test that process_header_line calls read_space_separated_header."""
    mock_read_single_prefix.side_effect = NotAHeaderRowError
    mock_read_space_separated.return_value = expected

    assert process_header_line(line) == expected
    mock_read_single_prefix.assert_called_once()
    mock_read_space_separated.assert_called_once()


@pytest.mark.parametrize(
    "line",
    [
        "#ignore this line",  # prefix in IGNORE_CHARACTERS
        "",  # empty line
        " ",  # line with only space
        "  ",  # line with only spaces
        "\t",  # line with only tab
        "\t\t",  # line with only tabs
        " \t",  # line with space and tab
        " \t ",  # line with space, tab, and space
    ],
)
def test_process_header_line_ignored(
    line, mock_read_single_prefix: MagicMock, mock_read_space_separated: MagicMock
):
    """Test that process_header_line raises IgnoreLineError."""
    with pytest.raises(IgnoreLineError):
        process_header_line(line)

    mock_read_single_prefix.assert_not_called()
    mock_read_space_separated.assert_not_called()
