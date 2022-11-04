from jax.geneweaver.core.config import CoreSettings
from jax.geneweaver.core.config import settings


def test_core_settings_schema():
    """Test the CoreSettings class."""
    schema = CoreSettings.schema()
    assert 'PROJECT_NAME' in schema['properties']
    assert 'LOG_LEVEL' in schema['properties']


def test_core_settings_default():
    """Test the CoreSettings class."""
    assert settings.PROJECT_NAME == 'jax-geneweaver-core'
    assert settings.VERSION == '0.0.2'
    assert settings.LOG_LEVEL == 'INFO'


def test_core_settings_kwargs():
    """Test the CoreSettings class."""
    these_settings = CoreSettings(PROJECT_NAME='test', LOG_LEVEL='DEBUG')
    assert these_settings.PROJECT_NAME == 'test'
    assert these_settings.LOG_LEVEL == 'DEBUG'
