"""Schemas for geneset."""

import datetime
from typing import List, Optional

from geneweaver.core.enum import (
    GeneIdentifier,
    GenesetAccess,
    GenesetTier,
    ScoreType,
    Species,
)
from geneweaver.core.schema.gene import GeneValue
from pydantic import BaseModel, Field


class Geneset(BaseModel):
    """Geneset schema."""

    id: int  # noqa: A003
    user_id: int
    file_id: int
    tier: GenesetTier = Field(..., alias="curation_id")
    species: Species = Field(..., alias="species_id")
    name: str
    abbreviation: str
    publication_id: int
    description: str
    count: int
    score_type: ScoreType
    threshold: str
    gene_id_type: GeneIdentifier
    created: datetime.date
    admin_flag: str
    updated: datetime.datetime
    status: str
    gsv_qual: str
    attribution: int
    is_edgelist: bool


class GenesetGenes(BaseModel):
    """Geneset genes schema."""

    genes: List[GeneValue]


class GenesetUpload(BaseModel):
    """Geneset upload schema."""

    name: str
    label: str
    score_type: ScoreType
    description: str
    pubmed_id: Optional[str]
    access: GenesetAccess
    groups: List[str] = []
    species: str
    gene_identifier: str
    gene_list: List[GeneValue]


class BatchUpload(BaseModel):
    """Batch upload schema."""

    batch_file: str
    curation_group: List[str]


class GenesetInfo(BaseModel):
    """Geneset info schema."""

    id: int  # noqa: A003
    page_views: int
    referers: List[str]
    analyses: List[str]
    resource_id: int
    last_sim: str
    last_ann: str
    jac_started: str
    jac_completed: str


class SimilarGeneset(Geneset):
    """Schema for similar geneset relation."""

    jax_value: float
    gic_value: float


class GenesetRow(BaseModel):
    """Geneset schema for database row."""

    gs_id: int
    usr_id: int
    file_id: int
    gs_name: str
    gs_abbreviation: str
    pub_id: int
    res_id: int
    cur_id: int
    gs_description: str
    sp_id: int
    gs_count: int
    gs_threshold_type: int
    gs_threshold: str
    gs_groups: str
    gs_attribution_old: str
    gs_uri: str
    gs_gene_id_type: int
    gs_created: datetime.date
    admin_flag: str
    gs_updated: datetime.datetime
    gs_status: str
    gsv_qual: str
    _comments_author: str
    _comments_curator: str
    gs_attribution: int
    gs_is_edgelist: bool
