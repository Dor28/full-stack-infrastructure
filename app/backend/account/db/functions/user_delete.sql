/*****************
* File name: user_delete.sql
* Author: Eldor
* Date: 2021-06-24
* Version: 1.0
*************
* Changelog
* 2021-06-24 First init
*************/


CREATE OR REPLACE FUNCTION user_delete(in_user_id BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'user_delete';
    ERR_CODE  INT  := 1002;

BEGIN
    IF in_user_id IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_user_id
            USING HINT = 'account_id cannot be null';
    END IF;

    IF NOT exists(SELECT 1 FROM users WHERE id_user = in_user_id) OR
       exists(SELECT 1 FROM users WHERE id_user = in_user_id AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_user_id
            USING HINT = 'user not exists';
    end if;

    UPDATE users SET is_delete = TRUE, exp_date = now() WHERE id_user = in_user_id;


end;
$$
    LANGUAGE 'plpgsql';

