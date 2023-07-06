import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.administration import *


class AdministrationDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_administration: AdministrationCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('administration_add',
                                 [in_administration.first_name, in_administration.last_name,
                                  in_administration.father_name,
                                  in_administration.user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    administration = cur.fetchone()
                    created_administration = AdministrationOut(id=administration[0],
                                                               first_name=administration[1],
                                                               last_name=administration[2],
                                                               father_name=administration[3],
                                                               user_id=administration[4],
                                                               created=administration[5],
                                                               updated=administration[6])
                    return created_administration

    def update(self, in_id, in_administration: AdministrationUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('administration_update',
                                 [in_id, in_administration.first_name, in_administration.last_name,
                                  in_administration.father_name, in_administration.user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    administration = cur.fetchone()
                    updated_administration = AdministrationOut(id=administration[0],
                                                               first_name=administration[1],
                                                               last_name=administration[2],
                                                               father_name=administration[3],
                                                               user_id=administration[4],
                                                               created=administration[5],
                                                               updated=administration[6])
                    return updated_administration

    def delete(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('administration_delete', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    return True

    def get(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('administration_get', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    administration = cur.fetchone()
                    get_administration = AdministrationOut(id=administration[0],
                                                 first_name=administration[1],
                                                 last_name=administration[2],
                                                 father_name=administration[3],
                                                 user_id=administration[4],
                                                 created=administration[5],
                                                 updated=administration[6])
                    return get_administration

    def get_list(self, id=None, first_name=None, last_name=None, father_name=None, user_id=None):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('administration_get_list', [id, first_name, last_name, father_name, user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    administration_list = cur.fetchall()
                    get_administration_list = []
                    for administration in administration_list:
                        get_administration_list.append(AdministrationOut(id=administration[0],
                                                               first_name=administration[1],
                                                               last_name=administration[2],
                                                               father_name=administration[3],
                                                               user_id=administration[4],
                                                               created=administration[5],
                                                               updated=administration[6]))

                    return AdministrationList(list=get_administration_list)
