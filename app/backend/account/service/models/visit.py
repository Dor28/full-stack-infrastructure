from datetime import datetime
from typing import List
from pydantic import BaseModel


class VisitCreateIn(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime
    status: str


class VisitUpdateIn(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime = None
    status: str = None


class VisitOut(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: datetime
    status: str
    created: datetime
    updated: datetime = None


class VisitList(BaseModel):
    list: List[VisitOut]
