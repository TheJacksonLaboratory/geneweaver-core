"""Python Package main config file.

For more options refer to pydantic base-settings docs:
https://pydantic-docs.helpmanual.io/usage/settings/
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class ExternalServiceSettings(BaseSettings):
    """External Service Config and Settings Configuration."""

    PUBMED_XLM_SVC_URL: str = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={0}&retmode=xml"
    )


class CoreSettings(BaseSettings):
    """Root Config and Settings Configuration."""

    PROJECT_NAME: str = "jax-geneweaver-core"
    VERSION: str = "0.0.2"
    LOG_LEVEL: str = "INFO"
    SERVICE_URLS: ExternalServiceSettings = ExternalServiceSettings()

    model_config = SettingsConfigDict(env_prefix="GW_")
