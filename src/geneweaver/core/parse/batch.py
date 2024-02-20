"""Parse batch geneset files.

This module provides a set of functions for processing batch geneset files and
their contents. It includes functionality to check the type of a file,
process lines of content, read headers and values, update and reset headers,
and create Geneset objects for batch upload.

File Type Identification Function:
- is_batch_file: Check if the provided file contents are a valid batch file.

Line Processing Function:
- process_lines: Process each line of content to build and return a list of
BatchUploadGeneset instances.

Header Processing Functions:
- read_header: Process a header line and update the corresponding state variables
accordingly.
- update_header: Update the header dictionary based on a key-value pair from the
processed line.
- reset_required_header_values: Reset required values in a header dictionary.
- check_has_required_header_values: Check if a header dictionary has required values.
- process_header_line: Process a header line into a key-value pair.
- read_single_prefix_header: Read a single-prefix header line into a key-value pair.
- read_space_separated_header: Read a space-separated header line into a key-value pair.

Value Processing Functions:
- read_values: Read a line assuming it's a value, and updates the reading mode if
necessary.
- process_value_line: Process a value line into a key-value pair.

Geneset Construction Function:
- create_geneset: Create a Geneset object from a batch upload.

Geneset Finalization Function:
- finalize_processed_geneset: Add the current geneset to the list and prepares for
processing the next one.

Exception Checking Function:
- string_has_newlines: Check if a string has newline characters.

Exceptions:
- UnsupportedFileTypeError: Raised if the file is neither a batch file nor a geneset
values file.
- MultiLineStringError: Raised if a value row is encountered with return characters.
- InvalidBatchValueLineError: Raised if a value row is encountered with more than two
values.
- NotAHeaderRowError: Raised when a header line is expected but not found.
- MissingRequiredHeaderError: Raised when any of the required keys are missing in the
header.
- IgnoreLineError: Raised if the line is to be ignored based on its prefix.
"""

from enum import Enum
from typing import List, Tuple

from geneweaver.core.parse.enum import GeneweaverFileType
from geneweaver.core.parse.exceptions import (
    IgnoreLineError,
    InvalidBatchValueLineError,
    MissingRequiredHeaderError,
    MultiLineStringError,
    NotAHeaderRowError,
    UnsupportedFileTypeError,
)
from geneweaver.core.schema.batch import BatchUploadGeneset, GenesetValueInput

# Header characters which DO NOT need to be space separated.
HEADER_CHARACTERS = {
    ":": "abbreviation",
    "=": "name",
    "+": "description",
    "@": "species",
    "!": "score",
    "%": "gene_id_type",
    "~": "ontology",
    "|": "uberon_id",
}

# Header characters which DO need to be space separated. This is because these
# characters can also be seen in the values section of the batch file.
SPACE_SEPARATED_HEADER_CHARACTERS = {
    "P": "pubmed_id",
    "A": "private",
    "T": "curation_id",
    "U": "user_id",
    "D": "attribution_id",
}

# Characters which should be ignored in the batch file.
IGNORE_CHARACTERS = {
    "#": "comment",
    " ": "space",
}

# Characters denoting required header information for all genesets.
REQUIRED_HEADERS = (":", "=", "+")


class ReadMode(Enum):
    """Enum to keep track of what part of the batch file is being read."""

    HEADER = "header"
    CONTENT = "content"


