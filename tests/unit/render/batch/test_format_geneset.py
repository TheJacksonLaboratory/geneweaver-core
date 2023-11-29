"""Test the format_geneset function."""

from unittest.mock import patch

import pytest
from geneweaver.core.render.batch import BatchUploadGeneset, format_geneset


def mock_format_geneset_metadata(geneset: BatchUploadGeneset) -> str:
    """Mock function for format_geneset_metadata."""
    return f"metadata-{geneset.name}"


def mock_format_geneset_values(geneset: BatchUploadGeneset) -> str:
    """Mock function for format_geneset_values."""
    return f"values-{geneset.name}"


@pytest.mark.parametrize(
    ("geneset_name", "expected_output"),
    [
        ("TestGeneset1", "metadata-TestGeneset1values-TestGeneset1"),
        ("TestGeneset2", "metadata-TestGeneset2values-TestGeneset2"),
    ],
)
def test_format_geneset(
    geneset_name: str,
    expected_output: str,
    mock_batch_upload_geneset_all_species_scores: BatchUploadGeneset,
):
    """Test the format_geneset function.

    This test checks if the function correctly concatenates the results of
    format_geneset_metadata and format_geneset_values.

    :param geneset_name: The name of the geneset to be formatted.
    :param expected_output: The expected output string.
    :param mock_batch_upload_geneset_all_species_scores: A mock geneset (a fixture).
    """
    mock_batch_upload_geneset_all_species_scores.name = geneset_name
    with patch(
        "geneweaver.core.render.batch.format_geneset_metadata",
        side_effect=mock_format_geneset_metadata,
    ), patch(
        "geneweaver.core.render.batch.format_geneset_values",
        side_effect=mock_format_geneset_values,
    ):
        result = format_geneset(mock_batch_upload_geneset_all_species_scores)
        assert result == expected_output
