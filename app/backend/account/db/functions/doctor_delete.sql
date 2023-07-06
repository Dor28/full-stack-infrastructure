/*****************
* File name: doctor_delete.sql
* Author: Eldor
* Date: 2021-06-27
* Version: 1.0
*************
* Changelog
* 2021-06-27 First init
*************/


CREATE OR REPLACE FUNCTION doctor_delete(in_id_doctor BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'doctor_delete';
    ERR_CODE  INT  := 4002;
    deleted_account INT;

BEGIN
    IF in_id_doctor IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_doctor
            USING HINT = 'in_id_doctor cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM doctor WHERE id_doctor=in_id_doctor) OR
       EXISTS(SELECT 1 FROM doctor WHERE id_doctor = in_id_doctor AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_doctor
            USING HINT = 'reception not exists';
    END IF;

    SELECT user_id INTO deleted_account FROM doctor WHERE id_doctor= in_id_doctor;
    PERFORM user_delete(deleted_account);

    UPDATE doctor SET is_delete = TRUE, exp_date = now() WHERE id_doctor = in_id_doctor;




end;
$$
    LANGUAGE 'plpgsql';
