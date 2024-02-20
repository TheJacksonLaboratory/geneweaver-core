"""Test the format_batch_file function."""

from unittest.mock import patch

from geneweaver.core.render.batch import format_batch_file


def mock_format_geneset(geneset):
    """Mock the format_geneset function."""
    return f"formatted-{geneset.name}"


# Test for an empty list of genesets
def test_format_batch_file_empty():
    """Test the format_batch_file function with an empty list of genesets."""
    with patch(
        "geneweaver.core.render.batch.format_geneset", side_effect=mock_format_geneset
    ):
        result = format_batch_file([])
        assert result == ""


# Test for a single geneset
def test_format_batch_file_single_geneset(mock_batch_upload_geneset_all_species_scores):
    """Test the format_batch_file function with a single geneset."""
    with patch(
        "geneweaver.core.render.batch.format_geneset", side_effect=mock_format_geneset
    ):
        result = format_batch_file([mock_batch_upload_geneset_all_species_scores])
        assert result == "formatted-Mock Species Geneset\n"


# Test for multiple genesets
def test_format_batch_file_multiple_genesets(
    mock_batch_upload_geneset_all_species_scores,
):
    """Test the format_batch_file function with multiple genesets."""
    with patch(
        "geneweaver.core.render.batch.format_geneset", side_effect=mock_format_geneset
    ):
        genesets = [mock_batch_upload_geneset_all_species_scores for _ in range(3)]
        result = format_batch_file(genesets)
        expected_result = (
            "\n".join(["formatted-Mock Species Geneset" for _ in range(3)]) + "\n"
        )
        assert result == expected_result
