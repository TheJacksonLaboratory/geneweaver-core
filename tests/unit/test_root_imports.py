
def test_can_import_enum():
    from geneweaver.core import enum
    assert enum is not None


def test_can_import_schema():
    from geneweaver.core import schema
    assert schema is not None


def test_can_import_config():
    from geneweaver.core import config
    assert config is not None
