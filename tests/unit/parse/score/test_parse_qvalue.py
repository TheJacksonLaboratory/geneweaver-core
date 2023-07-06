"""Tests for the parse_qvalue function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.score import (
    GenesetScoreType,
    InvalidScoreThresholdError,
    ScoreType,
    parse_qvalue,
)


@pytest.mark.parametrize(
    ("input_string", "expected_output"),
    [
        ("qvalue=0.05", GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.05)),
        ("q=0.1", GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.1)),
        ("q_val=1", GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=1)),
        ("qvalue = 0.5", GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.5)),
    ],
)
def test_parse_qvalue_valid(input_string, expected_output):
    """Tests the parse_qvalue function with valid inputs."""
    result = parse_qvalue(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold == expected_output.threshold


@pytest.mark.parametrize(
    "invalid_input",
    [
        "qvalue",  # no numeric value
        "q=abc",  # not a numeric value
        "q_val=1,0.5",  # more than one numeric value
        "qvalue = ",  # no numeric value
    ],
)
def test_parse_qvalue_invalid(invalid_input):
    """Tests the parse_qvalue function with invalid inputs."""
    with pytest.raises(InvalidScoreThresholdError):
        parse_qvalue(invalid_input)


@pytest.mark.parametrize(
    ("input_string", "mock_return", "expected_output"),
    [
        (
            "qvalue=0.05",
            0.05,
            GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.05),
        ),
        ("q=0.1", 0.1, GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.1)),
        ("q_val=1", 1, GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=1)),
        (
            "qvalue = 0.5",
            0.5,
            GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.5),
        ),
    ],
)
@patch("geneweaver.core.parse.score.extract_single_numeric_value")
def test_parse_qvalue_valid_with_mock(
    mock_extract, input_string, mock_return, expected_output
):
    """Tests the parse_qvalue function with valid inputs using a mock."""
    mock_extract.return_value = mock_return
    result = parse_qvalue(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold == expected_output.threshold
    mock_extract.assert_called_once_with(input_string)


@pytest.mark.parametrize(
    ("invalid_input", "mock_exception"),
    [
        ("qvalue", InvalidScoreThresholdError()),  # no numeric value
        ("q=abc", InvalidScoreThresholdError()),  # not a numeric value
        (
            "q_val=1,0.5",
            InvalidScoreThresholdError(),
        ),  # more than one numeric value
        ("qvalue = ", InvalidScoreThresholdError()),  # no numeric value
    ],
)
@patch("geneweaver.core.parse.score.extract_single_numeric_value")
def test_parse_qvalue_invalid_with_mock(mock_extract, invalid_input, mock_exception):
    """Tests the parse_qvalue function with invalid inputs using a mock."""
    mock_extract.side_effect = mock_exception
    with pytest.raises(InvalidScoreThresholdError):
        parse_qvalue(invalid_input)
    mock_extract.assert_called_once_with(invalid_input)
