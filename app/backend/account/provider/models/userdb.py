from datetime import datetime, timedelta
from typing import List, Optional

from pydantic import BaseModel
import bcrypt


class UserCreateIn(BaseModel):
    username: str
    password: str

    def set_password(self, psw):
        hashed_psw = bcrypt.hashpw(psw.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_psw.decode()

    def hash_password(self):
        hashed_psw = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_psw.decode()

    def check_password(self, psw):
        return bcrypt.checkpw(self.password.encode('utf-8'), psw.encode('utf-8'))


class UserUpdateIn(BaseModel):
    username: str = None
    password: str = None


class UserShortOut(BaseModel):
    id: int
    username: str


class UserDetailOut(BaseModel):
    id: int
    username: str
    password: str
    created: datetime
    updated: datetime = None


class UserList(BaseModel):
    list: List[UserDetailOut]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
