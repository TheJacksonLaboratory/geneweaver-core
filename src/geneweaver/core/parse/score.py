"""Parse various score types from string inputs.

This module provides a set of functions for parsing various types of
numerical scores from string inputs and converting them into GenesetScoreType
objects. It also provides functionality for extracting numerical values from
strings and ensuring the correct count of these values.

Parsing Functions:
- parse_score: Parse a score input string into a GenesetScoreType object.
- parse_binary: Convert a binary score input string into a GenesetScoreType object.
- parse_pvalue: Convert a p-value score input string into a GenesetScoreType object.
- parse_qvalue: Convert a q-value score input string into a GenesetScoreType object.
- parse_correlation: Convert a correlation score input string into a GenesetScoreType
object.
- parse_effect: Convert an effect score input string into a GenesetScoreType object.

Number Extraction Functions:
- extract_numerical_values: Extract all numerical values from a given string.
- extract_single_numerical_value: Extract a single numerical value from a given string.
- extract_one_or_two_numerical_values: Extract either one or two numerical values from a
given string.

Exceptions:
- InvalidScoreThresholdException: Raised when the number of numerical values extracted
  from a string does not meet the expected count.
"""

import re
from typing import List

from geneweaver.core.parse.exceptions import InvalidScoreThresholdError
from geneweaver.core.schema.score import GenesetScoreType, ScoreType


def parse_binary(score_input: str) -> GenesetScoreType:
    """Convert a binary score input string into a GenesetScoreType object.

    This function expects a binary score as input, and will convert it into a
    GenesetScoreType object with a score type of 'BINARY' and a threshold of 1.

    :param score_input: The binary score input as a string (e.g. 'binary'). This input
    will be ignored.

    :returns: An object representing the binary score type and its threshold.
    """
    return GenesetScoreType(score_type=ScoreType.BINARY, threshold=1)


def parse_pvalue(score_input: str) -> GenesetScoreType:
    """Convert a p-value score input string into a GenesetScoreType object.

    This function takes a p-value score input string, parses the p-value using the
    `extract_single_numeric_value` function, and returns a GenesetScoreType object with
    the score type set to 'P_VALUE' and the threshold set to the parsed p-value.

    :param score_input: The p-value score input as a string.

    :returns: An object representing the p-value score type and its threshold.
    """
    threshold = extract_single_numeric_value(score_input)
    return GenesetScoreType(score_type=ScoreType.P_VALUE, threshold=threshold)


def parse_qvalue(score_input: str) -> GenesetScoreType:
    """Convert a q-value score input string into a GenesetScoreType object.

    This function takes a q-value score input string, parses the q-value using the
    `extract_single_numeric_value` function, and returns a GenesetScoreType object with
    the score type set to 'Q_VALUE' and the threshold set to the parsed q-value.

    :param score_input: The q-value score input as a string.

    :returns: An object representing the q-value score type and its threshold.
    """
    threshold = extract_single_numeric_value(score_input)
    return GenesetScoreType(score_type=ScoreType.Q_VALUE, threshold=threshold)


def parse_correlation(score_input: str) -> GenesetScoreType:
    """Convert a correlation score input string into a GenesetScoreType object.

    This function takes a correlation score input string, parses the thresholds using
    the `extract_one_or_two_numeric_values` function, and returns a GenesetScoreType
    object with the score type set to 'CORRELATION', the low threshold set to the first
    parsed value, and the high threshold set to the second parsed value.

    :param score_input: The correlation score input as a string.

    :returns: An object representing the correlation score type and its thresholds.
    """
    thresholds = extract_one_or_two_numeric_values(score_input)
    return GenesetScoreType(
        score_type=ScoreType.CORRELATION,
        threshold_low=thresholds[0],
        threshold=thresholds[1],
    )


