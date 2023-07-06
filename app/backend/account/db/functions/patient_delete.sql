/*****************
* File name: patient_delete.sql
* Author: Eldor
* Date: 2021-07-01
* Version: 1.0
*************
* Changelog
* 2021-07-01 First init
*************/


CREATE OR REPLACE FUNCTION patient_delete(in_id_patient BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'patient_delete';
    ERR_CODE  INT  := 4002;


BEGIN
    IF in_id_patient IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_patient
            USING HINT = 'in_id_patient cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM patient WHERE id_patient=in_id_patient) OR
       EXISTS(SELECT 1 FROM patient WHERE id_patient=in_id_patient AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_patient
            USING HINT = 'patient not exists';
    END IF;

    UPDATE patient SET is_delete = TRUE, exp_date = now() WHERE id_patient=in_id_patient;




end;
$$
    LANGUAGE 'plpgsql';
