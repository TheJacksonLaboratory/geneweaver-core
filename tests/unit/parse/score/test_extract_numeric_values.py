"""Test the extract numeric values function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.score import extract_numeric_values

# Define two separate lists of parameters
input_strings = [
    # Single integer number in the string
    ("P-Value < 7", ["7"]),
    ("P-Value < 0.05", ["0.05"]),
    ("Q-Value < 0.05", ["0.05"]),
    # Multiple integer numbers in the string
    ("Q-Value < 7, 8, 9", ["7", "8", "9"]),
    ("0.40 < Correlation < 0.90", ["0.40", "0.90"]),
    ("6.0 < Effect < 22.50", ["6.0", "22.50"]),
    # Float numbers in the string
    ("P-Value < 7.5, 8.6, 9.7", ["7.5", "8.6", "9.7"]),
    # Float numbers with leading zeros
    ("Q-Value < 007.5, 08.6, 009.7", ["007.5", "08.6", "009.7"]),
    # Zero in the string
    ("Effect < 0, 0.0", ["0", "0.0"]),
    # Mixed float and integer numbers
    ("Correlation < 1, Q-Value < 2.2, 3, 4.4", ["1", "2.2", "3", "4.4"]),
    # Negative integer numbers in the string
    ("scores: -7, -8, -9", ["-7", "-8", "-9"]),
    # Negative float numbers in the string
    ("scores: -7.5, -8.6, -9.7", ["-7.5", "-8.6", "-9.7"]),
    # Numbers embedded in words without spaces
    ("The temperature is 25C", ["25"]),
    # Numbers embedded with other special characters
    ("Prices: $20, $30.5, $40.99", ["20", "30.5", "40.99"]),
    # No numbers present in the string
    ("no numbers here", []),
    # Empty string input
    ("", []),
    # Numeric words without actual numbers
    ("one two three", []),
    ("Binary", []),
]

transformations = [
    # No transformation
    (lambda x: x, lambda x: x),
    # Prepending and appending non-numeric characters
    (lambda x: f"**{x}**", lambda x: x),
    (lambda x: f"<{x}<", lambda x: x),
    (lambda x: f">{x}>", lambda x: x),
    # Adding spaces before and after the string
    (lambda x: f"    {x}    ", lambda x: x),
    # Upper-casing the string
    (lambda x: x.upper(), lambda x: x),
    # Lower-casing the string
    (lambda x: x.lower(), lambda x: x),
]


# Double parametrize the test function
@pytest.mark.parametrize(("score_input", "expected_output"), input_strings)
@pytest.mark.parametrize(("input_transform", "output_transform"), transformations)
def test_extract_numeric_values(
    score_input, expected_output, input_transform, output_transform
):
    """Tests the extract_numeric_values function."""
    transformed_input = input_transform(score_input)
    transformed_output = output_transform(expected_output)
    assert extract_numeric_values(transformed_input) == transformed_output
