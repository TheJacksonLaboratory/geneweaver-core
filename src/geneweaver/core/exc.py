"""Custom exceptions for the GeneWeaver project."""


class GeneweaverError(Exception):
    """Base class for all Geneweaver exceptions."""

    pass


class ExternalAPIError(GeneweaverError):
    """Base class for all external API exceptions."""

    pass
