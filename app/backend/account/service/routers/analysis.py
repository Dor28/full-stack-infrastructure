from fastapi import APIRouter

from data_contract.analysis import *
from settings import error_responses

api_router = APIRouter()

analysis_contract = AnalysisDB()


@api_router.post("/create/", response_model=AnalysisOut, responses=error_responses)
def analysis_create(in_analysis: AnalysisCreateIn):
    return analysis_contract.add(in_analysis)


@api_router.put("/{id}", response_model=AnalysisOut, responses=error_responses)
def analysis_update(id: int, in_analysis: AnalysisUpdateIn):
    return analysis_contract.update(id, in_analysis)


@api_router.delete("/{id}", responses=error_responses)
def analysis_delete(id: int):
    return analysis_contract.delete(id)


@api_router.get("/{id}", response_model=AnalysisOut, responses=error_responses)
def analysis_get(id: int):
    return analysis_contract.get(id)


@api_router.get("/get_list/", response_model=AnalysisList, responses=error_responses)
def analysis_get_list(id: int = None, document: str = None, patient_id: int = None):
    return analysis_contract.get_list(id, document, patient_id)
