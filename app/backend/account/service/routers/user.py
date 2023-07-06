from fastapi import APIRouter

from settings import error_responses
from data_contract.user import *

api_router = APIRouter()

user_contract = UserDB()


@api_router.post("/create/", response_model=UserOut, responses=error_responses)
def user_create(in_account: UserCreateIn):
    return user_contract.add(in_account)


@api_router.put("/{id}", response_model=UserOut, responses=error_responses)
def account_update(id: int, in_user: UserUpdateIn):
    return user_contract.update(id, in_user)


@api_router.delete("/{id}", responses=error_responses)
def account_delete(id: int):
    return user_contract.delete(id)


@api_router.get("/{id}", response_model=UserOut, responses=error_responses)
def account_get(id: int):
    return user_contract.get(id)


@api_router.get("/get_list/", response_model=UserList, responses=error_responses)
def account_get_list(id: int = None, username: str = None):
    return user_contract.get_list(id, username)
