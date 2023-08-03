"""Tests for geneweaver.core.parse.numpy.ndarray_to_gene_values_named function."""
import pytest
import numpy as np
from typing import List

from geneweaver.core.schema.batch import GenesetValueInput
from geneweaver.core.parse.numpy import ndarray_to_gene_values_named

from tests.unit.parse.numpy.const import (
    valid_labeled_geneset_array,
    valid_labeled_geneset_array_2,
    valid_labeled_geneset_array_3,
    missing_symbol_array,
    missing_value_array,
)

test_cases_gene_values = [
    (
        valid_labeled_geneset_array,
        [
            GenesetValueInput(symbol="GeneA", value=1.2),
            GenesetValueInput(symbol="GeneB", value=2.5),
        ],
    ),
    (
        valid_labeled_geneset_array_2,
        [
            GenesetValueInput(symbol="GeneC", value=3.6),
            GenesetValueInput(symbol="GeneD", value=4.7),
        ],
    ),
    (
        valid_labeled_geneset_array_3,
        [
            GenesetValueInput(symbol="GeneE", value=5.8),
            GenesetValueInput(symbol="GeneF", value=6.9),
        ],
    ),
    (missing_symbol_array, ValueError("Numpy array does not have gene labels")),
    (missing_value_array, ValueError("Numpy array does not have gene labels")),
    (np.array([1, 2, 3]), ValueError("Numpy array does not have gene labels")),
]


@pytest.mark.parametrize("geneset_array, expected", test_cases_gene_values)
def test_ndarray_to_gene_values_named(
    geneset_array: np.ndarray, expected: List[GenesetValueInput]
):
    if isinstance(expected, ValueError):
        with pytest.raises(ValueError) as err:
            ndarray_to_gene_values_named(geneset_array)
        assert str(err.value) == str(expected)
    else:
        result = ndarray_to_gene_values_named(geneset_array)
        assert result == expected
