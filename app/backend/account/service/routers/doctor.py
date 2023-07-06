from fastapi import APIRouter

from data_contract.doctor import *
from settings import error_responses

api_router = APIRouter()

doctor_contract = DoctorDB()


@api_router.post("/create/", response_model=DoctorOut, responses=error_responses)
def doctor_create(in_doctor: DoctorCreateIn):
    return doctor_contract.add(in_doctor)


@api_router.put("/{id}", response_model=DoctorOut, responses=error_responses)
def doctor_update(id: int, in_doctor: DoctorUpdateIn):
    return doctor_contract.update(id, in_doctor)


@api_router.delete("/{id}", responses=error_responses)
def doctor_delete(id: int):
    return doctor_contract.delete(id)


@api_router.get("/{id}", response_model=DoctorOut, responses=error_responses)
def doctor_get(id: int):
    return doctor_contract.get(id)


@api_router.get("/get_list/", response_model=DoctorList, responses=error_responses)
def doctor_get_list(id: int = None, first_name: str = None, last_name: str = None, father_name: str = None,
                       user_id: int = None):
    return doctor_contract.get_list(id, first_name, last_name, father_name, user_id)
