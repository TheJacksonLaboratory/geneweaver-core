"""
Python Package main config file.

For more options refer to pydantic base-settings docs:
https://pydantic-docs.helpmanual.io/usage/settings/
"""

from pydantic import BaseSettings


class CoreSettings(BaseSettings):
    """
    Root Config and Settings Configuration
    """
    PROJECT_NAME = 'jax-geneweaver-core'
    VERSION = '0.0.2'
    LOG_LEVEL: str = 'INFO'

    class Config:
        env_prefix = "GW_"


# Import me to access settings at runtime!
settings = CoreSettings()
