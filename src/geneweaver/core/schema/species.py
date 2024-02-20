"""Schemas relating to species."""

import datetime
from typing import Any, Optional

from geneweaver.core.enum import GeneIdentifier
from pydantic import BaseModel, Json


class Species(BaseModel):
    """Species schema."""

    id: int  # noqa: A003
    name: str
    taxonomic_id: int
    reference_gene_identifier: Optional[GeneIdentifier]


class SpeciesRow(BaseModel):
    """Species schema for database row."""

    sp_id: int
    sp_name: str
    sp_taxid: int
    sp_ref_gdb_id: Optional[int]
    sp_date: datetime.date
    sp_biomart_info: Optional[str]
    sp_source_data: Json[Any]
