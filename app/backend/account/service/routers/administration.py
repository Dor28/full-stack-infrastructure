from fastapi import APIRouter

from data_contract.administration import *
from settings import error_responses

api_router = APIRouter()

administration_contract = AdministrationDB()


@api_router.post("/create/", response_model=AdministrationOut, responses=error_responses)
def administration_create(in_administration: AdministrationCreateIn):
    return administration_contract.add(in_administration)


@api_router.put("/{id}", response_model=AdministrationOut, responses=error_responses)
def administration_update(id: int, in_administration: AdministrationUpdateIn):
    return administration_contract.update(id, in_administration)


@api_router.delete("/{id}", responses=error_responses)
def administration_delete(id: int):
    return administration_contract.delete(id)


@api_router.get("/{id}", response_model=AdministrationOut, responses=error_responses)
def administration_get(id: int):
    return administration_contract.get(id)


@api_router.get("/get_list/", response_model=AdministrationList, responses=error_responses)
def administration_get_list(id: int = None, first_name: str = None, last_name: str = None, father_name: str = None,
                       user_id: int = None):
    return administration_contract.get_list(id, first_name, last_name, father_name, user_id)
