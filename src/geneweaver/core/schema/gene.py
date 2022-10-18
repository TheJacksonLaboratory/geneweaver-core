from typing import List
from pydantic import BaseModel, Field


class Gene(BaseModel):
    id: int
    reference_id: str
    gdb_id: int
    species_id: int
    preference: bool
    date: str
    old_ids: List[int]


class GeneValue(BaseModel):
    gene_id: str = Field(..., alias='gene-id')
    value: str
