/*****************
* File name: reception_update.sql
* Author: Eldor
* Date: 2021-06-25
* Version: 1.0
*************
* Changelog
* 2021-06-25 First init
* 2021-07-01 duplicate in_id_reception deleted
*************/


CREATE OR REPLACE FUNCTION reception_update(in_id_reception BIGINT DEFAULT NULL, in_first_name TEXT DEFAULT NULL,
                                          in_last_name TEXT DEFAULT NULL, in_father_name TEXT DEFAULT NULL,
                                          in_user_id INT DEFAULT NULL)
    returns TABLE
            (
                out_id_reception  BIGINT,
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
    FUNC_NAME TEXT := 'reception_update';
    ERR_CODE  INT  := 4003;

BEGIN
    IF in_id_reception IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_reception, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'id_reception cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM reception WHERE id_reception = in_id_reception) OR
       EXISTS(SELECT 1 FROM reception WHERE id_reception = in_id_reception AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_reception, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'reception not exists';
    END IF;

    IF in_user_id IS NOT NULL AND (NOT EXISTS(SELECT 1 FROM users WHERE id_user = in_user_id) OR
                                      EXISTS(
                                              SELECT 1 FROM users WHERE id_user = in_user_id AND is_delete = TRUE)) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_reception, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'account not exists';
    END IF;

    IF in_user_id IS NOT NULL AND EXISTS(SELECT 1 FROM reception WHERE user_id = in_user_id) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %, %', ERR_CODE, FUNC_NAME, in_id_reception, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'a reception with the account_id already exists';
    END IF;

    UPDATE reception
    SET first_name=COALESCE(in_first_name, first_name),
        last_name=COALESCE(in_last_name, last_name),
        father_name=COALESCE(in_father_name, father_name),
        user_id=COALESCE(in_user_id, user_id),
        mod_date = now()
    WHERE id_reception = in_id_reception;

    RETURN QUERY SELECT id_reception, first_name, last_name, father_name, user_id, reg_date, mod_date
                 FROM reception
                 WHERE id_reception = in_id_reception;


end;
$$
    LANGUAGE 'plpgsql';
