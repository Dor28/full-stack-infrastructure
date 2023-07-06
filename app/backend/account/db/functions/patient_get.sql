/*****************
* File name: patient_get.sql
* Author: Eldor
* Date: 2021-07-01
* Version: 1.0
*************
* Changelog
* 2021-07-01 First init
*************/


CREATE OR REPLACE FUNCTION patient_get(in_id_patient BIGINT DEFAULT NULL)
    returns TABLE
            (
                out_id_patient  BIGINT,
                out_first_name  TEXT,
                out_last_name   TEXT,
                out_father_name TEXT,
                out_address  TEXT,
                out_phone TEXT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'patient_get';
    ERR_CODE  INT  := 4004;

BEGIN
    IF in_id_patient IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_patient
            USING HINT = 'id_patient cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM patient WHERE id_patient=in_id_patient) OR
       EXISTS(SELECT 1  FROM patient WHERE id_patient=in_id_patient AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_patient
            USING HINT = 'patient not exists';
    END IF;

    RETURN QUERY SELECT id_patient, first_name, last_name, father_name, address, phone,  reg_date, mod_date
                 FROM patient
                 WHERE id_patient=in_id_patient;




end;
$$
    LANGUAGE 'plpgsql';
