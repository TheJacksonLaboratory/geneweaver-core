"""
Python Package main config file.

For more options refer to pydantic base-settings docs:
https://pydantic-docs.helpmanual.io/usage/settings/
"""

from pydantic import BaseSettings


class GeneweaverBaseSettings(BaseSettings):

    class Config:
        env_prefix = "GW_"


class CoreSettings(GeneweaverBaseSettings):
    """
    Root Config and Settings Configuration
    """
    PROJECT_NAME = 'geneweaver-core'
    VERSION = '0.0.20'


# Import me to access settings at runtime!
settings = CoreSettings()
