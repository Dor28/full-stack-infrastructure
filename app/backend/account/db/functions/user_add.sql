/*****************
* File name: user_add.sql
* Author: Zafar
* Date: 2021-04-27
* Version: 1.0
*************
* Changelog
* 2021-04-28 First init
* 2021-05-02 change return params
*************/


CREATE OR REPLACE FUNCTION user_add(in_username TEXT DEFAULT NULL, in_password TEXT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'user_add';
    ERR_CODE  INT  := 1001;

BEGIN
    IF in_username IS NULL OR in_password IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %', ERR_CODE, FUNC_NAME, in_username, in_password
            USING HINT = 'Username or password cannot be null';
    END IF;

    IF exists(SELECT 1 FROM users WHERE username = in_username) THEN
        RAISE EXCEPTION 'Error --> % % params %, %', ERR_CODE, FUNC_NAME, in_username, in_password
            USING HINT = 'username already exists';
    end if;

    RETURN QUERY INSERT INTO users (username, password) VALUES (in_username, in_password)
        RETURNING id_user, username, password, reg_date, mod_date;


end;
$$
    LANGUAGE 'plpgsql';

