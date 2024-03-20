"""Test the check_threshold_list function."""

import pytest
from geneweaver.core.schema.score import GenesetScoreType
from geneweaver.core.threshold import check_threshold_list


@pytest.mark.parametrize(
    ("geneset_scores", "values", "expected"),
    [
        (GenesetScoreType(score_type=1, threshold=0.05), [0.01, 0.06], [True, False]),
        (GenesetScoreType(score_type=2, threshold=0.05), [0.01, 0.06], [True, False]),
        (GenesetScoreType(score_type=3, threshold=0.05), [0.01, 0.06], [False, True]),
        (
            GenesetScoreType(score_type=4, threshold=0.05, threshold_low=0.01),
            [0.03, 0.06],
            [True, False],
        ),
        (
            GenesetScoreType(score_type=5, threshold=0.05, threshold_low=0.01),
            [0.03, 0.06],
            [True, False],
        ),
        (
            GenesetScoreType(score_type="p-value", threshold=0.05),
            [0.01, 0.06],
            [True, False],
        ),
        (
            GenesetScoreType(score_type="q-value", threshold=0.05),
            [0.01, 0.06],
            [True, False],
        ),
        (
            GenesetScoreType(score_type="binary", threshold=0.05),
            [0.01, 0.06],
            [False, True],
        ),
        (
            GenesetScoreType(
                score_type="correlation", threshold=0.05, threshold_low=0.01
            ),
            [0.03, 0.06],
            [True, False],
        ),
        (
            GenesetScoreType(score_type="effect", threshold=0.05, threshold_low=0.01),
            [0.03, 0.06],
            [True, False],
        ),
    ],
)
def test_check_threshold_list(geneset_scores, values, expected):
    """Check each parametrized case with valid arguments."""
    assert check_threshold_list(geneset_scores, values) == expected
