"""Schemas for API Responses."""

from typing import List, Optional

from pydantic import AnyUrl, BaseModel


class PagingLinks(BaseModel):
    """Schema for holding paging links."""

    first: Optional[AnyUrl] = None
    previous: Optional[AnyUrl] = None
    next: Optional[AnyUrl] = None
    last: Optional[AnyUrl] = None


class Paging(BaseModel):
    """Schema for paging information."""

    page: Optional[int] = None
    items: Optional[int] = None
    total_pages: Optional[int] = None
    total_items: Optional[int] = None
    links: Optional[PagingLinks] = None


class CollectionResponse(BaseModel):
    """Schema for API responses with collections."""

    data: List
    paging: Optional[Paging] = None
