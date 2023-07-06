from fastapi import APIRouter

from data_contract.visit import *
from settings import error_responses

api_router = APIRouter()

visit_contract = VisitDB()


@api_router.post("/create/", response_model=VisitOut, responses=error_responses)
def visit_create(in_visit: VisitCreateIn):
    return visit_contract.add(in_visit)


@api_router.put("/{id}", response_model=VisitOut, responses=error_responses)
def visit_update(id: int, in_visit: VisitUpdateIn):
    return visit_contract.update(id, in_visit)


@api_router.delete("/{id}", responses=error_responses)
def visit_delete(id: int):
    return visit_contract.delete(id)


@api_router.get("/{id}", response_model=VisitOut, responses=error_responses)
def visit_get(id: int):
    return visit_contract.get(id)


@api_router.get("/get_list/", response_model=VisitList, responses=error_responses)
def visit_get_list(id: int = None, patient_id: int =None, doctor_id: int =None, date: datetime=None, status:str=None):
    return visit_contract.get_list(id, patient_id, doctor_id, date, status)
