from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.receptiondb import *
from settings import error_responses
import requests
from data_contract.reception import create_reception, get_reception_list, update_reception, get_reception, delete_reception

api_router = APIRouter()


@api_router.post("/create/", response_model=ReceptionShortOut, responses=error_responses)
def reception_create(in_reception: ReceptionCreateIn):
    out_reception = create_reception(in_reception)

    return out_reception


@api_router.get("/list/", response_model=ReceptionList, responses=error_responses)
def reception_list():
    out_reception = get_reception_list()
    return out_reception


@api_router.put("/{id}/", response_model=ReceptionDetailOut, responses=error_responses)
def reception_update(id: int, in_patient: ReceptionUpdateIn):
    return update_reception(id, in_patient)


@api_router.delete("/{id}/", responses=error_responses)
def reception_delete(id: int):
    return delete_reception(id)


@api_router.get("/{id}/", response_model=ReceptionDetailOut, responses=error_responses)
def reception_get(id: int):
    return get_reception(id)
