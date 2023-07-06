/*****************
* File name: visit_update.sql
* Author: Eldor
* Date: 2021-07-04
* Version: 1.0
*************
* Changelog
* 2021-07-04 First init
*************/


CREATE OR REPLACE FUNCTION visit_update(in_id_visit BIGINT DEFAULT NULL, in_patient_id INT DEFAULT NULL, in_doctor_id INT DEFAULT NULL,
                                       in_date TIMESTAMP WITH TIME ZONE DEFAULT NULL, in_status TEXT DEFAULT NULL)
    returns TABLE
            (   out_id_visit BIGINT,
                out_patient_id  INT,
                out_doctor_id  INT,
                out_date   TIMESTAMP WITH TIME ZONE,
                out_status TEXT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'visit_update';
    ERR_CODE  INT  := 4003;

BEGIN
    IF in_id_visit IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_visit, in_patient_id, in_doctor_id, in_date, in_status
            USING HINT = 'id_visit cannot be null';
    END IF;

     IF NOT EXISTS(SELECT 1 FROM visit WHERE id_visit=in_id_visit) OR
       EXISTS(SELECT 1 FROM visit WHERE id_visit=in_id_visit AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_visit
            USING HINT = 'visit not exists';
    END IF;



      IF EXISTS(SELECT 1 FROM visit WHERE patient_id = in_patient_id AND doctor_id = in_doctor_id AND date=in_date) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_patient_id, in_doctor_id, in_date, in_status
            USING HINT = 'visit with similar date and patient and doctor already exists';
    END IF;


    UPDATE visit
    SET patient_id=COALESCE(in_patient_id, patient_id),
        doctor_id=COALESCE(in_doctor_id, doctor_id),
        date=COALESCE(in_date, date),
        status=COALESCE(in_status, status),
        mod_date = now()
    WHERE id_visit = in_id_visit;

    RETURN QUERY SELECT id_visit, patient_id, doctor_id, date, status, reg_date, mod_date
                 FROM visit
                 WHERE id_visit = in_id_visit;


end;
$$
    LANGUAGE 'plpgsql';
