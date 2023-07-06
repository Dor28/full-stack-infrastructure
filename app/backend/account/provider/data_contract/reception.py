import requests

from models.receptiondb import ReceptionCreateIn, ReceptionUpdateIn
from exceptions.http_custom_exeption import HttpCustomExceptions
import urllib.parse
from data_contract.user import create_user

from settings import service_base_url


def create_reception(in_reception: ReceptionCreateIn):
    user_resp = create_user(in_reception.user)

    reception_req = in_reception.dict(exclude={'user'})

    reception_req.update({'user_id': user_resp.json()['id']})

    reception_url = urllib.parse.urljoin(service_base_url, 'reception/create/')
    try:
        reception_resp = requests.post(url=reception_url, json=reception_req)
    except:
        raise HttpCustomExceptions().service_connection_exception()

    if reception_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(reception_resp)
    return reception_resp.json()


def get_reception_list():
    reception_url = urllib.parse.urljoin(service_base_url, 'reception/get_list/')
    try:
        reception_resp = requests.get(url=reception_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if reception_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(reception_resp)
    return reception_resp.json()


def update_reception(id: int, in_patient: ReceptionUpdateIn):
    reception_url = urllib.parse.urljoin(service_base_url, 'reception/{}/'.format(id))
    try:
        reception_resp = requests.put(url=reception_url, json=in_patient.dict())
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if reception_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(reception_resp)
    return reception_resp.json()


def delete_reception(id: int):
    reception_url = urllib.parse.urljoin(service_base_url, 'reception/{}/'.format(id))
    try:
        reception_resp = requests.delete(url=reception_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if reception_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(reception_resp)
    return reception_resp.json()


def get_reception(id: int):
    reception_url = urllib.parse.urljoin(service_base_url, 'reception/{}/'.format(id))
    try:
        reception_resp = requests.get(url=reception_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if reception_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(reception_resp)
    return reception_resp.json()
