"""Publication schemas."""

from typing import Optional

from pydantic import BaseModel


class PublicationInfo(BaseModel):
    """Publication upload schema (no ID)."""

    pubmed_id: int
    authors: str
    title: str
    abstract: str = ""
    journal: Optional[str] = None
    volume: Optional[str] = None
    pages: Optional[str] = None
    month: Optional[str] = None
    year: Optional[int] = None


class Publication(PublicationInfo):
    """Publication schema (with ID)."""

    id: int  # noqa: A003
