/*****************
* File name: doctor_get.sql
* Author: Eldor
* Date: 2021-06-27
* Version: 1.0
*************
* Changelog
* 2021-06-27 First init
*************/


CREATE OR REPLACE FUNCTION doctor_get(in_id_doctor BIGINT DEFAULT NULL)
    returns TABLE
            (
                out_id_doctor  BIGINT,
                out_first_name  TEXT,
                out_last_name   TEXT,
                out_father_name TEXT,
                out_user_id  INT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'doctor_get';
    ERR_CODE  INT  := 4004;

BEGIN
    IF in_id_doctor IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_doctor
            USING HINT = 'id_doctor cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM doctor WHERE id_doctor=in_id_doctor) OR
       EXISTS(SELECT 1 FROM doctor WHERE id_doctor= in_id_doctor AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_doctor
            USING HINT = 'doctor not exists';
    END IF;

    RETURN QUERY SELECT id_doctor, first_name, last_name, father_name, user_id, reg_date, mod_date
                 FROM doctor
                 WHERE id_doctor= in_id_doctor;




end;
$$
    LANGUAGE 'plpgsql';
