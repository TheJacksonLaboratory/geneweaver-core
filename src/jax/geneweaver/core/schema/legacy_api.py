from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from jax.geneweaver.core.enum import GenesetAccess, GenesetScoreType


class AddGenesetByUserPublication(BaseModel):
    pub_abstract: Optional[str]
    pub_authors: Optional[str]
    pub_journal: Optional[str]
    pub_pages: Optional[str]
    pub_pubmed: Optional[str]
    pub_title: Optional[str]
    pub_volume: Optional[str]
    pub_year: Optional[str]


class AddGenesetByUserBase(BaseModel):
    gene_identifier: str
    gs_abbreviation: str
    gs_description: str
    gs_name: str
    gs_threshold_type: GenesetScoreType
    permissions: GenesetAccess
    publication: Optional[AddGenesetByUserPublication]
    select_groups: List[str]
    sp_id: str

    class Config:
        use_enum_values = True


class AddGenesetByUser(AddGenesetByUserBase):
    file_text: str


class AddGenesetByUserFile(AddGenesetByUserBase):
    file_url: HttpUrl

