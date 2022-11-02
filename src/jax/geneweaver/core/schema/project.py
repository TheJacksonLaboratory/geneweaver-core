from pydantic import BaseModel


class Project(BaseModel):
    id: int
    name: str
    groups: list
    session_id: str
    created: str
    notes: str
    star: str


class ProjectCreate(BaseModel):
    name: str
    notes: str
