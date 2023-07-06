from datetime import datetime
from typing import List
from pydantic import BaseModel


class PatientCreateIn(BaseModel):
    first_name: str
    last_name: str
    father_name: str = None
    address: str = None
    phone:str


class PatientUpdateIn(BaseModel):
    first_name: str
    last_name: str
    father_name: str = None
    address: str = None
    phone: str


class PatientOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    father_name: str = None
    address: str = None
    phone: str


class PatientList(BaseModel):
    list: List[PatientOut]
