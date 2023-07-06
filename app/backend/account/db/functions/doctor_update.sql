/*****************
* File name: doctor_update.sql
* Author: Eldor
* Date: 2021-06-27
* Version: 1.0
*************
* Changelog
* 2021-06-27 First init
*************/


CREATE OR REPLACE FUNCTION doctor_update(in_id_doctor BIGINT DEFAULT NULL, in_first_name TEXT DEFAULT NULL,
                                          in_last_name TEXT DEFAULT NULL, in_father_name TEXT DEFAULT NULL,
                                          in_user_id INT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'doctor_update';
    ERR_CODE  INT  := 4003;

BEGIN
    IF in_id_doctor IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_doctor, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'id_doctor cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM doctor WHERE id_doctor = in_id_doctor) OR
       EXISTS(SELECT 1 FROM doctor WHERE id_doctor = in_id_doctor AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_doctor, in_first_name, in_last_name, in_father_name, in_id_doctor
            USING HINT = 'doctor not exists';
    END IF;

    IF in_id_doctor IS NOT NULL AND (NOT EXISTS(SELECT 1 FROM users WHERE id_user = in_user_id) OR
                                      EXISTS(
                                              SELECT 1 FROM users WHERE id_user = in_user_id AND is_delete = TRUE)) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_doctor, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'account not exists';
    END IF;

    IF in_user_id IS NOT NULL AND EXISTS(SELECT 1 FROM doctor  WHERE user_id = in_user_id) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_doctor, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'a doctor with the account_id already exists';
    END IF;

    UPDATE doctor
    SET first_name=COALESCE(in_first_name, first_name),
        last_name=COALESCE(in_last_name, last_name),
        father_name=COALESCE(in_father_name, father_name),
        user_id=COALESCE(in_user_id, user_id),
        mod_date = now()
    WHERE id_doctor= in_id_doctor;

    RETURN QUERY SELECT id_doctor, first_name, last_name, father_name, user_id, reg_date, mod_date
                 FROM doctor
                 WHERE id_doctor = in_id_doctor;


end;
$$
    LANGUAGE 'plpgsql';
