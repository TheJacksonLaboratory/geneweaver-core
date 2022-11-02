from pydantic import BaseModel


class Publication(BaseModel):
    id: int
    authors: str
    title: str
    abstract: str
    journal: str
    volume: str
    pages: str
    month: str
    year: int
    pubmed: int
