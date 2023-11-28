"""Test the format_geneset_values function."""
from geneweaver.core.render.batch import format_geneset_values


def test_format_geneset_values_non_empty(mock_batch_upload_geneset):
    """Test the format_geneset_values function with a non-empty geneset."""
    formatted_values = format_geneset_values(mock_batch_upload_geneset)
    # Assert that the output is a string and has the expected structure
    assert isinstance(formatted_values, str)
    assert formatted_values.count("\n") == len(mock_batch_upload_geneset.values) - 1
    assert formatted_values.count("\t") == len(mock_batch_upload_geneset.values)


def test_format_geneset_values_empty(mock_empty_geneset):
    """Test the format_geneset_values function with an empty geneset."""
    formatted_values = format_geneset_values(mock_empty_geneset)
    assert formatted_values == ""
