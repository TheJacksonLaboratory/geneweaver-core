from jax.geneweaver.core.exc import GeneweaverException


def throw_geneweaver_exception():
    """Throw a Geneweaver exception."""
    raise GeneweaverException("Geneweaver Exception")


def test_catch_geneweaver_exception():
    """Catch a Geneweaver exception."""
    try:
        throw_geneweaver_exception()
    except GeneweaverException as e:
        assert str(e) == "Geneweaver Exception"
