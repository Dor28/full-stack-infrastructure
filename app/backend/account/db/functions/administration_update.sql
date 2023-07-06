/*****************
* File name: administartion_update.sql
* Author: Eldor
* Date: 2021-06-27
* Version: 1.0
*************
* Changelog
* 2021-06-27 First init
* 2021-06-29 id_administration = in_id_administration fixed;
*************/


CREATE OR REPLACE FUNCTION administration_update(in_id_administration BIGINT DEFAULT NULL, in_first_name TEXT DEFAULT NULL,
                                          in_last_name TEXT DEFAULT NULL, in_father_name TEXT DEFAULT NULL,
                                          in_user_id INT DEFAULT NULL)
    returns TABLE
            (
                out_id_administration  BIGINT,
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
    FUNC_NAME TEXT := 'administration_update';
    ERR_CODE  INT  := 4003;

BEGIN
    IF in_id_administration IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_administration, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'id_administration cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM administration WHERE id_administration = in_id_administration) OR
       EXISTS(SELECT 1 FROM administration WHERE id_administration = in_id_administration AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_administration, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'administration not exists';
    END IF;

    IF in_id_administration IS NOT NULL AND (NOT EXISTS(SELECT 1 FROM users WHERE id_user = in_user_id) OR
                                      EXISTS(
                                              SELECT 1 FROM users WHERE id_user = in_user_id AND is_delete = TRUE)) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_administration, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'account not exists';
    END IF;

    IF in_user_id IS NOT NULL AND EXISTS(SELECT 1 FROM administration WHERE user_id = in_user_id) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_administration, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'a administration with the account_id already exists';
    END IF;

    UPDATE administration
    SET first_name=COALESCE(in_first_name, first_name),
        last_name=COALESCE(in_last_name, last_name),
        father_name=COALESCE(in_father_name, father_name),
        user_id=COALESCE(in_user_id, user_id),
        mod_date = now()
    WHERE id_administration = in_id_administration;

    RETURN QUERY SELECT id_administration, first_name, last_name, father_name, user_id, reg_date, mod_date
                 FROM administration
                 WHERE id_administration = in_id_administration;


end;
$$
    LANGUAGE 'plpgsql';