def parse_effect(score_input: str) -> GenesetScoreType:
    """Convert an effect score input string into a GenesetScoreType object.

    This function takes an effect score input string, parses the thresholds using the
    `extract_one_or_two_numeric_values` function, and returns a GenesetScoreType object
    with the score type set to 'EFFECT', the low threshold set to the first parsed
    value, and the high threshold set to the second parsed value.

    :param score_input: The effect score input as a string.

    :returns: An object representing the effect score type and its thresholds.
    """
    thresholds = extract_one_or_two_numeric_values(score_input)
    return GenesetScoreType(
        score_type=ScoreType.EFFECT,
        threshold_low=thresholds[0],
        threshold=thresholds[1],
    )


# This dictionary maps score types to their respective parsing functions. It is used by
# the `parse_score` function to determine which parsing function to use for a given
# score type.
SCORE_PARSER_MAP = {
    "binary": parse_binary,
    "p-value": parse_pvalue,
    "q-value": parse_qvalue,
    "correlation": parse_correlation,
    "effect": parse_effect,
}


def parse_score(score_input: str) -> GenesetScoreType:
    """Parse a score input string into a GenesetScoreType object.

    This function takes a score input string, converts it to lowercase, and
    checks it against a mapping of score types to their respective parsers.
    If a match is found, it uses the corresponding parser to convert the input
    string into a GenesetScoreType object.

    Example valid `score_input` score type strings:
    'Binary'
    'P-Value < 0.05'
    'Q-Value < 0.05'
    '0.40 < Correlation < 0.90'
    '6.0 < Effect < 22.50'

    If no matching score type is found in the mapping, the function raises an
    InvalidScoreThresholdException.

    :param score_input: The score input as a string.

    :returns: An object representing the parsed score type and its thresholds.

    :raises InvalidScoreThresholdException: If no matching score type can be found in
    the mapping.
    """
    score_type = score_input.lower()
    for score_key, score_parser in SCORE_PARSER_MAP.items():
        if score_key in score_type:
            print(score_key, score_type)
            return score_parser(score_input)

    raise InvalidScoreThresholdError()


def extract_numeric_values(score_input: str) -> List[str]:
    """Extract all numerical values from a given string.

    This function uses regular expressions to find and return all numeric
    values in the input string. The numeric values can be integers or floats, positive
    or negative. The values can be separated by whitespace or other characters.

    :param score_input: The input string to search for numeric values.

    :returns: A list of all numeric values found in the input string.
    """
    # This regex uses negative lookbehind to ensure that a minus sign is not preceded
    # by a digit, which would indicate that it is a subtraction operator or a dash
    # separator. The simpler version of this regex, without the negative lookbehind,
    # would look like `(-?[0-9.]+)`, but would incorrectly match the dash in the
    # in a range as a negative sign (e.g. '4-5' would match as ['4', '-5'] instead of
    # ['4', '5']).
    return re.findall(r"((?<![0-9])-?[0-9.]+)", score_input)


def extract_single_numeric_value(score_input: str) -> float:
    """Extract a single numerical value from a given string.

    This function uses the `extract_numerical_values` function to find all numeric
    values in the input string, and ensures that exactly one value is present. If not,
    it raises an `InvalidScoreThresholdException`.

    :param score_input: The input string to search for a single numeric value.

    :returns: The single numeric value found in the input string.

    :raises InvalidScoreThresholdException: If there is not exactly one numeric value in
    the input string.
    """
    values = extract_numeric_values(score_input)
    if len(values) != 1:
        raise InvalidScoreThresholdError()

    return float(values[0])


def extract_one_or_two_numeric_values(score_input: str) -> list:
    """Extract either one or two numerical values from a given string.

    This function uses the `extract_numerical_values` function to find all numeric
    values in the input string, and ensures that either one or two values are present.
    If not, it raises an `InvalidScoreThresholdException`. If only one value is found,
    the function returns a list with `None` as the first element and the found value as
    the second element.

    :param score_input: The input string to search for one or two numeric values.

    :returns: A list of one or two numeric values found in the input string.

    :raises InvalidScoreThresholdException: If there are not either one or two numeric
    values in the input string.
    """
    values = extract_numeric_values(score_input)
    if len(values) not in (1, 2):
        raise InvalidScoreThresholdError()

    if len(values) == 1:
        values = [None, float(values[0])]
    else:
        values = [float(v) for v in values]

    return values
