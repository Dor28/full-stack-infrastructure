from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.doctordb import *
from settings import error_responses
import requests
from data_contract.doctor import create_doctor, get_doctor_list, update_doctor, delete_doctor, get_doctor

api_router = APIRouter()


@api_router.post("/create/", response_model=DoctorDetailOut, responses=error_responses)
def doctor_create(in_doctor: DoctorCreateIn):
    out_doctor = create_doctor(in_doctor)

    return JSONResponse(content=out_doctor)


@api_router.get("/list/", response_model=DoctorList, responses=error_responses)
def doctor_list():
    out_doctor = get_doctor_list()
    return out_doctor


@api_router.put("/{id}/", response_model=DoctorDetailOut, responses=error_responses)
def doctor_update(id: int, in_patient: DoctorUpdateIn):
    return update_doctor(id, in_patient)


@api_router.delete("/{id}/", responses=error_responses)
def doctor_delete(id: int):
    return delete_doctor(id)


@api_router.get("/{id}/", response_model=DoctorDetailOut, responses=error_responses)
def doctor_get(id: int):
    return get_doctor(id)
