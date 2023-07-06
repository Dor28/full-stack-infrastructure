import requests

from models.administrationdb import AdministrationCreateIn, AdministrationUpdateIn
from exceptions.http_custom_exeption import HttpCustomExceptions
import urllib.parse
from data_contract.user import create_user

from settings import service_base_url


def create_administration(in_administration: AdministrationCreateIn):
    user_resp = create_user(in_administration.user)

    administration_req = in_administration.dict(exclude={'user'})

    administration_req.update({'user_id': user_resp.json()['id']})

    administration_url = urllib.parse.urljoin(service_base_url, 'administration/create/')
    try:
        administration_resp = requests.post(url=administration_url, json=administration_req)
    except:
        raise HttpCustomExceptions().service_connection_exception()

    if user_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(administration_resp)

    return administration_resp.json()


def get_administrator_list():
    administrator_url = urllib.parse.urljoin(service_base_url, 'administration/get_list/')
    try:
        administrator_resp = requests.get(url=administrator_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if administrator_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(administrator_resp)
    return administrator_resp.json()


def update_administration(id: int, in_patient: AdministrationUpdateIn):
    administration_url = urllib.parse.urljoin(service_base_url, 'administration/{}/'.format(id))
    try:
        administration_resp = requests.put(url=administration_url, json=in_patient.dict())
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if administration_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(administration_resp)
    return administration_resp.json()


def delete_administration(id: int):
    administration_url = urllib.parse.urljoin(service_base_url, 'administration/{}/'.format(id))
    try:
        administration_resp = requests.delete(url=administration_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if administration_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(administration_resp)
    return administration_resp.json()


def get_administration(id: int):
    administration_url = urllib.parse.urljoin(service_base_url, 'administration/{}/'.format(id))
    try:
        administration_resp = requests.get(url=administration_url)
    except:
        raise HttpCustomExceptions().service_connection_exception()
    if administration_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(administration_resp)
    return administration_resp.json()
