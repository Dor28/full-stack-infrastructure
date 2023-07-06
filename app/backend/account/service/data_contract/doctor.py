import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.doctor import *


class DoctorDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_doctor: DoctorCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('doctor_add',
                                 [in_doctor.first_name, in_doctor.last_name,
                                  in_doctor.father_name,
                                  in_doctor.user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    administration = cur.fetchone()
                    created_doctor = DoctorOut(id=administration[0],
                                               first_name=administration[1],
                                               last_name=administration[2],
                                               father_name=administration[3],
                                               user_id=administration[4],
                                               created=administration[5],
                                               updated=administration[6])
                    return created_doctor

    def update(self, in_id, in_doctor: DoctorUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('doctor_update',
                                 [in_id, in_doctor.first_name, in_doctor.last_name,
                                  in_doctor.father_name, in_doctor.user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    doctor = cur.fetchone()
                    updated_doctor = DoctorOut(id=doctor[0],
                                               first_name=doctor[1],
                                               last_name=doctor[2],
                                               father_name=doctor[3],
                                               user_id=doctor[4],
                                               created=doctor[5],
                                               updated=doctor[6])
                    return updated_doctor

    def delete(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('doctor_delete', [id])
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
                    cur.callproc('doctor_get_list', [id, first_name, last_name, father_name, user_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    doctor_list = cur.fetchall()
                    get_doctor_list = []
                    for doctor in doctor_list:
                        get_doctor_list.append(DoctorOut(id=doctor[0],
                                                         first_name=doctor[1],
                                                         last_name=doctor[2],
                                                         father_name=doctor[3],
                                                         user_id=doctor[4],
                                                         created=doctor[5],
                                                         updated=doctor[6]))

                    return DoctorList(list=get_doctor_list)
