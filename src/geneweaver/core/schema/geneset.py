import datetime
from typing import List
from pydantic import BaseModel, Field

from geneweaver.core.enum import GenesetAccess
from geneweaver.core.schema.gene import GeneValue
from geneweaver.core.enum import GenesetScoreType


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
    gene_identifier: str = Field(..., alias='gene-identifier')
    gene_list: List[GeneValue] = Field(..., alias='gene-list')


class BatchUpload(BaseModel):
    batch_file: str
    curation_group: List[str]


class GenesetInfo(BaseModel):
    id: int
    page_views: int
    referers: List[str]
    analyses: List[str]
    resource_id: int
    last_sim: str
    last_ann: str
    jac_started: str
    jac_completed: str


class SimilarGeneset(Geneset):
    jax_value: float
    gic_value: float
