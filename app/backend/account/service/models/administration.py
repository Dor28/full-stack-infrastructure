from datetime import datetime
from typing import List
from pydantic import BaseModel


class AdministrationCreateIn(BaseModel):
    first_name: str
    last_name: str
    father_name: str = None
    user_id: int


class AdministrationUpdateIn(BaseModel):
    first_name: str = None
    last_name: str = None
    father_name: str = None
    user_id: int = None


class AdministrationOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    father_name: str = None
    user_id: int
    created: datetime
    updated: datetime = None


class AdministrationList(BaseModel):
    list: List[AdministrationOut]
