/*****************
* File name: administration_delete.sql
* Author: Eldor
* Date: 2021-06-27
* Version: 1.0
*************
* Changelog
* 2021-06-27 First init
*************/


CREATE OR REPLACE FUNCTION administration_delete(in_id_administration BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'administration_delete';
    ERR_CODE  INT  := 4002;
    deleted_account INT;

BEGIN
    IF in_id_administration IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_administration
            USING HINT = 'in_id_administration cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM administration WHERE id_administration=in_id_administration) OR
       EXISTS(SELECT 1 FROM administration WHERE id_administration = in_id_administration AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_administration
            USING HINT = 'administration not exists';
    END IF;

    SELECT user_id INTO deleted_account FROM administration WHERE id_administration = in_id_administration;
    PERFORM user_delete(deleted_account);

    UPDATE administration SET is_delete = TRUE, exp_date = now() WHERE id_administration = in_id_administration;




end;
$$
    LANGUAGE 'plpgsql';
