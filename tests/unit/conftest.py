"""Pytest fixtures for unit tests.

These fixtures are available to be used by all tests in the unit test suite.
"""
from typing import Any, Dict, List

import pytest
from geneweaver.core.config_class import CoreSettings
from geneweaver.testing.fixtures import *  # noqa: F403


@pytest.fixture(scope="session")
def core_settings_fields() -> List[str]:
    """Return a list of the pydantic Settings class fields."""
    return [field.name for field in CoreSettings.__fields__.values()]


@pytest.fixture(scope="session")
def core_settings_required_fields() -> List[str]:
    """Return a list of the pydantic Settings class fields."""
    return [field.name for field in CoreSettings.__fields__.values() if field.required]


@pytest.fixture(scope="session")
def core_settings_optional_fields() -> Dict[str, Any]:
    """Return a dict of the optional pydantic Settings class fields."""
    return {
        f.name: f.default for f in CoreSettings.__fields__.values() if not f.required
    }
