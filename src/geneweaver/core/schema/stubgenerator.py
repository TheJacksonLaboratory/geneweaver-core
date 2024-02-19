"""Stub generator schemas."""

from pydantic import BaseModel


class StubGenerator(BaseModel):
    """Stub generator schema."""

    id: int  # noqa: A003
    name: str
    querystring: str
    last_update: str