def is_batch_file(contents: str) -> GeneweaverFileType:
    """Check if the provided file contents are a valid batch file.

    We will consider a file to be a batch file if we encounter a header row before
    encountering a value row. If we encounter a value row before a header row, we will
    consider the file to be a geneset file.

    Processing stops as soon as a header or value row is encountered. If each line
    contains an ignore character (e.g. a comment), the entire file will be read.

    :param contents: The contents of the file to be checked.

    :raises: UnsupportedFileTypeError: If the file is neither a batch file nor a
    geneset values file. Or if any of the following errors are encountered during
    reading:
        - MultiLineStringError: If a value row is encountered with return characters.
        - InvalidBatchValueLineError: If a value row is encountered with more than two
        values (the gene identifier and the score).

    :returns: GeneweaverFileType.BATCH if the file is a batch file,
    GeneweaverFileType.VALUES otherwise.
    """
    for line in contents.splitlines():
        try:
            _ = process_header_line(line)
            return GeneweaverFileType.BATCH

        except NotAHeaderRowError:
            try:
                _ = process_value_line(line)
                return GeneweaverFileType.VALUES

            except InvalidBatchValueLineError as e:
                raise UnsupportedFileTypeError() from e

            except MultiLineStringError as e:
                raise UnsupportedFileTypeError() from e

        except IgnoreLineError:
            continue

    raise UnsupportedFileTypeError()


def process_lines(contents: str) -> List[BatchUploadGeneset]:
    """Process each line of content to build and return a list of BatchUploadGeneset.

    The function iterates over each line in the provided content. Depending on the
    current read mode and the content of the line, the function performs one of the
    following actions:

    - If the line contains header information and the current read mode is 'HEADER',
      it updates the header information for the current geneset.
    - If the line contains header information and the current read mode is 'CONTENT',
      it finalizes the current geneset and prepares for a new one. Header information
      encountered after the presence of geneset value information indicates that the
      current geneset is complete and should be appended to the genesets list.
    - If the line does not contain header information it reads the line as geneset value
      information, appends the value to the current geneset values and
      - will switch the read mode to 'CONTENT' if it is currently 'HEADER'.
    - If the line contains an ignored character, it ignores the line and continues.

    After processing all lines, the function appends the final geneset (created from the
    last header and value lines) to the genesets list.

    :param contents: The contents of the batch file to be processed.

    :returns: A list of genesets created from the processed batch file.
    """
    genesets, header, current_geneset_values, read_mode = [], {}, [], ReadMode.HEADER

    for line in contents.splitlines():
        try:
            genesets, current_geneset_values, header, read_mode = read_header(
                line, header, current_geneset_values, read_mode, genesets
            )

        except NotAHeaderRowError:
            current_geneset_values, read_mode = read_values(
                line, header, current_geneset_values, read_mode
            )

        except IgnoreLineError:
            continue

    genesets.append(create_geneset(header, current_geneset_values))

    return genesets


def read_header(
    line: str,
    header: dict,
    current_geneset_values: list,
    read_mode: ReadMode,
    genesets: List[BatchUploadGeneset],
) -> Tuple[list[BatchUploadGeneset], list, dict, ReadMode]:
    """Process a header line and update the corresponding state variables accordingly.

    This function takes a line from a batch file, processes it as a header line and
    updates the header dictionary, the current_geneset_values list, and the read_mode.
    If the read_mode was set to CONTENT prior to reading the line, it implies that the
    previous line was a geneset value line, thus it finalizes the current geneset and
    adds it to the genesets list, and resets the header and current_geneset_values for
    the next geneset.

    :param line: The line from the batch file to be processed.
    :param header: The dict that holds the header information for the current geneset.
    :param current_geneset_values: The list of current geneset values.
    :param read_mode: The current read mode - HEADER or CONTENT.
    :param genesets: The list of already processed genesets.

    :returns: A tuple containing:
         0. the updated list of processed genesets,
         1. the current geneset values,
         2. the updated header, and the updated read mode.

    :raises NotAHeaderRowError:Raised when a header line is expected but not found.
    MissingRequiredHeaderError
        If any of the required keys are missing in the header before trying to finalize
        the geneset (when switching from content to header).
    NotAHeaderRowError
        If the line does not follow the expected header format.
    """
    key, value = process_header_line(line)

    if read_mode is ReadMode.CONTENT:
        genesets, current_geneset_values, header = finalize_processed_geneset(
            genesets, header, current_geneset_values
        )
        read_mode = ReadMode.HEADER

    header = update_header(key, value, header)
    return genesets, current_geneset_values, header, read_mode


