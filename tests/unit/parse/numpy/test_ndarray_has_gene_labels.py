"""Test the ndarray_has_gene_labels function."""

import numpy as np
import pytest
from geneweaver.core.parse.numpy import ndarray_has_gene_labels

from tests.unit.parse.numpy.const import (
    empty_array,
    missing_symbol_array,
    missing_symbol_array_2,
    missing_symbol_array_3,
    missing_value_array,
    missing_value_array_2,
    missing_value_array_3,
    valid_gt_2_labeled_geneset_array,
    valid_gt_2_labeled_geneset_array_2,
    valid_labeled_geneset_array,
    valid_labeled_geneset_array_2,
    valid_labeled_geneset_array_3,
    valid_labeled_geneset_array_4,
    valid_labeled_geneset_array_5,
    valid_labeled_geneset_array_6,
)

test_cases_labels = [
    (valid_labeled_geneset_array, True),
    (valid_labeled_geneset_array_2, True),
    (valid_labeled_geneset_array_3, True),
    (valid_labeled_geneset_array_4, True),
    (valid_labeled_geneset_array_5, True),
    (valid_labeled_geneset_array_6, True),
    (valid_gt_2_labeled_geneset_array, True),
    (valid_gt_2_labeled_geneset_array_2, True),
    (empty_array, True),
    (missing_symbol_array, False),
    (missing_symbol_array_2, False),
    (missing_symbol_array_3, False),
    (missing_value_array, False),
    (missing_value_array_2, False),
    (missing_value_array_3, False),
    # unstructured numpy array
    (np.array([1, 2, 3]), False),
    # structured numpy array with only one field
    (np.array([("GeneA",)], dtype=[("Symbol", "U10")]), False),
]


@pytest.mark.parametrize(("geneset_array", "expected"), test_cases_labels)
def test_ndarray_has_gene_labels(geneset_array: np.ndarray, expected: bool):
    """Test that the ndarray_has_gene_labels function works as expected."""
    result = ndarray_has_gene_labels(geneset_array)
    assert result == expected
