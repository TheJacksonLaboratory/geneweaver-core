"""Project schemas."""

from pydantic import BaseModel


class Project(BaseModel):
    """Project schema."""

    id: int  # noqa: A003
    name: str
    groups: list
    session_id: str
    created: str
    notes: str
    star: str


class ProjectCreate(BaseModel):
    """Project create schema."""

    name: str
    notes: str
