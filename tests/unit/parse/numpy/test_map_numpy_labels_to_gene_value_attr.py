"""Test the map_ndarray_labels_to_gene_value_attr function."""

from typing import Tuple

import numpy as np
import pytest
from geneweaver.core.parse.numpy import map_ndarray_labels_to_gene_value_attr

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

# Test cases
test_cases = [
    (valid_labeled_geneset_array, ("Symbol", "Value")),
    (valid_labeled_geneset_array_2, ("Symbol", "Score")),
    (valid_labeled_geneset_array_3, ("GeneID", "PValue")),
    (valid_labeled_geneset_array_4, ("Gene_ID", "QValue")),
    (valid_labeled_geneset_array_5, ("Gene ID", "Effect")),
    (valid_labeled_geneset_array_6, ("GeneID", "Correlation")),
    (valid_gt_2_labeled_geneset_array, ("Symbol", "Value")),
    (valid_gt_2_labeled_geneset_array_2, ("Symbol", "Score")),
    (empty_array, ("Symbol", "Value")),
    (
        missing_symbol_array,
        ValueError("Could not map numpy array labels to GenesetValueInput attributes"),
    ),
    (
        missing_value_array,
        ValueError("Could not map numpy array labels to GenesetValueInput attributes"),
    ),
    (
        missing_symbol_array_2,
        ValueError("Could not map numpy array labels to GenesetValueInput attributes"),
    ),
    (
        missing_symbol_array_3,
        ValueError("Could not map numpy array labels to GenesetValueInput attributes"),
    ),
    (
        missing_value_array_2,
        ValueError("Could not map numpy array labels to GenesetValueInput attributes"),
    ),
    (
        missing_value_array_3,
        ValueError("Could not map numpy array labels to GenesetValueInput attributes"),
    ),
]


@pytest.mark.parametrize(("geneset_array", "expected"), test_cases)
def test_map_ndarray_labels_to_gene_value_attr(
    geneset_array: np.ndarray, expected: Tuple[str, str]
):
    """Test that map_ndarray_labels_to_gene_value_attr function works as expected."""
    if isinstance(expected, ValueError):
        with pytest.raises(type(expected)) as err:
            map_ndarray_labels_to_gene_value_attr(geneset_array)
        assert str(err.value) == str(expected)
    else:
        result = map_ndarray_labels_to_gene_value_attr(geneset_array)
        assert result == expected
