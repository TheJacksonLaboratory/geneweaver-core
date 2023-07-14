"""Test the two_sided_threshold function."""
# ruff: noqa: D103
import pytest
from geneweaver.core.parse.threshold import two_sided_threshold


@pytest.mark.parametrize(
    ("value", "threshold_low", "threshold", "expected_output"),
    [
        (0.1, 0.05, 0.15, True),  # Test case where value is equal to lower threshold
        (0.15, 0.05, 0.15, True),  # Test case where value is equal to upper threshold
        (0.1, 0.15, 0.05, False),  # Test case where value is out of bounds (too low)
        (0.2, 0.05, 0.15, False),  # Test case where value is out of bounds (too high)
        (0.12, 0.05, 0.15, True),  # Test case where value is within bounds
        (0.12, 0.15, 0.05, False),  # Test case where value is within reversed bounds
        (-0.1, -0.15, -0.05, True),  # Test case with negative values
        # Test case with one negative value
        (-0.1, -0.5, 0.15, True),
        (-0.1, -0.05, 0.15, False),
        (-0.1, 0.15, -0.05, False),
        # Test case with one negative value and reversed bounds
        (-0.1, 0.15, -0.05, False),
        (0.1, -0.05, 0.15, True),
        # Test case with one bound greater than 1.0
        (0.1, 0.05, 1.15, True),
        (0.1, 1.15, 0.05, False),
        # Test case with one bound less than -1.0
        (-0.1, -1.15, -0.05, True),
        (-0.1, -0.05, -1.15, False),
        # Test case with positive infinity
        (float("inf"), 0.0, 1.0, False),
        # Test case with negative infinity
        (-float("inf"), -1.0, 0.0, False),
        # Test case with threshold negative and positive infinity
        (0.5, -float("inf"), float("inf"), True),
        # Test case with both value and threshold as positive infinity
        (float("inf"), -float("inf"), float("inf"), True),
        # Test case with both value and threshold as negative infinity
        (-float("inf"), -float("inf"), float("inf"), True),
        (float("nan"), 0.0, 1.0, False),  # Test case with NaN
        (0.5, float("nan"), 1.0, False),  # Test case where lower threshold is NaN
        (0.5, 0.0, float("nan"), False),  # Test case where upper threshold is NaN
        # Test case with both value and threshold as NaN
        (float("nan"), float("nan"), float("nan"), False),
    ],
)
def test_two_sided_threshold(value, threshold_low, threshold, expected_output):
    assert two_sided_threshold(value, threshold_low, threshold) == expected_output
