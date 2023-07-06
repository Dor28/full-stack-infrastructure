import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.user import *


class UserDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_user: UserCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('user_add', [in_user.username, in_user.password])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    user = cur.fetchone()
                    created_user = UserOut(id=user[0], username=user[1], password=user[2], created=user[3],
                                           updated=user[4])
                    return created_user

    def update(self, in_id, in_user: UserUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('user_update', [in_id, in_user.username, in_user.password])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    user = cur.fetchone()
                    updated_user = UserOut(id=user[0], username=user[1], password=user[2], created=user[3],
                                           updated=user[4])
                    return updated_user

    def delete(self, in_id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('user_delete', [in_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    return True

    def get(self, in_id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('user_get', [in_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    user = cur.fetchone()
                    get_user = UserOut(id=user[0], username=user[1], password=user[2], created=user[3],
                                                updated=user[4])
                    return get_user

    def get_list(self, in_id=None, username=None):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('user_get_list', [in_id, username])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:

                    user_list = cur.fetchall()
                    get_user_list = []
                    for user in user_list:
                        get_user_list.append(
                            UserOut(id=user[0], username=user[1], password=user[2], created=user[3],
                                             updated=user[4]))
                    return UserList(list=get_user_list)
