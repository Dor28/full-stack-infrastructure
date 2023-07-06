from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt, JWTError
import requests
from models.userdb import *
# to get a string like this run:
# openssl rand -hex 32
from starlette import status
import urllib.parse
from settings import SECRET_KEY, ALGORITHM
from settings import service_base_url
from exceptions.http_custom_exeption import HttpCustomExceptions

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/user/token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    get_user_url = urllib.parse.urljoin(service_base_url, 'user/get_list/')
    try:
        user_resp = requests.get(get_user_url, params={'username': username})
    except:
        raise HttpCustomExceptions().service_connection_exception()

    if not user_resp.ok:
        raise HttpCustomExceptions().service_error(user_resp)

    if user_resp.json().get('list'):
        return UserDetailOut(**user_resp.json()['list'][-1])


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: UserDetailOut = Depends(get_current_user)):
    return current_user


def create_user(user: UserCreateIn):
    user.set_password(user.password)
    user_url = urllib.parse.urljoin(service_base_url, 'user/create/')
    try:
        user_resp = requests.post(user_url, json=user.dict())
    except:
        raise HttpCustomExceptions().service_connection_exception()

    if user_resp.status_code != 200:
        raise HttpCustomExceptions().service_error(user_resp)

    return user_resp
