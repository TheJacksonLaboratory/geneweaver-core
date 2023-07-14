"""Test the check_threshold function for various score types."""
from unittest.mock import patch

import pytest
from geneweaver.core.parse.threshold import check_threshold
from geneweaver.core.schema.batch import GenesetValueInput
from geneweaver.core.schema.score import GenesetScoreType, ScoreType


# Extend the previous mocking
@patch("geneweaver.core.parse.threshold.one_sided_threshold", side_effect=[True, False])
@patch("geneweaver.core.parse.threshold.two_sided_threshold", side_effect=[True, False])
@pytest.mark.parametrize(
    ("geneset_values", "score", "expected_output"),
    [
        # Test case for P-Value score type with one True and one False outcome
        (
            [
                GenesetValueInput(symbol="gene1", value=0.1),
                GenesetValueInput(symbol="gene2", value=0.2),
            ],
            GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=0.05),
            [True, False],
        ),
        # Test case for Q-Value score type with one True and one False outcome
        (
            [
                GenesetValueInput(symbol="gene1", value=0.1),
                GenesetValueInput(symbol="gene2", value=0.2),
            ],
            GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=0.05),
            [True, False],
        ),
        # Test case for Correlation score type with one True and one False outcome
        (
            [
                GenesetValueInput(symbol="gene1", value=0.1),
                GenesetValueInput(symbol="gene2", value=0.2),
            ],
            GenesetScoreType(
                score_type=ScoreType.CORRELATION, threshold=0.05, threshold_low=-0.05
            ),
            [True, False],
        ),
        # Test case for Effect score type with one True and one False outcome
        (
            [
                GenesetValueInput(symbol="gene1", value=0.1),
                GenesetValueInput(symbol="gene2", value=0.2),
            ],
            GenesetScoreType(
                score_type=ScoreType.EFFECT, threshold=0.05, threshold_low=-0.05
            ),
            [True, False],
        ),
    ],
)
def test_check_threshold(
    two_sided_mock, one_sided_mock, geneset_values, score, expected_output
):
    """Test the cases for non-binary score types."""
    assert check_threshold(geneset_values, score) == expected_output

    # For non-binary score types, check if the helper functions were called
    if score.score_type is not ScoreType.BINARY:
        if score.score_type in [ScoreType.P_VALUE, ScoreType.Q_VALUE]:
            one_sided_mock.assert_called()
        else:
            two_sided_mock.assert_called()


@patch("geneweaver.core.parse.threshold.one_sided_threshold")
@patch("geneweaver.core.parse.threshold.two_sided_threshold")
@pytest.mark.parametrize(
    ("geneset_values", "score", "expected_output"),
    [
        # Test case for binary score type
        (
            [
                GenesetValueInput(symbol="gene1", value=0.1),
                GenesetValueInput(symbol="gene2", value=0.2),
            ],
            GenesetScoreType(score_type=ScoreType.BINARY, threshold=0.05),
            [True, True],
        ),
        # Test case for binary score type with multiple values
        (
            [
                GenesetValueInput(symbol="gene1", value=0.1),
                GenesetValueInput(symbol="gene2", value=0.2),
                GenesetValueInput(symbol="gene3", value=0.3),
                GenesetValueInput(symbol="gene4", value=0.4),
            ],
            GenesetScoreType(score_type=ScoreType.BINARY, threshold=0.05),
            [True, True, True, True],
        ),
    ],
)
def test_check_threshold_binary(
    two_sided_mock, one_sided_mock, geneset_values, score, expected_output
):
    """Test the case for binary score type."""
    assert check_threshold(geneset_values, score) == expected_output
    assert not one_sided_mock.called
    assert not two_sided_mock.called
