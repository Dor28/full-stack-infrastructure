import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.patient import *


class PatientDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_patient: PatientCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('patient_add', [in_patient.first_name, in_patient.last_name, in_patient.father_name,
                                                 in_patient.address, in_patient.phone])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    patient = cur.fetchone()
                    created_patient = PatientOut(id=patient[0],
                                                 first_name=patient[1],
                                                 last_name=patient[2],
                                                 father_name=patient[3],
                                                 address=patient[4],
                                                 phone=patient[5],
                                                 created=patient[6],
                                                 updated=patient[7]
                                                 )
                    return created_patient

    def update(self, in_id, in_patient: PatientUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('patient_update', [in_id, in_patient.first_name, in_patient.last_name,
                                                    in_patient.father_name, in_patient.address, in_patient.phone])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    patient = cur.fetchone()
                    updated_patient = PatientOut(id=patient[0],
                                                 first_name=patient[1],
                                                 last_name=patient[2],
                                                 father_name=patient[3],
                                                 address=patient[4],
                                                 phone=patient[5],
                                                 created=patient[6],
                                                 updated=patient[7]
                                                 )
                    return updated_patient

    def delete(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('patient_delete', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    return True

    def get(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('patient_get', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    patient = cur.fetchone()
                    get_patient = PatientOut(id=patient[0],
                                             first_name=patient[1],
                                             last_name=patient[2],
                                             father_name=patient[3],
                                             address=patient[4],
                                             phone=patient[5],
                                             created=patient[6],
                                             updated=patient[7])
                    return get_patient

    def get_list(self, id=None, first_name=None, last_name=None, father_name=None, address=None, phone=None):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('patient_get_list', [id, first_name, last_name, father_name, address, phone])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    patient_list = cur.fetchall()
                    get_patient_list = []
                    for patient in patient_list:
                        get_patient_list.append(PatientOut(id=patient[0],
                                                           first_name=patient[1],
                                                           last_name=patient[2],
                                                           father_name=patient[3],
                                                           address=patient[4],
                                                           phone=patient[5],
                                                           created=patient[6],
                                                           updated=patient[7]))

                    return PatientList(list=get_patient_list)
