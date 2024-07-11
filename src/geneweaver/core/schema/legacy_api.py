"""Models needed to work with the legacy API."""

from typing import List, Optional

from geneweaver.core.enum import GenesetAccess, ScoreType
from pydantic import BaseModel, ConfigDict, HttpUrl


class AddGenesetByUserPublication(BaseModel):
    """Publication schema for adding genesets by user."""

    pub_abstract: Optional[str] = None
    pub_authors: Optional[str] = None
    pub_journal: Optional[str] = None
    pub_pages: Optional[str] = None
    pub_pubmed: Optional[str] = None
    pub_title: Optional[str] = None
    pub_volume: Optional[str] = None
    pub_year: Optional[str] = None


class AddGenesetByUserBase(BaseModel):
    """Base schema for adding genesets by user."""

    gene_identifier: str
    gs_abbreviation: str
    gs_description: str
    gs_name: str
    gs_threshold_type: ScoreType
    permissions: GenesetAccess
    publication: Optional[AddGenesetByUserPublication] = None
    select_groups: List[str]
    sp_id: str
    model_config = ConfigDict(use_enum_values=True)


class AddGenesetByUser(AddGenesetByUserBase):
    """Schema for adding genesets by user."""

    file_text: str


class AddGenesetByUserFile(AddGenesetByUserBase):
    """Schema for adding genesets by user from file."""

    file_url: HttpUrl
