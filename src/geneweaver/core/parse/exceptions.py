"""Exceptions related to file parsing."""


class UnsupportedFileTypeError(Exception):
    """Custom exception for when a file type is not supported."""

    pass



class NotAHeaderRowError(Exception):
    """Raised when a row is not a header row."""

    pass


class InvalidBatchValueLineError(Exception):
    """Raised when a value line is invalid."""

    pass


class MultiLineStringError(Exception):
    """Raised when a string is multiline (but shouldn't be)."""

    pass


class IgnoreLineError(Exception):
    """Raised when a line should be ignored."""

    pass


class MissingRequiredHeaderError(Exception):
    """Raised when a required header is missing."""

    pass


class InvalidScoreThresholdError(Exception):
    """Raised when a score threshold is invalid."""

    pass
