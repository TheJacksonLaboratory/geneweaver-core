"""User related schemas."""

import datetime
from typing import List, Optional

from geneweaver.core.enum import AdminLevelInt
from geneweaver.core.schema.stubgenerator import StubGenerator
from pydantic import BaseModel


class UserRequiredFields(BaseModel):
    """User schema for required fields."""

    id: int  # noqa: A003
    email: str
    prefs: str = "{}"
    is_guest: bool = False


class User(UserRequiredFields):
    """User schema."""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    admin: AdminLevelInt = AdminLevelInt.NORMAL_USER
    last_seen: Optional[datetime.datetime] = None
    create: Optional[datetime.date] = None
    ip_address: Optional[str] = None
    api_key: Optional[str] = None
    sso_id: Optional[str] = None


class UserFull(User):
    """User schema with full information."""

    groups: List[str]
    stubgenerators: List[StubGenerator]
