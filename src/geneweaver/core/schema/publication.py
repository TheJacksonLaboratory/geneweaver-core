from pydantic import BaseModel


class PublicationUpload(BaseModel):
    authors: str
    title: str
    abstract: str
    journal: str
    volume: str
    pages: str
    month: str
    year: int
    pubmed: int


class Publication(PublicationUpload):
    id: int
