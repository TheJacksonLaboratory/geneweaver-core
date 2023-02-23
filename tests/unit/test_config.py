import pytest

from jax.geneweaver.core.config import CoreSettings


@pytest.mark.parametrize("attribute", ['PROJECT_NAME', 'LOG_LEVEL'])
def test_core_settings_schema(attribute):
    """Test the CoreSettings class."""
    schema = CoreSettings.schema()
    assert attribute in schema['properties']


@pytest.mark.parametrize("attribute,expected",
                         [('PROJECT_NAME', 'jax-geneweaver-core'),
                          ('LOG_LEVEL', 'INFO')])
def test_core_settings_default(attribute, expected, core_settings_optional_fields):
    """Test the CoreSettings class."""
    assert attribute in core_settings_optional_fields
    assert core_settings_optional_fields[attribute] == expected


def test_core_settings_kwargs():
    """Test the CoreSettings class."""
    these_settings = CoreSettings(PROJECT_NAME='test', LOG_LEVEL='DEBUG')
    assert these_settings.PROJECT_NAME == 'test'
    assert these_settings.LOG_LEVEL == 'DEBUG'

