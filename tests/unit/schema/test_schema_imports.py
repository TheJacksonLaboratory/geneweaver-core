"""Test that we can import schema definitions."""
import importlib

import pytest

VALID_IMPORTS = [
    ("geneweaver.core.schema", "Gene"),
    ("geneweaver.core.schema", "GeneValue"),
    ("geneweaver.core.schema", "Geneset"),
    ("geneweaver.core.schema", "GenesetUpload"),
    ("geneweaver.core.schema", "Group"),
    ("geneweaver.core.schema", "UserAdminGroup"),
    ("geneweaver.core.schema", "Project"),
    ("geneweaver.core.schema", "ProjectCreate"),
    ("geneweaver.core.schema", "Publication"),
    ("geneweaver.core.schema", "StubGenerator"),
    ("geneweaver.core.schema", "User"),
    ("geneweaver.core.schema", "gene"),
    ("geneweaver.core.schema", "geneset"),
    ("geneweaver.core.schema", "group"),
    ("geneweaver.core.schema", "project"),
    ("geneweaver.core.schema", "publication"),
    ("geneweaver.core.schema", "stubgenerator"),
    ("geneweaver.core.schema", "user"),
    ("geneweaver.core.schema", "legacy_api"),
]

INVALID_IMPORTS = [
    ("geneweaver.core.schema", "AddGenesetByUserPublication"),
    ("geneweaver.core.schema", "AddGenesetByUser"),
    ("geneweaver.core.schema", "AddGenesetByUserPublication"),
    ("geneweaver.core.schema", "AddGenesetByUserBase"),
]


@pytest.mark.parametrize(("import_path", "package_attr"), VALID_IMPORTS)
def test_can_import(import_path: str, package_attr: str) -> None:
    """Test that we can import the module and the module has the expected attribute."""
    module = importlib.import_module(import_path)
    assert module is not None

    if package_attr is not None:
        assert getattr(module, package_attr) is not None


@pytest.mark.parametrize(("import_path", "package_attr"), INVALID_IMPORTS)
def test_cannot_import(import_path: str, package_attr: str) -> None:
    """Test to verify that modules that don't exist can't be imported."""
    module = importlib.import_module(import_path)
    package = None
    if package_attr is not None:
        try:
            package = getattr(module, package_attr)
        except AttributeError:
            pass

    assert module is None or package is None
