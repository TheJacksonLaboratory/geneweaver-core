
def test_can_import_enum():
    from jax.geneweaver.core import enum
    assert enum is not None


def test_can_import_schema():
    from jax.geneweaver.core import schema
    assert schema is not None


def test_can_import_config():
    from jax.geneweaver.core import config
    assert config is not None
