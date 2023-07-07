"""Python Package main config file.

For more options refer to pydantic base-settings docs:
https://pydantic-docs.helpmanual.io/usage/settings/
"""
from pydantic import BaseSettings


class CoreSettings(BaseSettings):
    """Root Config and Settings Configuration."""

    PROJECT_NAME = "jax-geneweaver-core"
    VERSION = "0.0.2"
    LOG_LEVEL: str = "INFO"

    class Config:
        """Pydantic Config class."""

        env_prefix = "GW_"
