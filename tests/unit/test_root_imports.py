"""Core module of GeneWeaver."""


def test_can_import_enum() -> None:
    """Test that we can import the enum module."""
    from geneweaver.core import enum

    assert enum is not None


def test_can_import_schema() -> None:
    """Test that we can import the schema module."""
    from geneweaver.core import schema

    assert schema is not None


def test_can_import_config() -> None:
    """Test that we can import the config module."""
    from geneweaver.core import config

    assert config is not None
