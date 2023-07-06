"""Tests for the read_space_separated_header function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.batch import (
    SPACE_SEPARATED_HEADER_CHARACTERS,
    NotAHeaderRowError,
    read_space_separated_header,
)


@pytest.mark.parametrize(
    ("prefix", "line", "expected"),
    [
        # normal case with prefix included in SPACE_SEPARATED_HEADER_CHARACTERS
        ("Y", "Y sample line", ("sample_key", "sample line")),
        # cases with different prefixes included in SPACE_SEPARATED_HEADER_CHARACTERS
        ("Z", "Z another sample line", ("another_key", "another sample line")),
        # tab character after prefix
        ("Y", "Y\tsample line", ("sample_key", "sample line")),
        # multiple spaces after prefix
        ("Y", "Y   sample line", ("sample_key", "sample line")),
        # multiple tabs after prefix
        ("Y", "Y\t\tsample line", ("sample_key", "sample line")),
    ],
)
def test_read_space_separated_header_success(prefix, line, expected):
    """Test that read_space_separated_header returns the expected value."""
    SPACE_SEPARATED_HEADER_CHARACTERS.update({prefix: expected[0]})
    assert read_space_separated_header(prefix, line) == expected
    SPACE_SEPARATED_HEADER_CHARACTERS.pop(prefix)  # cleaning up after test


@pytest.mark.parametrize(
    ("prefix", "line", "exception"),
    [
        # line with no space after prefix
        ("Y", "Ysample line", NotAHeaderRowError),
        # line with invalid prefix
        ("Z", " Z sample line", NotAHeaderRowError),
        # empty line
        ("", "", NotAHeaderRowError),
        # line with only prefix
        ("Y", "Y", NotAHeaderRowError),
    ],
)
def test_read_space_separated_header_failure(prefix, line, exception):
    """Test that read_space_separated_header raises the expected exception."""
    with pytest.raises(exception):
        read_space_separated_header(prefix, line)
