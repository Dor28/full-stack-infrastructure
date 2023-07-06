from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class UserCreateIn(BaseModel):
    username: str
    password: str


class UserUpdateIn(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None


class UserOut(BaseModel):
    id: int
    username: str
    password: str
    created: datetime
    updated: Optional[datetime] = None


class UserList(BaseModel):
    list: List[UserOut]
