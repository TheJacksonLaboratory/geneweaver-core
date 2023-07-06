"""Tests for the process_lines function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.score import (
    GenesetScoreType,
    InvalidScoreThresholdError,
    ScoreType,
    parse_effect,
)


@pytest.mark.parametrize(
    ("input_string", "expected_output"),
    [
        (
            "effect=0.05",
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=None, threshold=0.05
            ),
        ),
        (
            "effect=0.1,0.2",
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=0.1, threshold=0.2
            ),
        ),
        (
            "effect=1,2",
            GenesetScoreType(score_type=ScoreType.EFFECT, threshold_low=1, threshold=2),
        ),
        (
            "effect = 0.5,1",
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=0.5, threshold=1
            ),
        ),
    ],
)
def test_parse_effect_valid(input_string, expected_output):
    """Tests the parse_effect function with valid inputs."""
    result = parse_effect(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold_low == expected_output.threshold_low
    assert result.threshold == expected_output.threshold


@pytest.mark.parametrize(
    "invalid_input",
    [
        "effect",  # no numeric value
        "effect=abc",  # not a numeric value
        "effect=1,0.5,0.3",  # more than two numeric values
        "effect = ",  # no numeric value
    ],
)
def test_parse_effect_invalid(invalid_input):
    """Tests the parse_effect function with invalid inputs."""
    with pytest.raises(InvalidScoreThresholdError):
        parse_effect(invalid_input)


@pytest.mark.parametrize(
    ("input_string", "mock_return", "expected_output"),
    [
        (
            "effect=0.05",
            [None, 0.05],
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=None, threshold=0.05
            ),
        ),
        (
            "effect=0.1,0.2",
            [0.1, 0.2],
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=0.1, threshold=0.2
            ),
        ),
        (
            "effect=1,2",
            [1, 2],
            GenesetScoreType(score_type=ScoreType.EFFECT, threshold_low=1, threshold=2),
        ),
        (
            "effect = 0.5,1",
            [0.5, 1],
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=0.5, threshold=1
            ),
        ),
    ],
)
@patch("geneweaver.core.parse.score.extract_one_or_two_numeric_values")
def test_parse_effect_valid_with_mock(
    mock_extract, input_string, mock_return, expected_output
):
    """Tests the parse_effect function with valid inputs using a mock."""
    mock_extract.return_value = mock_return
    result = parse_effect(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold_low == expected_output.threshold_low
    assert result.threshold == expected_output.threshold
    mock_extract.assert_called_once_with(input_string)


@pytest.mark.parametrize(
    ("invalid_input", "mock_exception"),
    [
        ("effect", InvalidScoreThresholdError()),  # no numeric value
        ("effect=abc", InvalidScoreThresholdError()),  # not a numeric value
        (
            "effect=1,0.5,0.3",
            InvalidScoreThresholdError(),
        ),  # more than two numeric values
        ("effect = ", InvalidScoreThresholdError()),  # no numeric value
    ],
)
@patch("geneweaver.core.parse.score.extract_one_or_two_numeric_values")
def test_parse_effect_invalid_with_mock(mock_extract, invalid_input, mock_exception):
    """Tests the parse_effect function with invalid inputs using a mock."""
    mock_extract.side_effect = mock_exception
    with pytest.raises(InvalidScoreThresholdError):
        parse_effect(invalid_input)
    mock_extract.assert_called_once_with(invalid_input)
