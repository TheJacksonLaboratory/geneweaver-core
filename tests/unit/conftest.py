import pytest
from jax.geneweaver.core.config_class import CoreSettings


@pytest.fixture(scope="session")
def core_settings_fields():
    """ Return a list of the pydantic Settings class fields """
    return [field.name for field in CoreSettings.__fields__.values()]


@pytest.fixture(scope="session")
def core_settings_required_fields():
    """ Return a list of the pydantic Settings class fields """
    return [
        field.name
        for field in CoreSettings.__fields__.values()
        if field.required
    ]


@pytest.fixture(scope="session")
def core_settings_optional_fields():
    """ Return a list of the pydantic Settings class fields """
    return {
        f.name: f.default
        for f in CoreSettings.__fields__.values()
        if not f.required
    }
