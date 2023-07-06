"""Tests for the parse_qvalue function."""
# ruff: noqa: ANN001, ANN201, ANN101
from unittest.mock import patch

import pytest
from geneweaver.core.parse.batch import ReadMode, read_values


# Mocking GenesetValueInput
class MockGenesetValueInput:
    """Mocking GenesetValueInput class."""

    def __init__(self, symbol, value) -> None:
        """Mock GenesetValueInput initialization."""
        self.symbol = symbol
        self.value = value


@pytest.mark.skip(reason="Failing test due to comparison of mock objects")
@patch(
    "geneweaver.core.parse.batch.GenesetValueInput",
    new_callable=lambda: MockGenesetValueInput,
)
@patch("geneweaver.core.parse.batch.process_value_line")
@patch("geneweaver.core.parse.batch.check_has_required_header_values")
@pytest.mark.parametrize(
    (
        "line",
        "header",
        "current_geneset_values",
        "expected_values",
        "process_line_result",
    ),
    [
        # Test case when read_mode is HEADER
        (
            "symbol value",
            {"abbreviation": "abbr", "name": "name", "description": "desc"},
            [],
            [MockGenesetValueInput("symbol", "value")],
            ("symbol", "value"),
        ),
        # Test case when read_mode is CONTENT
        (
            "symbol value",
            {},
            [MockGenesetValueInput("symbol1", "value1")],
            [
                MockGenesetValueInput("symbol1", "value1"),
                MockGenesetValueInput("symbol", "value"),
            ],
            ("symbol", "value"),
        ),
    ],
)
def test_read_values_success(
    mock_check_header,
    mock_process_line,
    mock_geneset_input,
    line,
    header,
    current_geneset_values,
    expected_values,
    process_line_result,
):
    """Test case for read_mode is HEADER and check_has_required_header_values passes."""
    mock_process_line.return_value = process_line_result

    values, mode = read_values(line, header, current_geneset_values, ReadMode.HEADER)

    assert mode == ReadMode.CONTENT, f"Expected {ReadMode.CONTENT}, but got {mode}"
    assert values == expected_values, f"Expected {expected_values}, but got {values}"


@patch(
    "geneweaver.core.parse.batch.GenesetValueInput",
    new_callable=lambda: MockGenesetValueInput,
)
@patch("geneweaver.core.parse.batch.process_value_line")
@patch("geneweaver.core.parse.batch.check_has_required_header_values")
@pytest.mark.parametrize(
    ("line", "header", "current_geneset_values", "process_line_result"),
    [
        # Test case when read_mode is HEADER and MissingRequiredHeaderError is raised
        ("symbol value", {}, [], ("symbol", "value")),
    ],
)
def test_read_values_missing_header_error(
    mock_check_header,
    mock_process_line,
    mock_geneset_input,
    line,
    header,
    current_geneset_values,
    process_line_result,
):
    """Test case when check_has_required_header_values raises an error."""
    mock_process_line.return_value = process_line_result
    mock_check_header.side_effect = Exception("MissingRequiredHeaderError")

    with pytest.raises(Exception, match="MissingRequiredHeaderError"):
        values, mode = read_values(
            line, header, current_geneset_values, ReadMode.HEADER
        )
