"""Tests for the read_single_prefix_header function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.batch import (
    HEADER_CHARACTERS,
    NotAHeaderRowError,
    read_single_prefix_header,
)


@pytest.mark.parametrize(
    ("prefix", "line", "expected"),
    [
        # normal case with prefix included in HEADER_CHARACTERS
        ("#", "#sample line", ("sample_key", "sample line")),
        # cases with different prefixes included in HEADER_CHARACTERS
        ("@", "@another sample line", ("another_key", "another sample line")),
        # tab character after prefix
        ("#", "#\tsample line", ("sample_key", "sample line")),
        # multiple spaces after prefix
        ("#", "#   sample line", ("sample_key", "sample line")),
        # multiple tabs after prefix
        ("#", "#\t\tsample line", ("sample_key", "sample line")),
    ],
)
def test_read_single_prefix_header_success(prefix, line, expected):
    """Test that read_single_prefix_header returns the expected value."""
    HEADER_CHARACTERS.update({prefix: expected[0]})
    assert read_single_prefix_header(prefix, line) == expected
    HEADER_CHARACTERS.pop(prefix)  # cleaning up after test


@pytest.mark.parametrize(
    ("prefix", "line", "exception"),
    [
        # line with invalid prefix
        ("$", "$sample line", NotAHeaderRowError),
        # empty line
        ("", "", NotAHeaderRowError),
        # line with only prefix and no content
        ("#", "#", NotAHeaderRowError),
    ],
)
def test_read_single_prefix_header_failure(prefix, line, exception):
    """Test that read_single_prefix_header raises the expected exception."""
    with pytest.raises(exception):
        read_single_prefix_header(prefix, line)
