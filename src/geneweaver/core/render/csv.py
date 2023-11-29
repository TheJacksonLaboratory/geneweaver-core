"""Render data as CSV files."""

from geneweaver.core.render.gene_list import gene_list_str
from geneweaver.core.schema.batch import BatchUploadGeneset


def format_csv_file(
    geneset: BatchUploadGeneset, sep: str = ",", header_prefix: str = "#"
) -> str:
    """Format a geneset for a CSV file.

    :param geneset: The geneset to format.
    :param sep: The separator to use between values.
    :param header_prefix: The prefix to use for the header lines.

    :return: A string containing the geneset in CSV format.
    """
    data_str = format_csv_metadata(geneset, sep, header_prefix)
    data_str += f"gene{sep}value\n"
    data_str += gene_list_str(geneset.values, sep)
    return data_str


def format_csv_metadata(
    geneset: BatchUploadGeneset, sep: str = ",", header_prefix: str = "#"
) -> str:
    """Format geneset metadata for a CSV file.

    :param geneset: The geneset to format.
    :param sep: The separator to use between values.
    :param header_prefix: The prefix to use for the header lines.

    :return: A string containing the geneset metadata in CSV format.
    """
    geneset_dict = geneset.dict(exclude={"values", "curation_id"})
    return "\n".join(
        (f"{header_prefix}{key}{sep}{value}" for key, value in geneset_dict.items())
    )
