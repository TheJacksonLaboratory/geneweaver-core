"""Test the format_geneset_metadata function."""

from geneweaver.core.render.batch import format_geneset_metadata


def test_format_geneset_metadata_standard(mock_batch_upload_geneset_all_combinations):
    """Test the format_geneset_metadata function with a standard geneset."""
    formatted_metadata = format_geneset_metadata(
        mock_batch_upload_geneset_all_combinations
    )
    # Assert that the output is a string and has the expected structure
    assert isinstance(formatted_metadata, str)
    # Additional assertions can be made based on the specific format of the metadata
    assert formatted_metadata.count("\n") == 9
    for char in ["!", "@", "%", "A", ":", "=", "+"]:
        assert char in formatted_metadata
