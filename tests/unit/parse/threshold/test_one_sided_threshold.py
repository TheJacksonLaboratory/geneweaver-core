"""Test the one_sided_threshold function."""
# ruff: noqa: D103
import pytest
from geneweaver.core.parse.threshold import one_sided_threshold


@pytest.mark.parametrize(
    ("value", "threshold", "expected_output"),
    [
        (0.05, 0.05, True),  # Test case where value is equal to threshold
        (0.04, 0.05, True),  # Test case where value is less than threshold
        (0.06, 0.05, False),  # Test case where value is greater than threshold
        (-0.1, 0.0, True),  # Test case where value is less than zero threshold
        (0.0, 0.0, True),  # Test case where value is equal to zero threshold
        (0.1, 0.0, False),  # Test case where value is greater than zero threshold
        (0.0, -0.1, False),  # Test case where value is greater than negative threshold
        (-0.2, -0.1, True),  # Test case where value is less than negative threshold
        (-0.1, -0.1, True),  # Test case where value is equal to negative threshold
        # Test case where value is greater than larger negative threshold
        (-0.1, -0.2, False),
        (float("inf"), 1.0, False),  # Test case with positive infinity
        (-float("inf"), 1.0, True),  # Test case with negative infinity
        (1.0, float("inf"), True),  # Test case with threshold positive infinity
        (1.0, -float("inf"), False),  # Test case with threshold negative infinity
        # Test case with both value and threshold as NaN
        (float("inf"), float("inf"), True),
        # Test case with both value and threshold as negative infinity
        (-float("inf"), -float("inf"), True),
        # Test case with NaN
        (float("nan"), 1.0, False),
        # Test case where threshold is NaN
        (1.0, float("nan"), False),
        # Test case with both value and threshold as NaN
        (float("nan"), float("nan"), False),
    ],
)
def test_one_sided_threshold(value, threshold, expected_output):
    assert one_sided_threshold(value, threshold) == expected_output
