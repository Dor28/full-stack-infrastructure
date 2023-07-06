/*****************
* File name: visit_get.sql
* Author: Eldor
* Date: 2021-07-04
* Version: 1.0
*************
* Changelog
* 2021-07-04 First init
*************/


CREATE OR REPLACE FUNCTION visit_get(in_id_visit BIGINT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'visit_get';
    ERR_CODE  INT  := 4004;

BEGIN
    IF in_id_visit IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_visit
            USING HINT = 'id_visit cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM visit WHERE id_visit=in_id_visit) OR
       EXISTS(SELECT 1 FROM visit WHERE id_visit=in_id_visit AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_visit
            USING HINT = 'visit not exists';
    END IF;

    RETURN QUERY SELECT id_visit, patient_id, doctor_id, date, status, reg_date, mod_date
                 FROM visit
                 WHERE id_visit = in_id_visit;




end;
$$
    LANGUAGE 'plpgsql';
