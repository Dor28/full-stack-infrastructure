/*****************
* File name: user_get_list.sql
* Author: Eldor
* Date: 2021-06-24
* Version: 1.0
*************
* Changelog
* 2021-06-24 First init

*************/


CREATE OR REPLACE FUNCTION user_get_list(in_user_id BIGINT DEFAULT NULL, in_username TEXT DEFAULT NULL)
    returns TABLE
            (
                out_id_user  BIGINT,
                out_username TEXT,
                out_password TEXT,
                out_reg_date TIMESTAMP WITH TIME ZONE,
                out_mod_date TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'user_get_list';
    ERR_CODE  INT  := 1005;

BEGIN
    return QUERY SELECT id_user,
                        username,
                        password,
                        reg_date,
                        mod_date
                 FROM users

                 where (in_user_id IS NULL OR id_user = in_user_id)
                   AND (in_username IS NULL OR username = in_username)
                   AND is_delete = FALSE;
end;
$$
    LANGUAGE 'plpgsql';
