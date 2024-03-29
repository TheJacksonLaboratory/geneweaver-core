"""Test the format_csv_metadata function."""

import pytest
from geneweaver.core.render.csv import format_csv_metadata


def test_format_csv_metadata_default_params(mock_batch_upload_geneset_all_combinations):
    """Test the format_csv_metadata function with default parameters."""
    formatted_metadata = format_csv_metadata(mock_batch_upload_geneset_all_combinations)
    assert isinstance(formatted_metadata, str)
    assert formatted_metadata.startswith("#")
    assert "," in formatted_metadata


@pytest.mark.parametrize(
    ("separator", "header_prefix"), [(",", "#"), (";", "##"), ("\t", "")]
)
def test_format_csv_metadata_varied_params(
    mock_batch_upload_geneset_one_gene_id_one_microarray, separator, header_prefix
):
    """Test the format_csv_metadata function with varied parameters."""
    formatted_metadata = format_csv_metadata(
        mock_batch_upload_geneset_one_gene_id_one_microarray,
        sep=separator,
        header_prefix=header_prefix,
    )
    assert isinstance(formatted_metadata, str)
    assert formatted_metadata.startswith(header_prefix)
    assert separator in formatted_metadata
