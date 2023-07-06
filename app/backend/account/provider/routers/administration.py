from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.administrationdb import *
from settings import error_responses
import requests
from data_contract.administration import create_administration, get_administrator_list, update_administration, \
    delete_administration, get_administration

api_router = APIRouter()


@api_router.post("/create/", response_model=AdministrationDetailOut, responses=error_responses)
def administration_create(in_administration: AdministrationCreateIn):
    out_administration = create_administration(in_administration)

    return out_administration


@api_router.get("/list/", response_model=AdministrationList, responses=error_responses)
def administration_list():
    out_administrator = get_administrator_list()
    return out_administrator


@api_router.put("/{id}/", response_model=AdministrationDetailOut, responses=error_responses)
def administration_update(id: int, in_patient: AdministrationUpdateIn):
    return update_administration(id, in_patient)


@api_router.delete("/{id}/", responses=error_responses)
def administration_delete(id: int):
    return delete_administration(id)


@api_router.get("/{id}/", response_model=AdministrationDetailOut, responses=error_responses)
def administration_get(id: int):
    return get_administration(id)
