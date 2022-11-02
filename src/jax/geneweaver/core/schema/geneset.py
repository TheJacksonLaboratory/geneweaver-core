import datetime
from typing import List
from pydantic import BaseModel, Field

from jax.geneweaver.core.enum import GenesetAccess
from jax.geneweaver.core.schema.gene import GeneValue
from jax.geneweaver.core.enum import GenesetScoreType


class Geneset(BaseModel):
    name: str
    abbreviation: str
    description: str
    count: int
    threshold_type: int
    threshold: str
    gene_id_type: int
    created: datetime.date
    admin_flag: str
    updated: datetime.datetime
    status: str
    gsv_qual: str
    attribution: int
    is_edgelist: bool


class GenesetUpload(BaseModel):
    name: str
    label: str
    score_type: GenesetScoreType = Field(..., alias='score-type')
    description: str
    pubmed_id: str = Field(..., alias='pubmed-id')
    access: GenesetAccess
    groups: List[str]
    species: str
    gene_identifiers: str = Field(..., alias='gene-identifiers')
    gene_list: List[GeneValue] = Field(..., alias='gene-list')


class BatchUpload(BaseModel):
    batch_file: str
    curation_group: List[str]
