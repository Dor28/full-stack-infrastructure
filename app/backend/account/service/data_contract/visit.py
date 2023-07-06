import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.visit import *


class VisitDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_visit: VisitCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('visit_add', [in_visit.patient_id, in_visit.doctor_id, in_visit.date, in_visit.status])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    visit = cur.fetchone()
                    created_visit = VisitOut(id=visit[0],
                                             patient_id=visit[1],
                                             doctor_id=visit[2],
                                             date=visit[3],
                                             status=visit[4],
                                             created=visit[5],
                                             updated=visit[6])
                    return created_visit

    def update(self, in_id, in_visit: VisitUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('visit_update', [in_id, in_visit.patient_id, in_visit.doctor_id,
                                                  in_visit.date, in_visit.status])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    visit = cur.fetchone()
                    updated_visit = VisitOut(id=visit[0],
                                             patient_id=visit[1],
                                             doctor_id=visit[2],
                                             date=visit[3],
                                             status=visit[4],
                                             created=visit[5],
                                             updated=visit[6])
                    return updated_visit

    def delete(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('visit_delete', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    return True

    def get(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('visit_get', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    visit = cur.fetchone()
                    get_visit = VisitOut(id=visit[0],
                                         patient_id=visit[1],
                                         doctor_id=visit[2],
                                         date=visit[3],
                                         status=visit[4],
                                         created=visit[5],
                                         updated=visit[6])
                    return get_visit

    def get_list(self, id=None, patient_id=None, doctor_id=None, date=None, status=None):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('visit_get_list', [id, patient_id, doctor_id, date, status])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    visit_list = cur.fetchall()
                    get_visit_list = []
                    for visit in visit_list:
                        get_visit_list.append(VisitOut(id=visit[0],
                                                       patient_id=visit[1],
                                                       doctor_id=visit[2],
                                                       date=visit[3],
                                                       status=visit[4],
                                                       created=visit[5],
                                                       updated=visit[6]))

                    return VisitList(list=get_visit_list)
