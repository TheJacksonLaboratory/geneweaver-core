"""Test the Geneweaver exception module."""
import pytest
from geneweaver.core.exc import GeneweaverError


def throw_geneweaver_exception() -> None:
    """Throw a Geneweaver exception."""
    raise GeneweaverError("Geneweaver Exception")


def test_catch_geneweaver_exception() -> None:
    """Catch a Geneweaver exception."""
    with pytest.raises(GeneweaverError) as excinfo:
        throw_geneweaver_exception()

    assert str(excinfo.value) == "Geneweaver Exception"
