import requests

from models.patientdb import PatientCreateIn, PatientUpdateIn
from exceptions.http_custom_exeption import HttpCustomExceptions
import urllib.parse
from data_contract.user import create_user

from settings import service_base_url


def create_patient(in_patient: PatientCreateIn):

    patient_url = urllib.parse.urljoin(service_base_url, 'patient/create/')
    try:
        patient_resp = requests.post(url=patient_url, json=in_patient.dict())
    except:
        raise HttpCustomExceptions().service_connection_exception()

    if patient_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(patient_resp)
    return patient_resp.json()


def get_patient_list():
    patient_url = urllib.parse.urljoin(service_base_url, 'patient/get_list/')
    try:
        patient_resp = requests.get(url=patient_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if patient_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(patient_resp)
    return patient_resp.json()


def update_patient(id: int, in_patient: PatientUpdateIn):
    patient_url = urllib.parse.urljoin(service_base_url, 'patient/{}/'.format(id))
    try:
        patient_resp = requests.put(url=patient_url, json=in_patient.dict())
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if patient_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(patient_resp)
    return patient_resp.json()


def delete_patient(id: int):
    patient_url = urllib.parse.urljoin(service_base_url, 'patient/{}/'.format(id))
    try:
        patient_resp = requests.delete(url=patient_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if patient_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(patient_resp)
    return patient_resp.json()


def get_patient(id: int):
    patient_url = urllib.parse.urljoin(service_base_url, 'patient/{}/'.format(id))
    try:
        patient_resp = requests.get(url=patient_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if patient_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(patient_resp)
    return patient_resp.json()
