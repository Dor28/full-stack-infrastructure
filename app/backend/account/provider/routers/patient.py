from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.patientdb import *
from settings import error_responses
import requests
from data_contract.patient import *

api_router = APIRouter()


@api_router.post("/create/", response_model=PatientOut, responses=error_responses)
def patient_create(in_patient: PatientCreateIn):
    out_patient = create_patient(in_patient)

    return out_patient


@api_router.get("/list/", response_model=PatientList, responses=error_responses)
def patient_list():
    out_patient = get_patient_list()
    return out_patient


@api_router.put("/{id}/", response_model=PatientOut, responses=error_responses)
def patient_update(id: int, in_patient: PatientUpdateIn):
    return update_patient(id, in_patient)


@api_router.delete("/{id}/", responses=error_responses)
def patient_delete(id: int):
    return delete_patient(id)


@api_router.get("/{id}/", response_model=PatientOut, responses=error_responses)
def patient_get(id: int):
    return get_patient(id)
