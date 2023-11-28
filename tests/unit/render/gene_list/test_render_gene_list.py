"""Test the gene_list_str function."""
from typing import List

import pytest
from geneweaver.core.render.gene_list import gene_list_str
from geneweaver.core.schema.gene import GeneValue


def test_gene_list_str_success_single(mock_gene_value: GeneValue):
    """Test the gene_list_str function for a successful case."""
    expected_output = mock_gene_value.symbol + "\t" + str(mock_gene_value.value)
    assert gene_list_str([mock_gene_value]) == expected_output


@pytest.mark.parametrize("separator", ["\t", ",", " "])
def test_gene_list_str_single_with_different_separators(
    mock_gene_value: GeneValue, separator: str
):
    """Test the gene_list_str function with different separators."""
    expected_output = mock_gene_value.symbol + separator + str(mock_gene_value.value)
    assert gene_list_str([mock_gene_value], sep=separator) == expected_output


@pytest.mark.parametrize("separator", ["\t", ",", " "])
def test_gene_list_str_with_different_separators(
    mock_gene_value_list: List[GeneValue], separator: str
):
    """Test the gene_list_str function with different separators."""
    result = gene_list_str(mock_gene_value_list, sep=separator)

    assert result.count(separator) == len(mock_gene_value_list)
    assert result.count("\n") == len(mock_gene_value_list) - 1