def finalize_processed_geneset(
    genesets: List[BatchUploadGeneset], header: dict, current_geneset_values: list
) -> Tuple[List[BatchUploadGeneset], list, dict]:
    """Add the current geneset to the list and prepares for processing the next one.

    This function first checks that the header contains all required values. Then, it
    creates a new geneset using the header and the current_geneset_values list and
    appends it to the genesets list. It also resets the current_geneset_values list and
    the header for the next geneset.

    :param genesets: A list of BatchUploadGeneset instances that have been processed.
    :param header: A dictionary representing the current header data.
    :param current_geneset_values: A list of GenesetValueInput instances representing
    the current geneset values.

    :returns: A tuple containing three elements:
        0. The updated list of BatchUploadGeneset instances.
        1. The reset list for the next geneset values.
        2. The reset header dictionary for the next geneset.

    :raises MissingRequiredHeaderError:If any of the required keys are missing in the
    header before trying to finalize the geneset.
    """
    check_has_required_header_values(header)
    genesets.append(create_geneset(header, current_geneset_values))
    return genesets, [], reset_required_header_values(header)


def update_header(key: str, value: str, header: dict) -> dict:
    """Update the header dictionary based on a key-value pair from the processed line.

    The function updates the header dictionary in-place. This function is used to take
    any header-key specific action needed based on the header key type.

    If the key equals to 'description', it appends the value to the existing description
    value, if any, separated by a space. Otherwise, it simply updates or sets the value
    for the given key in the header.

    :param key: The key to update in the header, as a string.
    :param value: The new value for the given key, as a string.
    :param header: The header dictionary to update.

    :returns: The updated header dictionary.
    """
    if key == "description":
        header[key] = " ".join((header.get(key, ""), value))
    else:
        header[key] = value
    return header


def read_values(
    line: str, header: dict, current_geneset_values: list, read_mode: ReadMode
) -> Tuple[list, ReadMode]:
    r"""Read a line assuming it's a value, and updates the reading mode if necessary.

    This function assumes the given line is not a header row. It first uses the
    process_value_line function to parse the line into a symbol-value pair. Then, if the
    current read_mode is HEADER, it checks the header for required values and switches
    the read_mode to CONTENT. Finally, it appends a new GenesetValueInput
    instance to the current_geneset_values list.

    :param line: A string representing a line in the 'value' format, e.g.,
    'symbol\tvalue' or 'symbol value'. Will also accept multiple whitespace characters
    between the symbol and value.
    :param header: A dictionary representing the current header data.
    :param current_geneset_values: A list of GenesetValueInput instances representing
    the current geneset values.
    :param read_mode: A ReadMode enum value representing the current reading mode.

    :returns: A tuple where the first element is the updated list of GenesetValueInput
    instances, and the second element is the updated reading mode.

    :raises MissingRequiredHeaderError:If any of the required keys are missing in the
    header when switching from HEADER to CONTENT mode (the first time a content line is
    read after a header).
    """
    symbol, value = process_value_line(line)

    if read_mode is ReadMode.HEADER:
        check_has_required_header_values(header)
        read_mode = ReadMode.CONTENT

    current_geneset_values.append(GenesetValueInput(symbol=symbol, value=value))

    return current_geneset_values, read_mode


def create_geneset(
    header: dict, content: List[GenesetValueInput]
) -> BatchUploadGeneset:
    """Create a Geneset object for batch upload.

    This function takes a header and content, and constructs a BatchUploadGeneset object
    using these inputs.

    :param header: Dictionary containing header information.
    :param content: List containing content information.

    :returns: An object representing the Geneset for batch upload.
    """
    return BatchUploadGeneset(values=content, **header)


