/*****************
* File name: visit_add.sql
* Author: Eldor
* Date: 2021-07-04
* Version: 1.0
*************
* Changelog
* 2021-07-04 First init
*************/


CREATE OR REPLACE FUNCTION visit_add(in_patient_id INT DEFAULT NULL, in_doctor_id INT DEFAULT NULL,
                                       in_date TIMESTAMP WITH TIME ZONE DEFAULT NULL, in_status TEXT DEFAULT NULL)
    returns TABLE
            (
                out_id_visit  BIGINT,
                out_patient_id  INT,
                out_doctor_id  INT,
                out_date  TIMESTAMP WITH TIME ZONE,
                out_status TEXT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'visit_add';
    ERR_CODE  INT  := 4001;

BEGIN
    IF in_patient_id IS NULL OR in_doctor_id IS NULL  THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_patient_id, in_doctor_id, in_date, in_status
            USING HINT = 'patient_id and doctor_id  cannot be null';
    END IF;

    IF EXISTS(SELECT 1 FROM visit WHERE patient_id = in_patient_id AND doctor_id = in_doctor_id AND date=in_date) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_patient_id, in_doctor_id, in_date, in_status
            USING HINT = 'visit with similar date and patient and doctor already exists';
    END IF;

    RETURN QUERY INSERT INTO visit (patient_id, doctor_id, date, status) VALUES (in_patient_id, in_doctor_id, in_date, in_status)
        RETURNING id_visit, patient_id, doctor_id, date, status, reg_date, mod_date;


end;
$$
    LANGUAGE 'plpgsql';

