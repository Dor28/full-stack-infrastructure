from datetime import datetime
from typing import List
from pydantic import BaseModel


class AnalysisCreateIn(BaseModel):
    document: str
    patient_id: int


class AnalysisUpdateIn(BaseModel):
    document: str
    patient_id: int


class AnalysisOut(BaseModel):
    id: int
    document: str
    patient_id: int
    created: datetime
    updated: datetime = None


class AnalysisList(BaseModel):
    list: List[AnalysisOut]
