import pytest
import importlib

VALID_IMPORTS = [
    ('jax.geneweaver.core.schema', 'Gene'),
    ('jax.geneweaver.core.schema', 'GeneValue'),
    ('jax.geneweaver.core.schema', 'Geneset'),
    ('jax.geneweaver.core.schema', 'GenesetUpload'),
    ('jax.geneweaver.core.schema', 'Group'),
    ('jax.geneweaver.core.schema', 'UserAdminGroup'),
    ('jax.geneweaver.core.schema', 'Project'),
    ('jax.geneweaver.core.schema', 'ProjectCreate'),
    ('jax.geneweaver.core.schema', 'Publication'),
    ('jax.geneweaver.core.schema', 'StubGenerator'),
    ('jax.geneweaver.core.schema', 'User'),
    ('jax.geneweaver.core.schema', 'gene'),
    ('jax.geneweaver.core.schema', 'geneset'),
    ('jax.geneweaver.core.schema', 'group'),
    ('jax.geneweaver.core.schema', 'project'),
    ('jax.geneweaver.core.schema', 'publication'),
    ('jax.geneweaver.core.schema', 'stubgenerator'),
    ('jax.geneweaver.core.schema', 'user'),
    ('jax.geneweaver.core.schema', 'legacy_api'),
]

INVALID_IMPORTS = [
    ('jax.geneweaver.core.schema', 'AddGenesetByUserPublication'),
    ('jax.geneweaver.core.schema', 'AddGenesetByUser'),
    ('jax.geneweaver.core.schema', 'AddGenesetByUserPublication'),
    ('jax.geneweaver.core.schema', 'AddGenesetByUserBase'),
]


@pytest.mark.parametrize('import_path,package_attr', VALID_IMPORTS)
def test_can_import(import_path, package_attr):
    """Test that we can import the module and the module has the expected attribute."""
    module = importlib.import_module(import_path)
    assert module is not None

    if package_attr is not None:
        assert getattr(module, package_attr) is not None


@pytest.mark.parametrize('import_path,package_attr', INVALID_IMPORTS)
def test_cannot_import(import_path, package_attr):
    module = importlib.import_module(import_path)
    package = None
    if package_attr is not None:
        try:
            package = getattr(module, package_attr)
        except AttributeError:
            pass

    assert module is None or package is None
