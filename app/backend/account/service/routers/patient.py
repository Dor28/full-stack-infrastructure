from fastapi import APIRouter

from data_contract.patient import *
from settings import error_responses

api_router = APIRouter()

patient_contract = PatientDB()


@api_router.post("/create/", response_model=PatientOut, responses=error_responses)
def patient_create(in_patient: PatientCreateIn):
    return patient_contract.add(in_patient)


@api_router.put("/{id}", response_model=PatientOut, responses=error_responses)
def patient_update(id: int, in_patient: PatientUpdateIn):
    return patient_contract.update(id, in_patient)


@api_router.delete("/{id}", responses=error_responses)
def patient_delete(id: int):
    return patient_contract.delete(id)


@api_router.get("/{id}", response_model=PatientOut, responses=error_responses)
def patient_get(id: int):
    return patient_contract.get(id)


@api_router.get("/get_list/", response_model=PatientList, responses=error_responses)
def patient_get_list(id: int = None, first_name: str = None, last_name: str = None, father_name: str = None,
                     address: str = None, phone: str = None):
    return patient_contract.get_list(id, first_name, last_name, father_name, address, phone)
