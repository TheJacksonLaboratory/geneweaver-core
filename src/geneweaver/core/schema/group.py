"""Group schemas."""

import datetime
from typing import List

from geneweaver.core.schema.stubgenerator import StubGenerator
from pydantic import BaseModel


class Group(BaseModel):
    """Group schema."""

    id: int  # noqa: A003
    name: str
    private: bool
    created: datetime.date
    stubgenerators: List[StubGenerator]


class UserAdminGroup(BaseModel):
    """User admin group schema."""

    name: str
    public: bool
    created: datetime.date
