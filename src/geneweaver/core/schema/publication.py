"""Publication schemas."""
from pydantic import BaseModel


class PublicationUpload(BaseModel):
    """Publication upload schema (no ID)."""

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
    """Publication schema (with ID)."""

    id: int  # noqa: A003
