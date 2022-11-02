from typing import List
from pydantic import BaseModel
from jax.geneweaver.core.schema.stubgenerator import StubGenerator


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    prefs: str
    admin: int
    is_guest: bool
    # groups: List[Group]
    groups: List[str]
    stubgenerators: List[StubGenerator]
