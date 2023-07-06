/*****************
* File name: patient_add.sql
* Author: Eldor
* Date: 2021-06-30
* Version: 1.0
*************
* Changelog
* 2021-06-30 First init
*************/


CREATE OR REPLACE FUNCTION patient_add(in_first_name TEXT DEFAULT NULL, in_last_name TEXT DEFAULT NULL,
                                       in_father_name TEXT DEFAULT NULL, in_address TEXT DEFAULT NULL,
                                       in_phone TEXT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'patient_add';
    ERR_CODE  INT  := 4001;

BEGIN
    IF in_first_name IS NULL OR in_last_name IS NULL OR in_phone IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_first_name, in_last_name, in_father_name, in_address, in_phone
            USING HINT = 'first_name or last_name  cannot be null';
    END IF;

    RETURN QUERY INSERT INTO patient (first_name, last_name, father_name, address, phone) VALUES (in_first_name, in_last_name,
                                                                                            in_father_name, in_address, in_phone)
        RETURNING id_patient, first_name, last_name, father_name, address, phone, reg_date, mod_date;


end;
$$
    LANGUAGE 'plpgsql';

