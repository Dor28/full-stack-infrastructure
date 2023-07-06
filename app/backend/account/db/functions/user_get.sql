/*****************
* File name: user_get.sql
* Author: Eldor
* Date: 2021-06-24
* Version: 1.0
*************
* Changelog
* 2021-06-24 First init

*************/


CREATE OR REPLACE FUNCTION user_get(in_user_id BIGINT DEFAULT NULL)
    returns TABLE
            (
                out_id_user   BIGINT,
                out_username  TEXT,
                out_password  TEXT,
                out_reg_date  TIMESTAMP WITH TIME ZONE,
                out_mod_date  TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'user_get';
    ERR_CODE  INT  := 1004;

BEGIN
    IF in_user_id IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_user_id
            USING HINT = 'user_id cannot be null';
    END IF;

    IF NOT exists(SELECT 1 FROM users WHERE id_user = in_user_id) OR
       exists(SELECT 1 FROM users WHERE id_user = in_user_id AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_user_id
            USING HINT = 'user not exists';
    end if;

    RETURN QUERY SELECT id_user, username, password, reg_date, mod_date
                 FROM users
                 WHERE id_user = in_user_id;

end;
$$
    LANGUAGE 'plpgsql';

