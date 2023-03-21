import datetime
from typing import List, Optional
from pydantic import BaseModel

from geneweaver.core.schema.stubgenerator import StubGenerator
from geneweaver.core.enum import AdminLevel


class UserRequiredFields(BaseModel):
    id: int
    email: str
    prefs: str = "{}"
    is_guest: bool = False


class User(UserRequiredFields):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    admin: AdminLevel = AdminLevel.NORMAL_USER
    last_seen: Optional[datetime.datetime] = None
    create: Optional[datetime.date] = None
    ip_address: Optional[str] = None
    api_key: Optional[str] = None
    sso_id: Optional[str] = None


class UserFull(User):
    groups: List[str]
    stubgenerators: List[StubGenerator]
