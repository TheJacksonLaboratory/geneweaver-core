"""Publication schemas."""

from typing import Optional

from pydantic import BaseModel


class PublicationInfo(BaseModel):
    """Publication upload schema (no ID)."""

    authors: str
    title: str
    abstract: str
    journal: Optional[str] = None
    volume: Optional[str] = None
    pages: str
    month: str
    year: int
    pubmed_id: int


class Publication(PublicationInfo):
    """Publication schema (with ID)."""

    id: int  # noqa: A003
