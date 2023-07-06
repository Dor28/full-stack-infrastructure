from datetime import datetime
from typing import List

from pydantic import BaseModel

from models.userdb import UserCreateIn


class ReceptionCreateIn(BaseModel):
    first_name: str
    last_name: str
    father_name: str = None
    user: UserCreateIn


class ReceptionUpdateIn(BaseModel):
    first_name: str = None
    last_name: str = None
    father_name: str = None
    user_id: int = None


class ReceptionShortOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    father_name: str = None
    user_id: int


class ReceptionDetailOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    father_name: str = None
    user_id: int
    created: datetime
    updated: datetime = None


class ReceptionList(BaseModel):
    list: List[ReceptionDetailOut]



