"""Test the check_input_shape_and_type function."""
import numpy as np
import pytest
from geneweaver.core.parse.numpy import check_input_shape_and_type

from tests.unit.parse.numpy.const import (
    valid_geneset_array,
    valid_gt_2_labeled_geneset_array,
    valid_labeled_geneset_array,
)

# Test cases for check_input_shape_and_type function
test_cases_input = [
    # valid 2-dimensional numpy array
    (valid_geneset_array, None),
    # valid 2-dimensional numpy array with labels
    (valid_labeled_geneset_array, None),
    # valid 2-dimensional numpy array with labels
    (valid_gt_2_labeled_geneset_array, None),
    # 1-dimensional numpy array
    (
        np.array([1, 2, 3]),
        ValueError("Input must be a 2-dimensional array, or a structured array"),
    ),
    # 3-dimensional numpy array
    (
        np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
        ValueError("Input must be a 2-dimensional array, or a structured array"),
    ),
    ([1, 2, 3], ValueError("Input must be a numpy array")),
    ("test", ValueError("Input must be a numpy array")),
    (123, ValueError("Input must be a numpy array")),
]


@pytest.mark.parametrize(("input_array", "expected"), test_cases_input)
def test_check_input_shape_and_type(input_array: np.ndarray, expected: None):
    """Test that the check_input_shape_and_type function raises errors correctly."""
    if expected is None:
        check_input_shape_and_type(input_array)
    else:
        with pytest.raises(type(expected)) as err:
            check_input_shape_and_type(input_array)
        assert str(err.value) == str(expected)
