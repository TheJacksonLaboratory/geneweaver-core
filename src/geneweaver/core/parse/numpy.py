"""Functions for parsing numpy objects.

The top level functions are (in-order):
- ndarray_to_gene_values
- ndarray_to_gene_values_by_idx
- ndarray_to_gene_values_named

If you know that your numpy array has the gene symbol in the first column and the
gene value in the second column, you can use ndarray_to_gene_values_by_idx.
"""

from typing import List, Tuple

import numpy as np
from geneweaver.core.schema.batch import GenesetValueInput


def ndarray_to_gene_values(geneset_array: np.ndarray) -> List[GenesetValueInput]:
    """Convert a numpy array to a list of GeneValueInput objects.

    This function will try to map via labels first, then by index.

    :param geneset_array: The numpy array to convert.
    :raises ValueError: If there's a problem mapping the numpy array.
    :return: A set of the values in the numpy array.
    """
    check_input_shape_and_type(geneset_array)
    try:
        return ndarray_to_gene_values_named(geneset_array)
    except ValueError:
        return ndarray_to_gene_values_by_idx(geneset_array)


def ndarray_to_gene_values_by_idx(geneset_array: np.ndarray) -> List[GenesetValueInput]:
    """Convert a numpy array to a list of GeneValueInput objects.

    The numpy array must be a 2-dimensional array with 2 columns. The first column
    will be mapped to the GenesetValueInput.symbol attribute, and the second column will
    be mapped to the GenesetValueInput.value attribute.

    :param geneset_array: The numpy array to convert.
    :return: A set of the values in the numpy array.
    """
    try:
        return [GenesetValueInput(symbol=row[0], value=row[1]) for row in geneset_array]
    except IndexError as e:
        raise ValueError("Input must be a 2-dimensional array") from e


def ndarray_to_gene_values_named(geneset_array: np.ndarray) -> List[GenesetValueInput]:
    """Convert a numpy array to a list of GeneValueInput objects using labels.

    :param geneset_array: The numpy array to convert.
    :raises ValueError: If there's a problem mapping the numpy array using labels.
    :return: A set of the values in the numpy array.
    """
    if not ndarray_has_gene_labels(geneset_array):
        raise ValueError("Numpy array does not have gene labels")

    symbol_key, value_key = map_ndarray_labels_to_gene_value_attr(geneset_array)

    return [
        GenesetValueInput(symbol=row[symbol_key], value=row[value_key])
        for row in geneset_array
    ]


def check_input_shape_and_type(input_array: np.ndarray) -> None:
    """Check the shape and type of the input array.

    :raises ValueError: If the input array is not a numpy array or if it is not

    :param input_array: The array to check.
    """
    if not isinstance(input_array, np.ndarray):
        raise ValueError("Input must be a numpy array")

    if len(input_array.shape) != 2 and not input_array.dtype.names:
        raise ValueError("Input must be a 2-dimensional array, or a structured array")


def ndarray_has_gene_labels(geneset_array: np.ndarray) -> bool:
    """Check if the numpy array has gene labels.

    This function is used to check if a numpy array is structured (has names),
    and if it does, that it has at least 2 names.

    :param geneset_array: The numpy array to check.
    :return: True if the numpy array has gene labels, False otherwise.
    """
    if geneset_array.dtype.names is None:
        return False

    if len(geneset_array.dtype.names) < 2:
        return False

    return True


SYMBOL_KEYS = ("Symbol", "GeneID", "Gene_ID", "Gene ID")
VALUE_KEYS = ("Value", "Score", "PValue", "QValue", "Effect", "Correlation")


def map_ndarray_labels_to_gene_value_attr(geneset_array: np.ndarray) -> Tuple[str, str]:
    """Map numpy array labels to GenesetValueInput attributes.

    This function is used to check if a numpy array is structured (has names),
    and if it does, it checks if the names can be mapped to a GenesetValueInput object.

    In order, it will map ("Symbol", "GeneID", "Gene_ID", "Gene ID") to the
    GenesetValueInput symbol attribute.

    In order, it will map
    ("Value", "Score", "PValue", "QValue", "Effect", "Correlation") to the
    GenesetValueInput value attribute.

    If it cannot map to both symbol and value, it will raise an error.

    :param geneset_array: The numpy array to map.

    :raises ValueError: If the numpy array labels cannot be mapped to GenesetValueInput
    attributes.
    :return: A tuple, where the first value is the key mapping to the symbol attribute
    and the second value is the key mapping to the value attribute.
    """
    symbol_key, value_key = None, None
    for key in SYMBOL_KEYS:
        if key in geneset_array.dtype.names:
            symbol_key = key
            break

    for key in VALUE_KEYS:
        if key in geneset_array.dtype.names:
            value_key = key
            break

    if symbol_key is None or value_key is None:
        raise ValueError(
            "Could not map numpy array labels to GenesetValueInput attributes"
        )

    return symbol_key, value_key
