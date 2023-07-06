"""Tests for the parse_pvalue function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.score import (
    GenesetScoreType,
    InvalidScoreThresholdError,
    ScoreType,
    parse_pvalue,
)


@pytest.mark.parametrize(
    ("input_string", "expected_output"),
    [
        ("pvalue=0.05", GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.05)),
        ("p=0.1", GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.1)),
        ("p_val=1", GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=1)),
        ("pvalue = 0.5", GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.5)),
    ],
)
def test_parse_pvalue_valid(input_string, expected_output):
    """Tests the parse_pvalue function with valid inputs."""
    result = parse_pvalue(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold == expected_output.threshold


@pytest.mark.parametrize(
    "invalid_input",
    [
        "pvalue",  # no numeric value
        "p=abc",  # not a numeric value
        "p_val=1,0.5",  # more than one numeric value
        "pvalue = ",  # no numeric value
    ],
)
def test_parse_pvalue_invalid(invalid_input):
    """Tests the parse_pvalue function with invalid inputs."""
    with pytest.raises(InvalidScoreThresholdError):
        parse_pvalue(invalid_input)


@pytest.mark.parametrize(
    ("input_string", "mock_return", "expected_output"),
    [
        (
            "pvalue=0.05",
            0.05,
            GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.05),
        ),
        ("p=0.1", 0.1, GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.1)),
        ("p_val=1", 1, GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=1)),
        (
            "pvalue = 0.5",
            0.5,
            GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.5),
        ),
    ],
)
@patch("geneweaver.core.parse.score.extract_single_numeric_value")
def test_parse_pvalue_valid_with_mock(
    mock_extract, input_string, mock_return, expected_output
):
    """Tests the parse_pvalue function with valid inputs."""
    mock_extract.return_value = mock_return
    result = parse_pvalue(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold == expected_output.threshold
    mock_extract.assert_called_once_with(input_string)


@pytest.mark.parametrize(
    ("invalid_input", "mock_exception"),
    [
        ("pvalue", InvalidScoreThresholdError()),  # no numeric value
        ("p=abc", InvalidScoreThresholdError()),  # not a numeric value
        (
            "p_val=1,0.5",
            InvalidScoreThresholdError(),
        ),  # more than one numeric value
        ("pvalue = ", InvalidScoreThresholdError()),  # no numeric value
    ],
)
@patch("geneweaver.core.parse.score.extract_single_numeric_value")
def test_parse_pvalue_invalid_with_mock(mock_extract, invalid_input, mock_exception):
    """Tests the parse_pvalue function with invalid inputs."""
    mock_extract.side_effect = mock_exception
    with pytest.raises(InvalidScoreThresholdError):
        parse_pvalue(invalid_input)
    mock_extract.assert_called_once_with(invalid_input)
