"""Tests for the extract_one_or_two_numeric_values function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.score import (
    InvalidScoreThresholdError,
    extract_one_or_two_numeric_values,
)

# Define the list of parameters for input strings and expected outputs
valid_input_strings = [
    # Single integer number in the string
    ("score: 7", [None, 7.0]),
    # Single integer number at the start of the string
    ("7 is the score", [None, 7.0]),
    # Single integer number at the end of the string
    ("The score is 7", [None, 7.0]),
    # Single float number in the string
    ("score: 7.5", [None, 7.5]),
    # Two integer numbers in the string
    ("score: 7 and 8", [7.0, 8.0]),
    # Two float numbers in the string
    ("score: 7.5 and 8.5", [7.5, 8.5]),
    # Two numbers with one being a float and another being an integer in the string
    ("score: 7 and 8.5", [7.0, 8.5]),
    # Two numbers separated by multiple words
    ("score: 7 and the second score is 8", [7.0, 8.0]),
    # Two integer numbers where one is negative
    ("score: -7 and 8", [-7.0, 8.0]),
    ("score: 3 and -9", [3.0, -9.0]),
    # Two float numbers where one is negative
    ("score: -7.5 and 8.5", [-7.5, 8.5]),
    ("score: 5.2 and -1.5", [5.2, -1.5]),
    # Two numbers with one being a float and another being an integer where one is
    # negative
    ("score: -7 and 8.5", [-7.0, 8.5]),
    ("score: 5 and -3.5", [5.0, -3.5]),
    # TODO: This test fails since the regex thinks the dash is negative sign
    # Two numbers separated by a dash
    ("score: 7-8", [7.0, 8.0]),
]

invalid_input_strings = [
    # No numbers present in the string
    "no numbers here",
    # More than two numbers present in the string
    "scores: 7, 8, and 9",
    # Three numbers separated by multiple words
    "scores: 7, second score is 8 and the third score is 9",
    # String with a single non-numeric value
    "scores: seven",
    # String with two non-numeric values
    "scores: seven and eight",
]

transformations = [
    # Prepending and appending non-numeric characters
    (lambda x: f"**{x}**", lambda x: x),
    # Adding spaces before and after the string
    (lambda x: f"    {x}    ", lambda x: x),
    # Upper-casing the string
    (lambda x: x.upper(), lambda x: x),
    # Lower-casing the string
    (lambda x: x.lower(), lambda x: x),
]


# Test function for valid inputs
@pytest.mark.parametrize(("score_input", "expected_output"), valid_input_strings)
@pytest.mark.parametrize(("input_transform", "output_transform"), transformations)
def test_extract_one_or_two_numeric_values_valid(
    score_input, expected_output, input_transform, output_transform
):
    """Tests the extract_one_or_two_numeric_values function for valid inputs."""
    transformed_input = input_transform(score_input)
    transformed_output = output_transform(expected_output)
    assert extract_one_or_two_numeric_values(transformed_input) == transformed_output


# Test function for invalid inputs
@pytest.mark.parametrize("score_input", invalid_input_strings)
@pytest.mark.parametrize(("input_transform", "output_transform"), transformations)
def test_extract_one_or_two_numeric_values_invalid(
    score_input, input_transform, output_transform
):
    """Tests the extract_one_or_two_numeric_values function for invalid inputs."""
    transformed_input = input_transform(score_input)
    with pytest.raises(InvalidScoreThresholdError):
        extract_one_or_two_numeric_values(transformed_input)