def reset_required_header_values(header: dict) -> dict:
    """Reset required values in a header dictionary.

    This function attempts to delete specific keys from the header dictionary.

    :param header: The header dictionary.

    :returns: The updated header dictionary.
    """
    for key in REQUIRED_HEADERS:
        try:
            del header[HEADER_CHARACTERS[key]]
        except KeyError:
            continue
    return header


def check_has_required_header_values(header: dict) -> None:
    """Check if a header dictionary has required values.

    This function checks if specific keys are present in the header dictionary.

    :param header: The header dictionary.

    :returns: None

    :raises MissingRequiredHeaderError: If any of the required keys are missing in the
    header.
    """
    if not all((HEADER_CHARACTERS[key] in header for key in REQUIRED_HEADERS)):
        raise MissingRequiredHeaderError()


def process_header_line(line: str) -> Tuple[str, str]:
    """Process a header line into a key-value pair.

    This function reads a header line, and processes it into a key-value pair based on
    its prefix.

    :param line: The line to process.

    :returns: The key-value pair.

    :raises IgnoreLineError: If the line is to be ignored based on its prefix.
    :raises NotAHeaderRowError: If the line does not follow the expected header format.
    """
    line = line.strip()

    try:
        prefix = line[0]
    except IndexError:
        raise IgnoreLineError() from None

    if prefix in IGNORE_CHARACTERS:
        raise IgnoreLineError() from None

    try:
        key, value = read_single_prefix_header(prefix, line)
    except NotAHeaderRowError:
        key, value = read_space_separated_header(prefix, line)

    return key, value


def read_single_prefix_header(prefix: str, line: str) -> Tuple[str, str]:
    """Read a single-prefix header line into a key-value pair.

    This function reads a single-prefix header line, and returns it as a key-value pair.

    :param prefix: The prefix of the line (the first character).
    :param line: The line to process.

    :returns: The key-value pair.

    :raises NotAHeaderRowError: If the line does not follow the expected single-prefix
    header format.
    """
    try:
        key = HEADER_CHARACTERS[prefix]
        value = line[1:].strip()

    except (KeyError, IndexError):
        raise NotAHeaderRowError() from None

    return key, value


def read_space_separated_header(prefix: str, line: str) -> Tuple[str, str]:
    """Read a space-separated header line into a key-value pair.

    This function reads a space-separated header line, and returns it as a key-value
    pair.

    :param prefix: The prefix of the line (the first character).
    :param line: The line to process.

    :returns: first value is the header key, second is the header value.

    :raises NotAHeaderRowError: If the line does not follow the expected space-separated
    header format.
    """
    try:
        if line[1] not in (" ", "\t"):
            raise NotAHeaderRowError()

        key = SPACE_SEPARATED_HEADER_CHARACTERS[prefix]
        value = line[2:].strip()

    except (KeyError, IndexError):
        raise NotAHeaderRowError() from None

    return key, value


def process_value_line(line: str) -> Tuple[str, str]:
    """Process a value line into a key-value pair.

    This function splits a line into two parts, and returns them as a symbol-value pair.

    :param line: The line to process.

    :returns: The first value is the gene symbol, the second is the value.

    :raises MultiLineStringError: If the line contains newline characters.
    :raises InvalidBatchValueLine: If the line does not split into exactly two parts.
    """
    if string_has_newlines(line):
        raise MultiLineStringError()

    split_line = line.split()

    if len(split_line) != 2:
        raise InvalidBatchValueLineError()

    return split_line[0], split_line[1]


def string_has_newlines(input_str: str) -> bool:
    r"""Check if a string has newline characters.

    This function checks if a string contains either "\n" or "\r" characters.

    :param input_str: The string to check.

    :returns: True if the string contains newline characters, False otherwise.
    """
    # Here we return the results of the expression evaluation. This means that it will
    # return True if either "\n" or "\r" is in the string, and False otherwise.
    return "\n" in input_str or "\r" in input_str
