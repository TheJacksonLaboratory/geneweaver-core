"""Test the ndarray_to_gene_values function."""
import pytest
import numpy as np
from typing import List
from geneweaver.core.schema.batch import GenesetValueInput

from geneweaver.core.parse.numpy import ndarray_to_gene_values

from tests.unit.parse.numpy.const import (
    valid_geneset_array,
    valid_labeled_geneset_array,
    valid_labeled_geneset_array_2,
    valid_labeled_geneset_array_3,
)

# Test cases for ndarray_to_gene_values function
test_cases_gene_values = [
    # Can be converted by labels
    (valid_labeled_geneset_array, [GenesetValueInput(symbol='GeneA', value=1.2), GenesetValueInput(symbol='GeneB', value=2.5)]),
    (valid_labeled_geneset_array_2, [GenesetValueInput(symbol='GeneC', value=3.6), GenesetValueInput(symbol='GeneD', value=4.7)]),
    (valid_labeled_geneset_array_3, [GenesetValueInput(symbol='GeneE', value=5.8), GenesetValueInput(symbol='GeneF', value=6.9)]),
    (np.array([('GeneA', 1.2, 'extra')], dtype=[('Symbol', 'U10'), ('Value', 'f8'), ('Extra', 'U10')]), [GenesetValueInput(symbol='GeneA', value=1.2)]),  # more than 2 columns
    # Can be converted by index
    (valid_geneset_array, [GenesetValueInput(symbol='GeneA', value=1.2), GenesetValueInput(symbol='GeneB', value=2.5)]),
    # (test_case_array_2, [GenesetValueInput('GeneY', 8.1)]),
    # (test_case_array_3, [GenesetValueInput('GeneZ', 9.2)]),
    # Cannot be converted
    (np.array([1, 2, 3]), ValueError("Input must be a 2-dimensional array, or a structured array")),  # not 2-dimensional
    (np.array([('GeneA',)], dtype=[('Symbol', 'U10')]), ValueError("Input must be a 2-dimensional array")),  # less than 2 columns
]


@pytest.mark.parametrize('geneset_array, expected', test_cases_gene_values)
def test_ndarray_to_gene_values(geneset_array: np.ndarray, expected: List[GenesetValueInput]):
    if isinstance(expected, ValueError):
        with pytest.raises(ValueError) as err:
            ndarray_to_gene_values(geneset_array)
        assert str(err.value) == str(expected)
    else:
        result = ndarray_to_gene_values(geneset_array)
        assert result == expected
