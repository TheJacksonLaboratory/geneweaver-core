"""Test the format_csv_file function."""

from unittest.mock import MagicMock, patch

from geneweaver.core.render.csv import format_csv_file


def test_format_csv_file_with_mocks():
    """Test the format_csv_file function with mocks for dependent functions."""
    mock_batch_upload_geneset = MagicMock()
    with patch(
        "geneweaver.core.render.csv.format_csv_metadata"
    ) as mock_metadata, patch(
        "geneweaver.core.render.csv.gene_list_str"
    ) as mock_gene_list:
        mock_metadata.return_value = "mocked_metadata\n"
        mock_gene_list.return_value = "gene1,value1\ngene2,value2"

        csv_content = format_csv_file(mock_batch_upload_geneset)

        mock_metadata.assert_called_once()
        mock_gene_list.assert_called_once()
        assert csv_content.startswith("mocked_metadata")
        assert "gene,value" in csv_content
        assert "gene1,value1\ngene2,value2" in csv_content
