"""Functions for rendering gene lists to strings."""

from typing import Iterable

from geneweaver.core.schema.gene import GeneValue


def gene_list_str(gene_ids: Iterable[GeneValue], sep: str = "\t") -> str:
    """Render a list of GeneValue objects to a string.

    This can be useful for creating csv files, or for uploading to Geneweaver with the
    "Gene List" text input option.

    :param gene_ids: Iterable of GeneValue objects.
    :param sep: Separator to use between symbol and value.
    :return: String representation of the GeneValue objects.
    """
    return "\n".join(
        (f"{gene_value.symbol}{sep}{gene_value.value}" for gene_value in gene_ids)
    )
