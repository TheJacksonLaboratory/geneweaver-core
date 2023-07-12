"""Tests for the check_has_required_header_values function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.batch import (
    MissingRequiredHeaderError,
    check_has_required_header_values,
)

from tests.unit.parse.batch.conftest import (
    HAS_REQUIRED_HEADER_FIELDS,
    MISSING_REQUIRED_HEADER_FIELDS,
)


@pytest.mark.parametrize("header", HAS_REQUIRED_HEADER_FIELDS)
def test_check_has_required_header_values_passes(header):
    """Test case when check_has_required_header_values passes."""
    # Should not raise any exception
    check_has_required_header_values(header)


@pytest.mark.parametrize("header", MISSING_REQUIRED_HEADER_FIELDS)
def test_check_has_required_header_values_fails(header):
    """Test case when check_has_required_header_values fails."""
    with pytest.raises(MissingRequiredHeaderError):
        check_has_required_header_values(header)
