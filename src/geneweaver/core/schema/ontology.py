from typing import List
from pydantic import BaseModel


class Ontology(BaseModel):
    ontology_id: int
    reference_id: int
    name: str
    description: str
    children: List['Ontology']
    parents: List['Ontology']
    ontdb_id: int
    ro_ont_id: int


class OntologyDB(BaseModel):
    ontology_db_id: int
    name: str
    prefix: str
    ncbo_id: str
    date: str
    linkout_url: str
    ncbo_vid: str
