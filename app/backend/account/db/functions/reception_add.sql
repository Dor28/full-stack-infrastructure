/*****************
* File name: reception_add.sql
* Author: Eldor
* Date: 2021-06-25
* Version: 1.0
*************
* Changelog
* 2021-06-25 First init
* 2021-06-25 out_reg_date, out_mod_date added
*************/


CREATE OR REPLACE FUNCTION reception_add(in_first_name TEXT DEFAULT NULL, in_last_name TEXT DEFAULT NULL,
                                       in_father_name TEXT DEFAULT NULL, in_user_id INT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'reception_add';
    ERR_CODE  INT  := 4001;

BEGIN
    IF in_first_name IS NULL OR in_last_name IS NULL OR in_user_id IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'first_name or last_name or account_id cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM users WHERE id_user = in_user_id) OR
       EXISTS(SELECT 1 FROM users WHERE id_user = in_user_id AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'user not exists';
    END IF;

    IF EXISTS(SELECT 1 FROM reception WHERE user_id = in_user_id) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_first_name, in_last_name, in_father_name, in_user_id
            USING HINT = 'a reception with the user_id already exists';
    END IF;

    RETURN QUERY INSERT INTO reception (first_name, last_name, father_name, user_id) VALUES (in_first_name, in_last_name,
                                                                                            in_father_name, in_user_id)
        RETURNING id_reception, first_name, last_name, father_name, user_id, reg_date, mod_date;


end;
$$
    LANGUAGE 'plpgsql';

