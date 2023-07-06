/*****************
* File name: patient_update.sql
* Author: Eldor
* Date: 2021-07-01
* Version: 1.0
*************
* Changelog
* 2021-07-01 First init
*************/


CREATE OR REPLACE FUNCTION patient_update(in_id_patient BIGINT DEFAULT NULL, in_first_name TEXT DEFAULT NULL,
                                          in_last_name TEXT DEFAULT NULL, in_father_name TEXT DEFAULT NULL,
                                          in_address TEXT DEFAULT NULL, in_phone TEXT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'patient_update';
    ERR_CODE  INT  := 4003;

BEGIN
    IF in_id_patient IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_patient, in_first_name, in_last_name, in_father_name, in_address, in_phone
            USING HINT = 'id_patient cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM patient WHERE id_patient = in_id_patient) OR
       EXISTS(SELECT 1 FROM patient WHERE id_patient = in_id_patient AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_patient, in_first_name, in_last_name, in_father_name, in_address, in_phone
            USING HINT = 'reception not exists';
    END IF;

    UPDATE patient
    SET first_name=COALESCE(in_first_name, first_name),
        last_name=COALESCE(in_last_name, last_name),
        father_name=COALESCE(in_father_name, father_name),
        address=COALESCE(in_address, address),
        address=COALESCE(in_phone, phone),
        mod_date = now()
    WHERE id_patient = in_id_patient;

    RETURN QUERY SELECT id_patient, first_name, last_name, father_name, address, phone,  reg_date, mod_date
                 FROM patient
                 WHERE id_patient = in_id_patient;


end;
$$
    LANGUAGE 'plpgsql';
