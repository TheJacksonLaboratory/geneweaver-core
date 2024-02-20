"""Exceptions related to file parsing."""


class UnsupportedFileTypeError(Exception):
    """Custom exception for when a file type is not supported."""

    pass


class EmptyFileError(UnsupportedFileTypeError):
    """Custom exception for when a file is empty.

    Attributes
    ----------
        file_path -- the path of the file that is empty
        message -- explanation of the error

    """

    def __init__(
        self: "EmptyFileError", file_path: str, message: str = "File is empty."
    ) -> None:
        """Initialize the exception."""
        self.file_path = file_path
        self.message = message
        super().__init__(self.message)

    def __str__(self: "EmptyFileError") -> str:
        """Return a string representation of the exception."""
        return f"{self.file_path} -> {self.message}"


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
