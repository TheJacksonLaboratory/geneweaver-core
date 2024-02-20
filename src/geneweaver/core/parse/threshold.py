"""Code to check if geneset values fall within a score threshold.

This module contains code to check if geneset values fall within a score threshold.
This is required for inserting geneset values into the database.

To check if geneset values fall within a score threshold, use the `check_threshold`
function. You can pass multiple values in a list, allowing you to check an entire
geneset at once.

Or, you can pass a single value to check a single geneset, just
encapsulate the value in a list.

High-level functions:
- `check_threshold`: Check if geneset values fall within a score threshold.

Utility functions:
- `one_sided_threshold`: Check if a value falls within a one-sided threshold.
- `two_sided_threshold`: Check if a value falls within a two-sided threshold.
"""

from typing import List

from geneweaver.core.schema.batch import GenesetValueInput
from geneweaver.core.schema.score import GenesetScoreType, ScoreType


def check_threshold(
    geneset_values: List[GenesetValueInput], score: GenesetScoreType
) -> List[bool]:
    """Check to see if the geneset values fall within the score threshold.

    This function checks to see if the geneset values fall within the score threshold.

    :param geneset_values: The list of geneset values to check.
    :param score: The score type to check against.

    :returns: A list of booleans representing whether each geneset value falls within
    the score threshold.
    """
    score_type = score.score_type
    if score_type is ScoreType.BINARY:
        return [True] * len(geneset_values)

    elif score_type is ScoreType.P_VALUE or score_type is ScoreType.Q_VALUE:
        return [
            one_sided_threshold(gsv.value, score.threshold) for gsv in geneset_values
        ]

    elif score_type is ScoreType.EFFECT or score_type is ScoreType.CORRELATION:
        return [
            two_sided_threshold(gsv.value, score.threshold_low, score.threshold)
            for gsv in geneset_values
        ]


def one_sided_threshold(value: float, threshold: float) -> bool:
    """Check if a value falls within a one-sided threshold.

    This function checks if a value falls within a one-sided threshold. For example, if
    the threshold is 0.05, then this function will return True if the value is less than
    or equal to 0.05.

    :param value: The value to check.
    :param threshold: The threshold to check against.

    :returns: True if the value falls within the threshold, False otherwise.
    """
    return value <= threshold


def two_sided_threshold(value: float, threshold_low: float, threshold: float) -> bool:
    """Check if a value falls within a two-sided threshold.

    This function checks if a value falls within a two-sided threshold. For example, if
    the threshold_low is 0.1 and the threshold is 0.05, then this function will return
    True if the value is between 0.1 and 0.05.

    :param value: The value to check.
    :param threshold_low: The lower threshold to check against.
    :param threshold: The upper threshold to check against.

    :returns: True if the value falls within the threshold, False otherwise.
    """
    # If you're coming from C, you might think this wouldn't work...
    # But Python is cool like that.
    # https://docs.python.org/3/reference/expressions.html#comparisons
    # tl;dr This is equivalent to: threshold_low <= value and value <= threshold
    return threshold_low <= value <= threshold
