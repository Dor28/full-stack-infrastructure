/*****************
* File name: patient_delete.sql
* Author: Eldor
* Date: 2021-07-01
* Version: 1.0
*************
* Changelog
* 2021-07-01 First init
*************/


CREATE OR REPLACE FUNCTION visit_delete(in_id_visit BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'visit_delete';
    ERR_CODE  INT  := 4002;


BEGIN
    IF in_id_visit IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_visit
            USING HINT = 'in_id_visit cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM visit WHERE id_visit=in_id_visit) OR
       EXISTS(SELECT 1 FROM visit WHERE id_visit=in_id_visit AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_visit
            USING HINT = 'visit not exists';
    END IF;

    UPDATE visit SET is_delete = TRUE, exp_date = now() WHERE id_visit=in_id_visit;




end;
$$
    LANGUAGE 'plpgsql';
