/*****************
* File name: analysis_get.sql
* Author: Eldor
* Date: 2021-07-05
* Version: 1.0
*************
* Changelog
* 2021-07-05 First init
*************/


CREATE OR REPLACE FUNCTION analysis_get(in_id_analysis BIGINT DEFAULT NULL)
    returns TABLE
            (
                out_id_analysis  BIGINT,
                out_document  TEXT,
                out_patient_id  INT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'analysis_get';
    ERR_CODE  INT  := 4004;

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

   RETURN QUERY SELECT id_analysis, document,  patient_id,  reg_date, mod_date
                 FROM analysis
                 WHERE id_analysis = in_id_analysis;





end;
$$
    LANGUAGE 'plpgsql';
