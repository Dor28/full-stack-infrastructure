from fastapi import APIRouter

from data_contract.reception import *
from settings import error_responses

api_router = APIRouter()

reception_contract = ReceptionDB()

@api_router.post("/create/", response_model=ReceptionOut, responses=error_responses)
def reception_create(in_reception: ReceptionCreateIn):
    return reception_contract.add(in_reception)


@api_router.put("/{id}", response_model=ReceptionOut, responses=error_responses)
def reception_update(id: int, in_reception: ReceptionUpdateIn):
    return reception_contract.update(id, in_reception)


@api_router.delete("/{id}", responses=error_responses)
def reception_delete(id: int):
    return reception_contract.delete(id)


@api_router.get("/{id}", response_model=ReceptionOut, responses=error_responses)
def reception_get(id: int):
    return reception_contract.get(id)


@api_router.get("/get_list/", response_model=ReceptionList, responses=error_responses)
def reception_get_list(id: int = None, first_name: str = None, last_name: str = None, father_name: str = None,
                     user_id: int = None):
    return reception_contract.get_list(id, first_name, last_name, father_name, user_id)
