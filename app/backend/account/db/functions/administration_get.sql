/*****************
* File name: administration_get.sql
* Author: Eldor
* Date: 2021-06-27
* Version: 1.0
*************
* Changelog
* 2021-06-27 First init
*************/


CREATE OR REPLACE FUNCTION administration_get(in_id_administration BIGINT DEFAULT NULL)
    returns TABLE
            (
                out_id_administration  BIGINT,
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
    FUNC_NAME TEXT := 'administration_get';
    ERR_CODE  INT  := 4004;

BEGIN
    IF in_id_administration IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_administration
            USING HINT = 'id_administration cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM administration WHERE id_administration=in_id_administration) OR
       EXISTS(SELECT 1 FROM administration WHERE id_administration = in_id_administration AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_administration
            USING HINT = 'administration not exists';
    END IF;

    RETURN QUERY SELECT id_administration, first_name, last_name, father_name, user_id, reg_date, mod_date
                 FROM administration
                 WHERE id_administration= in_id_administration;




end;
$$
    LANGUAGE 'plpgsql';
