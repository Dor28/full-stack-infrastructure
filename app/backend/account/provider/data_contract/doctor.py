import requests

from models.doctordb import DoctorCreateIn, DoctorUpdateIn
from exceptions.http_custom_exeption import HttpCustomExceptions
import urllib.parse
from data_contract.user import create_user

from settings import service_base_url


def create_doctor(in_doctor: DoctorCreateIn):
    user_resp = create_user(in_doctor.user)

    doctor_req = in_doctor.dict(exclude={'user'})

    doctor_req.update({'user_id': user_resp.json()['id']})

    doctor_url = urllib.parse.urljoin(service_base_url, 'doctor/create/')
    try:
        doctor_resp = requests.post(url=doctor_url, json=doctor_req)
    except:
        raise HttpCustomExceptions().service_connection_exception()

    if user_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(doctor_resp)

    return doctor_resp.json()


def get_doctor_list():
    doctor_url = urllib.parse.urljoin(service_base_url, 'doctor/get_list/')
    try:
        doctor_resp = requests.get(url=doctor_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if doctor_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(doctor_resp)
    return doctor_resp.json()


def update_doctor(id: int, in_patient: DoctorUpdateIn):
    doctor_url = urllib.parse.urljoin(service_base_url, 'doctor/{}/'.format(id))
    try:
        doctor_resp = requests.put(url=doctor_url, json=in_patient.dict())
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if doctor_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(doctor_resp)
    return doctor_resp.json()


def delete_doctor(id: int):
    doctor_url = urllib.parse.urljoin(service_base_url, 'doctor/{}/'.format(id))
    try:
        doctor_resp = requests.delete(url=doctor_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if doctor_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(doctor_resp)
    return doctor_resp.json()


def get_doctor(id: int):
    doctor_url = urllib.parse.urljoin(service_base_url, 'doctor/{}/'.format(id))
    try:
        doctor_resp = requests.get(url=doctor_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if doctor_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(doctor_resp)
    return doctor_resp.json()
