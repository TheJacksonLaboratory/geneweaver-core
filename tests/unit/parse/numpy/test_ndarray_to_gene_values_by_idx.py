"""Test the ndarray_to_gene_values_by_idx function."""
from typing import List

import numpy as np
import pytest
from geneweaver.core.parse.numpy import ndarray_to_gene_values_by_idx
from geneweaver.core.schema.batch import GenesetValueInput

from tests.unit.parse.numpy.const import (
    valid_geneset_array,
    valid_gt_2_labeled_geneset_array,
    valid_labeled_geneset_array,
)

# Additional test cases for ndarray_to_gene_values_by_idx function
test_case_array_1 = np.array(
    [("GeneX", 7.0)], dtype=[("Symbol", "U10"), ("Value", "f8")]
)
test_case_array_2 = np.array(
    [("GeneY", 8.1)], dtype=[("Symbol", "U10"), ("Value", "f8")]
)
test_case_array_3 = np.array(
    [("GeneZ", 9.2)], dtype=[("Symbol", "U10"), ("Value", "f8")]
)

# Test cases for ndarray_to_gene_values_by_idx function
test_cases_by_idx = [
    (
        valid_geneset_array,
        [
            GenesetValueInput(symbol="GeneA", value=1.2),
            GenesetValueInput(symbol="GeneB", value=2.5),
        ],
    ),
    (
        valid_labeled_geneset_array,
        [
            GenesetValueInput(symbol="GeneA", value=1.2),
            GenesetValueInput(symbol="GeneB", value=2.5),
        ],
    ),
    (
        valid_gt_2_labeled_geneset_array,
        [
            GenesetValueInput(symbol="GeneA", value=1.2),
            GenesetValueInput(symbol="GeneB", value=2.5),
        ],
    ),
    (test_case_array_1, [GenesetValueInput(symbol="GeneX", value=7.0)]),
    (test_case_array_2, [GenesetValueInput(symbol="GeneY", value=8.1)]),
    (test_case_array_3, [GenesetValueInput(symbol="GeneZ", value=9.2)]),
]


@pytest.mark.parametrize(("geneset_array", "expected"), test_cases_by_idx)
def test_ndarray_to_gene_values_by_idx(
    geneset_array: np.ndarray, expected: List[GenesetValueInput]
):
    """Test that the ndarray_to_gene_values_by_idx function works as expected."""
    result = ndarray_to_gene_values_by_idx(geneset_array)
    assert result == expected
