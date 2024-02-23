"""Batch upload file rendering."""

from typing import List

from geneweaver.core.schema.batch import (
    HEADER_CHARACTERS,
    IGNORE_CHARACTERS,
    INV_CHAR_MAP,
    SPACE_SEPARATED_HEADER_CHARACTERS,
    BatchUploadGeneset,
)

CHAR_MAP = HEADER_CHARACTERS | SPACE_SEPARATED_HEADER_CHARACTERS | IGNORE_CHARACTERS


def format_batch_file(genesets: List[BatchUploadGeneset]) -> str:
    """Format a batch upload file from a list of genesets.

    :param genesets: A list of genesets to format.

    :return: A string containing the genesets in batch upload format.
    """
    data_str = ""
    for geneset in genesets:
        data_str += format_geneset(geneset)
        data_str += "\n"
    return data_str


def format_geneset_metadata(geneset: BatchUploadGeneset) -> str:
    """Format geneset metadata for a batch upload file.

    :param geneset: The geneset to format.

    :return: A string containing the geneset metadata in batch upload format.
    """
    data_str = "\n".join(
        (
            f"{INV_CHAR_MAP[key] if key in INV_CHAR_MAP else key} {str(value)}"
            for key, value in geneset
            if key != "values" and value is not None
        )
    )
    data_str += "\n\n"
    return data_str


def format_geneset_values(geneset: BatchUploadGeneset) -> str:
    """Format geneset values for a batch upload file.

    :param geneset: The geneset to format.

    :return: A string containing the geneset values in batch upload format.
    """
    return "\n".join((str(gene_value) for gene_value in geneset.values))  # noqa: PD011


def format_geneset(geneset: BatchUploadGeneset) -> str:
    """Format a geneset for a batch upload file.

    :param geneset: The geneset to format.

    :return: A string containing the geneset in batch upload format.
    """
    data_str = format_geneset_metadata(geneset)
    data_str += format_geneset_values(geneset)
    return data_str
