"""Tests for the extract_single_numeric_value function in the score module."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.score import (
    InvalidScoreThresholdError,
    extract_single_numeric_value,
)

# valid inputs: a list of tuples (input_string, expected_output)
valid_inputs = [
    ("score: 7", 7.0),  # Single integer
    ("7", 7.0),  # Single integer, no other characters
    ("score: 7.5", 7.5),  # Single float
    ("7.5", 7.5),  # Single float, no other characters
    (" 7 ", 7.0),  # Single integer with leading/trailing spaces
    (" 7.5 ", 7.5),  # Single float with leading/trailing spaces
    ("score: 0", 0.0),  # Single integer at 0
    ("-1", -1.0),  # Negative single integer
    ("score: -1.5", -1.5),  # Negative single float
    ("-1.5", -1.5),  # Negative single float, no other characters
    (" 0 ", 0.0),  # Single integer at 0 with leading/trailing spaces
    (" -1.5 ", -1.5),  # Negative single float with leading/trailing spaces
    ("score:-1", -1.0),  # Negative single integer without space after colon
    ("score:-1.5", -1.5),  # Negative single float without space after colon
]

# invalid inputs: a list of input strings
invalid_inputs = [
    "",  # Empty string
    "score",  # String with no numbers
    "7.5 7.6",  # Two floats
    "7 8",  # Two integers
    "score: 7 8",  # Two integers with extra characters
    "score: 7.5 7.6",  # Two floats with extra characters
    "7 8.5",  # Mixed integers and floats
    "-",  # Just the negative sign
    "- score",  # Negative sign with string
    "7-8",  # Integer range without spaces
    "7.5-8.5",  # Float range without spaces
    "-7 -8",  # Two negative integers
    "-7.5 -8.5",  # Two negative floats
    "-7 -8.5",  # Mixed negative integers and floats
    "7 -8",  # Mixed positive and negative integers
    "7.5 -8.5",  # Mixed positive float and negative float
    "  ",  # Just spaces
    "score: ",  # Just a colon with spaces and no numbers
]


@pytest.mark.parametrize(("input_string", "expected_output"), valid_inputs)
def test_extract_single_numeric_value_valid(input_string, expected_output):
    """Tests the extract_single_numeric_value function with valid inputs."""
    assert extract_single_numeric_value(input_string) == expected_output


@pytest.mark.parametrize("input_string", invalid_inputs)
def test_extract_single_numeric_value_invalid(input_string):
    """Tests the extract_single_numeric_value function with invalid inputs."""
    with pytest.raises(InvalidScoreThresholdError):
        extract_single_numeric_value(input_string)
