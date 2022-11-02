import datetime
from typing import List
from pydantic import BaseModel

from jax.geneweaver.core.schema.stubgenerator import StubGenerator


class Group(BaseModel):
    id: int
    name: str
    private: bool
    created: datetime.date
    stubgenerators: List[StubGenerator]


class UserAdminGroup(BaseModel):
    name: str
    public: bool
    created: datetime.date
