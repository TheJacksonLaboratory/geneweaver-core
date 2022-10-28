from geneweaver.core.exc import GeneweaverException


def throw_base_exception():
    """Throw a base exception."""
    raise Exception("Base Exception")


def throw_geneweaver_exception():
    """Throw a Geneweaver exception."""
    raise GeneweaverException("Geneweaver Exception")


def test_catch_base_exception():
    """Catch a base exception."""
    try:
        throw_base_exception()
    except Exception as e:
        assert str(e) == "Base Exception"


def test_catch_geneweaver_exception():
    """Catch a Geneweaver exception."""
    try:
        throw_geneweaver_exception()
    except GeneweaverException as e:
        assert str(e) == "Geneweaver Exception"
