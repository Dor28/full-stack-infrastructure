import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.reception import *


class ReceptionDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_reception: ReceptionCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('reception_add', [in_reception.first_name, in_reception.last_name, in_reception.father_name,
                                                 in_reception.user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    reception = cur.fetchone()
                    created_reception = ReceptionOut(id=reception[0],
                                                      first_name=reception[1],
                                                      last_name=reception[2],
                                                      father_name=reception[3],
                                                      user_id=reception[4],
                                                     created=reception[5],
                                                     updated=reception[6])
                    return created_reception

    def update(self, in_id, in_reception: ReceptionUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('reception_update', [in_id, in_reception.first_name, in_reception.last_name,
                                                    in_reception.father_name, in_reception.user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    reception = cur.fetchone()
                    updated_reception = ReceptionOut(id=reception[0],
                                                      first_name=reception[1],
                                                      last_name=reception[2],
                                                      father_name=reception[3],
                                                      user_id=reception[4],
                                                     created=reception[5],
                                                     updated=reception[6])
                    return updated_reception

    def delete(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('reception_delete', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    return True

    def get(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('reception_get', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    reception = cur.fetchone()
                    get_reception = ReceptionOut(id=reception[0],
                                                   first_name=reception[1],
                                                   last_name=reception[2],
                                                   father_name=reception[3],
                                                   user_id=reception[4],
                                                   created=reception[5],
                                                   updated=reception[6])
                    return get_reception

    def get_list(self, id=None, first_name=None, last_name=None, father_name=None, user_id=None):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('reception_get_list', [id, first_name, last_name, father_name, user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    reception_list = cur.fetchall()
                    get_reception_list = []
                    for reception in reception_list:
                        get_reception_list.append(ReceptionOut(id=reception[0],
                                                   first_name=reception[1],
                                                   last_name=reception[2],
                                                   father_name=reception[3],
                                                   user_id=reception[4],
                                                   created=reception[5],
                                                   updated=reception[6]))

                    return ReceptionList(list=get_reception_list)
