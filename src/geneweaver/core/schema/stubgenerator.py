from pydantic import BaseModel


class StubGenerator(BaseModel):
    id: int
    name: str
    querystring: str
    last_update: str
