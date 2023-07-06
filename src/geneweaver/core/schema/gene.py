"""Gene schema."""
import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Gene(BaseModel):
    """Gene schema."""

    id: int  # noqa: A003
    reference_id: str
    gene_database: str
    species: str
    preferred: bool
    date: str


class GeneRow(BaseModel):
    """Gene schema for database row."""

    ode_gene_id: int
    ode_ref_id: str
    gdb_id: int
    sp_id: int
    ode_pref: bool
    ode_date: Optional[str]
    old_ode_gene_ids: Optional[List[int]]


class GeneValue(BaseModel):
    """Schema for summary Gene values."""

    gene_id: str = Field(..., alias="gene-id")
    value: str


class GeneDatabase(BaseModel):
    """Gene database schema."""

    name: str
    shortname: str
    species: str
    data: datetime.datetime
    precision: int


class GeneDatabaseRow(BaseModel):
    """Gene database schema for database row."""

    gdb_id: int
    gdb_name: str
    sp_id: int
    gdb_shortname: str
    gdb_date: str
    gdb_precision: int
    gdb_linkout_url: Optional[str]
