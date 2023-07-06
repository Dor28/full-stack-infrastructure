/*****************
* File name: analysis_delete.sql
* Author: Eldor
* Date: 2021-07-05
* Version: 1.0
*************
* Changelog
* 2021-07-05 First init
*************/


CREATE OR REPLACE FUNCTION analysis_delete(in_id_analysis BIGINT DEFAULT NULL)
    returns VOID
as
$$
DECLARE
    FUNC_NAME TEXT := 'analysis_delete';
    ERR_CODE  INT  := 4002;


BEGIN
    IF in_id_analysis IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_analysis
            USING HINT = 'id_analysis cannot be null';
    END IF;

    IF NOT EXISTS(SELECT 1 FROM analysis WHERE id_analysis=in_id_analysis) OR
       EXISTS(SELECT 1 FROM analysis WHERE id_analysis=in_id_analysis AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_analysis
            USING HINT = 'analysis not exists';
    END IF;

    UPDATE analysis SET is_delete = TRUE, exp_date = now() WHERE id_analysis=in_id_analysis;




end;
$$
    LANGUAGE 'plpgsql';
