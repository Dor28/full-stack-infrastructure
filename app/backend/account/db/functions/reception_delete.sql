/*****************
* File name: reception_delete.sql
* Author: Eldor
* Date: 2021-06-25
* Version: 1.0
*************
* Changelog
* 2021-06-25 First init
*************/


CREATE OR REPLACE FUNCTION reception_delete(in_id_reception BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'reception_delete';
    ERR_CODE  INT  := 4002;
    deleted_account INT;

BEGIN
    IF in_id_reception IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_reception
            USING HINT = 'in_id_reception cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM reception WHERE id_reception=in_id_reception) OR
       EXISTS(SELECT 1 FROM reception WHERE id_reception = in_id_reception AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_reception
            USING HINT = 'reception not exists';
    END IF;

    SELECT user_id INTO deleted_account FROM reception WHERE id_reception = in_id_reception;
    PERFORM user_delete(deleted_account);

    UPDATE reception SET is_delete = TRUE, exp_date = now() WHERE id_reception = in_id_reception;




end;
$$
    LANGUAGE 'plpgsql';
