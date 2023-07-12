"""Tests for the check_has_required_header_values function."""
# ruff: noqa: ANN001, ANN201
from unittest.mock import patch

import pytest
from geneweaver.core.parse.batch import (
    MissingRequiredHeaderError,
    check_has_required_header_values,
    finalize_processed_geneset,
)

from tests.unit.parse.batch.conftest import (
    HAS_REQUIRED_HEADER_FIELDS,
)


@pytest.mark.parametrize("genesets", [[], ["geneset1", "geneset2"]])
@pytest.mark.parametrize("header", HAS_REQUIRED_HEADER_FIELDS)
@pytest.mark.parametrize("current_geneset_values", [[], ["symbol", "1.0"]])
def test_finalize_processed_geneset(genesets, header, current_geneset_values):
    """Tests finalize_processed_geneset successfully creates and adds geneset."""
    geneset_start_len = len(genesets)
    with patch("geneweaver.core.parse.batch.create_geneset") as create_mock:
        create_mock.return_value = "geneset3"
        (
            updated_genesets,
            updated_current_geneset_values,
            updated_header,
        ) = finalize_processed_geneset(genesets, header.copy(), current_geneset_values)
    assert len(updated_genesets) == geneset_start_len + 1
    assert updated_current_geneset_values == []

    with pytest.raises(MissingRequiredHeaderError):
        check_has_required_header_values(updated_header)


@pytest.mark.parametrize(
    "header",
    [
        ({"key1": "value1"}),
    ],
)
def test_finalize_processed_geneset_missing_required_header(header):
    """Test that the right error is raised when required header is missing.

    Tests finalize_processed_geneset raises MissingRequiredHeaderError when required
    header is missing.
    """
    with pytest.raises(MissingRequiredHeaderError):
        finalize_processed_geneset([], header, ["value1", "value2"])


@pytest.mark.parametrize(
    "header",
    [
        ({"key1": "value1", "key2": "value2", "key3": "value3"}),
        ({"key1": "value1"}),
    ],
)
def test_finalize_processed_geneset_with_mocks(header):
    """Tests finalize_processed_geneset with mocks."""
    with patch(
        "geneweaver.core.parse.batch.check_has_required_header_values"
    ) as mock_check, patch(
        "geneweaver.core.parse.batch.create_geneset"
    ) as mock_create, patch(
        "geneweaver.core.parse.batch.reset_required_header_values"
    ) as mock_reset:
        genesets = []
        created_geneset = "geneset1"
        current_geneset_values = ["value1", "value2"]
        reset_header = {"key1": "value1"}
        mock_create.return_value = created_geneset
        mock_reset.return_value = reset_header

        (
            updated_genesets,
            updated_current_geneset_values,
            updated_header,
        ) = finalize_processed_geneset(genesets, header, current_geneset_values)

        mock_check.assert_called_once_with(header)
        mock_create.assert_called_once_with(header, current_geneset_values)
        mock_reset.assert_called_once_with(header)

        assert updated_genesets == [created_geneset]
        assert updated_current_geneset_values == []
        assert updated_header == reset_header
