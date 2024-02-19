"""Models needed to work with the legacy API."""

from typing import List, Optional

from geneweaver.core.enum import GenesetAccess, ScoreType
from pydantic import BaseModel, HttpUrl


class AddGenesetByUserPublication(BaseModel):
    """Publication schema for adding genesets by user."""

    pub_abstract: Optional[str]
    pub_authors: Optional[str]
    pub_journal: Optional[str]
    pub_pages: Optional[str]
    pub_pubmed: Optional[str]
    pub_title: Optional[str]
    pub_volume: Optional[str]
    pub_year: Optional[str]


class AddGenesetByUserBase(BaseModel):
    """Base schema for adding genesets by user."""

    gene_identifier: str
    gs_abbreviation: str
    gs_description: str
    gs_name: str
    gs_threshold_type: ScoreType
    permissions: GenesetAccess
    publication: Optional[AddGenesetByUserPublication]
    select_groups: List[str]
    sp_id: str

    class Config:
        """Pydantic config."""

        use_enum_values = True


class AddGenesetByUser(AddGenesetByUserBase):
    """Schema for adding genesets by user."""

    file_text: str


class AddGenesetByUserFile(AddGenesetByUserBase):
    """Schema for adding genesets by user from file."""

    file_url: HttpUrl
