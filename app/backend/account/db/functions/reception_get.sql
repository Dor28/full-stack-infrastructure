/*****************
* File name: reception_get.sql
* Author: Eldor
* Date: 2021-06-25
* Version: 1.0
*************
* Changelog
* 2021-06-25 First init
*************/


CREATE OR REPLACE FUNCTION reception_get(in_id_reception BIGINT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'reception_get';
    ERR_CODE  INT  := 4004;

BEGIN
    IF in_id_reception IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_reception
            USING HINT = 'id_reception cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM reception WHERE id_reception=in_id_reception) OR
       EXISTS(SELECT 1 FROM reception WHERE id_reception = in_id_reception AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_reception
            USING HINT = 'reception not exists';
    END IF;

    RETURN QUERY SELECT id_reception, first_name, last_name, father_name, user_id, reg_date, mod_date
                 FROM reception
                 WHERE id_reception = in_id_reception;




end;
$$
    LANGUAGE 'plpgsql';
