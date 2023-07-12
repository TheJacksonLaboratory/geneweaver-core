"""Test the parse_score function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import Mock, patch

import pytest
from geneweaver.core.parse.score import (
    GenesetScoreType,
    InvalidScoreThresholdError,
    ScoreType,
    parse_score,
)


@pytest.mark.parametrize(
    ("input_string", "expected_output"),
    [
        ("Binary", GenesetScoreType(score_type=ScoreType.BINARY, threshold=1)),
        (
            "P-Value < 0.05",
            GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.05),
        ),
        (
            "Q-Value < 0.05",
            GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.05),
        ),
        (
            "0.40 < Correlation < 0.90",
            GenesetScoreType(
                score_type=ScoreType.CORRELATION, threshold_low=0.4, threshold=0.9
            ),
        ),
        (
            "6.0 < Effect < 22.50",
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=6, threshold=22.5
            ),
        ),
    ],
)
def test_parse_score_valid(input_string, expected_output):
    """Tests the parse_score function with valid inputs."""
    result = parse_score(input_string)
    assert result.score_type == expected_output.score_type
    assert result.threshold_low == expected_output.threshold_low
    assert result.threshold == expected_output.threshold


@pytest.mark.parametrize(
    "invalid_input",
    [
        "UnknownScoreType",  # Unknown score type
        "P-Value = abc",  # Invalid p-value score
        "Q-Value = abc",  # Invalid q-value score
        "Correlation = abc",  # Invalid correlation score
        "Effect = abc",  # Invalid effect score
    ],
)
def test_parse_score_invalid(invalid_input):
    """Tests the parse_score function with invalid inputs."""
    with pytest.raises(InvalidScoreThresholdError):
        parse_score(invalid_input)


@pytest.mark.parametrize(
    ("input_string", "mock_parser", "mock_return"),
    [
        (
            "Binary",
            "binary",
            GenesetScoreType(score_type=ScoreType.BINARY, threshold=1),
        ),
        (
            "P-Value < 0.05",
            "p-value",
            GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.05),
        ),
        (
            "Q-Value < 0.05",
            "q-value",
            GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.05),
        ),
        (
            "0.40 < Correlation < 0.90",
            "correlation",
            GenesetScoreType(
                score_type=ScoreType.CORRELATION, threshold_low=0.4, threshold=0.9
            ),
        ),
        (
            "6.0 < Effect < 22.50",
            "effect",
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold_low=6, threshold=22.7
            ),
        ),
    ],
)
def test_parse_score_valid_with_mock(input_string, mock_parser, mock_return):
    """Tests the parse_score function with valid inputs using a mock."""
    with patch.dict("geneweaver.core.parse.score.SCORE_PARSER_MAP") as mock_map:
        mock_map.clear()
        mock_map[mock_parser] = Mock()
        mock_map[mock_parser].return_value = mock_return
        result = parse_score(input_string)
        assert result.score_type == mock_return.score_type
        assert result.threshold_low == mock_return.threshold_low
        assert result.threshold == mock_return.threshold
        assert mock_map[mock_parser].call_count == 1


@pytest.mark.parametrize(
    "invalid_input",
    [
        "UnknownScoreType",  # Unknown score type
        "P-Value = abc",  # Invalid p-value score
        "Q-Value = abc",  # Invalid q-value score
        "Correlation = abc",  # Invalid correlation score
        "Effect = abc",  # Invalid effect score
    ],
)
@patch("geneweaver.core.parse.score.parse_binary")
@patch("geneweaver.core.parse.score.parse_pvalue")
@patch("geneweaver.core.parse.score.parse_qvalue")
@patch("geneweaver.core.parse.score.parse_correlation")
@patch("geneweaver.core.parse.score.parse_effect")
def test_parse_score_invalid_with_mock(
    mock_effect, mock_correlation, mock_qvalue, mock_pvalue, mock_binary, invalid_input
):
    """Tests the parse_score function with invalid inputs using a mock."""
    with pytest.raises(InvalidScoreThresholdError):
        parse_score(invalid_input)
