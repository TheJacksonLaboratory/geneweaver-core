"""A module for functions dealing with thresholding."""

from typing import List

from geneweaver.core.schema.score import GenesetScoreType


def check_threshold(geneset_score: GenesetScoreType, value: float) -> bool:
    """Check to see if a value falls within the score threshold.

    :param geneset_score: The geneset score type and threshold arguments.
    :param value: The value to check against.
    :return: A boolean that indicates if the value falls within the range specified by
            the threshold.
    """
    score_type = int(geneset_score.score_type)
    value = float(value)

    # P and Q values
    if score_type == 1 or score_type == 2:
        return value <= geneset_score.threshold

    # Correlation and effect scores
    elif score_type == 4 or score_type == 5:
        return geneset_score.threshold_low <= value <= geneset_score.threshold

    # Binary
    else:
        return value >= geneset_score.threshold


def check_threshold_list(
    geneset_score: GenesetScoreType, values: List[float]
) -> List[bool]:
    """Check to see if a list of values falls within the score threshold.

    :param geneset_score: The geneset score type and threshold arguments.
    :param values: The list of values to check against.
    :return: A list of booleans that indicates if the value falls within the range
            specified by the threshold.
    """
    return [check_threshold(geneset_score, value) for value in values]
