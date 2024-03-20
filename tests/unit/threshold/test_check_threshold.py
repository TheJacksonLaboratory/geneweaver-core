"""Test the check_threshold function."""

import pytest
from geneweaver.core.schema.score import GenesetScoreType
from geneweaver.core.threshold import check_threshold


@pytest.mark.parametrize(
    ("geneset_score", "value", "expected"),
    [
        (GenesetScoreType(score_type=1, threshold=0.05), 0.01, True),
        (GenesetScoreType(score_type=1, threshold=0.05), 0.06, False),
        (GenesetScoreType(score_type=2, threshold=0.05), 0.01, True),
        (GenesetScoreType(score_type=2, threshold=0.05), 0.06, False),
        (GenesetScoreType(score_type=3, threshold=0.05), 0.01, False),
        (
            GenesetScoreType(score_type=4, threshold=0.05, threshold_low=0.01),
            0.03,
            True,
        ),
        (
            GenesetScoreType(score_type=4, threshold=0.05, threshold_low=0.01),
            0.06,
            False,
        ),
        (
            GenesetScoreType(score_type=5, threshold=0.05, threshold_low=0.01),
            0.03,
            True,
        ),
    ],
)
def test_check_threshold(geneset_score, value, expected):
    """Check each parametrized case with valid arguments."""
    assert check_threshold(geneset_score, value) == expected
