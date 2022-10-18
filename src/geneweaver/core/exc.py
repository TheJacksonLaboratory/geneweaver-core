"""
This namespace contains custom exceptions for the GeneWeaver project.
"""


class GeneweaverException(Exception):
    """
    Base class for all Geneweaver exceptions.
    """
    pass


class GeneweaverError(GeneweaverException):
    """
    Base class for all Geneweaver errors.
    """
    pass


class GeneweaverWarning(GeneweaverException):
    """
    Base class for all Geneweaver warnings.
    """
    pass
