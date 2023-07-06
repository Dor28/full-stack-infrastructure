import psycopg2
from fastapi import HTTPException
from db_manager import get_db
from models.analysis import *


class AnalysisDB:

    def __init__(self):
        self.conn = get_db()

    def add(self, in_analysis: AnalysisCreateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('analysis_add', [in_analysis.document, in_analysis.patient_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    analysis = cur.fetchone()
                    created_analysis = AnalysisOut(id=analysis[0],
                                                   document=analysis[1],
                                                   patient_id=analysis[2],
                                                   created=analysis[3],
                                                   updated=analysis[4])
                    return created_analysis

    def update(self, in_id, in_analysis: AnalysisUpdateIn):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('analysis_update', [in_id, in_analysis.document, in_analysis.patient_id, ])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    analysis = cur.fetchone()
                    updated_analysis = AnalysisOut(id=analysis[0],
                                                   document=analysis[1],
                                                   patient_id=analysis[2],
                                                   created=analysis[3],
                                                   updated=analysis[4])
                    return updated_analysis

    def delete(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('analysis_delete', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    return True

    def get(self, id):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('analysis_get', [id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    analysis = cur.fetchone()
                    get_analysis = AnalysisOut(id=analysis[0],
                                               document=analysis[1],
                                               patient_id=analysis[2],
                                               created=analysis[3],
                                               updated=analysis[4])
                    return get_analysis

    def get_list(self, id=None, document=None, patient_id=None):
        with self.conn:
            with self.conn.cursor() as cur:
                try:
                    cur.callproc('analysis_get_list', [id, document, patient_id])
                except psycopg2.Error as e:
                    raise HTTPException(status_code=400, detail=e.diag.message_primary + "; " + e.diag.message_hint)
                else:
                    analysis_list = cur.fetchall()
                    get_analysis_list = []
                    for analysis in analysis_list:
                        get_analysis_list.append(AnalysisOut(id=analysis[0],
                                                             document=analysis[1],
                                                             patient_id=analysis[2],
                                                             created=analysis[3],
                                                             updated=analysis[4]))

                    return AnalysisList(list=get_analysis_list)
